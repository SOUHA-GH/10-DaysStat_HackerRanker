import sys
import statistics as s

# Rean data
points = []
n = 0
for line in sys.stdin:
    points.append(tuple(map(int, line.rstrip().split())))
    n+=1
		
# Unzip, get 2 tuples X,Y		
X,Y = zip(*points) 

# Dot product function
def ave_dot_pd(X,Y,n):
    dot = 0
    for i in range(n):
        dot += X[i]*Y[i]
    return dot/n

# Compute Coefficients b, a ---> Y^ = a + bX
muX = s.mean(X)
muY = s.mean(Y)
b = (ave_dot_pd(X,Y,n)-muX*muY)/(ave_dot_pd(X,X,n) - muX**2)
a = muY-b*muX

# Apply for x = 80
x = 80
print(round(a + b*x,3))
