import data

def backtest(ticker, strategy, start, end):
    df = data.load_data(ticker, start, end)

    for date, row in df.iterrows():  #iterrows() loops through a DataFrame row by row
        prices = {}
        prices[ticker] = row["Close"].item()  
        history = df.loc[:date]  #give me all rows from the start up to date
        
        strategy.on_bar(ticker, date, prices, history)

        strategy.portfolio.update_equity(prices)
        #on those early days where there isn't enough history yet, the portfolio 
        #hasn't bought anything, meaning your equity is just your starting cash.
        #The equity curve will have a flat line at the start, then start moving 
        #once your strategy begins making trades.
