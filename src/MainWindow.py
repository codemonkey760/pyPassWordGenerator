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
        self.btnResetSpecialChars.clicked.connect(self.reset_special_chars_input)

    @pyqtSlot()
    def reset_special_chars_input(self):
        special_chars = re.sub("[a-z]*[A-Z]*[0-9]*\\s*", '', string.printable)
        self.leSpecialChars.setText(special_chars)

    @pyqtSlot()
    def generate_password(self):
        char_maps = {
            (False, False): string.ascii_lowercase,
            (True, False): string.ascii_lowercase + string.ascii_uppercase,
            (False, True): string.ascii_lowercase + string.digits,
            (True, True): string.ascii_lowercase + string.ascii_uppercase + string.digits
        }

        try:
            min_length = int(self.lePassWordMinLength.text())
            max_length = int(self.lePassWordMaxLength.text())
            if min_length < 1 or min_length > 99:
                raise Exception('Min password length out of range')
            if max_length < 1 or max_length > 99:
                raise Exception('Max password length out of range')
            if min_length > max_length:
                raise Exception('Min password length must be less or equal to max password length')
        except Exception as err:
            print(err)

            return

        special_chars = self.leSpecialChars.text()
        if self._has_duplicates(special_chars):
            print('Special chars input cannot have duplicate values')

            return

        length = random.randint(min_length, max_length)
        char_set = char_maps[(self.bUseCaps.isChecked(), self.bUseNumbers.isChecked())]

        if self.bUseSpecialChars.isChecked() and len(special_chars) != 0:
            char_set = char_set + special_chars

        print(char_set)

        pass_word = ''
        for _ in range(length):
            index = random.randint(0, len(char_set) - 1)
            pass_word = pass_word + char_set[index]

        self.lePassWordResult.setText(pass_word)

    def _has_duplicates(self, input_string):
        encountered_chars = []

        for char in input_string:
            if char in encountered_chars:
                return True
            else:
                encountered_chars.append(char)

        return False
