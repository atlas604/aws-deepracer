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



