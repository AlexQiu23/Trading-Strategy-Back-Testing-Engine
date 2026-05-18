import portfolio 

class Strategy:
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def on_bar(self, ticker, date, prices, data):
        pass

class SMACrossover(Strategy):
    def __init__(self, portfolio, size, short_window, long_window):
        super().__init__(portfolio)
        self.short_window = short_window
        self.long_window = long_window
        self.size = size     #amount of money to spend on shares

    def on_bar(self, ticker, date, prices, data):
        if len(data) < self.long_window:
            return
        
        close = data["Close"][ticker]
        short_ma = close.tail(self.short_window).mean()
        long_ma = close.tail(self.long_window).mean()

        if short_ma > long_ma:
            if self.size > self.portfolio.cash:
                return
            self.portfolio.buy(ticker, prices[ticker], self.size // prices[ticker])
        elif short_ma < long_ma:
            self.portfolio.sell(ticker, prices[ticker], self.portfolio.positions.get(ticker,0))

class RSIStrategy(Strategy):
    def __init__(self, portfolio, size, window = 14, oversold = 30, overbought = 70):
        super().__init__(portfolio)
        self.size = size
        self.window = window
        self.oversold = oversold
        self.overbought = overbought

    def on_bar(self, ticker, date, prices, data):
        if len(data) < self.window:
            return
        
        close = data["Close"][ticker]
        rsi = self.compute_rsi(close, self.window)

        if rsi < self.oversold:
            if self.size > self.portfolio.cash:
                return
            self.portfolio.buy(ticker, prices[ticker], self.size // prices[ticker])
        elif rsi > self.overbought:
            self.portfolio.sell(ticker, prices[ticker], self.portfolio.positions.get(ticker,0))

    def compute_rsi(self, close, window):
        pass


         

