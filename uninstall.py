#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

with open("/data/data/com.termux/files/home/.bashrc", "r") as f:
    raw = f.read().lower().replace("alias sudo='python3 ~/sudopass/pass.py && sudo'", " ")
    file = open("/data/data/com.termux/files/home/.bashrc", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/home/.bashrc", "r") as f:
    raw = f.read().lower().replace("alias sudo='sudo python3 ~/sudopass/pass.py && sudo", " ")
    file = open("/data/data/com.termux/files/home/.bashrc", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/home/.zshrc", "r") as f:
    raw = f.read().lower().replace("alias sudo='python3 ~/sudopass/pass.py && sudo'", " ")
    file = open("/data/data/com.termux/files/home/.zshrc", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/home/.zshrc", "r") as f:
    raw = f.read().lower().replace("alias sudo='sudo python3 ~/sudopass/pass.py && sudo", " ")
    file = open("/data/data/com.termux/files/home/.zshrc", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/home/.bashrc", "r") as f:
    raw = f.read().lower().replace("alias tsu='python3 ~/sudopass/pass.py && tsu'", " ")
    file = open("/data/data/com.termux/files/home/.bashrc", "w")
    file.write(raw)
    file.close()
    f.close()


with open("/data/data/com.termux/files/home/.bashrc", "r") as f:
    raw = f.read().lower().replace("alias su='python3 ~/sudopass/pass.py && su'", " ")
    file = open("/data/data/com.termux/files/home/.bashrc", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/home/.zshrc", "r") as f:
    raw = f.read().lower().replace("alias su='python3 ~/sudopass/pass.py && su'", " ")
    file = open("/data/data/com.termux/files/home/.bashrc", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/home/.zshrc", "r") as f:
    raw = f.read().lower().replace("alias tsu='python3 ~/sudopass/pass.py && tsu'", " ")
    file = open("/data/data/com.termux/files/home/.bashrc", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/home/.bashrc", "r") as f:
    raw = f.read().lower().replace("alias su='python3 ~/sudopass/pass.py && su'", " ")
    file = open("/data/data/com.termux/files/home/.bashrc", "w")
    file.write(raw)
    file.close()
    f.close()

os.system("bash ~/sudopass/unadd.sh && cd ~ && rm -rf ~/sudopass")
