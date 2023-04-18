# Check GPU with Python
My codes to check if GPUs are available after system reinstallation and creating new conda envs.

## `conda` environments and packages backup
### Install Python Packages
```
conda install -c conda-forge opencv
conda install -c conda-forge matplotlib

conda install -c conda-forge notebook nb_conda_kernels jupyterlab
```


### Install PyTorch for CUDA 11.7
```
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu114
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
```
Check the cuda version of pytorch installation (or if the pytorch supports cuda):
```
python -c "import torch; print(torch.version.cuda)"
```

### Other packages
```
pip install gdown
```
