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
batch_size = 64
lr = 0.001
holdout_ratio = 0.7

train_num = round(holdout_ratio * num_signals)
test_num = num_signals - train_num

# %% Carga Datos de entrenamiento y test
d_trn = np.zeros((num_signals, signal_len))
l_trn = np.zeros((num_signals, 1))
for i in range(5000):
    j = i + 1
    d_trn[i, :] = np.genfromtxt('./data/lapiz_lazuli ' + str(j), delimiter=',', dtype=float)
    l_trn[i] = float(0)

h = 5000
for i in range(h):
    j = i + 1
    print(j, h+i)
    d_trn[h+i, :] = np.genfromtxt('./data/cafe ' + str(j), delimiter=',', dtype=float)
    l_trn[h+i] = float(1)

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
print("Training started")

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

    print("epoch: %d\tloss: %0.10f" % (epoch, running_loss))
    loss_array.append(running_loss)


end = time.time()
print("Training complete. It took %5.2f seconds" % (end - start))

plt.figure()
plt.title("Loss")
plt.xlabel("epoch [num]")
plt.ylabel("loss [num]")
plt.plot(loss_array)
plt.show()

# %% Testing


