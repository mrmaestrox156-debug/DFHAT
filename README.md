DFHAT - Deep Forensic and Hunting Analysis Tool

DFHAT is a modular open-source intelligence (OSINT) and defensive security auditing tool designed for real-time target structural analysis directly from the terminal.

![DFHAT Banner](https://i.postimg.cc/QN08WLJh/Novo-projeto-535-86EE2C6.png)

Core Modules:
- LINK: HTTP routing trace and server metadata extraction.
- SITE: HTML skeleton dissection mapping active forms, input fields, and tethered scripts.
- FAKE EMAIL: Live DNS record verification and domain integrity checking.
- SPAM NUMBER: Telecommunications structural analysis and geographic area routing mapping.

![DFHAT Interface](https://raw.githubusercontent.com/mrmaestrox156-debug/DFHAT/main/1000099481.jpg)

---

Installation & Execution

Termux:
$pkg update && pkg upgrade -y$ pkg install python git -y
$git clone https://github.com/mrmaestrox156-debug/DFHAT.git$ cd DFHAT
$ python dfhat.py

Kali Linux:
$sudo apt update && sudo apt upgrade -y$ sudo apt install python3 git -y
$git clone https://github.com/mrmaestrox156-debug/DFHAT.git$ cd DFHAT
$ python3 dfhat.py

---

System Update

If the tool receives updates or to ensure script integrity, run these commands inside the project repository directory:

$git reset --hard$ git pull origin main

---

Disclaimer

This software is developed strictly for educational purposes and authorized penetration testing. Any misuse or damage caused by this tool is the sole responsibility of the operator.
