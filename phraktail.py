import turtle
class LSystem2D:
    def __init__(self, t, axiom, width, length, angle):
        self.axiom = axiom
        self.state = axiom
        self.width = width
        self.length = length
        self.angle = angle
        self.t = t
        self.rules = {}
        self.t.pensize(self.width)


    def add_rules(self, *rules):
        for key, value in rules:
            self.rules[key] = value

    def generate_path(self, n_iter):
        for n in range(n_iter):
            for key, value in self.rules.items():
                self.state = self.state.replace(key, value.lower())

            self.state = self.state.upper()

    def draw_turtle(self, start_pos, start_angle):
        turtle.tracer(1, 0)
        self.t.up()
        self.t.setpos(start_pos)
        self.t.seth(start_angle)
        self.t.down()

        for move in self.state:
            if move == 'F':
                self.t.forward(self.length)
            elif move == 'S':
                self.t.up()
                self.t.forward(self.length)
                self.t.down()
            elif move == '+':
                self.t.left(self.angle)
            elif move == '-':
                self.t.right(self.angle)

        turtle.done()

print("введите ширину окна")
width = int(input()) #ввод длинный окна
print("введите высоту окна")
height = int(input()) #ввод высоты окна
screen = turtle.Screen()
screen.setup(width, height, 0, 0)
t = turtle.Turtle()
t.ht()

pen_width = 2 #ширина кисти
print("введите масштаб")
f_len = int(input()) #масштабироваание
angle = 90
axiom = "X"

l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
l_sys.add_rules(("X", "-YF+XFX+FY-"), ("Y", "+XF-YFY-FX+"))
print("введите кол-во итераций")
l_sys.generate_path(int(input()))
print(l_sys.state)
l_sys.draw_turtle( (0, 0), -180)