class Strategy:
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def on_bar(self, ticker, date, prices, data):
        pass

class SMACrossover(Strategy):
    def __init__(self, portfolio, short_window, long_window):
        super().__init__(portfolio)
        self.short_window = short_window
        self.long_window = long_window

    def on_bar(self, ticker, date, prices, data):
        if len(data) < self.long_window:
            return
        
        close = data["Close"][ticker]
        short_ma = close.tail(self.short_window).mean()
        long_ma = close.tail(self.long_window).mean()

        if short_ma > long_ma:
            if self.portfolio.positions.get(ticker,0) == 0:   #buy only you dont have positions, or after selling positions
                self.portfolio.buy(ticker, prices[ticker],  (self.portfolio.cash * 0.5) // prices[ticker]) #invest 50% of available cash
        elif short_ma < long_ma:
            self.portfolio.sell(ticker, prices[ticker], self.portfolio.positions.get(ticker,0))

class RSIStrategy(Strategy):
    def __init__(self, portfolio, window = 14, oversold = 30, overbought = 70):
        super().__init__(portfolio)
        self.window = window
        self.oversold = oversold
        self.overbought = overbought

    def on_bar(self, ticker, date, prices, data):
        if len(data) < self.window:
            return
        
        close = data["Close"][ticker]
        rsi = self.compute_rsi(close, self.window)

        if rsi <= self.oversold:
            if self.portfolio.positions.get(ticker,0) == 0:
                self.portfolio.buy(ticker, prices[ticker], (self.portfolio.cash * 0.5) // prices[ticker])
        elif rsi >= self.overbought:
            self.portfolio.sell(ticker, prices[ticker], self.portfolio.positions.get(ticker,0))

    def compute_rsi(self, close, window):
        diff = close.diff()
        gains = diff.clip(lower=0) #positive daily change
        losses = diff.clip(upper=0).abs() #negative daily change
        mean_gains = gains.rolling(window).mean()   #rolling() calculates the mean over a specific time window
        mean_losses = losses.rolling(window).mean()
        rs = mean_gains/mean_losses
        rsi= 100 - (100 / (1 + rs))
        return rsi.iloc[-1].round(2) #rsi is a series of rsi values


         

