import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler

httpd = HTTPServer(("0.0.0.0", 4443), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    certfile="server.pem",
    keyfile="key.pem",
    server_side=True,
    ssl_version=ssl.PROTOCOL_TLS,
)
httpd.serve_forever()
