# Check GPU with Python
My codes to check if GPUs are available after system reinstallation and creating new conda envs.

## `conda` environments and packages backup
### Install Python Packages
```
conda install -c conda-forge opencv
conda install -c conda-forge matplotlib

conda install -c conda-forge notebook nb_conda_kernels jupyterlab
```


### Install PyTorch for CUDa 11.4
```
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu114
```

### Other packages
```
pip install gdown
```