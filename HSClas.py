"""
Programa Basado en el libro de Joshua Willman
 "Modern Pyqt - Create GUI Applications for Project Management, Computer Vision, and Data Analysis"
 
 El programa se relizo con la version de PyQT 5.9.2
 
 21 de enero de 2023
"""
# Import necessary modules
import sys, os, cv2
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
    QFileDialog, QMessageBox, QHBoxLayout, QVBoxLayout, QAction)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

style_sheet = """
    QLabel#ImageLabel{
        color: darkgrey;
        border: 2px dashed darkgrey
    }
    
    QLabel{
        qproperty-alignment: AlignCenter
    }"""

class DisplayImage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Tamaño de ventana."""
        self.setMinimumSize(1200, 500)
        self.setWindowTitle('IFUNAM LANCIC')

        self.setupWindow()
        self.setupMenu()
        self.show()

    def setupWindow(self):
        """Configuracion de la ventana principal."""
        # Create two QLabels, one for original image and one for 
        # displaying example from OpenCV
        original_img_header = QLabel("Imaagen Original")
        self.original_label = QLabel()
        self.original_label.setObjectName("ImageLabel")

        opencv_img_header = QLabel("Imagen Procesada")
        self.opencv_label = QLabel()
        self.opencv_label.setObjectName("ImageLabel")

        # Create horizontal and vertical layouts
        original_v_box = QVBoxLayout()
        original_v_box.addWidget(original_img_header)
        original_v_box.addWidget(self.original_label, 1)

        opencv_v_box = QVBoxLayout()
        opencv_v_box.addWidget(opencv_img_header)
        opencv_v_box.addWidget(self.opencv_label, 1)

        main_h_box = QHBoxLayout()
        main_h_box.addLayout(original_v_box, Qt.AlignCenter)
        main_h_box.addLayout(opencv_v_box, Qt.AlignCenter)

        # Create container widget and set main window's widget
        container = QWidget()
        container.setLayout(main_h_box)
        self.setCentralWidget(container)

    def setupMenu(self):
        """Definicion del Menu."""
        # Create actions for file menu
        open_act = QAction('Abrir...', self)
        open_act.setShortcut('Ctrl+A')
        open_act.triggered.connect(self.openImageFile)
        
        

        # Create menu bar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add actions
        file_menu = menu_bar.addMenu('Archivo')
        file_menu.addAction(open_act)
        

    def openImageFile(self):
        """Despliega la imegen del archivo elegido"""
        image_file, _ = QFileDialog.getOpenFileName(self, "Abrir ...", 
            os.getenv('HOME'), "Images (*.png *.jpeg *.jpg *.bmp)")
        
        if image_file:
            image = QImage() # Create QImage instance
            image.load(image_file)
            # Set the pixmap for the original_label using the QImage instance
            self.original_label.setPixmap(QPixmap.fromImage(image).scaled(
                    self.original_label.width(), self.original_label.height(), Qt.KeepAspectRatioByExpanding))

            # Display the image that has been converted from the OpenCV Mat object to a Qt QImage
            converted_image = self.convertCVToQImage(image_file)
            self.opencv_label.setPixmap(QPixmap.fromImage(converted_image).scaled(
                self.opencv_label.width(), self.opencv_label.height(), Qt.KeepAspectRatioByExpanding))
            self.adjustSize() # Adjust the size of the main window to better fit its contents   
        else:
            QMessageBox.information(self, "Error",
                "No pude abrir el Archivo ", QMessageBox.Ok)

    def convertCVToQImage(self, image_file):
        """Demonstrates how to load a cv image and convert the image to a Qt QImage. 
        Returns the converted Qimage."""
        cv_image = cv2.imread(image_file)
        
        # Get the shape of the image, height * width * channels. BGR/RGB/HSV images have 3 channels
        height, width, channels = cv_image.shape # Format: (rows, columns, channels)
        # Number of bytes required by the image pixels in a row; dependency on the number of channels
        bytes_per_line = width * channels
        # Create instance of QImage using data from cv_image
        converted_Qt_image = QImage(cv_image, width, height, bytes_per_line, QImage.Format_RGB888)
        return converted_Qt_image

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = DisplayImage()
    sys.exit(app.exec_())