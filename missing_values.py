"""

date:1st January 2025
programmer:Ponduri Venkata Sai Lakshmi Deepthi
subject:machine learning
content :handling missing values in data frame

"""

#Handling missinf values
import pandas as pd
import numpy as np
#create sample datasets
data={
    'A':[1,2,np.nan,4],
    'B':[np.nan,2,3,4],
    'C':[1,2,3,4]
    }
df=pd.DataFrame(data)
#option1:Drop missing values
df_dropped=df.dropna()
#option2:Fill missing values with the mean
df_filled=df.fillna(df.mean())
print("Data after dropping missing values:\n",df_dropped)
print("DataFrame after filling midding values:\n",df_filled)
"""
output:
Data after dropping missing values:
      A    B  C
1  2.0  2.0  2
3  4.0  4.0  4
DataFrame after filling midding values:
           A    B  C
0  1.000000  3.0  1
1  2.000000  2.0  2
2  2.333333  3.0  3
3  4.000000  4.0  4
"""
