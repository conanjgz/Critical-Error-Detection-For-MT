import torch
import pandas as pd
from transformers import AutoTokenizer, AutoConfig
from torch.utils.data import Dataset

class CEDDataset(Dataset):

    def __init__(self, path, huggingface_model):
        # read from tsv files
        self.df = pd.read_table(path, names=['id', 'source', 'translation', 'errors', 'error_labels'])
        
    def __len__(self):
        # length of the dataset, return the number of examples
        return len(self.df.index)

    def __getitem__(self, idx):
        # get the i-th example in the Dataset
        src_texts = self.df['source']
        trg_texts = self.df['translation']

        src_text = src_texts[idx]
        trg_text = trg_texts[idx]

        label = self.df['error_labels'][idx]
        label = 0 if label == 'NOT' else 1

        return (src_text, trg_text, label)