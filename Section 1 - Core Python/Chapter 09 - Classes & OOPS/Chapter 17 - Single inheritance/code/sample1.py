class Pen():
    def __init__(self, size, name):
        self.name = name
        self.size = size

    def set_name(self, name):
        self.name = name

class BallPen(Pen):
    def __init__(self, size, name, color):
        self.color = color
        super().__init__(size, name)

    def set_color(self, color):
        self.color = color


pb = BallPen(10, "Renolds", "Green")
