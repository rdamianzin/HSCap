from spectral import *

import spectral.io.envi as envi

import numpy as np

def norma(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angulo(v1, v2):
    v1_u = norma(v1)
    v2_u = norma(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

img = envi.open('./img/004.hdr', "./img/004.float")

data_trn = img[50:160, 50:160,:]

pixel = data_trn[0][0]

data_cln = [[pixel]]

data_cmp = []

idx_cln = 0

data_trest = data_trn[:, 1:, :]

# primer loop con el primer pixel

for largo in data_trest:
    for ancho in largo:
        if (angulo(ancho, pixel) > 0):
            data_cmp.append([ancho])
    
# sigo con el siguiente pixel

data_cln.append(data_cmp[0])

data_cmp = data_cmp[1:]

idx_cln = idx_cln + 1

data_paso = data_cln
            