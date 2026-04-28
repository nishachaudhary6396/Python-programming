import re
player_names = "Virat,Rohit,bumrah,Tilak,Abhishek,ABD"
pattern = ','
split_name = re.split(pattern,player_names)
print(split_name)
print(split_name[1])