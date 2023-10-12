import sys

from PyQt5.QtWidgets import *

from PyQt5.QtGui import *

from PyQt5.QtCore import *

import utils.QtUtiles as qu

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from matplotlib.figure import Figure


class PQLabel(QLabel):
    
    def __init__(self, *args):
        super().__init__(*args)
        self.se_puede_pintar = False 
        self.pixmap = QPixmap()
        self.pixmap.fill(Qt.white)
        self.painter = QPainter()
        self.pen = QPen()
        self.last_x = None
        self.last_y = None
        self.previous_pos = None

    def paintEvent(self, event):
        return super().paintEvent(event)
    
    def mousePressEvent(self, event: QMouseEvent):
        """Override from QWidget
    
        Called when user clicks on the mouse
    
        """
        self.previous_pos = event.pos()
        QWidget.mousePressEvent(self, event)


    def mouseMoveEvent(self, event):
        current_pos = event.pos()
        self.painter.begin(self.pixmap)
        self.painter.setRenderHints(QPainter.Antialiasing, True)
        self.painter.setPen(self.pen)
        self.painter.drawLine(self.previous_pos, current_pos)
        self.painter.end()

        self.previous_pos = current_pos
        self.update()
        print(self.previous_pos, current_pos)
        QWidget.mouseMoveEvent(self, event)

        # Update the origin for next time.
        self.last_x = event.x()
        self.last_y = event.y()

    def mouseReleaseEvent(self, event):
        self.last_x = None
        self.last_y = None

    def carga_archivo(self):
        self.imagen, self.data_img = qu.openImageFile(self)
        self.pixmap = QPixmap.fromImage(self.imagen)
        self.update()



class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class wmain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(5, 30, 1500, 800)
        self.uinit()
        
    def uinit(self):
        #sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc = MplCanvas(self)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        main_layout = QHBoxLayout(self)
        der_layout = QVBoxLayout(self)
        self.push = QPushButton("Press", self)
        self.push.clicked.connect(self.abreArchivo)

        self.img_label = PQLabel()
        
        der_layout.addWidget(self.push, 5)
        der_layout.addWidget(sc, 5)
        
        main_layout.addWidget(self.img_label, 8)
        main_layout.addLayout(der_layout, 2)
        
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        
    def abreArchivo(self):
        """
        self.imagen, self.data_img = qu.openImageFile(self)
        self.canvas = QPixmap.fromImage(self.imagen)
        self.img_label.setPixmap(self.canvas)
        self.img_label.puedeDibujar = True   """
        self.img_label.carga_archivo()
        
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = wmain()
    window.show()
    sys.exit(app.exec())

