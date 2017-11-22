import machine
from network import WLAN
import config

wlan = WLAN() # get current object, without changing the mode

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(mode=WLAN.STA)
    # configuration below MUST match your home router settings!!
    wlan.ifconfig(config=(config.STATIC_IP, config.SUBNET, config.GATEWAY, config.DNS_SERVER))

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect(config.SSID, auth=(WLAN.WPA2, config.SSID_PW), timeout=5000)
    while not wlan.isconnected():
        machine.idle() # save power while waiting
