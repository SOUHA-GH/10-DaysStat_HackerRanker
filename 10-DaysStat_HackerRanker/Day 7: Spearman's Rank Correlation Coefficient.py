import sys
from operator import itemgetter

n = int(input())
X = list(map(float, input().rstrip().split()))
Y = list(map(float, input().rstrip().split()))
N = [i+1 for i in range(n)]

z = list(zip(X,Y))
z_X = sorted(z, key=itemgetter(0)) 
add_rx = dict(zip(z_X,N)) 
z_Y = sorted(z, key=itemgetter(1)) 
add_ry = dict(zip(z_Y,N))

add_d_sq = {x:(add_rx.get(x,0)-add_ry.get(x, 0))**2 for x in set(add_rx).union(add_ry)}
d_sq = list(add_d_sq.values())

rxy = 1 - 6*sum(d_sq)/(n*(n**2-1))       
print(round(rxy,3))    
