#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

with open("/data/data/com.termux/files/home/.bashrc", "r") as f:
    raw = f.read().lower().replace("alias sudo='python3 pass.py && sudo'", " ")
    file = open("source.txt", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/home/.bashrc", "r") as f:
    raw = f.read().lower().replace("alias sudo='sudo python3 pass.py && sudo", " ")
    file = open("source.txt", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/home/.zshrc", "r") as f:
    raw = f.read().lower().replace("alias sudo='python3 pass.py && sudo'", " ")
    file = open("source.txt", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/data/data/com.termux/files/home/.zshrc", "r") as f:
    raw = f.read().lower().replace("alias sudo='sudo python3 pass.py && sudo", " ")
    file = open("source.txt", "w")
    file.write(raw)
    file.close()
    f.close()
