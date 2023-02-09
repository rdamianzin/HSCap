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

img = envi.open('./img/004.hdr', "./img/004.float")

data_trn = img[50:160, 50:160,:]

# inicializo estructuras

d_renglones, d_colunmas, d_bandas = np.shape(data_trn)

idx_largo = 0

idx_ancho = 0

data_cmp = []

data_trest = []

data_clasifica = []

data_pixel_clasifica = []

#aplano la matriz de espectros y le agrgo su posicion en el arreglo original
# l_2 = l_2.astype(np.float32)

for largo in data_trn:
    for ancho in largo:
        arr_coord = np.float32([idx_largo, idx_ancho])
        arr_banda_plus = np.concatenate((ancho, arr_coord)) 
        data_trest.append([arr_banda_plus])
        idx_ancho = idx_ancho + 1
    idx_largo = idx_largo + 1
    idx_ancho = 0

# voy a hacer una lista de clases que esten muy cercanas, empiezo con 0.2

data_clases = []

data_pixel_clases = []

# %%
"""
while (len(data_trest)):
    pixel = data_trest[0]
    
    data_trest = data_trest[1:]
    
    # ojo la longitud del espectro debe de ser variable
    
    pixel = np.reshape(pixel, (d_bandas,))
    
    data_cln.append([pixel])
    
    for largo in data_trest:
        for ancho in largo:
            if (angulo(ancho, pixel) > 0):
                data_cmp.append([ancho])
    print(len(data_trest))
    data_trest = data_cmp
    data_cmp = []
"""
# %%
while (len(data_trest)):
    pixel = data_trest[0]
    
    data_trest = data_trest[1:]
    
    pixel = np.reshape(pixel, (d_bandas,))
    
    data_clasifica.append([pixel])
    
    for largo in data_trest:
        for ancho in largo:
            if (angulo(ancho, pixel) < 0.3):
                data_clasifica.append([ancho])
            else:
                data_cmp.append([ancho])
    print(len(data_trest))
    data_trest = data_cmp
    data_clases.append(data_clasifica)
    data_cmp = []
    data_clasifica = []

x = np.linspace(0, 1, 128)

for y_1 in data_clases:
    y = np.array(y_1[0])[0]
    plt.plot(x, y)













            