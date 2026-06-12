stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150
}

total = 0

while True:
    stock = input("Enter stock name (or 'done'): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        qty = int(input("Enter quantity: "))
        total += stocks[stock] * qty
    else:
        print("Stock not found!")

print("Total Investment Value: $", total)
