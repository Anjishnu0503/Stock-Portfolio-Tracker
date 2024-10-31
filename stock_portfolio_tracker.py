import yfinance as yf

portfolio = {
    'RELIANCE.NS': 10,  # Reliance Industries
    'TCS.NS': 5,        # Tata Consultancy Services
    'HDFCBANK.NS': 15,  # HDFC Bank
    'INFY.NS': 8,       # Infosys
    'ITC.NS': 20        # ITC Limited
}

def fetch_current_prices(stock_symbols):
    """Fetch the latest stock prices for the given stock symbols."""
    prices = {}
    for symbol in stock_symbols:
        stock = yf.Ticker(symbol)
        latest_price = stock.history(period="1d")['Close'].iloc[-1]
        prices[symbol] = latest_price
    return prices

def display_portfolio(prices):
    """Display the stock portfolio along with current prices and total values."""
    total_portfolio_value = 0
    print(f"{'Stock Symbol':<15} {'Shares Owned':<15} {'Current Price (INR)':<20} {'Total Value (INR)':<20}")
    print("-" * 70)
    
    for symbol, shares in portfolio.items():
        current_price = prices[symbol]
        total_value_per_stock = current_price * shares
        total_portfolio_value += total_value_per_stock
        
        print(f"{symbol:<15} {shares:<15} {current_price:<20.2f} {total_value_per_stock:<20.2f}")

    print("-" * 70)
    print(f"{'Total Portfolio Value (INR):':<50} {total_portfolio_value:.2f}")

if __name__ == "__main__":
    stock_symbols = portfolio.keys()
    current_prices = fetch_current_prices(stock_symbols)

    display_portfolio(current_prices)
