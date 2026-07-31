class cookie:
    def __init__(self,color):
        self.color=color
    
    def get_color(self):
        return self.color
    
    def set_color(self,color):
        self.color=color

cookie_one = cookie("green")
cookie_two = cookie("blue")

print(cookie_one.get_color())

cookie_one.set_color("yellow")

print(cookie_one.get_color())