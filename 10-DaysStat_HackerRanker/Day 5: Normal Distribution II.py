import math as m
def cdf(mn, std, x):
    return 1/2 * (1 + m.erf((x-mn)/(std*m.sqrt(2))))
    
print(f'{(1 - cdf(70,10,80))*100:.2f}')
print(f'{(1 - cdf(70,10,60))*100:.2f}')
print(f'{cdf(70,10,60)*100:.2f}')
