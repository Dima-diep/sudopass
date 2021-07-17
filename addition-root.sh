#!/bin/bash
apt install tsu root-repo
sudo chown root ~/sudopass/chpass.py
sudo chown root ~/sudopass/pass.py
sudo chmod 511 ~/sudopass/chpass.py
sudo chmod 511 ~/sudopass/pass.py
sudo chattr +i ~/sudopass/pass.py
sudo chattr +i ~/sudopass/chpass.py
