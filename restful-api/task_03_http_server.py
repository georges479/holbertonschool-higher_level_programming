#!/usr/bin/python3
"""
A simple HTTP server using http.server module.

- Root `/` responds with plain text.
- `/data` returns a JSON dataset.
- `/status` returns "OK".
- Any other endpoint returns 404 Not Found.
"""

import http.server
import json
from http import HTTPStatus


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Custom HTTP request handler for a simple API."""

    def do_GET(self):
        """Handle GET requests and route to specific endpoints."""
        if self.path == "/":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == "/status":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

    def log_message(self, format, *args):
        """Override to disable logging to stdout."""
        return


if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Starting server on port 8000...")
    httpd.serve_forever()
