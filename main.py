import backtest
import strategy
import portfolio
import data
import matplotlib.pyplot as plt

TICKER = "NVDA"
STARTING_CASH = 100000
START = "2023-01-01"
END = "2024-01-01"

#buy-and-hold
p_buy_hold = portfolio.Portfolio(STARTING_CASH)
df_bh = data.load_data(TICKER, START, END)
close = df_bh["Close"][TICKER]
first_price = close.iloc[0]
last_price = close.iloc[-1]
p_buy_hold.buy(TICKER, first_price, STARTING_CASH // first_price)

final_stock_value = last_price * p_buy_hold.positions[TICKER] + p_buy_hold.cash
total_return_bh = (final_stock_value - STARTING_CASH) / STARTING_CASH * 100
print("Final Portfolio Value when buying and holding:", round(final_stock_value, 2))
print("Total Return when buying and holding:", round(total_return_bh, 2),"%")

plt.plot(close.index, close * p_buy_hold.positions[TICKER] + p_buy_hold.cash, label = "Buy and Hold")


#SMA Crossover strategy 
p_sma = portfolio.Portfolio(STARTING_CASH)
s = strategy.SMACrossover(p_sma, short_window=20, long_window=75)
backtest.backtest(TICKER, s, START, END)

final_value_sma = p_sma.equity_curve[-1]                                                                                                                                                                                          
total_return_sma = (final_value_sma - STARTING_CASH) / STARTING_CASH * 100 
print("Final Portfolio Value using SMA Crossover strategy:", round(final_value_sma, 2))
print("Total Return using SMA Crossover strategy:", round(total_return_sma, 2),"%")

df_sma = data.load_data(TICKER, START, END)
date = df_sma.index                             #.index returns the row labels of a DataFrame which gives a sequence of dates like [2023-01-03, 2023-01-04, 2023-01-05, ...]
plt.plot(date, p_sma.equity_curve, label = "SMA Crossover")


#RSI strategy
p_rsi = portfolio.Portfolio(STARTING_CASH)
r = strategy.RSIStrategy(p_rsi)
backtest.backtest(TICKER, r, START, END)

final_value_rsi = p_rsi.equity_curve[-1]
total_return_rsi = (final_value_rsi - STARTING_CASH) / STARTING_CASH * 100
print("Final Portfolio Value using RSI strategy:", round(final_value_rsi, 2))
print("Total Return using RSI strategy:", round(total_return_rsi, 2),"%") 

df_rsi = data.load_data(TICKER, START, END)
date = df_rsi.index
plt.plot(date, p_rsi.equity_curve, label = "RSI")


#Plot equity curves
plt.title("Equity Curves")
plt.xlabel("Time")
plt.ylabel("Portfolio Value")
plt.legend()
plt.show()