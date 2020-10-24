if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets, uic
    from src.MainWindow import MainWindow

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
