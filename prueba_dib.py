from spectral import *

import spectral.io.envi as envi

import numpy as np

import matplotlib as plt

from PIL import Image

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

for largo in data_img:
    for ancho in largo:
        b1 = int(ancho[40] * 255)
        b2 = int(ancho[20] * 255)
        b3 = int(ancho[10] * 255)
        data[x][y] = [b1, b2, b3]
        y = y + 1
    x = x + 1
    y = 0

img = Image.fromarray(data)

#imgplot = plt.pyplot.imshow(data)

pixmap = QPixmap().loadFromData(img)