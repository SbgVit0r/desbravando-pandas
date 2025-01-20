#%% 
import pandas as pd 
import sqlalchemy 
#%%
engine = sqlalchemy.create_engine('sqlite:///../data/database.db')

# %%
df_trans_cart = pd.read_sql_table('transactions_cart',engine)
df_trans_cart
# %%
query = 'SELECT * FROM customers LIMIT 10'
df_customers = pd.read_sql_query(query,engine)
df_customers
# %%
data_01 = {
    'id':[1,2,3,4],
    'nome':['Vitor', 'Paulo', 'Jorge', 'Souza'],
    'idade':[31,33,21,42]
}

df_01 = pd.DataFrame(data_01)

data_02 = {
    'id':[5,6,7,8],
    'nome':['Jonas', 'Mauro', 'Felipe', 'Pedro'],
    'idade':[23,19,41,18]
}

df_02 = pd.DataFrame(data_02)
# %%
df_01.to_sql('tb_TABELINHA', engine, index=False)
# %%
