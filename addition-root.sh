#!/bin/bash
apt install tsu root-repo
sudo chown root ~/sudopass/chpass.rb
sudo chown root ~/sudopass/pass.py
sudo chmod 500 ~/sudopass/chpass.rb
sudo chmod 500 ~/sudopass/pass.py
sudo chattr +i ~/sudopass/pass.py
sudo chattr +i ~/sudopass/chpass.rb
