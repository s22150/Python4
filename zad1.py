import math


def panel_calc(a1, b1, a2, b2, c):
    pow_podlogi = a1 * b1 * 1.1
    pow_paneli = a2 * b2
    ilosc_paneli = pow_podlogi / pow_paneli
    ilosc_opakowan = math.ceil(ilosc_paneli / c)
    return ilosc_opakowan


print("Potrzeba : " + str(panel_calc(4, 4, 0.20, 1, 10)))
