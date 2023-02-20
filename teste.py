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
#plt.show()

# Gráficos usando Potly 
periodo = 5

dados['Media_Movel'] = dados['Close'].rolling(window=periodo).mean()
grafico1 = px.line(
    dados,
    y='Close',
    title='Fechamento'
)
#grafico1.show()

grafico_customizado = go.Figure(
    data=go.Scatter(
        x=dados.index,
        y=dados['Close'],
        line=(dict(color='firebrick', width=3))
    )
)

grafico_customizado.update_layout(
    title='Análise de Fechamento',
    xaxis_title='Periodo',
    yaxis_title='Preço de Fechamento'
)
#grafico_customizado.show()

# Gráfico Candlestick com Potly
grafico_candlestick = go.Figure(
    data=[
        go.Candlestick(
            x=dados.index,
            open=dados['Open'],
            high=dados['High'],
            low=dados['Low'],
            close=dados['Close'],
            increasing_line_color='cyan',
            decreasing_line_color='gray',
        )
    ]
)

grafico_candlestick.update_layout(
    xaxis_rangeslider_visible=False,
    title='Análise de Fechamento',
    xaxis_title='Período',
    yaxis_title='Preço de Fechamento'
)

#grafico_candlestick.show()

# Criação de relatório
relatorio = make_subplots(
    rows=2,
    cols=1,
    specs=[
        [{'type':'scatter'}],
        [{'type':'scatter'}]
    ],
    vertical_spacing=0.075,
    shared_xaxes=True,
    subplot_titles=('Cotação', 'Fechamento')
)

#Layout e Dimensão
relatorio.update_layout(
   width=1000,
   height=800,
   title_text='<b>Advanced Analytics</b> <br> Follow-up Petrobras'
)

# Adicionando um gráfico na 1ª posição
relatorio.add_trace(
    go.Candlestick(
        x=dados.index,
        open=dados['Open'],
        high=dados['High'],
        low=dados['Low'],
        close=dados['Close'],
        increasing_line_color='green',
        decreasing_line_color='red',
    ),
    row=1,
    col=1,
)

relatorio.add_trace(
    go.Scatter(
        x=dados.index,
        y=dados['Media_Movel'],
        mode='lines',
        name='Média Móvel',
        line=dict(color='yellow')
    ),
    row=1,
    col=1
)

relatorio.update_layout(
    xaxis_rangeslider_visible=False,
)

# Adicionando um gráfico na 1ª posição
relatorio.add_trace(
    go.Scatter(
        x=dados.index,
        y=dados['Close'],
        mode='lines',
        name='Fechamento',
        line=dict(color='green')
    ),
    row=2,
    col=1
)

relatorio.add_trace(
    go.Scatter(
        x=dados.index,
        y=dados['Media_Movel'],
        mode='lines',
        name='Média Móvel',
        line=dict(color='purple')
    ),
    row=2,
    col=1
)

relatorio.update_layout(
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1,
        font=dict(size=10)
    )
)

relatorio.add_annotation(
    showarrow=False,
    text='Análise feita para fins de teste',
    font=dict(size=14),
    xref='x domain',
    x=1,
    yref='y domain',
    y=-1.4
    
)

relatorio.add_annotation(
    showarrow=False,
    text='By: Giovanna Resende',
    font=dict(size=14),
    xref='x domain',
    x=0,
    yref='y domain',
    y=-1.4
    
)

relatorio.show()

# Exportando pra PDF
relatorio.write_image('Cotação_Petrobras.pdf')