# downloading the zip

# APT
sudo apt install docker-compose unzip -y

# create the required folders
mkdir ~/.desktopstudio

# extract and copy files
unzip release.zip
cp -r release/defaults ~/.desktopstudio/