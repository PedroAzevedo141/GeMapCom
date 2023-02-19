# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'tela_filtros_BLASTbCZelq.ui'
##
# Created by: Qt User Interface Compiler version 5.15.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import rc_control_ext_files


class Ui_tela_Filtros_BLAST(object):
    def setupUi(self, tela_Filtros_BLAST):
        if not tela_Filtros_BLAST.objectName():
            tela_Filtros_BLAST.setObjectName(u"tela_Filtros_BLAST")
        tela_Filtros_BLAST.resize(1000, 600)
        tela_Filtros_BLAST.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(tela_Filtros_BLAST)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.scrollArea.setFont(font)
        self.scrollArea.setContextMenuPolicy(Qt.CustomContextMenu)
        self.scrollArea.setAcceptDrops(True)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 980, 558))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_11 = QFrame(self.scrollAreaWidgetContents)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_11, 6, 2, 1, 1)

        self.line_7 = QFrame(self.scrollAreaWidgetContents)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 2, 0, 1, 1)

        self.line_8 = QFrame(self.scrollAreaWidgetContents)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_8, 8, 0, 1, 1)

        self.checkBox_Identidade = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_Identidade.setObjectName(u"checkBox_Identidade")

        self.gridLayout_2.addWidget(self.checkBox_Identidade, 3, 0, 1, 1)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 6, 0, 1, 2)

        self.line_12 = QFrame(self.scrollAreaWidgetContents)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_12, 4, 2, 1, 2)

        self.line_9 = QFrame(self.scrollAreaWidgetContents)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_9, 2, 2, 1, 2)

        self.label_EspacoBranco1 = QLabel(self.scrollAreaWidgetContents)
        self.label_EspacoBranco1.setObjectName(u"label_EspacoBranco1")
        self.label_EspacoBranco1.setAutoFillBackground(True)

        self.gridLayout_2.addWidget(self.label_EspacoBranco1, 10, 0, 1, 4)

        self.pushButton_Continuar = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Continuar.setObjectName(u"pushButton_Continuar")
        self.pushButton_Continuar.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_Continuar.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.pushButton_Continuar, 11, 3, 1, 1)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 3, 2, 1, 2)

        self.label_EspacoBranco2 = QLabel(self.scrollAreaWidgetContents)
        self.label_EspacoBranco2.setObjectName(u"label_EspacoBranco2")

        self.gridLayout_2.addWidget(self.label_EspacoBranco2, 1, 0, 1, 4)

        self.checkBox_EValue = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_EValue.setObjectName(u"checkBox_EValue")

        self.gridLayout_2.addWidget(self.checkBox_EValue, 5, 0, 1, 1)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 7, 1, 1, 1)

        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_6, 4, 0, 1, 1)

        self.checkBox_RAG = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_RAG.setObjectName(u"checkBox_RAG")

        self.gridLayout_2.addWidget(self.checkBox_RAG, 7, 0, 1, 1)

        self.pushButton_Voltar = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Voltar.setObjectName(u"pushButton_Voltar")
        self.pushButton_Voltar.setMaximumSize(QSize(100, 16777215))
        self.pushButton_Voltar.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.pushButton_Voltar, 11, 0, 1, 1)

        self.SpinBox_EValue = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.SpinBox_EValue.setObjectName(u"SpinBox_EValue")
        self.SpinBox_EValue.setCursor(QCursor(Qt.IBeamCursor))
        self.SpinBox_EValue.setWrapping(False)
        self.SpinBox_EValue.setAccelerated(False)
        self.SpinBox_EValue.setKeyboardTracking(True)
        self.SpinBox_EValue.setProperty("showGroupSeparator", False)
        self.SpinBox_EValue.setDecimals(10)
        self.SpinBox_EValue.setMaximum(1.000000000000000)

        self.gridLayout_2.addWidget(self.SpinBox_EValue, 5, 2, 1, 2)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 5, 1, 1, 1)

        self.line_10 = QFrame(self.scrollAreaWidgetContents)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_10, 8, 2, 1, 1)

        self.SpinBox_RAG = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.SpinBox_RAG.setObjectName(u"SpinBox_RAG")
        self.SpinBox_RAG.setCursor(QCursor(Qt.IBeamCursor))
        self.SpinBox_RAG.setDecimals(10)
        self.SpinBox_RAG.setMaximum(1.000000000000000)

        self.gridLayout_2.addWidget(self.SpinBox_RAG, 7, 2, 1, 2)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 3, 1, 1, 1)

        self.logo = QLabel(self.scrollAreaWidgetContents)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(962, 0))
        self.logo.setMaximumSize(QSize(962, 16777215))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Sunken)
        self.logo.setLineWidth(3)
        self.logo.setPixmap(QPixmap(u":/images/Gemapcom_banner_blast.png"))
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setWordWrap(False)

        self.gridLayout_2.addWidget(self.logo, 0, 0, 1, 4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        tela_Filtros_BLAST.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(tela_Filtros_BLAST)
        self.statusbar.setObjectName(u"statusbar")
        tela_Filtros_BLAST.setStatusBar(self.statusbar)

        self.retranslateUi(tela_Filtros_BLAST)

        QMetaObject.connectSlotsByName(tela_Filtros_BLAST)
    # setupUi

    def retranslateUi(self, tela_Filtros_BLAST):
        tela_Filtros_BLAST.setWindowTitle(
            QCoreApplication.translate("tela_Filtros_BLAST", u"Filtros", None))
# if QT_CONFIG(tooltip)
        self.scrollArea.setToolTip(QCoreApplication.translate(
            "tela_Filtros_BLAST", u"Digite o valor o E-Value ...", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(statustip)
        self.scrollArea.setStatusTip("")
# endif // QT_CONFIG(statustip)
# if QT_CONFIG(whatsthis)
        self.scrollArea.setWhatsThis("")
# endif // QT_CONFIG(whatsthis)
# if QT_CONFIG(accessibility)
        self.scrollArea.setAccessibleName(QCoreApplication.translate(
            "tela_Filtros_BLAST", u"Digite o valor o E-Value ...", None))
# endif // QT_CONFIG(accessibility)
# if QT_CONFIG(accessibility)
        self.scrollArea.setAccessibleDescription("")
# endif // QT_CONFIG(accessibility)
        self.checkBox_Identidade.setText(QCoreApplication.translate(
            "tela_Filtros_BLAST", u"Filtro por Identidade", None))
        self.label_EspacoBranco1.setText("")
        self.pushButton_Continuar.setText(QCoreApplication.translate(
            "tela_Filtros_BLAST", u"Continuar", None))
        self.label_EspacoBranco2.setText("")
        self.checkBox_EValue.setText(QCoreApplication.translate(
            "tela_Filtros_BLAST", u"Filtro dos alinhamentos gerados pelo E-Value", None))
        self.checkBox_RAG.setText(QCoreApplication.translate(
            "tela_Filtros_BLAST", u"Filtro pela Raz\u00e3o entre o Tamanho do Alinhamento e o Tamanho do Gene (RAG)", None))
        self.pushButton_Voltar.setText(QCoreApplication.translate(
            "tela_Filtros_BLAST", u"Voltar", None))
# if QT_CONFIG(tooltip)
        self.SpinBox_EValue.setToolTip(QCoreApplication.translate(
            "tela_Filtros_BLAST", u"Digite o valor o E-Value ...", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.SpinBox_RAG.setToolTip(QCoreApplication.translate(
            "tela_Filtros_BLAST", u"Digite o valor do Limiar ...", None))
# endif // QT_CONFIG(tooltip)
        self.logo.setText("")
    # retranslateUi
