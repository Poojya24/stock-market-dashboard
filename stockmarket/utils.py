import yfinance as yf
import plotly.graph_objs as go
from django.shortcuts import render

def get_prices(symbol):
    stock = yf.Ticker(symbol)
    prices = stock.history(period="1d", interval="1m")
    return prices

def plot_prices(prices, symbol):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=prices.index, y=prices['Close']))
    fig.update_layout(title=f"{symbol} 1min Prices", xaxis_title="Time", yaxis_title="Price")
    return fig

def stock_prices(request, symbol):
    print(symbol)
    prices = get_prices(symbol)
    print(prices)
    fig = plot_prices(prices, symbol)
    graph = fig.to_html(full_html=False)
    return render(request, 'stock_prices.html', {'graph': graph})