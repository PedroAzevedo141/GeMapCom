from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Tela_Principal(object):
    """

      Classe que contem todas as configurações da tela inicial da ferramenta.

      Nessa classe usa-se propriedades da biblioteca PyQt5 para facilitar o
      gerenciamento das configurações e interações da tela em questão.

      """
    def setupUi(self, Tela_Principal):
        Tela_Principal.setObjectName("Tela_Principal")
        Tela_Principal.setWindowModality(Qt.NonModal)
        Tela_Principal.resize(1000, 600)
        Tela_Principal.setAutoFillBackground(False)
        Tela_Principal.setToolButtonStyle(Qt.ToolButtonIconOnly)
        Tela_Principal.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(Tela_Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.botao_sair = QPushButton(self.centralwidget)
        self.botao_sair.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_sair.setObjectName("botao_sair")
        self.gridLayout.addWidget(self.botao_sair, 6, 0, 1, 1)
        self.botao_tela_converter = QPushButton(self.centralwidget)
        self.botao_tela_converter.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_tela_converter.setObjectName("botao_tela_converter")
        self.gridLayout.addWidget(self.botao_tela_converter, 2, 0, 1, 1)
        spacerItem = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.botao_tela_comparacao = QPushButton(self.centralwidget)
        self.botao_tela_comparacao.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_tela_comparacao.setObjectName("botao_tela_comparacao")
        self.gridLayout.addWidget(self.botao_tela_comparacao, 0, 0, 1, 1)
        self.botao_tela_outras = QPushButton(self.centralwidget)
        self.botao_tela_outras.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_tela_outras.setObjectName("botao_tela_outras")
        self.gridLayout.addWidget(self.botao_tela_outras, 4, 0, 1, 1)
        spacerItem2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Sunken)
        self.label.setLineWidth(4)
        self.label.setMidLineWidth(0)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.line = QFrame(self.centralwidget)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        Tela_Principal.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Tela_Principal)
        self.statusbar.setObjectName("statusbar")
        Tela_Principal.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(Tela_Principal)
        self.menuBar.setGeometry(QRect(0, 0, 922, 22))
        self.menuBar.setObjectName("menuBar")
        Tela_Principal.setMenuBar(self.menuBar)

        self.retranslateUi(Tela_Principal)
        QMetaObject.connectSlotsByName(Tela_Principal)

    def retranslateUi(self, Tela_Principal):
        _translate = QCoreApplication.translate
        Tela_Principal.setWindowTitle(_translate("Tela_Principal", "Tela Inicial - GeMapCom"))
        self.botao_sair.setText(_translate("Tela_Principal", "SAIR"))
        self.botao_tela_converter.setText(_translate("Tela_Principal", "CONVERTER SEQUENCIA"))
        self.botao_tela_comparacao.setText(_translate("Tela_Principal", "COMPARAR SEQUENCIAS"))
        self.botao_tela_outras.setText(_translate("Tela_Principal", "OUTRAS FERRAMENTAS"))
        self.label.setText(_translate("Tela_Principal", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">GeMapCom</span></p></body></html>"))
