#%% 
import pandas as pd
#%%
dados = pd.read_csv('../data/ipea/homicidios.csv', sep=';')
dados
#%%
dados.info(memory_usage='deep')
# %%
dados.shape
# %%
dados.columns[0]
# %%
dados.columns[3]
# %%
