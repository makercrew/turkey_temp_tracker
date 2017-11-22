import pycom
from machine import ADC
from network import WLAN

import config
from thermistor import Thermistor
from temp_trackers import LosantDinnerTracker

def main():
    # Use the RGB LED as an indicator of WiFi status
    pycom.heartbeat(False)
    wlan = WLAN()
    if wlan.isconnected():
        pycom.rgbled(0x000f00)
    else:
        pycom.rgbled(0x0f0000)

    # Set up the onboard ADC and establish a channel for each thermistor
    adc = ADC()
    adc.vref(config.VREF_ACTUAL_IN_MILLIAMPS)
    oven_channel = adc.channel(pin=config.OVEN_THERM_ADC_PIN, attn=ADC.ATTN_11DB)
    food_channel = adc.channel(pin=config.FOOD_THERM_ADC_PIN, attn=ADC.ATTN_11DB)

    # Modify config.py with your thermistor values from the datasheet
    oven = Thermistor(oven_channel,
                      config.THERM_NOMINAL_TEMP,
                      config.THERM_NOMINAL_RES,
                      config.THERM_BETA,
                      config.SERIES_RESISTOR_1,
                      12.0)
    food = Thermistor(food_channel,
                      config.THERM_NOMINAL_TEMP,
                      config.THERM_NOMINAL_RES,
                      config.THERM_BETA,
                      config.SERIES_RESISTOR_2,
                      12.0)

    dinner_tracker = LosantDinnerTracker(oven, food, status_led=config.STATUS_LED_PIN)
    dinner_tracker.start()

main()
