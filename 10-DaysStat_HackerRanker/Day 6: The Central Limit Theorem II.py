import math as m
def cdf(mn, std, x):
    return 1/2 * (1 + m.erf((x-mn)/(std*m.sqrt(2))))
print(f'{cdf(2.4*100, 2*m.sqrt(100), 250):.4f}')
