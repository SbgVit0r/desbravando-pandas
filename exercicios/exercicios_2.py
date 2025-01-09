#%% 
import pandas as pd
#%%
dados = {
    "nome":["Teo", "Nah", "Napoleao"],
    "idade": [31, 12, 14]
}
dados

# %%
df_dados = pd.DataFrame(dados)
df_dados
# %%
df_dados.describe()
# %%
df_dados['idade'].mean()
# %%
df_dados['nome'].tail(1)