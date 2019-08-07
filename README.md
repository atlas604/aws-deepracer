# AWS DeepRacer

### Local Environment Setup (Ubuntu 18.04.2 LTS)

---

#### Step 1 - Install NVIDIA Drivers

```
sudo add-apt-repository ppa:graphics-drivers
sudo apt-get update
sudo apt-get install screen
screen
sudo apt install nvidia-driver-430 && sudo reboot 
```

```
sudo apt install nvidia-cuda-toolkit
```


Verify the Installations
```
nvidia-smi
nvcc --version
```

#### Step 2 - Set up an Anaconda Environment

Download here: https://www.anaconda.com/distribution/

```
bash Anaconda3-2019.07-Linux-x86_64.sh
source ~/.bashrc
conda list
```
```
conda create --name sagemaker python=3.6
conda activate sagemaker
conda install -c conda-forge awscli 
```

#### Step 3 - 

```
git clone --recurse-submodules https://github.com/crr0004/deepracer.git
```

```
cd deepracer
pip install -U sagemaker-python-sdk/ pandas 
pip install urllib3==1.24.3
pip install ipython
```

#### Step 4 - Install Docker

https://docs.docker.com/install/linux/docker-ce/ubuntu/

https://docs.docker.com/install/linux/linux-postinstall/


Configure Default Docker Runtime to nvidia-docker 2.0

https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)


#### Step 5 - Rebuild Docker Images with GPU Support

```
cd sagemaker-tensorflow-container
python3 setup.py sdist
cp dist/sagemaker_tensorflow_container-2.0.0.tar.gz docker/1.12.0/
cd docker/1.12.0
wget https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.12.0-cp36-cp36m-linux_x86_64.whl
docker build -t 520713654638.dkr.ecr.us-west-2.amazonaws.com/sagemaker-tensorflow-scriptmode:1.12.0-gpu-py3 --build-arg py_version=3 --build-arg framework_installable=tensorflow_gpu-1.12.0-cp36-cp36m-linux_x86_64.whl -f Dockerfile.gpu .
```

Verify the Images

```
docker images
```

#### Step 5 - Build the sagemaker-container



