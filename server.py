from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

lock = threading.Lock()
counter_file = "counter.txt"

def get_next():
    with lock:
        try:
            with open(counter_file, "r") as f:
                num = int(f.read().strip())
        except:
            num = 1

        with open(counter_file, "w") as f:
            f.write(str(num + 1))

        return num

def reset_counter():
    with lock:
        with open(counter_file, "w") as f:
            f.write("1")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/next":
            num = get_next()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"{num:02d}".encode())

        elif self.path == "/reset":
            reset_counter()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"RESET OK")

        elif self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Counter server running")

        else:
            self.send_response(404)
            self.end_headers()

HTTPServer(("0.0.0.0", 10000), Handler).serve_forever()