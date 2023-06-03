import statistics as stat
from sys import stdin, stdout
def correlation(X, Y, n):
    std_x = stat.pstdev(X)
    std_y = stat.pstdev(Y)
    m_x = stat.mean(X)
    m_y = stat.mean(Y)
    corr= 0
    for x in range(n):
        corr += (X[x]-m_x)*(Y[x]-m_y)/n
    p_coeff = corr/(std_x*std_y)
    stdout.write(str(round(p_coeff, 3)))
        
    
n = int(stdin.readline().strip())
X = list(map(float, stdin.readline().strip().split()))
Y = list(map(float, stdin.readline().strip().split()))
correlation(X, Y, n)
