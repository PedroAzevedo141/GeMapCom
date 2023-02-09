# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'tela_BLASTDrycNy.ui'
##
# Created by: Qt User Interface Compiler version 5.15.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_tela_BLAST(object):
    def setupUi(self, tela_BLAST):
        if not tela_BLAST.objectName():
            tela_BLAST.setObjectName(u"tela_BLAST")
        tela_BLAST.resize(1000, 600)
        self.centralwidget = QWidget(tela_BLAST)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 980, 525))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.GAP = QLabel(self.frame)
        self.GAP.setObjectName(u"GAP")

        self.verticalLayout_2.addWidget(self.GAP)

        self.MATCH = QLabel(self.frame)
        self.MATCH.setObjectName(u"MATCH")

        self.verticalLayout_2.addWidget(self.MATCH)

        self.MISMATCH = QLabel(self.frame)
        self.MISMATCH.setObjectName(u"MISMATCH")

        self.verticalLayout_2.addWidget(self.MISMATCH)

        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LineGAP = QLineEdit(self.frame)
        self.LineGAP.setObjectName(u"LineGAP")
        self.LineGAP.setLayoutDirection(Qt.LeftToRight)
        self.LineGAP.setAlignment(Qt.AlignCenter)
        self.LineGAP.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.LineGAP)

        self.LineMATCH = QLineEdit(self.frame)
        self.LineMATCH.setObjectName(u"LineMATCH")
        self.LineMATCH.setLayoutDirection(Qt.LeftToRight)
        self.LineMATCH.setAlignment(Qt.AlignCenter)
        self.LineMATCH.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.LineMATCH)

        self.LineMISMATCH = QLineEdit(self.frame)
        self.LineMISMATCH.setObjectName(u"LineMISMATCH")
        self.LineMISMATCH.setLayoutDirection(Qt.LeftToRight)
        self.LineMISMATCH.setAlignment(Qt.AlignCenter)
        self.LineMISMATCH.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.LineMISMATCH)

        self.gridLayout_3.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.Parametros = QLabel(self.frame)
        self.Parametros.setObjectName(u"Parametros")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.Parametros.sizePolicy().hasHeightForWidth())
        self.Parametros.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.Parametros, 0, 0, 1, 1)

        self.gridLayout_2.addWidget(self.frame, 3, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(QFont.Bold)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QFrame.Box)
        self.label_3.setFrameShadow(QFrame.Sunken)
        self.label_3.setLineWidth(3)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 3)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.SalvarComo = QLabel(self.frame_3)
        self.SalvarComo.setObjectName(u"SalvarComo")

        self.gridLayout_5.addWidget(self.SalvarComo, 0, 1, 1, 1)

        self.ASN1 = QRadioButton(self.frame_3)
        self.ASN1.setObjectName(u"ASN1")
        self.ASN1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.ASN1, 3, 3, 1, 1)

        self.BLAST_Format = QRadioButton(self.frame_3)
        self.BLAST_Format.setObjectName(u"BLAST_Format")

        self.gridLayout_5.addWidget(self.BLAST_Format, 4, 3, 1, 1)

        self.Comma = QRadioButton(self.frame_3)
        self.Comma.setObjectName(u"Comma")

        self.gridLayout_5.addWidget(self.Comma, 4, 2, 1, 1)

        self.FLATIdentities = QRadioButton(self.frame_3)
        self.FLATIdentities.setObjectName(u"FLATIdentities")
        self.FLATIdentities.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.FLATIdentities, 1, 2, 1, 1)

        self.FLATnoIdentities = QRadioButton(self.frame_3)
        self.FLATnoIdentities.setObjectName(u"FLATnoIdentities")
        self.FLATnoIdentities.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.FLATnoIdentities, 2, 2, 1, 1)

        self.NoIdentities = QRadioButton(self.frame_3)
        self.NoIdentities.setObjectName(u"NoIdentities")
        self.NoIdentities.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.NoIdentities, 3, 1, 1, 1)

        self.ShowingIdentities = QRadioButton(self.frame_3)
        self.ShowingIdentities.setObjectName(u"ShowingIdentities")
        self.ShowingIdentities.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.ShowingIdentities, 2, 1, 1, 1)

        self.TextoBinary = QRadioButton(self.frame_3)
        self.TextoBinary.setObjectName(u"TextoBinary")
        self.TextoBinary.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.TextoBinary, 4, 1, 1, 1)

        self.Tabular_Co = QRadioButton(self.frame_3)
        self.Tabular_Co.setObjectName(u"Tabular_Co")
        self.Tabular_Co.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.Tabular_Co, 2, 3, 1, 1)

        self.XML = QRadioButton(self.frame_3)
        self.XML.setObjectName(u"XML")
        self.XML.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.XML, 3, 2, 1, 1)

        self.Pairwise = QRadioButton(self.frame_3)
        self.Pairwise.setObjectName(u"Pairwise")
        self.Pairwise.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.Pairwise, 1, 3, 1, 1)

        self.Tabular = QRadioButton(self.frame_3)
        self.Tabular.setObjectName(u"Tabular")
        self.Tabular.setCursor(QCursor(Qt.PointingHandCursor))
        self.Tabular.setChecked(True)

        self.gridLayout_5.addWidget(self.Tabular, 1, 1, 1, 1)

        self.gridLayout_2.addWidget(self.frame_3, 3, 1, 1, 2)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.NomeArquivoQUERY = QLineEdit(self.frame_2)
        self.NomeArquivoQUERY.setObjectName(u"NomeArquivoQUERY")
        self.NomeArquivoQUERY.setCursor(QCursor(Qt.ArrowCursor))
        self.NomeArquivoQUERY.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.NomeArquivoQUERY)

        self.CabecalhoArquivoQUERY = QLineEdit(self.frame_2)
        self.CabecalhoArquivoQUERY.setObjectName(u"CabecalhoArquivoQUERY")
        self.CabecalhoArquivoQUERY.setCursor(QCursor(Qt.ArrowCursor))
        self.CabecalhoArquivoQUERY.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.CabecalhoArquivoQUERY)

        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ButtonQuery = QPushButton(self.frame_2)
        self.ButtonQuery.setObjectName(u"ButtonQuery")
        self.ButtonQuery.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.ButtonQuery)

        self.ButtomSearchQuery = QPushButton(self.frame_2)
        self.ButtomSearchQuery.setObjectName(u"ButtomSearchQuery")
        self.ButtomSearchQuery.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.ButtomSearchQuery)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.NomeArquivoSUBJECT = QLineEdit(self.frame_2)
        self.NomeArquivoSUBJECT.setObjectName(u"NomeArquivoSUBJECT")
        self.NomeArquivoSUBJECT.setCursor(QCursor(Qt.ArrowCursor))
        self.NomeArquivoSUBJECT.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.NomeArquivoSUBJECT)

        self.CabecalhoArquivoSUBJECT = QLineEdit(self.frame_2)
        self.CabecalhoArquivoSUBJECT.setObjectName(u"CabecalhoArquivoSUBJECT")
        self.CabecalhoArquivoSUBJECT.setCursor(QCursor(Qt.ArrowCursor))
        self.CabecalhoArquivoSUBJECT.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.CabecalhoArquivoSUBJECT)

        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ButtonSubject = QPushButton(self.frame_2)
        self.ButtonSubject.setObjectName(u"ButtonSubject")
        self.ButtonSubject.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.ButtonSubject)

        self.ButtomSearchSubject = QPushButton(self.frame_2)
        self.ButtomSearchSubject.setObjectName(u"ButtomSearchSubject")
        self.ButtomSearchSubject.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.ButtomSearchSubject)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.gridLayout_4.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Voltar_Prin = QPushButton(self.centralwidget)
        self.Voltar_Prin.setObjectName(u"Voltar_Prin")
        self.Voltar_Prin.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.Voltar_Prin)

        self.Alinhar = QPushButton(self.centralwidget)
        self.Alinhar.setObjectName(u"Alinhar")
        self.Alinhar.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.Alinhar)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        tela_BLAST.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(tela_BLAST)
        self.statusbar.setObjectName(u"statusbar")
        tela_BLAST.setStatusBar(self.statusbar)

        self.retranslateUi(tela_BLAST)

        QMetaObject.connectSlotsByName(tela_BLAST)
    # setupUi

    def retranslateUi(self, tela_BLAST):
        tela_BLAST.setWindowTitle(QCoreApplication.translate(
            "tela_BLAST", u"MainWindow", None))
        self.GAP.setText(QCoreApplication.translate(
            "tela_BLAST", u"GAP:", None))
        self.MATCH.setText(QCoreApplication.translate(
            "tela_BLAST", u"MATCH:", None))
        self.MISMATCH.setText(QCoreApplication.translate(
            "tela_BLAST", u"MISMATCH:", None))
        self.LineGAP.setText(
            QCoreApplication.translate("tela_BLAST", u"2", None))
        self.LineMATCH.setText(
            QCoreApplication.translate("tela_BLAST", u"2", None))
        self.LineMISMATCH.setText(
            QCoreApplication.translate("tela_BLAST", u"-3", None))
        self.Parametros.setText(QCoreApplication.translate(
            "tela_BLAST", u"Par\u00e2metros:", None))
        self.label_3.setText(QCoreApplication.translate(
            "tela_BLAST", u"BLAST", None))
        self.SalvarComo.setText(QCoreApplication.translate(
            "tela_BLAST", u"Salvar como...", None))
        self.ASN1.setText(QCoreApplication.translate(
            "tela_BLAST", u"&Texto ASN.1", None))
        self.BLAST_Format.setText(QCoreApplication.translate(
            "tela_BLAST", u"B&LAST archive format (ASN.1)", None))
        self.Comma.setText(QCoreApplication.translate(
            "tela_BLAST", u"&Comma-separated Values", None))
        self.FLATIdentities.setText(QCoreApplication.translate(
            "tela_BLAST", u"Flat - Showing Identities", None))
        self.FLATnoIdentities.setText(QCoreApplication.translate(
            "tela_BLAST", u"Flat - No Identities", None))
        self.NoIdentities.setText(QCoreApplication.translate(
            "tela_BLAST", u"&No Identities", None))
        self.ShowingIdentities.setText(QCoreApplication.translate(
            "tela_BLAST", u"Showin&g Identities", None))
        self.TextoBinary.setText(QCoreApplication.translate(
            "tela_BLAST", u"Texto Binary ASN.&1", None))
        self.Tabular_Co.setText(QCoreApplication.translate(
            "tela_BLAST", u"Tab&ular - Comentado", None))
        self.XML.setText(QCoreApplication.translate(
            "tela_BLAST", u"Saida &XML", None))
        self.Pairwise.setText(QCoreApplication.translate(
            "tela_BLAST", u"Pairwise", None))
        self.Tabular.setText(QCoreApplication.translate(
            "tela_BLAST", u"Tabular", None))
# if QT_CONFIG(whatsthis)
        self.ButtonQuery.setWhatsThis(QCoreApplication.translate(
            "tela_BLAST", u"<html><head/><body><p><br/></p></body></html>", None))
# endif // QT_CONFIG(whatsthis)
        self.ButtonQuery.setText(
            QCoreApplication.translate("tela_BLAST", u"Query", None))
        self.ButtomSearchQuery.setText(
            QCoreApplication.translate("tela_BLAST", u"Search", None))
        self.ButtonSubject.setText(
            QCoreApplication.translate("tela_BLAST", u"Subject", None))
        self.ButtomSearchSubject.setText(
            QCoreApplication.translate("tela_BLAST", u"Search", None))
        self.Voltar_Prin.setText(
            QCoreApplication.translate("tela_BLAST", u"Voltar", None))
        self.Alinhar.setText(QCoreApplication.translate(
            "tela_BLAST", u"Alinhar", None))
    # retranslateUi
