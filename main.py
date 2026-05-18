import backtest
import strategy
import portfolio


TICKER = "AAPL"
STARTING_CASH = 100000
START = "2020-01-01"
END = "2021-01-01"

p = portfolio.Portfolio(STARTING_CASH)
s = strategy.SMACrossover(p, size=10000, short_window=20, long_window=75)
bt = backtest.backtest(TICKER, s, START, END)

final_value = p.equity_curve[-1]                                                                                                                                                                                          
total_return = (final_value - STARTING_CASH) / STARTING_CASH * 100 
print("Final Portfolio Value:", round(final_value, 2))
print("Total Return:", round(total_return, 2), "%")      