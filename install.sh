#!/bin/bash

# install unikey
sudo apt install ibus-unikey -y
ibus restart
ibus-daemon -drx

#install microsoft font
sudo apt install ttf-mscorefonts-installer -y

#install onlyoffice
sudo apt install snapd -y
sudo systemctl start --now snapd
sudo systemctl enable --now snapd
sudo systemctl start --now snapd.apparmor
sudo systemctl enable --now snapd.apparmor
sudo snap install onlyoffice-desktopeditors

#install zalo
mkdir -p ~/Applications
cd ~/Applications
git clone https://github.com/realdtn2/zalo-linux-2026.git
cd zalo-linux-2026
./install.sh