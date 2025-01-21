"""
name:PVSL Deepthi date:21/01/2025
program:apply the discretization preprocessing technique for a given set
Language:python 
"""
#dicretization
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer
#create dataset
data={
'A':[4,5,12,7,4,3,1,2]
}
df=pd.DataFrame(data)
#discretize the data into 3 bins
discretizer=KBinsDiscretizer(n_bins=4,encode='ordinal',strategy='uniform')
df['A_binned']=discretizer.fit_transform(df[['A']])
print("Discretized DataFrame:n_bins=4 and strategy =uniform\n",df)
