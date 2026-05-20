import backtest
import strategy
import portfolio
import data

TICKER = "NVDA"
STARTING_CASH = 100000
START = "2023-01-01"
END = "2024-01-01"

#buy-and-hold
p_buy_hold = portfolio.Portfolio(STARTING_CASH)
df = data.load_data(TICKER, START, END)
close = df["Close"][TICKER]
first_price = close.iloc[0]
last_price = close.iloc[-1]
p_buy_hold.buy(TICKER, first_price, STARTING_CASH // first_price)

final_stock_value = last_price * p_buy_hold.positions[TICKER] + p_buy_hold.cash
total_return_bh = (final_stock_value - STARTING_CASH) / STARTING_CASH * 100
print("Final Portfolio Value when buying and holding:", round(final_stock_value, 2))
print("Total Return when buying and holding:", round(total_return_bh, 2),"%") 

#SMA Crossover strategy 
p_sma = portfolio.Portfolio(STARTING_CASH)
s = strategy.SMACrossover(p_sma, short_window=20, long_window=75)
backtest.backtest(TICKER, s, START, END)

final_value_sma = p_sma.equity_curve[-1]                                                                                                                                                                                          
total_return_sma = (final_value_sma - STARTING_CASH) / STARTING_CASH * 100 
print("Final Portfolio Value using SMA Crossover strategy:", round(final_value_sma, 2))
print("Total Return using SMA Crossover strategy:", round(total_return_sma, 2),"%") 

#RSI strategy
p_rsi = portfolio.Portfolio(STARTING_CASH)
r = strategy.RSIStrategy(p_rsi)
backtest.backtest(TICKER, r, START, END)

final_value_rsi = p_rsi.equity_curve[-1]
total_return_rsi = (final_value_rsi - STARTING_CASH) / STARTING_CASH * 100
print("Final Portfolio Value using RSI strategy:", round(final_value_rsi, 2))
print("Total Return using RSI strategy:", round(total_return_rsi, 2),"%") 