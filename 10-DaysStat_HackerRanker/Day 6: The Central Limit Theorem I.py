import math as m
def cdf(mn, std, x):
    return 1/2 * (1 + m.erf((x-mn)/(std*m.sqrt(2))))
print(f'{cdf(205*49, 15*m.sqrt(49), 9800):.4f}')
