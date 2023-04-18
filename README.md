# Check GPU with Python
My codes to check if GPUs are available after system reinstallation and creating new conda envs.

## `conda` environments and packages backup
### Install Python Packages
```
conda install -c conda-forge opencv
conda install -c conda-forge matplotlib

conda install -c conda-forge notebook nb_conda_kernels jupyterlab
```

## PyTorch and CUDA related
### Install PyTorch for CUDA 11.7
[PyTorch GET STARTED](https://pytorch.org/get-started/locally/)
```
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu114
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
```
Check the cuda version of pytorch installation (or if the pytorch supports cuda):
```
python -c "import torch; print(torch.version.cuda)"
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
