import yfinance as yf

portfolio = {}

def add_stock(ticker, shares, purchase_price):
    portfolio[ticker.upper()] = {
        'shares': shares,
        'purchase_price': purchase_price
    }

def remove_stock(ticker):
    portfolio.pop(ticker.upper(), None)

def fetch_current_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")['Close'].iloc[-1]
        return price
    except:
        return None

def show_portfolio():
    print("\n📊 Your Portfolio:")
    total_value = 0
    for ticker, data in portfolio.items():
        current_price = fetch_current_price(ticker)
        if current_price is None:
            print(f"{ticker}: Error fetching price.")
            continue
        value = current_price * data['shares']
        gain = (current_price - data['purchase_price']) * data['shares']
        print(f"{ticker}: {data['shares']} shares @ ${data['purchase_price']} | "
              f"Current: ${current_price:.2f} | Value: ${value:.2f} | Gain/Loss: ${gain:.2f}")
        total_value += value
    print(f"Total Portfolio Value: ${total_value:.2f}\n")

def menu():
    while True:
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Show Portfolio")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            ticker = input("Enter stock ticker: ")
            shares = float(input("Enter number of shares: "))
            price = float(input("Enter purchase price per share: "))
            add_stock(ticker, shares, price)
        elif choice == "2":
            ticker = input("Enter stock ticker to remove: ")
            remove_stock(ticker)
        elif choice == "3":
            show_portfolio()
        elif choice == "4":
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    print("📈 Stock Portfolio Tracker")
    menu()

