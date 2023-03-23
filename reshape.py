from spectral import *

import spectral.io.envi as envi

import numpy as np

class mia:
    data = []
    def llena_data():
        img = envi.open("./img/004.hdr", "./img/004.float")
        
        data_img = img[:,:,:]
        
        for largo in data_img:
            for ancho in largo:
                b1 = int(ancho[40] * 255)
                b2 = int(ancho[20] * 255)
                b3 = int(ancho[10] * 255)
                data.append([b1, b2, b3])