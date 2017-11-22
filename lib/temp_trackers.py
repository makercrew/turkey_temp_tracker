from machine import Pin, Timer
import config
from losant_mqtt import Device

class DinnerTracker(object):
    def __init__(self, oven_thermistor, food_thermistor, status_led=None):
        self.oven = oven_thermistor
        self.food = food_thermistor
        self.status_led = None
        self._alarm = None

        if status_led:
            self.status_led = Pin(status_led, mode=Pin.OUT, value=1)

    def report_readings(self, readings):
        raise NotImplementedError('report_readings must be defined in a subclass')

    def take_readings(self, alarm):
        if self.status_led:
            self.status_led.value(0)

        readings = {"oven": self.oven.read_temperature_in_f(),
                    "food": self.food.read_temperature_in_f()}
        self.report_readings(readings)

        if self.status_led:
            self.status_led.value(1)

    def start(self):
        self._alarm = Timer.Alarm(self.take_readings,
                                  config.UPDATE_INTERVAL_IN_SEC,
                                  periodic=True)

    def stop(self):
        if self._alarm:
            self._alarm.cancel()

class LosantDinnerTracker(DinnerTracker):
    def __init__(self, *args, **kwargs):
        self.losant_device = Device(config.LOSANT_DEVICE_ID,
                                    config.LOSANT_API_KEY,
                                    config.LOSANT_API_SECRET)

        self.losant_device.connect()
        super(LosantDinnerTracker, self).__init__(*args, **kwargs)

    def report_readings(self, readings):
        self.losant_device.send_state(readings)
