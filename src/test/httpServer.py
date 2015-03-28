# coding:utf-8
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import BaseHTTPServer


class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        print 'do_GET'
        
        code = 200
        message = 'this is the get message'
        try:
            short, long = self.responses[code]
        except KeyError:
            short, long = '???', '???'
        if message is None:
            message = short
        explain = long
        self.log_error("code %d, message %s", code, message)
        
        print 'requestline :', self.requestline
        
        self.send_response(200, message)
        self.send_header("Content-Type", self.error_content_type)
        print 'error_content_type :', self.error_content_type
        
        self.send_header('Connection', 'close')
        self.end_headers()
        self.wfile.write('write the body : this is the content message \n')
        
        self.wfile.write(open('./NewFile.html').read())

# BaseHTTPServer.test(HandlerClass=myHandler)
myHandler.protocol_version = "HTTP/1.0"
server_address = ('127.0.0.1', 8080)

httpd = HTTPServer(server_address, myHandler)

sa = httpd.socket.getsockname()

print "Serving HTTP on", sa[0], "port", sa[1], "..."

httpd.serve_forever()





