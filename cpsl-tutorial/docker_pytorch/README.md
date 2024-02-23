# Install Docker with Nvidia GPU support

## Shortcut
```
docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 -it --rm -v $HOME:$HOME -w /workspace nvcr.io/nvidia/pytorch:24.01-py3 python main.py
```


## About
* Develop like a Pro with NVIDIA + Docker + VS Code + PyTorch
https://blog.roboflow.com/nvidia-docker-vscode-pytorch/

* NVIDIA Docs Hub  NVIDIA Optimized Frameworks  NVIDIA Optimized Frameworks  Running PyTorch:
https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/running.html

* NVIDIA Docs Hub  NVIDIA Optimized Frameworks  NVIDIA Optimized Frameworks  Containers For Deep Learning Frameworks User Guide >> 5. Running A Container
https://docs.nvidia.com/deeplearning/frameworks/user-guide/index.html#runcont




## Install Docker Engine on Ubuntu:
Copied from: https://blog.roboflow.com/nvidia-docker-vscode-pytorch/


Run the following command to uninstall all conflicting packages:

```
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

apt-get might report that you have none of these packages installed.


### Install using the apt repository
Before you install Docker Engine for the first time on a new host machine, you need to set up the Docker repository. Afterward, you can install and update Docker from the repository.

1. Set up Docker's apt repository.


* Add Docker's official GPG key:
    ```
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc
    ```

* Add the repository to Apt sources:
    ```
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    ```
* Install the Docker packages.

    ```
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```


* ```sudo docker run hello-world```

    This command downloads a test image and runs it in a container. When the container runs, it prints a confirmation message and exits.

You have now successfully installed and started Docker Engine.

## Install nvidia-container-toolkit
To use the native support on a new installation of Docker, first enable the new GPU support in Docker.
$ sudo apt-get install -y docker nvidia-container-toolkit

## Some permission things...
#### create the docker group
`sudo groupadd docker`
#### add your user to the docker group
`sudo usermod -aG docker $USER`

## Pull the latest container.
Source: https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/running.html

* Pull the latest container:
`docker pull nvcr.io/nvidia/pytorch:24.01-py3`

* To run the container image, select one of the following modes:
### Interactive
If you have Docker 19.03 or later, a typical command to launch the container is:
`docker run --gpus all -it --rm -v local_dir:container_dir nvcr.io/nvidia/pytorch:<xx.xx>-py3`


* If you have Docker 19.02 or earlier, a typical command to launch the container is:
`nvidia-docker run -it --rm -v local_dir:container_dir nvcr.io/nvidia/pytorch:<xx.xx>-py3`


### Non-interactive
If you have Docker 19.03 or later, a typical command to launch the container is:
`docker run --gpus all --rm -v local_dir:container_dir nvcr.io/nvidia/pytorch:<xx.xx>-py3 <command>`


* If you have Docker 19.02 or earlier, a typical command to launch the container is:
`nvidia-docker run --rm -v local_dir:container_dir nvcr.io/nvidia/pytorch:<xx.xx>-py3 <command>`

