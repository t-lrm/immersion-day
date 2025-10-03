from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from datetime import datetime, timezone
import threading
import zipfile
import os
import signal
import sys
import socket

# ----------------- Config -----------------
SETUP_FILE = Path("setup.sh")
HOST, PORT = "0.0.0.0", 42000
SERVE_PORT = PORT + 1

# Folders to include in the zip (relative or absolute paths)
FOLDERS_TO_ZIP = [
    "sujet_1",
    "sujet_2",
    "sujet_3",
    "tools",
    ".idea"
]
ZIP_FILE = Path("bundle.zip")

def get_ipv4():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    output = s.getsockname()[0]
    s.close()
    return output
# ------------------------------------------


def _only_host(header_host: str | None) -> str:
    """
    Extract only the host part (without port) from the Host header.
    Falls back to 127.0.0.1 if missing.
    """
    if not header_host:
        return "127.0.0.1"
    return header_host.split(":", 1)[0]


def create_zip(zip_path: Path, folders: list[str]) -> None:
    """
    Create (or overwrite) a zip containing all files from the given folders.
    The directory structure inside the zip is preserved relative to each folder's parent.
    Missing folders are skipped.
    """
    folders = [Path(p).resolve() for p in folders]

    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for folder in folders:
            if not folder.exists() or not folder.is_dir():
                print(f"[ZIP] Skipping missing/non-dir: {folder}")
                continue

            base = folder.parent
            for root, _, files in os.walk(folder):
                root_path = Path(root)
                for fname in files:
                    fpath = root_path / fname
                    arcname = fpath.relative_to(base)
                    zf.write(fpath, arcname)

    size = zip_path.stat().st_size if zip_path.exists() else 0
    print(f"[ZIP] Created {zip_path} ({size} bytes)")


class OneFile(BaseHTTPRequestHandler):
    """Serves setup.sh on PORT with __IP__ and __PORT__ substitution."""
    def do_GET(self):
        if self.path not in ("/", "/setup.sh"):
            self.send_error(404, "Not found")
            return

        if not SETUP_FILE.exists():
            self.send_error(500, "Template missing")
            return

        # Read setup file and substitute
        body = SETUP_FILE.read_text(encoding="utf-8")
        body = body.replace("__IP__", _only_host(self.headers.get("Host")))
        body = body.replace("__PORT__", str(SERVE_PORT))
        data = body.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/x-sh; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Content-Disposition", 'attachment; filename="setup.sh"')
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/x-sh; charset=utf-8")
        self.end_headers()


class ZipServer(BaseHTTPRequestHandler):
    """Serves bundle.zip on PORT+1."""
    def _send_common_headers(self, length: int, last_modified: float):
        self.send_header("Content-Type", "application/zip")
        self.send_header("Content-Length", str(length))
        self.send_header("Content-Disposition", 'attachment; filename="bundle.zip"')
        self.send_header("Cache-Control", "no-store")
        self.send_header(
            "Last-Modified",
            datetime.fromtimestamp(last_modified, tz=timezone.utc).strftime(
                "%a, %d %b %Y %H:%M:%S GMT"
            ),
        )

    def do_GET(self):
        if self.path not in ("/", "/bundle.zip"):
            self.send_error(404, "Not found")
            return

        if not ZIP_FILE.exists():
            self.send_error(500, "Zip missing")
            return

        data = ZIP_FILE.read_bytes()
        st = ZIP_FILE.stat()
        self.send_response(200)
        self._send_common_headers(len(data), st.st_mtime)
        self.end_headers()
        self.wfile.write(data)

    def do_HEAD(self):
        if not ZIP_FILE.exists():
            self.send_error(500, "Zip missing")
            return
        st = ZIP_FILE.stat()
        self.send_response(200)
        self._send_common_headers(st.st_size, st.st_mtime)
        self.end_headers()


def serve(addr, handler):
    HTTPServer(addr, handler).serve_forever()


if __name__ == "__main__":
    print("[ZIP] Zipping files (do not exit now)...")
    create_zip(ZIP_FILE, FOLDERS_TO_ZIP)

    # Start both servers
    t1 = threading.Thread(target=serve, args=((HOST, PORT), OneFile), daemon=True)
    t2 = threading.Thread(target=serve, args=((HOST, SERVE_PORT), ZipServer), daemon=True)
    t1.start()
    t2.start()

    print(f"[SERVE] Host setup.sh:  http://{HOST}:{PORT}/setup.sh")
    print(f"[SERVE] Host bundle.zip: http://{HOST}:{SERVE_PORT}/bundle.zip")
    print(f"[INFO] You can now run 'curl -fsSL {get_ipv4()}:{PORT} | sh' on other machines.")

    # Keep main thread alive; allow Ctrl+C to stop both
    try:
        signal.pause()  # Linux/Unix
    except (AttributeError, KeyboardInterrupt):
        try:
            while True:
                signal.sleep(3600)
        except KeyboardInterrupt:
            pass
    finally:
        print("\n[SERVE] Shutting down… (press Ctrl+C again if it doesn’t exit)")
        sys.exit(0)

