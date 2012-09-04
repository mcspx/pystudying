from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

__author__ = 'rpm'

class Session :
    pass

class MyServer (SimpleHTTPRequestHandler):

    def do_GET(self):
        try :
            counter = Session.counter
            print "counter available"
        except AttributeError as e:
            print "except ".join(e)
            Session.counter = 0
            counter = 0

#        users={"counter" : 0}
#        with  open("users.txt", 'r') as file :
#            if len(file.read()) > 1 :
#                users = pickle.load(file)
#
#
#        users["counter"] = users["counter"] =+ 1
        self.wfile.write("counter = " + str(counter))
        Session.counter += 1


#        file = open('users.txt', 'w')
#        pickle.dump(file, users)
if __name__ == "__main__" :
    httpd = HTTPServer(("", 8080), MyServer)
    httpd.serve_forever()
