import numpy as np
from sklearn.linear_model import LogisticRegression
x=np.array([[1,2],[2,3],[3,2],[4,2],[5,1]])
y=np.array([0,1,0,1,0])
lor=LogisticRegression()
lor.fit(x,y)
w=lor.coef_
b=lor.intercept_
print("Weight (slope):",w)
print("Bias (Intercept):",b)

new_x=2
new_y=2
new_point=[(new_x,new_y)]
p=lor.predict(new_point)
print("Predicted value:",p)
