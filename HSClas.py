"""
Programa Basado en el libro de Joshua Willman
 "Modern Pyqt - Create GUI Applications for Project Management, Computer Vision, and Data Analysis"
 
 El programa se relizo con la version de PyQT 5.9.2
 
 21 de enero de 2023
"""
# %% Import necessary modules
from spectral import *

import spectral.io.envi as envi

import numpy as np

import json

from HSModel import Network

import torch

import matplotlib as plt

from PIL import Image

import sys, os, cv2
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
    QFileDialog, QMessageBox, QHBoxLayout, QVBoxLayout, QAction)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

#%% Style Sheet
style_sheet = """
    QLabel#ImageLabel{
        color: darkgrey;
        border: 2px dashed darkgrey
    }
    
    QLabel{
        qproperty-alignment: AlignCenter
    }"""
#%% classe principal
class DisplayImage(QMainWindow):
    #%% Constructor
    
    
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
        
    #%% Configuracion Ventana Principal
    def initializeUI(self):
        """Tamaño de ventana."""
        self.setMinimumSize(1200, 500)
        self.setWindowTitle('IFUNAM LANCIC')

        self.setupWindow()
        self.setupMenu()
        self.show()
    #%% Componentes de la ventna principal
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
    #%% Componentes del Menu
    def setupMenu(self):
        """Definicion del Menu."""
        # Create actions for file menu
        open_act = QAction('Abrir...', self)
        open_act.setShortcut('Ctrl+A')
        open_act.triggered.connect(self.openImageFile)

        procesa_act = QAction('Procesar', self) 
        procesa_act.setShortcut('Ctrl+P')
        procesa_act.triggered.connect(self.procesaImagen)

        # Create menu bar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add actions
        file_menu = menu_bar.addMenu('Archivo')
        file_menu.addAction(open_act)
        
        procesa_menu = menu_bar.addMenu('Procesar')
        procesa_menu.addAction(procesa_act)
        
        
    #%% Dialog de archivos , despliega la primera imagen
    def openImageFile(self):
        """Despliega la imegen del archivo elegido"""
        hdr_file, _ = QFileDialog.getOpenFileName(self, "Abrir ...", 
            os.getenv('HOME'), "HDR (*.hdr)")
        a_file = hdr_file.split('.')
        float_file = a_file[0] + '.float'

        img = envi.open(hdr_file, float_file)
        
        # este es ek arreglo que tiene los datos del archivo hiperespectral
        self.data_img = img[:,:,:]

        l, r, b = self.data_img.shape

        tipo = (l, r, 3)

        x = 0
        y = 0

        self.data = np.zeros(tipo, dtype=np.uint8)

        for largo in self.data_img:
            for ancho in largo:
                b1 = int(ancho[40] * 255)
                b2 = int(ancho[20] * 255)
                b3 = int(ancho[10] * 255)
                self.data[x][y] = [b1, b2, b3]
                y = y + 1
            x = x + 1
            y = 0
        
        image = QImage(self.data.data, self.data.shape[1], self.data.shape[0], QImage.Format_RGB888)
        
        self.original_label.setPixmap(QPixmap.fromImage(image).scaled(self.original_label.width(), 
                                                                      self.original_label.height(), 
                                                                      Qt.KeepAspectRatioByExpanding))
        

    #%% procesa imagen
    def procesaImagen(self):
        json_file, _ = QFileDialog.getOpenFileName(self, "Abrir ...", 
            os.getenv('HOME'), "JSON (*.json)")
        a_file = json_file.split('.')
        model_file = a_file[0] + ".pth"
        with open(json_file, "r") as read_file:
            data_json = json.load(read_file)
        bands = data_json['bands']
        device_str = data_json['device']
        clases_rgb = data_json['classes']
        classes = []
        device = torch.device(device_str)

        for x in clases_rgb :
            classes.append(x)
        
        model = Network(bands, classes)
        
        model.load_state_dict(torch.load(model_file))
        
        model.eval()
        
        model.to(device)
        
        
        
        


#%% script principal
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = DisplayImage()
    sys.exit(app.exec_())