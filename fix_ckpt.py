# The original ckpt doesn't have "__author__" key, which will 
# cause Detectron2 to rename many keys containing "_". This script
# is used to add "__author__" key to the ckpt.
import torch
import sys

ckpt = torch.load(sys.argv[1])
new_ckpt = { "model": ckpt["model"], "__author__": "torchvision", "matching_heuristics": True }
torch.save(new_ckpt, sys.argv[2])
