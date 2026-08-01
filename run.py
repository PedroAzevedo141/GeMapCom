import sys
from PySide6.QtWidgets import QApplication
from src.gemapcom.app import Main

def main():
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
