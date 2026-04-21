class human:
    def __init__(self,name):
        self.name = name
    
    def greet(self):
        return "Heyyy, " + self.name
    
    def blessings(self):
        return "god bless you.."

    def welcome(self):
        message = self.greet()
        blessings = self.blessings()
        print(message + "!!! you're welcome here. " + blessings)

h1 = human("Nisha")
h1.welcome()