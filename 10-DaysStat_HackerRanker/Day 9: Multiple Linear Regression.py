from sklearn import linear_model
from numpy import multiply as mult
m,n = map(int, input().split())
lst_features, lst_y = [], []

for _ in range(n):
    *features, y = map(float, input().split())
    lst_features.append(features)
    lst_y.append(y)

lm = linear_model.LinearRegression()
lm.fit(lst_features, lst_y)
a = lm.intercept_
b = lm.coef_

for _ in range(int(input())):
    feature_set = list(map(float, input().split()))
    mult_sum = sum(mult(b, feature_set))
    print(round(a + mult_sum, 2))
