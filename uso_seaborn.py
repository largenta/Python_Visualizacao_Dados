import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Gráfico de Dispersão
sns.jointplot(x = 'idade', y='salario', data = df, kind = 'scatter')  # ['scatter', 'hist', 'hex', 'kde', 'reg', 'resid']
plt.show()

# Gráfico de Densidade
plt.figure(figsize = (10,6))
sns.kdeplot(df['salario'], fill = True, color ='#863e9c')
plt.title('Densidade de Salários')
plt.xlabel('Salários')
plt.show()

# Gráfico de Pairplot - Dispersão e Histograma
sns.pairplot(df[['idade', 'salario', 'anos_experiencia']])
plt.show()

# Gráfico de Regressão
sns.regplot(x = 'idade', y = 'salario', data = df, color = '#278f65', scatter_kws = {'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Salário por Idade')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

# Gráfico countplot com hue
sns.countplot(x = 'estado_civil', hue ='nivel_educacao', data = df, palette ='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade de Clientes')
plt.legend( title = 'Nível de Educação')
plt.show()

