import csv
from io import StringIO
data = "name,age\nNisha,22\nAnushka,12"
r = csv.reader(StringIO(data))
for row in r:
    print(row)

# by csv.DictReader() .....for reading in dictionary format
r = csv.DictReader(StringIO(data))
for row in r:
    print(row)

# writing to csv file
with open('01_basics/filehandling/example.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['name','age'])
    w.writerow(['Nishaa', 22])

