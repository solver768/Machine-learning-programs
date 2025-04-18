import numpy as np
from sklearn import svm
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay

X=np.array([[2,1],[1,3],[6,3]])
#testing pattern
y=np.array([-1,-1,1])

#classification based on Support Vector Classifier
sv=SVC(kernel='linear')
model=sv.fit(X,y)
#testing Pattern
new_x=2
new_y=0
new_point=[(new_x,new_y)]
p=sv.predict(new_point)
print("Support Vectors are:")
print(sv.support_vectors_)
print("predicted value:",p)
def plot_training_data_with_decision_boundary():
    #setting for plotting
    fig,ax=plt.subplots(figsize=(10,10))
    x_min,x_max,y_min,y_max=0,10,0,10
    ax.set(xlim=(x_min,x_max),ylim=(y_min,y_max))
    #plot decision boundary and margins
    common_params={'estimator':sv,'X':X,"ax":ax}
    DecisionBoundaryDisplay.from_estimator(
        **common_params,
        plot_method="contour",
        levels=[-1,0,1],
        colors=["b","r","g"],
        linestyles=["--","-","--"]
        )
    #plot samples by color and add legend
    sc=ax.scatter(X[:,0],X[:,1],c=y,s=450)
    ax.scatter(X[:,0],X[:,1],c=y,s=450)
    ax.legend(*sc.legend_elements(),loc="upper right",title="Classes")
    ax.set_title("Decision to boundaries in src")
plot_training_data_with_decision_boundary()
plt.show()
