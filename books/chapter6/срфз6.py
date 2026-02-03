import torch
from torch import nn

torch.__version__

device = "cuda" if torch.cude.is_avaliable else "cpu"
