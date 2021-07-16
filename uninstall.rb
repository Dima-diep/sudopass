File.write("/data/data/com.termux/files/home/.bashrc", File.open("/data/data/com.termux/files/home/.bashrc",&:read).gsub("alias sudo=\'python3 ~/sudopass/pass.py && sudo\'", " "))
File.write("/data/data/com.termux/files/home/.zshrc", File.open("/data/data/com.termux/files/home/.zshrc",&:read).gsub("alias sudo=\'python3 ~/sudopass/pass.py && sudo\'", " "))
