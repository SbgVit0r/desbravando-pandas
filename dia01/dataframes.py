#%%
import pandas as pd
#%%
data = {
    "nome":['vitor', 'marcos', 'maria', 'jose'],
    "sobrenome":['souza', 'nobrega', 'silva', 'santos'],
    "idade":[31, 32, 35, 48]
}
data
# %%
# Retorna idade da primeira pessoa
data['idade'][0]
# %%
df = pd.DataFrame(data)
df
# %%
df['idade']
# %%
type(df['idade'])
# %%
# Retorna idade da primeira pessoa
df['idade'].iloc[0]
# %%
type(df.loc[0])
# %%
df.loc[0]
# %%
df.index = [3,2,1,5]
df
# %%
df.columns
# %%
df.info(memory_usage='deep')
# %%
df.dtypes
# %%
df.describe()
# %%
df['altura'] = [174, 163, 178, 182]
alturas = df.describe()
alturas
# %%
alturas['altura']['std']
# %%
df.head(2)
# %%
df.tail(2)
# %%
