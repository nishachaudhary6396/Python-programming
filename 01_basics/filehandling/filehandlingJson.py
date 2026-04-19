import json            #  for writing
data = [
    {"name": "Nisha", "age": 22},
    {"name": "Anushka", "age": 12}
    ]
with open('01_basics/filehandling/example.json', 'w') as f:
    json.dump(data,f)  # dump for writing and load for reading remember this


# for reading
with open('01_basics/filehandling/example.json', 'r') as f:
    data = json.load(f)
    print(data)

    