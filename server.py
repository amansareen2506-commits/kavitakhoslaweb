import http.server
import socketserver
import os

PORT = 8000

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Disable browser caching of HTML, CSS, JS, images, etc.
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

# Set current directory to project root
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Allow port reuse to avoid 'Address already in use' errors
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
    print(f"Server started on http://localhost:{PORT} with caching disabled.")
    httpd.serve_forever()
