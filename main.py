import io
import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from UI import Ui_MainWindow


class DrawYellowCircle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        r, g, b = randint(0, 256), randint(0, 256), randint(0, 256)
        pen = QPen(QColor(r, g, b))
        qp.setPen(pen)
        qp.setBrush(QBrush(QColor(r, g, b)))
        x = randint(1, 255)
        y = randint(1, 255)
        delta = randint(1, 100)
        qp.drawEllipse(x, y, x + delta, y + delta)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawYellowCircle()
    ex.show()
    sys.exit(app.exec_())
