# NumPy (Intermediate)
#  A retail company records daily sales of 5 products across 30 days in a 2D NumPy array of shape (30, 5).
#  Due to a system error, negative values appear in the dataset.
# Task:
# Replace negative values with 0


# Compute the average weekly sales per product (assume 7 days = 1 week)


# Identify the product with the highest average weekly sales

import numpy as np
sales = np.random.randint(-10,100,(30,5))
print(sales)
sales[sales<0] = 0
print("Updated saled data: \n", sales)

#weekly sales
weekly_sales = sales[0:28].reshape(4,7,5)
#average weekly sales
avg_weekly_sales = np.mean(weekly_sales, axis=(0,1))
print("Average Weekly sales per product: \n")
print(avg_weekly_sales)

#product with highest average weekly sales
highest_product = np.argmax(avg_weekly_sales)
print("\nHighest Average Weekly Sales: ")
print("Product", highest_product + 1)



