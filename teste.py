#Pacotes de análise de dados
from statistics import mean
from pandas.core import window
import pandas as pd
import pandas_datareader.data as web
import numpy as np

#Análises Gráficas
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

#Função para data
from datetime import datetime

#YFinance
import yfinance as yf
yf.pdr_override()


# Coletando dados
dados = web.get_data_yahoo('PETR4.SA', period='1y')
    
# Plotando dados com matplotlib
# plt.plot(dados['Close'])
# plt.xlabel('Data')
# plt.ylabel('Valor (R$)')
# plt.title('Preço Fechamento')
# plt.show()

# Usando função rolling para pegar dados dentro de uma janela deslizante
periodo = 5

plt.plot(dados['Close'])
plt.plot(dados['Close'].rolling(window=periodo).mean())
plt.plot(dados['Close'].rolling(window=periodo + 20).mean())
plt.title('Preço Fechamento')
plt.legend(['Close', 'Média 5 dias', 'Média 25 dias'])
plt.ylabel('Valor de fechamento')
plt.xlabel('Período')
plt.show()

