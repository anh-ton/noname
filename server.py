from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        with open("counter.txt", "r+") as f:
            num = int(f.read().strip())
            f.seek(0)
            f.write(str(num + 1))
            f.truncate()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"{num:02d}".encode())

HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()