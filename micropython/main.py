from micropython.connect_wifi import connect
from machine import ADC, Pin
from micropython.measurement import tds_value
import utime

connect()

sensor = ADC(Pin(36))

while True:
    lst_voltage = []
    while len(lst_voltage) < 30:
        sensor.atten(ADC.ATTN_11DB)
        sensor.width(ADC.WIDTH_10BIT)
        lst_voltage.append(sensor.read())

    tds = tds_value(lst_voltage, 3.3)
    utime.sleep(2)
