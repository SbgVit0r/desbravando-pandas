#%%
import pandas as pd

data_01 = {
    'id':[1,2,3,4],
    'nome':['Vitor', 'Paulo', 'Jorge', 'Souza'],
    'idade':[31,33,21,42]
}

df_01 = pd.DataFrame(data_01)
df_01
# %%
data_02 = {
    'id':[5,6,7,8],
    'nome':['Jonas', 'Mauro', 'Felipe', 'Pedro'],
    'idade':[23,19,41,18]
}

df_02 = pd.DataFrame(data_02)
df_02
#%%
pd.concat([df_01, df_02]).reset_index(drop=True)
# %%
data_03 = {
    'sobrenome':['Silva', 'Costa', 'Pereira', 'Braga'],
    'renda':[3145,1243,4321,8365]
}

df_03 = pd.DataFrame(data_03).sort_values(['renda', 'sobrenome'], ascending=[False, True])
df_03
# %%

pd.concat([df_01, df_03], axis=1)
# %%
