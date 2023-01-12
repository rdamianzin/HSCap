from spectral import *

import spectral.io.envi as envi

import numpy as np

import matplotlib.pyplot as plt


def norma(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angulo(v1, v2):
    v1_u = norma(v1)
    v2_u = norma(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))



img = envi.open('./img/008.hdr', './img/008.float')

view = imshow(img, (29, 19, 9))


# En data_trn tengo todos los datos de un pigmento.
data_trn = img[290:400, 286:390,:]

view = imshow(data_trn, (30, 20, 10))

pixel = data_trn[0][0]

n_archivo = "./data/lapiz_lazuli"
idx = 1

for largo in data_trn:
    for ancho in largo:
        a = angulo(pixel, ancho)
        if a > 0.3:
            np.savetxt(n_archivo + " " + str(idx), ancho)
            idx += 1


        
img = envi.open("./img/012.hdr", "./img/012.float")
view = imshow(img, (29, 19, 9))

data_trn = img[320:440, 50:170,:]

view = imshow(data_trn, (30, 20, 10))

