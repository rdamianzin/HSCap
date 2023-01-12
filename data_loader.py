import os
import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
from natsort import natsorted

class Carga_dato(Dataset):
    def __init__(self, directorio):
         
        # Set the loading directory
        self.directorio = directorio
         
        # List all images in folder and count them
        all_arch = os.listdir(directorio)
        self.total_arch = natsorted(all_arch)

    def __len__(self):
        # Return the previously computed number of images
        return len(self.total_arch)

    def __getitem__(self, idx):
        arch_loc = os.path.join(self.directorio, self.total_arch[idx])
         
        # Use PIL for image loading
        spect = np.loadtxt(arch_loc, delimiter=",", dtype=float)
        # Apply the transformations
        tensor_spect = torch.tensor(spect)
        return tensor_spect

#  Comprobar el Dataloader  
#   for i in range(len(ds_trn)):
#    sample = ds_trn[i]
#    print(i, sample)


# Comprobar dataloader en 4 batches
#for i , spec in enumerate(dl_trn):
#    print(i, spec)
#    if i == 3:
#        break



