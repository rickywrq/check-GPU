import sys
import torch
import torchvision
from subprocess import call
print('----------')
print('Python VERSION:', sys.version)
print('PyTorch VERSION:', torch.__version__)
print('PyTorch CUDA VERSION:', torch.version.cuda)
print('----------')
if torch.cuda.is_available():
    
    num_cuda_devices = torch.cuda.device_count()
    
    
    print('__CUDNN VERSION:', torch.backends.cudnn.version())
    print('__Number CUDA Devices:', torch.cuda.device_count())
    print('__Devices')
    call(["nvidia-smi", "--format=csv", "--query-gpu=index,name,driver_version,memory.total,memory.used,memory.free"])
    print('__Devices Properties')
    for i in range(num_cuda_devices):
        print('  ', torch.cuda.get_device_properties('cuda:{}'.format(i)))
    
    
    
    print('__Current cuda device #', torch.cuda.current_device())
    
else:
    print('CUDA is not available')
print('----------')