# What is RoBERTA?
# RoBERTA with fill_mask() method

# Load ROBAERTa
import torch
roberta = torch.hub.load('pytorch/fairseq', 'roberta.large')
roberta.eval() 

# Apply Byte-Pair Encoding to input text
#tokens = roberta.encode('')
#print(tokens.tolist())
#roberta.decode(tokens) == ''
# Extract features from RoBERTa