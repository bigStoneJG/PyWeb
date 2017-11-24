#-*- coding:utf-8 -*-
import BaseHTTPServer


class RequestHander(BaseHTTPServer.BaseHTTPRequestHandler):

    Page = '''\
    <html>
    <body>
    <p>Hello,web!</p>
    <p>Hello,Python!</p>
    </body>
    </html>
    '''

    def do_GET(self):
        try:
            f = open(self.path[1:], 'r')
            self.send_response(200)
            self.send_header("Content-Type","text/html")
            #self.send_header("Content-Length",str(len(self.Page)))
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404,'file not found:%s' %self.path)

if __name__ == '__main__':
#    print("github test1")
#   print ("github test2")
#   print("github test3")
    print "test1"
    serverAddress = ('',8080)
    server = BaseHTTPServer.HTTPServer(serverAddress,RequestHander)
    server.serve_forever()


