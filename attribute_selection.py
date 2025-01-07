"""
Date:1st January 2025
Programmer:Ponduri Venkata Sai Lakshmi Deepthi
Subject:machine learning
Content : attribute selection from the data of loas_iris by importing from scikit-learn/datasets
"""
#attribute selection
import pandas as pd
from sklearn.datasets import load_iris,load_diabetes,load_wine
from sklearn.feature_selection import SelectKBest,f_classif
#load iris dataset
d=load_diabetes()
X=pd.DataFrame(d.data,columns=d.feature_names)
Y=pd.Series(d.target)
#select the 3 features
selector=SelectKBest(score_func=f_classif,k=2)
X_selected=selector.fit_transform(X,Y)
print("Selected feature from diabetes dataset:\n",X.columns[selector.get_support()])
"""
output:
Selected feature from diabetes dataset:
 Index(['bmi', 's5'], dtype='object')
"""
