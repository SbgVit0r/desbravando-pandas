#%% 
import pandas as pd
import numpy as np

data = {
    'Nome': ['Vitor', 'João', 'Paulo', 'Marcos', 'Maria', 'João'],
    'Idade': [31, 33, 21, 24, 28, np.nan],
    'Renda': [np.nan, 2352, 2564, 2346, 3245, np.nan]
}

dataframe = pd.DataFrame(data)
# %%
dataframe
# %%
dataframe['Idade'].isna().sum()
# %%
dataframe.isna().sum()
# %%
dataframe.describe()
# %%
dataframe.isna().mean()
# %%
dataframe.fillna({'Idade': dataframe['Idade'].mean(),
'Renda': dataframe['Renda'].mean()})
# %%
dataframe.dropna(subset=['Idade', 'Renda'],how='all')
# %%
dataframe.dropna(axis=1, thresh=2)
# %%
