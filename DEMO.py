import http.server
import socketserver
import threading
from time import sleep

def thread_function(httpd):
    print("Entrei")
    httpd.serve_forever()
        
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

block = True
while(block):
    try:
        httpd = socketserver.TCPServer(("", PORT), Handler)
        block = False
    except:
        PORT += 1
    
print("serving at port", PORT)

x = threading.Thread(target=thread_function, args=(httpd,))

x.start()

sleep(10)

print("Depois do sleep")
httpd.shutdown()
httpd.server_close()
x.join()
