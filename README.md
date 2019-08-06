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

Verify the Installation `nvidia-smi`

#### Step 2 - Set up an Anaconda Environment

```
cd /tmp
sudo apt install curl
curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
```

Verify the Data Integrity of the Installer `sha256sum Anaconda3-2019.03-Linux-x86_64.sh`

Output `45c851b7497cc14d5ca060064394569f724b67d9b5f98a926ed49b834a6bb73a  Anaconda3-2019.03-Linux-x86_64.sh`

```
bash Anaconda3-2019.03-Linux-x86_64.sh
source ~/.bashrc
```
```
conda create --name sagemaker python=3.6
conda activate sagemaker
conda install -c conda-forge awscli 
```





