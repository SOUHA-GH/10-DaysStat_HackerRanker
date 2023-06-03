import math as m
def cdf(mn, std, x):
    return 0.5 * (1 + m.erf((x-mn)/(std*m.sqrt(2))))
    
print(f'{cdf(20,2,19.5):.3f}')
print(f'{cdf(20,2,22) - cdf(20,2,20):.3f}')
