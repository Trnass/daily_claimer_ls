# Christmas Daily Claimer LeoSight
## Popis aplikace
Aplikace slouží k sbírání daily rewards na Vánoční kalendář na portálu LeoSight.
## Potřébná fakta
Musíme si vytvořit složku, v mém případě je to /var/py_cron/christmas_daily_leosight
Musíme instalovat několik knihoven, chromium a chromedriver, vším si projdeme během dalších několika kroků.
Aplikace je psaná v Pythonu3 verze 3.9.2
Všechny příkazy spouštíme ve složce kterou jsme vytvořili.
Chromedriver následně přesuneme do složky /etc/drivers/chromedriver
## Instalace potřebných závislostí
sudo apt update
sudo apt upgrade
sudo apt install -y wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
wget https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mkdir /etc/drivers
mkdir /etc/drivers/chromedrive
sudo mv chromedriver /etc/drivers/chromedriver
sudo chmod +x /etc/drivers/chromedriver
export PATH=$PATH:/etc/drivers/chromedriver
pro ověření instalace spustíme chromedriver --version
pip3 install selenium
## Povolení spuštění
chmod +x /var/py_cron/christmas_daily_leosight/main.py
## Vytvoření CRONu
crontab -e
55 4 * * * /usr/bin/python3 /var/py_cron/christmas_daily_leosight/main.py
