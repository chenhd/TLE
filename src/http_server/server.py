# coding:utf-8
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urllib2
from crawler.crawl import crawl



def search(args):
#     ['search', 'selenium+%E4%B9%A6']
    print 'searching args:', args
    
    search_data = urllib2.unquote(args)
    print 'searching data:', search_data
    crawl(search_data)
    
    return 'on searching ...', search_data, '\n', 'please wait'

def result(args):
    
    return 'result data ' + args

dic_method = {
              'search' : search,
              'result' : result,
              }

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        request_path = self.requestline.split()[1][1:]
        if request_path == 'favicon.ico':
            return
        
        
#         code = 200
#         try:
#             short, long = self.responses[code]
#             print short, long
#         except KeyError:
#             short, long = '???', '???'
        
        self.send_response(200, 'OK') 
        self.send_header("Content-Type", self.error_content_type)
        self.send_header('Connection', 'close')
        self.end_headers()
        
#         list(<type 'str'>): 
#         ['GET', '/', 'HTTP/1.1']
#         ['GET', '/?input_name=asdsada', 'HTTP/1.1']
#         self.requestline.split()

        request_path = self.requestline.split()[1][1:]
        
        if len(request_path)>0 and request_path[0]=='?':
            request_path = request_path[1:].split('=')
            print request_path
            data = 'request_path'
            if request_path[0] in dic_method:
                data = dic_method[request_path[0]](request_path[1])
        else:
            data = open('./index.html').read()
        
        
        
        self.wfile.write(data)
        
        
        

# MyRequestHandler.protocol_version = "HTTP/1.0"
server_address = ('127.0.0.1', 8090)

httpd = HTTPServer(server_address, MyRequestHandler)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."

httpd.serve_forever()












