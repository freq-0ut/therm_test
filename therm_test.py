import time
import math

# Import the ADS1x15 module.
import Adafruit_ADS1x15

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

thermistor_25 = 1000000

refCurrent = 0.000005

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

# Main loop.
while True:

    adc0 = adc.read_adc(0, gain=GAIN) # Read ADC value from ADS1115

    Voltage = adc0 * (5.0 / 65535) # Replace 5.0 with whatever the actual Vcc of your Arduino is

    resistance = (Voltage / refCurrent) # Using Ohm's Law to calculate resistance of thermistor

    ln = math.log(resistance / thermistor_25) # Log of the ratio of thermistor resistance and resistance at 25 deg. C

    kelvin = 1 / (0.0033540170 + (0.00025617244 * ln) + (0.0000021400943 * ln * ln) + (-0.000000072405219 * ln * ln * ln)) # Using the Steinhart-Hart Thermistor Equation to calculate temp in K

    temp = kelvin - 273.15 # Converting Kelvin to Celcuis

    print("AIN0: ") # Print ADC value to Serial Monitor

    print(adc0)

    print("\tTemperature: ") # Print temperature to Serial Monitor in Celcius

    print(temp, 7)

    print()

    time.sleep(0.5) # Pause for half a second.