import math

_NUM_SAMPLES_PER_READ = 20

class Thermistor(object):
    def __init__(self,
                 adc_channel,
                 nominal_temperature,
                 nominal_resistance,
                 beta_coefficent,
                 series_resistor,
                 adc_num_bits):

        self.adc = adc_channel
        self.nominal_temperature = nominal_temperature
        self.nominal_resistance = nominal_resistance
        self.beta_coefficent = beta_coefficent
        self.series_resistor = series_resistor
        self.adc_steps = math.pow(2, adc_num_bits) - 1
        self.debug = False

    def read_resistance(self):
        samples = []
        for i in range(_NUM_SAMPLES_PER_READ):
            samples.append(self.adc())

        average = sum(samples)/len(samples)

        if(self.debug):
            print('Average ADC reading: {}'.format(average))

        resistance = (self.adc_steps / average) - 1
        if resistance == 0:
            # We've pegged our ADC to the rails
            resistance = 0.001
        resistance = self.series_resistor / resistance

        if(self.debug):
            print('Thermistor resistance: {}'.format(resistance))

        return resistance

    def read_temperature_in_c(self):
        resistance = self.read_resistance()
        steinhart = 0.0
        steinhart = resistance / self.nominal_resistance
        steinhart = math.log(steinhart)
        steinhart /= self.beta_coefficent
        steinhart += 1.0 / (self.nominal_temperature + 273.15)
        temp_in_kelvin = 1.0 / steinhart
        temp_in_c = temp_in_kelvin - 273.15;

        return temp_in_c

    def read_temperature_in_f(self):
        return self.read_temperature_in_c() * 1.8 + 32
