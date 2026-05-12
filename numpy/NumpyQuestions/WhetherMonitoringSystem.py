# Set 3 (Weather Monitoring System)
# NumPy (Intermediate)
#  A weather station stores hourly temperature readings for 7 days in a NumPy array of shape (7, 24).
# Task:
# Find the daily maximum and minimum temperature


# Identify the day with the largest temperature variation


# Replace outliers beyond ±2 standard deviations with the mean temperature


import numpy as np
temp = np.random.randint(10,50,(7,24))
print("Original Temperature Data: \n", temp)
# Daily max and min
daily_max = np.max(temp, axis=1)
daily_min = np.min(temp, axis=1)
print("\nDaily Maximum Temperatures: \n", daily_max)
print("\nDaily Minimum Temperatures: \n", daily_min)

# Day with largest variation
variation = daily_max - daily_min
largest_variation_day = np.argmax(variation)
print("\nDay with Largest Temperature Variation: Day", largest_variation_day + 1)

#outliers
mean_temp = np.mean(temp)
std_temp = np.std(temp)
outliers = (temp < mean_temp - 2 * std_temp) | (temp > mean_temp + 2*std_temp)
temp[outliers] = mean_temp
print("\n Temp after updating outliers: \n",temp)


