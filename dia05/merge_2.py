#%%
import pandas as pd 

df_customer = pd.read_csv('../data/customers.csv', sep=';')
df_customer
# %%
df_transactions = pd.read_excel('../data/transactions.xlsx')
df_transactions
# %%
df_transactions.merge(df_customer, how='inner'
, left_on='IdCustomer', right_on='UUID', suffixes=['_transacao', '_cliente'])

# %%
