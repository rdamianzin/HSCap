from spectral import *

import spectral.io.envi as envi

import numpy as np

#%%  Funcion para nombrar los archivos

def graba_archivo(archivo):
    idx = 1

    for largo in data_trn:
        for ancho in largo:
            np.savetxt(archivo + str(idx), ancho)
            idx += 1

# Se extraeran los espectros de las muestra de la tabla de pigmentos
#%% tomaremos el archivo 004 como la parte superior izquierda y numeramos los rectangulos de 
# izquierda a derecha de arriba abajo.

img = envi.open('./img/004.hdr', "./img/004.float")

view = imshow(img, bands = (29, 19, 9))

  # primer cuadro esquina superior (50, 50) esquina opuesta inferior (160, 160)

data_trn = img[50:160, 50:160,:]

#view = imshow(data_trn, bands = (29, 19, 9))

n_archivo = "./data/pigmento_1_"  

graba_archivo(n_archivo)
  
  # Segundo cuadro esquina superior (290, 50) esquina opuesta inferior (400, 160)

data_trn = img[50:160, 290:400,:]

n_archivo = "./data/pigmento_2_"

graba_archivo(n_archivo)

  # Tercero cuadro esquina superior (540, 50) esquina opuesta inferior (650, 160)

data_trn = img[50:160, 540:650,:]

n_archivo = "./data/pigmento_3_"

graba_archivo(n_archivo)
  
  # Cuarto cuadro esquina superior (40, 300) esquina opuesta inferior (150, 415)
  
data_trn = img[300:415, 40:150,:]

n_archivo = "./data/pigmento_4_"

graba_archivo(n_archivo)

  # Quinto cuadro esquina superior (290, 300) esquina opuesta inferior (400, 415)

data_trn = img[300:415, 290:400,:]

n_archivo = "./data/pigmento_5_"

graba_archivo(n_archivo)

  # Sexto cuadro esquina superior (540, 300) esquina opuesta inferior (650, 415)  

data_trn = img[300:415, 540:650,:]

n_archivo = "./data/pigmento_6_"

graba_archivo(n_archivo)

#%% Siguiente archivo 005 imagenes 7, 8, 9, 10
img = envi.open('./img/005.hdr', "./img/005.float")

#septimo cuadro esquina superior (310, 50) esquina opuesta inferior (400,160)

data_trn = img[50:160, 310:400,:]

n_archivo = "./data/pigmento_7_"

#octavo cuadro esquina superior (545, 50) esquina opuesta inferior (645, 160)

data_trn = img[50:160, 545:645,:]

n_archivo = "./data/pigmento_8_"

#noveno cuadro esquina superior (290, 300) esquina opuesta inferior (400, 415)

data_trn = img[300:415, 290:400,:]

n_archivo = "./data/pigmento_9_"

#decimo cuadro esquina superior (540, 300) esquina opuesta inferior (650, 410)

data_trn = img[300:410, 540:650,:]

n_archivo = "./data/pigmento_10_"


#%% Suiguiente Archivo 008 imagenes 11, 12, 13, 14, 15, 16

img = envi.open('./img/008.hdr', "./img/008.float")

#undecimo cuadro esquina superior (40, 50) esquina opuesta inferior (150, 160)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_11_"

#duodecimo cuadro esquina superior (280, 50) esquina opuesta inferior (400, 160)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_12_"

#decimotercero cuadro esquina superior (550, 50) esquina opuesta inferior (640, 160)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_13_"

#decimocuarto cuadro esquina superior (40, 290) esquina opuesta inferior (150, 400)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_14_"

#decimoquinto cuadro esquina superior (280, 290) esquina opuesta inferior (390, 400)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_15_"

#decimosexto cuadro esquina superior (530, 290) esquina opuesta inferior (640, 400)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_16_"


#%% Siguiente Archivo 010 imagenes 17, 18, 19, 20

img = envi.open('./img/010.hdr', "./img/010.float")

#decimoseptimo cuadro esquina superior (290, 50) esquina opuesta inferior (400, 160)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_17_"

#decimoseptimo cuadro esquina superior (540, 50) esquina opuesta inferior (650, 160)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_18_"

#decimoseptimo cuadro esquina superior (290, 290) esquina opuesta inferior (400, 400)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_19_"

#decimoseptimo cuadro esquina superior (530, 290) esquina opuesta inferior (650, 410)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_20_"

#%% Suiguiente Archivo 014 imagenes 21, 22, 23

img = envi.open('./img/014.hdr', "./img/014.float")

#decimoseptimo cuadro esquina superior (530, 290) esquina opuesta inferior (650, 410)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_21_"

#decimoseptimo cuadro esquina superior (530, 290) esquina opuesta inferior (650, 410)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_22_"

#decimoseptimo cuadro esquina superior (530, 290) esquina opuesta inferior (650, 410)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_23_"


#%% Siguiente Archivo 012 imagenes 24, 25

#decimoseptimo cuadro esquina superior (530, 290) esquina opuesta inferior (650, 410)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_24_"

#decimoseptimo cuadro esquina superior (530, 290) esquina opuesta inferior (650, 410)

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_25_"


img = envi.open('./img/012.hdr', "./img/012.float")

