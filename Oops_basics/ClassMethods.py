# Ques from w3school...find the area of rectange

class Reactangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def Area(self):
        length = self.length
        width = self.width
        return length * width
    
R = Reactangle(4,5)
print(R.Area())