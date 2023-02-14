import threading
import http.server
import socketserver

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from Telas.tela_QWebView import Ui_telaQWebView


class kablammoBlast:

    def initScreens(self, homeScreen) -> None:
        
        self.homeScreen = homeScreen
        self.qWebView = homeScreen.telaQWebView_1
        self.QtStack = homeScreen.QtStack
        
        self.qWebView.pushButton_voltar.clicked.connect(self.voltarTelaBlast)
        
    def gerarPortas(self):
        self.PORT = 8000

        Handler = http.server.SimpleHTTPRequestHandler

        block = True
        while (block):
            try:
                self.httpd = socketserver.TCPServer(("", self.PORT), Handler)
                block = False
            except:
                self.PORT += 1

        print("serving at port", self.PORT)

        self.net = threading.Thread(target=self.thread_start)

        self.net.start()
        
    def abrirQWebView(self): 
        self.gerarPortas()
        self.qWebView.webViewXML.setUrl(QUrl('http://localhost:' + str(self.PORT)))
        self.QtStack.setCurrentIndex(7)
        
    def voltarTelaBlast(self):
        """

            Função para abrir tela do INICIAL do BLAST.

        """
        self.thread_shutdown()
        self.homeScreen.QtStack.setCurrentIndex(4)
        
    def thread_start(self):
        print("Entrei no thread_start")
        self.httpd.serve_forever()
        
    def thread_shutdown(self):
        self.httpd.shutdown()
        self.httpd.server_close()
        self.net.join()
