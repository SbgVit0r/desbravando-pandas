#%% 
import pandas as pd
#%%
dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
dados
#%%
series_dados = pd.Series(dados)
series_dados
# %%
series_dados.mean()
# %%
series_dados.std()
# %%
series_dados.max()