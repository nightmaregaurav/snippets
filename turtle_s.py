import random
import turtle


class WriteS:
    def __init__(self, turtle_object, initial_position):
        super().__init__()
        self.turtle_object = turtle_object
        self.turtle_object.speed(0)
        self.initial_position = initial_position

        self.colorList = ["red", "orange", "purple", "blue", "pink"]

    def run(self) -> None:
        self.turtle_object.color("white")
        self.turtle_object.right(90)
        self.turtle_object.forward(self.initial_position)
        self.turtle_object.left(90)
        for i in range(1, 502):
            self.turtle_object.color(self.colorList[random.randint(0, len(self.colorList)-1)])
            self. square(10)
            self.turtle_object.forward(10)
            self.turtle_object.right(i)

    def square(self, x) -> None:
        self.turtle_object.forward(x)
        self.turtle_object.right(90)
        self.turtle_object.forward(x)
        self.turtle_object.right(90)
        self.turtle_object.forward(x)
        self.turtle_object.right(90)
        self.turtle_object.forward(x)


t1 = WriteS(turtle.Turtle(), 200)
t1.run()
