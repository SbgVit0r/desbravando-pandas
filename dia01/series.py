# %%
import pandas as pd

# %%
idades = [30, 20, 10, 40, 60]
idades
# %%

media = sum(idades) / len(idades)

total = 0
for i in idades:
    total += (media - i)**2

variancia = total / (len(idades) - 1)
variancia
# %%

series_idades = pd.Series(idades)
series_idades
# %%
series_idades.mean()
# %%
series_idades.var()
# %%
series_idades.median()
# %%
series_idades.quantile(0.50)
# %%
series_idades.describe()
# %%
series_idades.shape
# %%
series_idades.std()
# %%
idades[0]
# %%
series_idades[3]
# %%
series_idades.index 
# %%
series_idades.index = ['v', 'i', 't', 'o', 'r']
series_idades
# %%
series_idades.index = [80, 62, 37, 58, 23]
series_idades

# %%
series_idades.loc[62]
# %%
series_idades.iloc[2:5]
# %%
series_idades = pd.Series(idades, name='idades')
series_idades
# %%
