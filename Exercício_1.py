%pip install pandas 
import numpy as np

df_vendas = pd.read_csv('01.amazon_sales_dataset.csv')

df_vendas.dtypes
df_vendas.info()

coluna_alvo = 'discount'
# Medidas de Tendencias Centrais 
total_discount = df_vendas[coluna_alvo].sum()
media_valor_discount = df_vendas[coluna_alvo].mean()
discount_minima = df_vendas[coluna_alvo].min()
discount_maxima = df_vendas[coluna_alvo].max()
coluna_alvo