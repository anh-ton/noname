#!/bin/bash

# install unikey
sudo apt install ibus-unikey -y
ibus restart
ibus-daemon -drx

#install microsoft font
sudo apt install ttf-mscorefonts-installer -y