from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import html
import socket

SETUP_FILE = Path("setup.sh")
HOST, PORT = "0.0.0.0", 42000

class OneFile(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/", "/setup.sh"):
            self.send_error(404, "Not found")
            return

        if not SETUP_FILE.exists():
            self.send_error(500, "Template missing")
            return

        # Read setup file and substitute
        body = SETUP_FILE.read_text()
        body = body.replace("__IP__", self.headers.get("Host").split(':')[0])
        body = body.replace("__PORT__", str(PORT))
        data = body.encode()

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

if __name__ == "__main__":
    HTTPServer((HOST, PORT), OneFile).serve_forever()


