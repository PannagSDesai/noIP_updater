# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:05:54 2022

@author: panna
"""

import logging
from requests import get
import time
last_ip = ""

#No IP credentials
username = ""
password = ""

while (1):
    ip = get('https://api.ipify.org').text
    print(f'My public IP address is: {ip}')
    if last_ip != ip:
        resp = get(f'http://{username}:{password}@dynupdate.no-ip.com/nic/update?hostname=halbch-auto.ddns.net&myip={ip}').text
        last_ip = ip
        if  "nochg" not in resp or "good" not in resp:
            fh = logging.FileHandler('noIP_errors.log')
            logger.warning(resp)
            fh.setLevel(logging.WARN)
            logger.addHandler(fh)
            
    time.sleep(60)
