import http.server


class Handler(http.server.BaseHTTPRequestHandler):

    def counter(self):
        with open('counter.txt', "w+") as f:
            count = f.readline()
            if not count:
                count = 0
    
            count = int(count) + 1
            f.write(str(count))
        return str(count)

    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        with open('Hello.html', encoding='utf-8') as hello:
            for line in hello.readlines():  
                self.wfile.write(line.encode("utf-8"))
        self.wfile.write('Counter = {}'.format(self.counter()).encode('utf-8'))

def main():
    PORT = 8000
    server = http.server.HTTPServer(("", PORT), Handler)
    print(f"Server is running on port {PORT}")
    server.serve_forever()
    
if __name__ == "__main__":
    main()


