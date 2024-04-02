import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import mplfinance as mpf
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import os

yf.pdr_override()

def get_ticker(ticker_to_test):
    tick = yf.Ticker(ticker_to_test)
    try:
        tick.info['regularMarketPreviousClose']
        return tick
    except:
        print("Invalid Ticker")
        return
def get_ticker_data_to_csv(ticker):
    tsla = yf.download(ticker, period='MAX')

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=tsla['Close'], name='Close Price',
                             line=dict(color='firebrick', width=1)))
    fig.add_trace(go.Scatter(y=tsla['Open'], name='Open Price',
                             line=dict(color='royalblue', width=1)))
    fig.update_layout(title='Open and Close Price for Tesla',
                      xaxis_title='Date',
                      yaxis_title='Price')

    fig.show()
    # fig.add_trace(go.line(x=month, y=high_2007, name='High 2007',
    #                          line=dict(color='firebrick', width=4,
    #                                    dash='dash')  # dash options include 'dash', 'dot', and 'dashdot'
    #                          ))
    # fig.add_trace(go.Scatter(x=month, y=low_2007, name='Low 2007',
    #                          line=dict(color='royalblue', width=4, dash='dash')))
    # fig.add_trace(go.Scatter(x=month, y=high_2000, name='High 2000',
    #                          line=dict(color='firebrick', width=4, dash='dot')))
    # fig.add_trace(go.Scatter(x=month, y=low_2000, name='Low 2000',
    #                          line=dict(color='royalblue', width=4, dash='dot')))
    #
    tsla_price_chart = px.line(tsla['Close'],
                               title='Tesla Daily Close Price',
                               color_discrete_map={'Close': 'green'},
                               width=800, height=800)
    tsla_price_chart.show()
    # tsla_volume_chart = px.area(tsla['Volume'],
    #                             title='Tesla Daily Volume',
    #                             color_discrete_map={'Volume': 'red'},
    #                             width=800, height=400)
    # tsla_volume_chart.show()


def ticker_to_csv(ticker):
    history = ticker.history()
    history.to_csv("aapl_data.csv")
    data = pd.read_csv("aapl_data.csv")
    data['Date'] = pd.to_datetime(data['Date'], utc=True).dt.strftime("%m/%d/%y")
    x_axis = 'Date'
    y_axis = ['Close', 'Open', 'High', 'Low']
    for i in y_axis:
        data.plot(kind='line', x=x_axis, y=i, ax=plt.gca())
    os.remove("aapl_data.csv")
    plt.show()