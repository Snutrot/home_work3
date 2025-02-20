import turtle

def draw_cat():
    # Тело
    turtle.fillcolor("gray")
    turtle.begin_fill()
    turtle.circle(100)  # Тело
    turtle.end_fill()

    # Голова
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.fillcolor("gray")
    turtle.begin_fill()
    turtle.circle(50)  # Голова
    turtle.end_fill()

    # Глаза
    for x in [-20, 20]:
        turtle.penup()
        turtle.goto(x, 130)
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(10)  # Глаз
        turtle.end_fill()

        # Зрачки
        turtle.fillcolor("black")
        turtle.penup()
        turtle.goto(x, 135)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(5)  # Зрачок
        turtle.end_fill()

    # Уши
    turtle.fillcolor("gray")
    for x in [-30, 30]:
        turtle.penup()
        turtle.goto(x, 150)
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(x - 20, 180)  # Линия уха
        turtle.goto(x + 20, 150)  # Линия уха
        turtle.end_fill()

    # Нос
    turtle.penup()
    turtle.goto(0, 120)
    turtle.pendown()
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.goto(-10, 110)
    turtle.goto(10, 110)
    turtle.goto(0, 120)
    turtle.end_fill()

    # Усы
    for x in [-10, 10]:
        turtle.penup()
        turtle.goto(0, 115)
        turtle.pendown()
        turtle.goto(x, 115)  # Усы

def main():
    turtle.speed(3)
    draw_cat()
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()

