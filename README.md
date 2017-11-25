# Turkey Temperature Tracker
This repository contains the source code for the Turkey Temperature Tracker
project built with the WiPy IoT hardware platform with a [Losant](https://hubs.ly/H08M0dT0) backend. A full project writeup can be found on [Hackster.io](https://www.hackster.io/sidwarkd/turkey-temperature-tracker-b4dbd8).

# Wire Things Up
![Schematic of Turkey Temp Tracker](/schematic/temp_tracker_bb.png)

# Setting Up Losant
This project sends data to Losant as the IoT cloud platform. You can create a
free account to use with this project. For instructions on how to configure an
application in Losant to work with this project see the [walk through video](https://youtu.be/v42Tutbfan4).

# LAN Configuration for WiPy
It's easiest to communicate with the WiPy device over a local network. I
recommend configuring your LAN to reserve a static IP address for the device
so that it is easy to reconnect to it without having to look up the dynamic
address each time it boots up.

# Configuring Your Project
There are a lot of project-specific settings you must configure before running
the code on your Pycom device. All settings are found in [config.py](config.py).
The following table describes each setting.

| Setting                  |                                                                          Description                                                                         |
|--------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| SSID                     | SSID of your WiFi network                                                                                                                                    |
| SSID_PW                  | WiFi password                                                                                                                                                |
| GATEWAY                  | IP address of your router                                                                                                                                    |
| SUBNET                   | Usually 255.255.255.0                                                                                                                                        |
| STATIC_IP                | The static IP for the WiPy you setup in your router                                                                                                          |
| DNS_SERVER               | The same DNS server settings from your router                                                                                                                |
| LOSANT_DEVICE_ID         | The ID of the device created in your Losant account to track readings                                                                                        |
| LOSANT_API_KEY           | API key from the Access Key created in Losant                                                                                                                |
| LOSANT_API_SECRET        | API secret from the Access Key created in Losant                                                                                                             |
| VREF_ACTUAL_IN_MILLIAMPS | Actual internal 1.1v reference voltage value. See the [docs](https://docs.pycom.io/chapter/tutorials/all/adc.html) for instructions on how to get this value |
| UPDATE_INTERVAL_IN_SEC   | How often to take readings and send them to Losant. Default is 10 seconds.                                                                                   |
| THERM_BETA               | The Beta coefficient for the thermistor used. Found in thermistor datasheet.                                                                                 |
| THERM_NOMINAL_TEMP       | The thermistor nominal temperature. Found in thermistor datasheet.                                                                                           |
| THERM_NOMINAL_RES        | The nominal resistance of the thermistor at the nominal temperature. Found in thermistor datasheet.                                                          |
| SERIES_RESISTOR_1        | The series resistance value connected to thermistor 1                                                                                                        |
| SERIES_RESISTOR_2        | The series resistance value connected to thermistor 2                                                                                                        |
| OVEN_THERM_ADC_PIN       | The ADC pin connected to the thermistor reading oven temperature                                                                                             |
| FOOD_THERM_ADC_PIN       | The ADC pin connected to the thermistor reading food temperature                                                                                             |
| STATUS_LED_PIN           | Optional pin used to blink an indicator LED when measurements are taken                                                                                      |
