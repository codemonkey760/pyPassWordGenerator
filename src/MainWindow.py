import random
import re
import string

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('resources/main_window.ui', self)

        self.btnGenPassWord.clicked.connect(self.generate_password)

    @pyqtSlot()
    def generate_password(self):
        char_maps = {
            (False, False, False): string.ascii_lowercase,
            (True, False, False): string.ascii_lowercase + string.ascii_uppercase,
            (False, True, False): string.ascii_lowercase + string.digits,
            (True, True, False): string.ascii_lowercase + string.ascii_uppercase + string.digits
        }

        char_set = char_maps[(self.bUseCaps.isChecked(), self.bUseNumbers.isChecked(), False)]

        pass_word = ''
        for _ in range(int(self.lePassWordLength.text())):
            index = random.randint(0, len(char_set) - 1)
            pass_word = pass_word + char_set[index]

        self.lePassWordResult.setText(pass_word)
