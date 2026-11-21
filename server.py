from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.request import urlopen

API = "http://34.41.70.175:8080/api/update"

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/update":
            try:
                with urlopen(API, timeout=10) as response:
                    data = response.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(data)
            except Exception as e:
                self.send_error(502, str(e))
        else:
            super().do_GET()

ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
