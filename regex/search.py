import re
subjects = "Maths,physics,Autometa,DIP,Cryptography,physics"
search_find = re.search("physics",subjects)
print(search_find)
if search_find:
    print("found",search_find.group())
else:
    print("Not found")