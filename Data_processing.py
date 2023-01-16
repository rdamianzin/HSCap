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

#%% Siguiente archivo 
img = envi.open('./img/005.hdr', "./img/005.float")

#septimo cuadro esquina superior () esquina opuesta inferior

data_trn = img[320:430, 50:170,:]

n_archivo = "./data/pigmento_7_"


