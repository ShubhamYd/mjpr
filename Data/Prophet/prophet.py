# -*- coding: utf-8 -*-
"""prophet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SIH9OLZM6PWS_sgE3E918UPeSJGG5iha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet

df = pd.read_csv('AAPL.csv')
df.head()

data = df[['Date','Close']]
data = data.rename(columns = {'Date':'ds','Close':'y'})
data.head()

train =data[0:int(len(data)*0.8)]
test = data[int(len(data)*0.8):]

from fbprophet import Prophet

m = Prophet(yearly_seasonality=True,daily_seasonality=True)
m.fit(train)

future = m.make_future_dataframe(periods = 100)
predictions = m.predict(future)
m.plot(predictions);

m.plot_components(predictions);

import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.io as pio
pio.renderers.default = 'colab'
from plotly.offline import init_notebook_mode, iplot

from fbprophet.plot import plot_plotly
fig = plot_plotly(m,predictions)
py.iplot(fig)
fig.write_html("prophet.html")