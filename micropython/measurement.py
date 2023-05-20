from machine import ADC, Pin


def tds_median(lst_voltage):

    lst_voltage = sorted(lst_voltage)
    if len(lst_voltage) % 2 != 0:
        index = (len(lst_voltage)-1)/2
        median = lst_voltage[index]
    else:
        index1 = len(lst_voltage)/2
        index2 = index1 - 1

        median = (lst_voltage[index1] + lst_voltage[index2])/2

    return median


def tds_value(lst_voltage, vref, temperatur=25):
    average_voltage = (tds_median(lst_voltage) * vref)/1024

    compensasi_temperature = 1 + 0.02*(temperatur-25)
    kompensasi_voltage = average_voltage/compensasi_temperature
    try:
        tds_value = (133 * (kompensasi_voltage**3) - 255.8 *
                     (kompensasi_voltage**2) + 857.39*kompensasi_voltage)*0.5
    except:
        tds_value = 0

    return tds_value
