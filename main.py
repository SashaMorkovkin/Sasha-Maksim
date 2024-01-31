import requests
import pprint
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import QtGui
import sys
import io
from PyQt5 import uic
from PyQt5.QtGui import QPixmap


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('01.ui', self)

    def initUI(self):
        mashtab = '5.16457,36.90619'
        geocoder_request = f'https://static-maps.yandex.ru/1.x/?ll=125.746181,-20.4' \
                           f'83765&spn={mashtab}&l=map'

        response = requests.get(geocoder_request)
        if response:
            self.map = "map.png"
            with open(self.map, "wb") as file:
                file.write(response.content)
                self.label.setPixmap(QPixmap(self.map))
        else:
            pprint.pprint("Ошибка выполнения запроса:")
            pprint.pprint(geocoder_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
