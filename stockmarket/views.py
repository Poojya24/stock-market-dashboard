import yfinance as yf
import plotly.graph_objs as go
from django.shortcuts import render

# def get_prices(symbol):
#     stock = yf.Ticker(symbol)
#     prices = stock.history(period="1d", interval="1m")
#     return prices

def get_prices(symbol):
    stock = yf.Ticker(symbol)
    # history = stock.history(period='max')
    prices = stock.history(period="1d", interval="1m")
    print(prices)
    latest_price = prices['Close'][-1]
    previous_price = prices['Close'][-2]
    change = latest_price - previous_price
    # print(prices['Close'])
    percentage_change = (change / previous_price) * 100
    return prices, round(latest_price, 2), change, round(percentage_change, 2)

def plot_prices(prices, symbol):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=prices.index, y=prices['Close']))
    fig.update_layout(title=f"{symbol} 1min Prices", xaxis_title="Time", yaxis_title="Price")
    return fig

def stock_prices(request):
    symbol = request.GET.get('symbol')
    if symbol:
        prices, latest_price, change, percentage_change = get_prices(symbol)
        # print(prices)
        # print(latest_price, change, percentage_change)
        fig = plot_prices(prices, symbol)
        graph = fig.to_html(full_html=False)
        return render(request, 'stock_prices.html', {'graph': graph, 'symbol': symbol,
                                                     'latest_price': latest_price,
                                                     'change': change, 
                                                     'percentage_change': percentage_change})
    else:
        return render(request, 'stock_prices.html')
    