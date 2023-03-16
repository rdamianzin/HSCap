import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
import json

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from HSModel import Network
from utils.signals import generateSignalData
import time
import os

#%% la clase de pigmentos
'''classes = {'p1':(160, 130, 10), 'p2':(230, 240, 110),   'p3':(240, 220, 70),    'p4':(240, 150, 70),    'p5':(160, 80, 10),
           'p6':(70, 40, 10),   'p7':(30, 30, 120),     'p8':(100, 70, 10),     'p9':(30, 30, 30),      'p10':(30, 0, 60),
           'p11':(60, 0, 110),  'p12':(100, 10, 200),   'p13':(120, 100, 20),   'p14':(100, 160, 10),   'p15':(100, 100, 80),
           'p16':(80, 110, 180),'p17':(40, 100, 200),   'p18':(70, 100, 150),   'p19':(120, 120, 140),  'p20':(100, 0, 0),
           'p21':(150, 0, 0),  'p22':(150, 0, 100),    'p23':(250, 150, 50),   'p24':(250, 50, 50),    'p25':(250, 100, 0)}
'''
#%% Cargamos la Informacion de modelo para poder cargar el modelo

with open("./model/t_1_pigment_net.json", "r") as read_file:
    data = json.load(read_file)
    
bands = data['bands']

clases_rgb = data['classes']




