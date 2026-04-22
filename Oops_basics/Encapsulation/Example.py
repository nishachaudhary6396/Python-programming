# Inside the editor, complete the following steps:
# Create a class ScoreBoard
# Add an __init__ with a score parameter and store it as a private attribute
# Add a method called get_score that returns the private score
# Create an object s1 with a score of 0
# Print the score of s1

class scoreboard:
    def __init__(self,name,score):
        self.name = name
        self.__score = score
    def get_score(self):
        return self.__score
s1 = scoreboard("cricket",0)
print(s1.name)
print(s1.get_score())