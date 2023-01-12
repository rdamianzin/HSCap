from spectral import *

import spectral.io.envi as envi

import numpy as np

img = envi.open('./img/008.hdr', "./img/008.float")

view = imshow(img, bands = (29, 19, 9))

data_trn = img[290:400, 286:390,:]

pixel = data_trn[0][0]

n_archivo = "./data/lapiz_lazuli"
idx = 1

for largo in data_trn:
    for ancho in largo:
        np.savetxt(n_archivo + " " + str(idx), ancho)
        idx += 1

img = envi.open('./img/012.hdr', "./img/012.float")

data_trn = img[320:430, 50:170,:]

pixel = data_trn[0][0]

n_archivo = "./data/cafe"
idx = 1

for largo in data_trn:
    for ancho in largo:
        np.savetxt(n_archivo + " " + str(idx), ancho)
        idx += 1