#%% 
import pandas as pd 

# %%

# Importando o CSV
df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers
#%%

# Checando quantas linhas e colunas o DataFrame possui
df_customers.shape
# %%
# Checando informações do DataFrame (Índice das colunas, Nome, tipo de dados e uso de memória com o parâmetro 'deep')
df_customers.info(memory_usage='deep')
# %%

# Comando retornando as medidas estatísticas da coluna 'Points' como média, desvio padrão, m ediana, 1° 2° e 3° quartil, e valores minimo e maximo

df_customers['Points'].describe()
#%%

# Criando um filtro para retornar apenas as linhas onde tem pessoas com mais de 1000 pontos
condicao = df_customers['Points'] > 1000
df_customers[condicao]
# %%
maximo = df_customers['Points'].max()
condicao = df_customers['Points'] == maximo
df_customers[condicao]
# %%
condicao = df_customers['Points'] == df_customers['Points'].max()
df_maior = df_customers[condicao]
df_maior['Name'].iloc[0]
# %%
condicao = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_1000_2000 = df_customers[condicao]

df_1000_2000['Points'] = df_1000_2000['Points'] + 1000
# %%
a = [1, 2, 3, 4]
b = a.copy()
print(a)
print(b)

b.append(5)
print(a)
print(b)
# %%

df_customers[['UUID','Name']]
# %%
df_customers.columns
# %%
colunas = df_customers.columns.tolist()
colunas.sort()

df_customers = df_customers[colunas]
df_customers
# %%
df_customers.rename(columns={
    "Name": "Nome",
    "Points": "Pontos",
    "UUID": "ID"
    }, inplace=True)
# %%
df_customers
# %%
