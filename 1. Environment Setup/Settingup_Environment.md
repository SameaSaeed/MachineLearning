Setting Up AI Project

Step 1: Set Up a Python Virtual Environment
sudo apt update
sudo apt install python3
sudo apt install python3-pip

Install python3-venv if not already available:
sudo apt install python3-venv -y

Create a virtual environment:
python3 -m venv dl-env

Activate the environment:
source dl-env/bin/activate

Step 2: Install Deep Learning Libraries

Step 3: Launch Jupyter Notebook to verify:
jupyter notebook
Press Ctrl+C to stop the notebook server after confirming it starts.

Step 4: Install Docker and Run a Container

Install Docker:
sudo apt install docker.io -y

Start and enable the Docker service:
sudo systemctl start docker
sudo systemctl enable docker

Run a simple container to verify:
sudo docker run hello-world
This confirms that Docker is working correctly.