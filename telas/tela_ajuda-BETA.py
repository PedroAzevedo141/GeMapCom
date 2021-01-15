from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import (Qt,QPixmap)

class Ui_Tela_Ajuda(object):
    """

    Classe que contem todas as configurações da tela Ajuda da ferramenta.

    Nessa classe usa-se propriedades da biblioteca PyQt5 para facilitar o
    gerenciamento das configurações e interações da tela em questão.

    """
    def setupUi(self, Tela_Ajuda):
        Tela_Ajuda.setObjectName("Tela_Ajuda")
        Tela_Ajuda.resize(1276, 585)
        self.centralwidget = QtWidgets.QWidget(Tela_Ajuda)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 1221, 391))
        self.label.setPixmap(QPixmap("images/voltar.png"))
        self.label.setGeometry(20, 20, 1221, 391)
        self.label.setObjectName("label")
        Tela_Ajuda.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tela_Ajuda)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1276, 25))
        self.menubar.setObjectName("menubar")
        Tela_Ajuda.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tela_Ajuda)
        self.statusbar.setObjectName("statusbar")
        Tela_Ajuda.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Ajuda)
        QtCore.QMetaObject.connectSlotsByName(Tela_Ajuda)

    def retranslateUi(self, Tela_Ajuda):
        _translate = QtCore.QCoreApplication.translate
        Tela_Ajuda.setWindowTitle(_translate("Tela_Ajuda", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_Ajuda = QtWidgets.QMainWindow()
    ui = Ui_Tela_Ajuda()
    ui.setupUi(Tela_Ajuda)
    Tela_Ajuda.show()
    sys.exit(app.exec_())
