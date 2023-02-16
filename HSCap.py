import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from HSModel import Network
from utils.signals import generateSignalData
import time
import os

# para poner un arreglo en el archivo
# a = np.asarray([1., data_trn[0][0]], dtype="object")
# np.savetxt("paso.txt", a, delimiter = ",",fmt='%s')

   # %% parametros de los espectros

classes = ["p 1",  "p 2",  "p 3", "p 4", "p 5",
           "p 6",  "p 7",  "p 8", "p 9", "p 10",
           "p 11", "p 12", "p 13", "p 14", "p 15",
           "p 16", "p 17", "p 18", "p 19", "p 20",
           "p 21", "p 22", "p 23", "p 24", "p 25"]

Fs = 2000
signal_len = 128
t = np.linspace(0, (signal_len - 1) / Fs, signal_len)
amp_max = 10
amp_min = 0
freq_max = 100
freq_min = 10

noise_std_percent = 0.1


 # %% parametros de entrenamiento
num_signals = 10000
num_epochs = 10
batch_size = 8
lr = 0.001
holdout_ratio = 0.8

# %% Carga Datos de entrenamiento y test

l_dir = os.listdir('./data')

num_signals = len(l_dir)

d_trn = np.zeros((num_signals, signal_len))
l_trn = np.zeros((num_signals, 1))

for i in range(num_signals):
    p_arch = l_dir[i].split('_')
    d_trn[i, :] = np.genfromtxt('./data/' + l_dir[i], delimiter=',', dtype=float)
    l_trn[i] = float(p_arch[1]) - 1.0
    print('procesando:' + l_dir[i])

train_num = round(holdout_ratio * num_signals)
test_num = num_signals - train_num

data_std = np.std(d_trn)

# %% preparamos los datasets de entrenamiento y prueba
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

dataset = TensorDataset(torch.tensor(d_trn), torch.tensor(l_trn).type(torch.LongTensor))

# holdout
train_set, test_set = torch.utils.data.random_split(dataset, [train_num, test_num])

train_dataloader = DataLoader(train_set, batch_size=batch_size, shuffle=True)
test_dataloader = DataLoader(test_set, batch_size=test_num)

# %% Training

model = Network(signal_len, classes)
model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=lr)

print(model)

start = time.time()
print("Empezando el entrenamiento")

loss_array = []

for epoch in range(num_epochs):
    running_loss = 0

    for i, data in enumerate(train_dataloader, 0):
        train_signals, train_labels = data[0].to(device, dtype=torch.float), data[1].to(device, dtype=torch.float)

        # reformating the label array to the form that the loss expects
        train_labels = train_labels.view(train_labels.shape[0]).to(device)
        train_labels = train_labels.type(torch.LongTensor).to(device)

        optimizer.zero_grad()

        outputs = model(train_signals.unsqueeze(1) / data_std).to(device)
        loss = criterion(outputs, train_labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    print("epoca: %d\t perdida: %0.10f" % (epoch, running_loss))
    loss_array.append(running_loss)


end = time.time()
print("Entrenamiento Completo. Tomo %5.2f segundos" % (end - start))

plt.figure()
plt.title("Perdida")
plt.xlabel("epoca [num]")
plt.ylabel("perdida [num]")
plt.plot(loss_array)
plt.show()

PATH = './model/t_1_pigment_net.pth'
torch.save(model.state_dict(), PATH)

# %% Testing
t_tst = torch.tensor([d_trn[999]/data_std])
t_tst = t_tst.float().to(device)
o = model(t_tst)
_, predicted = torch.max(o, 1)
predicted = predicted.detach().cpu().numpy()
print(classes[predicted[0]])






