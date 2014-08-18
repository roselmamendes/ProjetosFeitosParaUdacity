import turtle

def draw_triangle(tri):
    tri.forward(80)
    tri.left(120)
    tri.forward(70)
    tri.left(110)
    tri.forward(80)

def principal():
    window = turtle.Screen()
    window.bgcolor("red")
    tri = turtle.Turtle()
    tri.color("pink")

    for i in range(2):
        draw_triangle(tri)
        tri.right(3)

    window.exitonclick()

principal()
