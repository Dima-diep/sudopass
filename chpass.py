#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

with open("/data/data/com.termux/files/home/sudopass/pass.py", "r") as f:
    raw = f.read().lower().replace("oldpass", "newpass")
    file = open("/data/data/com.termux/files/home/sudopass/pass.py", "w")
    file.write(raw)
    file.close()
    f.close()
