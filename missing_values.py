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
print("Data after dropping missing values:",df_dropped)
print("DataFrame after filling midding values:",df_filled)
