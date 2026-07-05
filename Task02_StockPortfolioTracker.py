###   PROJECT 2: STOCK PORTFOLIO TRACKER   ###

# Dictionary containing stock names and their prices
stock = {
    "Tesla": 160000,
    "NVIDIA": 760000,
    "Apple": 180000,
    "Google": 140000,
    "Microsoft": 230000,
    "Samsung": 260000
}

# Stores the total investment value
total = 0

# Create and open a file in write mode
file = open("portfolio.txt", "w")

# Write the heading in the file
file.write(f"{'=' * 10} STOCK PORTFOLIO TRACKER {'=' * 10}\n\n")
file.write("Stocks List:\n")

# Ask the user how many different stocks they own
print(">> How many different Stocks do you own?")
num = int(input(">> Enter amount of Stocks: "))

# Loop according to the number of stocks entered
for i in range(num):

    # Take stock name and quantity from the user
    name = input("\nEnter Stock Name: ")
    quantity = int(input("Enter Quantity: "))

    # Check whether the stock exists in the dictionary
    if name in stock:

        # Calculate investment for the current stock
        investment = stock[name] * quantity
        total += investment

        # Display stock details on the screen
        print(name, ":", quantity, "x", stock[name], "= $", investment)

        # Save stock details in the file
        file.write(name + " : " + str(quantity) + " x " + str(stock[name]) +
                   " = $" + str(investment) + "\n")

    else:

        # If stock is not available in the dictionary
        print("Stock not Found!")
        file.write(name + " : Stock not Found!\n")

# Display total investment
print("\nTotal Investment = $", total)

# Save total investment to the file
file.write("\nTotal Investment = $" + str(total) + "\n")
file.write("=" * 45)

# Close the file to save all changes
file.close()

print("\nPortfolio saved to portfolio.txt")
