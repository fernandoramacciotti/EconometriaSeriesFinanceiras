# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

import plotly
plotly.offline.init_notebook_mode()
import plotly.offline as po
import plotly.plotly as py
import plotly.graph_objs as go
import cufflinks as cf
import plotly.figure_factory as ff

symbols = ['ITUB4', 'ABEV3', 'BBDC4', 'PETR4', 'VALE5']
taxas = ['risk_free', 'ipca']

dados = pd.DataFrame()
for stock in symbols:
    df_p = pd.read_csv('./dados/' + stock + '.SA_price.csv', index_col = 0, usecols = ['Date', 'Adj Close'])
    df_p.columns = [stock + '_price']
    df_p.index.name = 'Dates'   
    dados = pd.concat([dados, df_p],join='outer',axis=1)

# data frame de ipca e risk_free
ipca = pd.read_csv('./dados/ipca.csv', index_col = 0, sep = ';')
ipca.index.name = 'Dates'
risk_free = pd.read_csv('./dados/risk_free.csv', index_col = 0, sep = ';')
risk_free.index.name = 'Dates'


# dataframe consolidado de precos, ipca e rf
#dados = pd.concat([dados, ipca, risk_free], join = 'outer', axis = 1)


# dataframe de dividendos
for stock in symbols:
    df_d = pd.read_csv('./dados/' + stock + '.SA_dividend.csv', index_col = 0)
    df_d.columns = [stock + '_div']
    df_d.index.name = 'Dates'