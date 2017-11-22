import json
from umqtt import MQTTClient

class Device(object):
    """
    Losant MQTT Device class
    Used to communicate as a particular device over MQTT to Losant
    and report device state and receive commands.
    """

    mqtt_endpoint = "broker.losant.com"

    def __init__(self, device_id, key, secret):
        self._device_id = device_id
        self._key = key
        self._secret = secret

        self._mqtt_client = None
        self._initial_connect = False

    def is_connected(self):
        """ Returns if the client is currently connected to Losant """
        # pylint: disable=W0212
        return self._mqtt_client and self._mqtt_client.sock

    def connect(self):
        """ Attempts to establish a connection to Losant.
        Will be blocking or non-blocking depending on the value of
        the 'blocking' argument.  When non-blocking, the 'loop' function
        must be called to perform network activity.
        """
        if self._mqtt_client:
            return

        self._initial_connect = True

        port = 1883

        self._mqtt_client = MQTTClient(self._device_id,
                                       self.mqtt_endpoint,
                                       port,
                                       self._key,
                                       self._secret)


        print("Connecting to Losant as {}".format(self._device_id))

        resp = self._mqtt_client.connect()
        self._cb_client_connect(resp)


    def close(self):
        """ Closes the connection to Losant """
        if self._mqtt_client:
            self._mqtt_client.disconnect()

    def send_state(self, state):
        """ Reports the given state to Losant for this device """
        print("Sending state for {}".format(self._device_id))
        if not self._mqtt_client:
            return False

        payload = json.dumps({"data": state})
        self._mqtt_client.publish(self._state_topic(), payload)


    # ============================================================
    # Private functions
    # ============================================================

    def _command_topic(self):
        return "losant/{0}/command".format(self._device_id)

    def _state_topic(self):
        return "losant/{0}/state".format(self._device_id)

    def _cb_client_connect(self, response_code):
        if response_code == 0:
            return

        print("{} failed to connect, with mqtt error {}".format(self._device_id, response_code))

        if response_code in (1, 2, 4, 5):
            raise Exception("Invalid Losant credentials - error code {0}".format(response_code))
