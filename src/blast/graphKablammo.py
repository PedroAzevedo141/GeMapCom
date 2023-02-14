import threading
import http.server
import socketserver

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class filtrosBlast:

    def initScreens(self, blastScreen) -> None:
        
        PORT = 8000
        
        Handler = http.server.SimpleHTTPRequestHandler

        block = True
        while (block):
            try:
                self.httpd = socketserver.TCPServer(("", PORT), Handler)
                block = False
            except:
                PORT += 1
                
        print("serving at port", PORT)

        self.net = threading.Thread(target=self.thread_start)

        self.net.start()
        
    def thread_start(self):
        print("Entrei")
        self.httpd.serve_forever()
        
    def thread_shutdown(self):
        self.httpd.shutdown()
        self.httpd.server_close()
