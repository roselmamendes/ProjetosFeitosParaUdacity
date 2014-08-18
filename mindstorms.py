import turtle

def draw_square(some_turtle):
     for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    tri = turtle.Turtle()
    tri.color("pink")
    tri.forward(80)
    tri.left(120)
    tri.forward(70)
    tri.left(110)
    tri.forward(80)

def principal():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    
    for i in range(36):
        draw_square(brad)
        brad.right(10)
        
    window.exitonclick()

principal()

    
