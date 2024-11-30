# APT
sudo apt-get update
sudo apt-get install curl unzip ca-certificates zsh batcat lsd python3 python3-pip vim nano git dos2unix -y

# Add Docker's official GPG key:
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

# create the required folders
mkdir ~/.desktopstudio
mkdir ~/.desktopstudio/keys
mkdir ~/.desktopstudio/packages
mkdir ~/.desktopstudio/plugins
mkdir ~/.desktopstudio/bin


# create VENV and pip requirements
python3 -m venv ~/.desktopstudio/venv
source ~/.desktopstudio/venv/bin/activate
pip install rich

# extract and copy files
cp -r funcs ~/.desktopstudio/funcs
cp -r bin ~/.desktopstudio/bin

# add to the path the executable file
cp DesktopStudio ~/.desktopstudio/DesktopStudio
chmod +x ~/.desktopstudio/DesktopStudio