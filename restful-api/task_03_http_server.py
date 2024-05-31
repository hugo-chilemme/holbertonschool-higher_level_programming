import http.server
import socketserver
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

	def do_GET(self):

		if self.path == '/':
			
			self.send_response(200) 

			self.send_header('Content-type', 'text/plain')

			self.end_headers()

			self.wfile.write(b'Hello, this is a simple API!')

			return

		
		if self.path == '/data':

			self.send_response(200) 

			self.send_header('Content-type', 'application/json')

			self.end_headers()

			self.wfile.write(b'{"name": "John", "age": 30, "city": "New York"}')

			return


		if self.path == '/status':

			self.send_response(200) 

			self.send_header('Content-type', 'text/plain')

			self.end_headers()

			self.wfile.write(b'OK')

			return


		self.send_response(404) 

		self.send_header('Content-type', 'text/plain')

		self.end_headers()

		self.wfile.write(b'Endpoint not found')

		

if __name__ == '__main__':

	server_address = ('', 8000)

	httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)

	httpd.serve_forever()