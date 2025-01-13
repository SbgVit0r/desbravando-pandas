#%% 
import pandas as pd
#%%
import numpy as np
#%%
import re
#%%
df = pd.read_csv('../data/customers.csv', sep=';')
df
#%%
df['Points_dobble'] = df['Points'] * 2
df
# %%
df['Points_ratio']= df['Points_dobble'] / df['Points']
df 
# %%
df['Constante'] = 1
df
# %%
df['Points_log']= np.log(df['Points'])
df
# %%
df['Name'].str.upper()
# %%
df['Name'].str.split('_').str[0]
# %%
def pegar_primeiro(nome):
    return nome.split("_")[0]

# %%
pegar_primeiro('Fulano_Silva')
# %%
df['Name'].apply(pegar_primeiro)
# %%
get_f = lambda nome: nome.split('_')[0]
get_f("Pedro")
#%%
df['Name'].apply(lambda x: x.split('_')[0])
# %%
def intervalo_pontos(pontos):
    if pontos < 2500:
        return 'Baixo'
    elif pontos < 3500:
        return 'Médio'
    else:
        return 'Alto'
    
df['Faixa_Points'] = df['Points'].apply(intervalo_pontos)
df
# %%
data = {
    "nome": ['Vitor', 'Paulo', 'Jonas', 'Felipe'],
    "recencia": [30, 45, 1, 10],
    "valor": [2000, 300, 1500, 1300],
    'frequencia': [1, 3, 2, 5]
}

dataframe = pd.DataFrame(data)

# %%
dataframe
# %%
def calc_crm(linha):
    if linha['recencia'] > 15:
        nota =+ 0
    elif linha['recencia'] < 15:
        nota =+ 5
    
    if linha['frequencia'] >= 2:
        nota += 5
    else:
        nota += 0
        
    return nota

dataframe['RFV'] = dataframe.apply(calc_crm, axis=1)
# %%
dataframe
# %%
