import yfinance as yf

def load_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data

if __name__ == "__main__":
    print(load_data("AAPL", "2020-01-01", "2021-01-01"))
