from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Tela_Converter(object):
    """

      Classe que contem todas as configurações da tela de converter da ferramenta.

      Nessa classe usa-se propriedades da biblioteca PyQt5 para facilitar o
      gerenciamento das configurações e interações da tela em questão.

    """
    def setupUi(self, Tela_Converter):
        font = QFont("Consolas", 9)
        Tela_Converter.setObjectName("Tela_Converter")
        Tela_Converter.resize(1000, 600)
        self.centralwidget = QWidget(Tela_Converter)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QFrame(self.centralwidget)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.setar_sequencia = QTextEdit(self.centralwidget)
        self.setar_sequencia.setReadOnly(True)
        self.setar_sequencia.setFont(font)
        self.setar_sequencia.setObjectName("setar_sequencia")
        self.verticalLayout.addWidget(self.setar_sequencia)
        self.botao_abrir_arquivo = QPushButton(self.centralwidget)
        self.botao_abrir_arquivo.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_abrir_arquivo.setObjectName("botao_abrir_arquivo")
        self.verticalLayout.addWidget(self.botao_abrir_arquivo)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.botao_voltar = QPushButton(self.centralwidget)
        self.botao_voltar.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addPixmap(QPixmap("../images/voltar.png"), QIcon.Normal, QIcon.Off)
        self.botao_voltar.setIcon(icon)
        self.botao_voltar.setObjectName("botao_voltar")
        self.horizontalLayout_2.addWidget(self.botao_voltar)
        self.botao_converter = QPushButton(self.centralwidget)
        self.botao_converter.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_converter.setObjectName("botao_converter")
        self.horizontalLayout_2.addWidget(self.botao_converter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Tela_Converter.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Tela_Converter)
        self.statusbar.setObjectName("statusbar")
        Tela_Converter.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Converter)
        QMetaObject.connectSlotsByName(Tela_Converter)

    def retranslateUi(self, Tela_Converter):
        _translate = QCoreApplication.translate
        Tela_Converter.setWindowTitle(_translate("Tela_Converter", "Tela de Converter - GeMapCom"))
        self.label.setText(_translate("Tela_Converter", "TIPO DE CONVERSÃO: "))
        self.comboBox.setItemText(0, _translate("Tela_Converter", "GENBANK - FASTA"))
        self.comboBox.setItemText(1, _translate("Tela_Converter", "FASTQ - FASTA"))
        self.botao_abrir_arquivo.setText(_translate("Tela_Converter", "ABRIR ARQUIVO"))
        self.botao_voltar.setText(_translate("Tela_Converter", "VOLTAR"))
        self.botao_converter.setText(_translate("Tela_Converter", "CONVERTER"))
