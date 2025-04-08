import numpy as np
from sklearn.linear_model import LinearRegression
x=np.array([[5,4],[3,2],[2,2]])
y=np.array([4,2,3])
lr=LinearRegression()
lr.fit(x,y)
w=lr.coef_
b=lr.intercept_
print("Weight (slope):",w)
print("Bias (Intercept):",b)
