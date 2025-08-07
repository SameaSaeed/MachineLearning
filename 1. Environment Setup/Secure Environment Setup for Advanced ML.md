##### Secure Environment Setup for Advanced ML



**1. Install and Configure the Linux Environment for ML**

sudo apt update \&\& sudo apt upgrade -y



a. Install essential development tools: Tools will allow you to compile packages that are necessary for ML libraries.

sudo apt install build-essential dkms curl git wget -y



b. Add necessary PPAs and repositories: Add the Python 3.9 repository (or any other latest Python version).

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt update

sudo apt install python3.9 python3.9-venv python3.9-dev python3-pip -y



c. Secure the environment: Set up ufw (Uncomplicated Firewall) to limit unwanted access to your system.

sudo apt install ufw -y

sudo ufw allow OpenSSH  # Allow SSH

sudo ufw enable

sudo ufw status



d. Disable root access to enhance security (if necessary):

sudo passwd -l root



e. Enable fail2ban to prevent brute-force attacks:

sudo apt install fail2ban -y

sudo systemctl enable fail2ban

sudo systemctl start fail2ban



**2. Set Up Python and Virtual Environments**



a. Install Python 3.9 and pip:

sudo apt install python3-pip -y



b. Install and set up a virtual environment to isolate your ML projects:

python3 -m venv ml\_env

source ml\_env/bin/activate



c. Install Jupyter Notebook:

pip install jupyter



d. Install libraries like NumPy, Pandas, Scikit-learn, TensorFlow, and PyTorch:

pip install numpy pandas scikit-learn matplotlib seaborn tensorflow pytorch

pip install keras opencv-python pillow



**3. Secure Jupyter Notebook**



i. Set a password for Jupyter:

a. Run the following command to generate a configuration file:

jupyter notebook --generate-config



b. Set a password for Jupyter:

jupyter notebook password



ii. Configure Jupyter to use HTTPS:

You can set up SSL by generating certificates or using an existing one.

Modify the ~/.jupyter/jupyter\_notebook\_config.py to add:



c.NotebookApp.certfile = u'/path/to/your/certificate.pem'

c.NotebookApp.keyfile = u'/path/to/your/privatekey.pem'

c.NotebookApp.ip = '0.0.0.0'

c.NotebookApp.open\_browser = False

c.NotebookApp.port = 8888



**4. Test the Setup**



a. Run Jupyter Notebook:

After configuration, run:

jupyter notebook



b. Access Jupyter via https://localhost:8888 (or replace with your server IP if remote).



c. Test ML Libraries:

Open a new notebook and run the following test code:

import tensorflow as tf

print(f"TensorFlow version: {tf.\_\_version\_\_}")

print(f"PyTorch version: {torch.\_\_version\_\_}")

