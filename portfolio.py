class Portfolio:
    def __init__(self, starting_cash):
        self.cash = starting_cash  #amount of money
        self.positions = {}        #stocks you own and amount of shares
        self.equity_curve = []     #total value (cash + value of stocks)

    def buy(self, ticker, price, shares):
        if self.cash < price * shares:
            return
        self.cash -= price * shares
        self.positions[ticker] = self.positions.get(ticker, 0) + shares

    def sell(self, ticker, price, shares):
        if self.positions.get(ticker, 0) < shares or shares <= 0:
            return
        self.cash += price * shares
        self.positions[ticker] = self.positions.get(ticker, 0) - shares

    def update_equity(self, prices):      
        total = self.cash
        for ticker, shares in self.positions.items(): 
            total += shares * prices[ticker]
        self.equity_curve.append(total)
    #when self.positions is an empty dict, self.positions.items() returns nothing,
    #so the for loop body never runs at all, so ticker and shares are never assigned
    #prices will be a dict like {"AAPL": 150.0, "TSLA": 200.0} it contains today's closing prices



