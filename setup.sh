#!bin/bash
echo"[*] Before running Tool You must Install Some Packages"
echo "Update & Upgrade"
apt update && apt upgrade -y
apt install figlet -y
figlet HawkHackers
echo "Python and Python2"
apt install python -y
apt install python2 -y
echo "installing modules"
pip install pygeoip
echo "DONE1!"
figlet "Done!!!"
