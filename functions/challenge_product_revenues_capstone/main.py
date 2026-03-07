def calculate_revenue(prices, quantities_sold):
    revenue = []
    for price, quantity in zip(prices, quantities_sold):
        revenue.append(price * quantity)
    return revenue

def formatted_output(revenues):
    sorted_revenues = sorted(revenues, key=lambda x: x[0])
    for revenue in sorted_revenues:
        print(f"{revenue[0]} has total revenue of ${revenue[1]}")

# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))
formatted_output(revenue_per_product)

# Example of expected output line (do not remove):
print(f"{revenue_per_product[0][0]} has total revenue of ${revenue_per_product[0][1]}")