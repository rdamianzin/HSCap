from spectral import *

import spectral.io.envi as envi

import sys, os, cv2
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QFileDialog, QMessageBox, QHBoxLayout, QVBoxLayout, QAction)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

img = envi.open('./HSDiego/006.hdr', "./HSDiego/006.float")

view = imshow(img, bands = (29, 19, 9))

data_img = img[:,:,:]

l, r, b = data_img.shape

tipo = (l, r, 3)

x = 0
y = 0


data = np.zeros(tipo)

for largo in data:img:
    for ancho in largo:
        b1 = ancho[40]
        b2 = ancho[20]
        b3 = ancho[10]
        data[x][y] = [b1, b2, b3]
        y = y + 1
    x = x + 1

pixmap = QPixmap().loadFromData(data_img)