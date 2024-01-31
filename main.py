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


import os
import sys
import requests
import pprint
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.get_image()
        self.initUI()

    def get_image(self):
        request = 'http://static-maps.yandex.ru/1.x/?ll=2.294494,48.858247&spn=0.0000001645799,0.0061999&l=sat'
        response = requests.get(request)
        if response:
            self.map_file = 'map.jpg'
            with open(self.map_file, 'wb') as file:
                file.write(response.content)


    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Карта')
        self.pixmap = QPixmap(self.map_file)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(800, 600)
        self.image.setPixmap(self.pixmap)

    def closeEvent(self, event):
        os.remove(self.map_file)

    def keyPressEvent(self, event):
            if event.key() == Qt.Key_Enter:
                print('Ура')
                sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

