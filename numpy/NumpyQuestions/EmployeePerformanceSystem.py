# Set 2 (Employee Performance System)
# NumPy (Intermediate)
#  An HR system stores employee performance ratings (scale 1–5) for 100 employees over 4 quarters in a NumPy array.
# Task:
# Normalize the ratings using min-max normalization


# Calculate the average rating per employee


# Identify employees whose average rating is above the company mean

import numpy as np
ratings = np.random.randint(1,6,(100,4))
print("Original Ratings: \n", ratings)

#Min-max normalization
min_val = np.min(ratings)
max_val = np.max(ratings)
normalized_ratings = (ratings - min_val) / (max_val - min_val)
print("\nNormalized Ratings: \n", normalized_ratings)

# Average rating per employee
avg_ratings = np.mean(ratings, axis=1)
print("\nAverage Ratings per Employee: \n", avg_ratings)

# Company mean rating
company_mean = np.mean(avg_ratings)
print("\nCompany Mean Rating: ", company_mean)

# Employees above company mean
above_mean = np.where(avg_ratings > company_mean)[0]
print("\nEmployees Above Company Mean: ", above_mean)