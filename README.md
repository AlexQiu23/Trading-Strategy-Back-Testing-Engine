**Trading Strategy Backtesting Engine**

A modular, event-driven backtesting framework written in Python for simulating and evaluating trading strategies on historical stock data. Built with object-oriented design principles so new strategies can be added without modifying the core engine.

**Overview**

This project simulates how a given trading strategy would have performed over historical stock data. It loops through each trading day bar by bar, lets the strategy decide whether to buy or sell, tracks the resulting portfolio value over time, and produces an equity curve that can be compared against a buy-and-hold benchmark.
The engine is designed around a clean separation of concerns:

  - **Data** — fetches historical price data via the yfinance API

  - **Portfolio** — tracks cash, positions, and equity over time

  - **Strategy** — an abstract base class defining the contract any trading strategy must follow

  - **Backtest** — orchestrates the event loop, feeding each bar/day to the strategy

**Implemented Strategies**

**SMA Crossover** — A trend-following strategy. Buys when the short-window simple moving average crosses above the long-window simple moving average (a "golden cross") and sells on the reverse crossover (a "death cross"). Default windows are 20 and 75 days.

**RSI Mean Reversion** — A mean-reverting strategy using the Relative Strength Index. Buys when RSI drops below the oversold threshold (default 30) and sells when RSI rises above the overbought threshold (default 70). Default RSI window is 14 days, following the standard convention from Wilder (1978).

New strategies can be plugged in by overriding the on_bar method. The core engine never needs to change.

**Requirements**

- Python 3.10+
- pandas
- yfinance
- matplotlib

Install dependencies:

pip install pandas yfinance matplotlib

**Known Limitations**

The project is in active development. Current limitations I'm aware of:

- **Look ahead bias**. Trades currently execute at the closing price of the bar that generated the signal, which introduces mild lookahead bias. Next planned change is to execute fills at the following bar's open price.

- **No transaction costs**. Commissions and slippage are not yet modeled. Adding even a modest 0.1% per-trade cost meaningfully impacts strategy returns and will be added.

- **Single ticker**. The engine currently backtests one ticker at a time. Multi-asset portfolios are not yet supported.











