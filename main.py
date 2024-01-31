import requests
import pprint
import pygame
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import QtGui
import sys
import io
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

mashtab = '5.16457,36.90619'
geocoder_request = f'https://static-maps.yandex.ru/1.x/?ll=125.746181,-20.4' \
                   f'83765&spn={mashtab}&l=map'

response = requests.get(geocoder_request)


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('01.ui', self)
        if response:
            map = "map.png"
            with open(map, "wb") as file:
                file.write(response.content)
                self.pix = QtGui.QPixmap(file)
                self.image = QPixmap(self.pix)
                self.label.setPixmap(self.image)
        else:
            pprint.pprint("Ошибка выполнения запроса:")
            pprint.pprint(geocoder_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())