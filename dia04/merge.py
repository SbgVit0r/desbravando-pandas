#%% 
import pandas as pd 

data = {
    'Id': [1,2,3,4],
    'Nomes': ['Fulano','Ciclano', 'Beltrano', 'Kikano']
}

data_users = pd.DataFrame(data)
# %%
data_users
# %%
data_users['Idade'] = [18, 21, 33, 24]
# %%
data_users
# %%
data_transacoes = {
    'id_user':[1,1,1,2,2,3,3],
    'Valor':[532,234,243,421,423,412,142],
    'qtProdutos':[5,8,12,4,3,2,1]
}

df_transaction = pd.DataFrame(data_transacoes)
df_transaction
# %%
df_transaction.merge(data_users, how='left', left_on='id_user', right_on='Id')
# %%
df_transaction.merge(data_users, how='inner', left_on='id_user', right_on='Id')
# %%
df_transaction.merge(data_users, how='right', left_on='id_user', right_on='Id')
# %%
