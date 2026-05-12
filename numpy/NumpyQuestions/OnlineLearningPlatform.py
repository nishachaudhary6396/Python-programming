#  (Online Learning Platform)
# NumPy (Intermediate)
#  An online platform tracks time spent (in minutes) by students on 6 courses over 14 days using a NumPy array.
# Task:
# Compute total time spent per course


# Identify courses where average daily engagement exceeds a threshold


# Rank courses based on engagement

import numpy as np
data = np.random.randint(1,50,(14,6))
print(":Student data:\n", data)

#total time spent per course
total_time = np.sum(data,axis =0)
print("\nTotal time spemt per courseL\n", total_time)

#average engagement
avg_engagement = np.mean(data, axis =0)
threshold = 30
high_engagement = np.where(avg_engagement>threshold)[0]
print("\nCourses with above engagement:\n",high_engagement+1)

# Rank courses by engagement
ranking = np.argsort(total_time)[::-1]

print("\nCourse Ranking:")
print(ranking + 1)



