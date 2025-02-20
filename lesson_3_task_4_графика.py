# Настройки черепахи.

from turtle import *

my_turtle = Turtle()
my_turtle.shape("turtle") # Изменение курсора.
my_turtle.speed(10) # Скорость черепахи.
my_turtle.shapesize(1) # Размер черепахи.
my_turtle.screen.bgcolor("orange") # Цвет фона.
my_turtle.pensize(0), 0 # Ширина линии.
my_turtle.screen.setup(1440, 900) # Разрешение открывающегося окна.

# Нарисовать квадрат.

def draw_rect(t):
    for x in range(0, 4):
        t.right(90)
        t.forward(100)

# Рисует квадраты в цикле.

for x in range(0, 360):
    draw_rect(my_turtle)
    my_turtle.right(1)

# Необходимо, чтобы окно не закрывалось само, а только по клику.

my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()