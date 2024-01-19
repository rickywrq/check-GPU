# Check GPU with Python
My codes to check if GPUs are available after system reinstallation and creating new conda envs.

## `conda` environments and packages backup
### Install Python Packages
```
conda install -c conda-forge opencv
conda install -c conda-forge matplotlib

conda install -c conda-forge notebook nb_conda_kernels jupyterlab tqdm
conda install -c conda-forge ipywidgets

```

## PyTorch and CUDA related
```
https://anaconda.org/nvidia/cuda-toolkit
conda install -c nvidia cuda-toolkit
```
### Install PyTorch for CUDA 11.7
[PyTorch GET STARTED](https://pytorch.org/get-started/locally/)
```
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```
Check the cuda version of pytorch installation (or if the pytorch supports cuda):
```
python3 -c "import torch; print("CUDA:", torch.version.cuda)"
```
```
python3 -c "import torch; print('Torch:', torch.__version__); print('CUDA:', torch.version.cuda); import torchvision; print('Torchvision:', torchvision.__version__)"
```

### Exports for CUDA (needed for tensorflow)
```
export CUDA_HOME=/usr/local/cuda
export PATH=${CUDA_HOME}/bin:${PATH}
export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH
```

### Problems with GCC for conda
\>\> `GLIBCXX_3.4.30' not found
\>\> [reference](https://stackoverflow.com/questions/73317676/importerror-usr-lib-aarch64-linux-gnu-libstdc-so-6-version-glibcxx-3-4-30)
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/xxx/lib
```

## Other packages
```
pip install gdown
```
