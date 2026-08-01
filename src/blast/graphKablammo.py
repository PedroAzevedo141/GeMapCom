import threading
import http.server
import socketserver
from typing import Optional

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
        self.httpd: Optional[socketserver.TCPServer] = None
        self.is_running = threading.Event()
        self.net: Optional[threading.Thread] = None

    def gerarPortas(self) -> None:
        if self.is_running.is_set():
            return
            
        self.PORT = 8000
        Handler = http.server.SimpleHTTPRequestHandler
        Handler.log_message = lambda *args, **kwargs: None

        block = True
        while block:
            try:
                self.httpd = socketserver.TCPServer(("127.0.0.1", self.PORT), Handler)
                block = False
            except OSError:
                self.PORT += 1

        print("serving at port", self.PORT)
        self.is_running.set()
        self.net = threading.Thread(target=self.thread_start, daemon=True)
        self.net.start()
        
    def abrirQWebView(self) -> None: 
        self.gerarPortas()
        self.qWebView.webViewXML.setUrl(QUrl('http://127.0.0.1:' + str(self.PORT)))
        self.QtStack.setCurrentIndex(7)
        
    def voltarTelaBlast(self) -> None:
        """
            Função para abrir tela do INICIAL do BLAST.
        """
        self.thread_shutdown()
        self.homeScreen.QtStack.setCurrentIndex(4)
        
    def thread_start(self) -> None:
        if self.httpd:
            try:
                self.httpd.serve_forever()
            except Exception:
                pass
        
    def thread_shutdown(self) -> None:
        if self.is_running.is_set() and self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()
            self.is_running.clear()
            if self.net:
                self.net.join(timeout=1.0)
