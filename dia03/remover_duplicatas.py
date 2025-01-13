#%%
import pandas as pd

data = {
    'Nome': ['Vitor', 'João', 'Paulo', 'Marcos', 'Maria', 'João'],
    'Idade': [31, 33, 21, 24, 28, 33],
    'updated_at': [1,2,3,1,2,3]
}
#%%
df = pd.DataFrame(data)
df.sort_values(by=['updated_at'], ascending=False, inplace=True)
# %%
df.drop_duplicates(subset=['Nome', 'Idade'], keep='first')
# %%
df
# %%
