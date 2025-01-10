#%% 
import pandas as pd
#%%
df = pd.read_csv('../data/products.csv', sep=';', header=None, names=['ID', 'Name', 'Description'])
df
# %%
df.rename(columns={'Name': 'Nome', 
                   'Description':'Descricao'
                   }, inplace=True)
df
# %%
