# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)
import control_ext_files_rc

class Ui_Tela_Principal(object):
    def setupUi(self, Tela_Principal):
        if not Tela_Principal.objectName():
            Tela_Principal.setObjectName(u"Tela_Principal")
        Tela_Principal.setWindowModality(Qt.NonModal)
        Tela_Principal.resize(1000, 600)
        Tela_Principal.setAutoFillBackground(False)
        Tela_Principal.setToolButtonStyle(Qt.ToolButtonIconOnly)
        Tela_Principal.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(Tela_Principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Sunken)
        self.label.setLineWidth(0)
        self.label.setMidLineWidth(0)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setPixmap(QPixmap(u":/images/Gemapcom_banner.png"))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.botao_tela_comparacao = QPushButton(self.centralwidget)
        self.botao_tela_comparacao.setObjectName(u"botao_tela_comparacao")
        self.botao_tela_comparacao.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.botao_tela_comparacao)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.botao_tela_converter = QPushButton(self.centralwidget)
        self.botao_tela_converter.setObjectName(u"botao_tela_converter")
        self.botao_tela_converter.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.botao_tela_converter)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.botao_tela_outras = QPushButton(self.centralwidget)
        self.botao_tela_outras.setObjectName(u"botao_tela_outras")
        self.botao_tela_outras.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.botao_tela_outras)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.botao_tela_outras_2 = QPushButton(self.centralwidget)
        self.botao_tela_outras_2.setObjectName(u"botao_tela_outras_2")
        self.botao_tela_outras_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.botao_tela_outras_2)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.botao_sair = QPushButton(self.centralwidget)
        self.botao_sair.setObjectName(u"botao_sair")
        self.botao_sair.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_sair.setAutoDefault(False)
        self.botao_sair.setFlat(False)

        self.verticalLayout_2.addWidget(self.botao_sair)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        Tela_Principal.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Tela_Principal)
        self.statusbar.setObjectName(u"statusbar")
        Tela_Principal.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Principal)

        self.botao_sair.setDefault(False)


        QMetaObject.connectSlotsByName(Tela_Principal)
    # setupUi

    def retranslateUi(self, Tela_Principal):
        Tela_Principal.setWindowTitle(QCoreApplication.translate("Tela_Principal", u"Tela Inicial - GeMapCom", None))
        self.label.setText("")
        self.botao_tela_comparacao.setText(QCoreApplication.translate("Tela_Principal", u"COMPARAR SEQUENCIAS", None))
        self.botao_tela_converter.setText(QCoreApplication.translate("Tela_Principal", u"CONVERTER SEQUENCIA", None))
        self.botao_tela_outras.setText(QCoreApplication.translate("Tela_Principal", u"BLAST+", None))
        self.botao_tela_outras_2.setText(QCoreApplication.translate("Tela_Principal", u"OUTRAS FERRAMENTAS", None))
        self.botao_sair.setText(QCoreApplication.translate("Tela_Principal", u"SAIR", None))
    # retranslateUi

