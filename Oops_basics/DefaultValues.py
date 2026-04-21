class human:
    def __init__(self,name,gender=22):
        self.name = name
        self.gender = gender

h1 = human("Nisha")
h2 = human("Anushka", 12)

print(h1.name, h1.gender)
print(h2.name, h2.gender)
