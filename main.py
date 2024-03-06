#v0.0.2
import torch


a = torch.cuda.is_available()
aa = torch.cuda.device_count()
aaa = torch.cuda.current_device()
b = torch.device(0)
c = torch.cuda.memory_reserved(device=0) #should be the first gpu
#d = torch.cuda.memory_reserved(device=1) #assuming you have another gpu
e = torch.cuda.memory_stats(device=0) #status of the first gpu
f = torch.cuda.memory_summary(torch.device, abbreviated=False) 





print(b)
print(f"Amount of GPUs == {aa}")
print(f"Current device == {aaa}")
print(f"State of CUDA == {a}")
print(f"Memory Reserved on GPU{000} = {c}")
#print(f"Memory Reserved on GPU2 = {d}")
print(f"Memory stats for GPU{aaa} = {e}")
print(f"Statistics on GPU{aaa} = {f}")
#print(f"Max Memory Reserved = {max_memory_reserved()}")