#v0.0.1

import torch

a = torch.cuda.is_available()
b = torch.device(1)
c = torch.cuda.memory_reserved(device=0)
d = torch.cuda.memory_reserved(device=1)
e = torch.cuda.memory_stats(device=0)
f = torch.cuda.memory_summary(torch.device, abbreviated=False)





print(b)
print(f"State of CUDA == {a}")
print(f"Memory Reserved on GPU1 = {c}")
print(f"Memory Reserved on GPU2 = {d}")
print(f"Memory stats for GPU1 = {e}")
print(f"Statistics on GPU1 = {f}")
#print(f"Max Memory Reserved = {max_memory_reserved()}")