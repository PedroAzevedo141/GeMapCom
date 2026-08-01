# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'tela_resultado_webViewgkeLhV.ui'
##
# Created by: Qt User Interface Compiler version 5.15.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView


class Ui_telaQWebView(object):
        
    def setupUi(self, telaQWebView):
        if not telaQWebView.objectName():
            telaQWebView.setObjectName(u"telaQWebView")
        telaQWebView.resize(1000, 600)
        self.centralwidget = QWidget(telaQWebView)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.webViewXML = QWebEngineView(self.centralwidget)
        self.webViewXML.setObjectName(u"webViewXML")
        self.webViewXML.setUrl(QUrl(u"about:blank"))

        self.gridLayout.addWidget(self.webViewXML, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_voltar = QPushButton(self.centralwidget)
        self.pushButton_voltar.setObjectName(u"pushButton_voltar")

        self.horizontalLayout.addWidget(self.pushButton_voltar)

        self.pushButton_saveXML = QPushButton(self.centralwidget)
        self.pushButton_saveXML.setObjectName(u"pushButton_saveXML")

        self.horizontalLayout.addWidget(self.pushButton_saveXML)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        telaQWebView.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(telaQWebView)
        self.statusbar.setObjectName(u"statusbar")
        telaQWebView.setStatusBar(self.statusbar)

        self.retranslateUi(telaQWebView)

        QMetaObject.connectSlotsByName(telaQWebView)
    # setupUi

    def retranslateUi(self, telaQWebView):
        telaQWebView.setWindowTitle(QCoreApplication.translate(
            "telaQWebView", u"Visualiza\u00e7\u00e3o do resultado", None))
        self.pushButton_voltar.setText(
            QCoreApplication.translate("telaQWebView", u"Voltar", None))
        self.pushButton_saveXML.setText(
            QCoreApplication.translate("telaQWebView", u"Gravar XML", None))
    # retranslateUi
