from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from datetime import datetime, timezone
import zipfile
import os

# ----------------- Config -----------------
HOST = "0.0.0.0"
PORT = 42000
SERVE_PORT = PORT + 1

# Add the folders you want to include in the zip here (relative or absolute paths)
FOLDERS_TO_ZIP = [
    "sujet_1",
    "sujet_2",
    "sujet_3",
    "tools",
]

ZIP_FILE = Path("sujets.zip")
# ------------------------------------------


def create_zip(zip_path: Path, folders: list[str]) -> None:
    """
    Create (or overwrite) a zip containing all files from the given folders.
    The directory structure inside the zip is preserved relative to each folder's parent.
    Missing folders are skipped.
    """
    # Make paths absolute for consistent arcname creation
    folders = [Path(p).resolve() for p in folders]

    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for folder in folders:
            if not folder.exists() or not folder.is_dir():
                print(f"[zip] Skipping missing/non-dir: {folder}")
                continue

            # We’ll store paths relative to the folder’s parent so that
            # the folder name itself appears at the top level in the zip.
            base = folder.parent
            for root, _, files in os.walk(folder):
                root_path = Path(root)
                for fname in files:
                    fpath = root_path / fname
                    # Create an archive name like "<folder_name>/.../file"
                    arcname = fpath.relative_to(base)
                    zf.write(fpath, arcname)
                    # Optional: print progress
                    # print(f"[zip] Added {fpath} as {arcname}")

    print(f"[zip] Created {zip_path} ({zip_path.stat().st_size} bytes)")


class ZipServer(BaseHTTPRequestHandler):
    def _send_common_headers(self, length: int, last_modified: float):
        self.send_header("Content-Type", "application/zip")
        self.send_header("Content-Length", str(length))
        self.send_header("Content-Disposition", 'attachment; filename="bundle.zip"')
        # Cache settings; tweak as needed
        self.send_header("Cache-Control", "no-store")
        # Helpful last-modified header
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
        self.send_response(200)
        self._send_common_headers(len(data), ZIP_FILE.stat().st_mtime)
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


if __name__ == "__main__":
    # Build the zip once on startup. You can call this again elsewhere if you want to refresh it.
    create_zip(ZIP_FILE, FOLDERS_TO_ZIP)

    # Serve only the zip on PORT+1
    print(f"[serve] Hosting {ZIP_FILE} on http://{HOST}:{SERVE_PORT}/bundle.zip")
    HTTPServer((HOST, SERVE_PORT), ZipServer).serve_forever()

