import turtle
from turtle import Screen

tree = True
bird_clone = []

wn = Screen()


def setup_page() :  # setup the page at the startup
    turtle.setup(800, 800)
    turtle.penup()
    turtle.setpos(-340, 350)
    turtle.pendown()
    turtle.listen()
    turtle.speed(0)


def draw_innersquare():  # draw a rectangle within the window to define the boundry
    turtle.fillcolor("pink")
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(700)
        turtle.right(90)
    turtle.end_fill()


def draw_circle(centre_x, centre_y, radius, pen_color, fill_color):  # draw a circle at the given position with the given radius
    turtle.penup()
    turtle.setpos(centre_x, centre_y)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()


def write_text(pos_x, pos_y, text):  # write a text at a given point
    turtle.penup()
    turtle.setpos(pos_x, pos_y)
    turtle.pendown()
    turtle.write(text, align='center')


def handle_click(x, y):  # handle the click functions
    global tree
    global bird_clone
    if(x >= -10.0 and x<= 10.0 and y >= 360.0 and y<= 386.0):  # check whether tree radio button clicked
        print('inside tree click')
        turtle.clearstamp(bird_clone[0])  # delete the top left corner bird
        tree = True
        turtle.stamp()
        turtle.shape('arrow')
        turtle.penup()
        turtle.home()
        turtle.pendown()
        draw_circle(0, 370, 10, 0, 'green')  # draw radio button
        draw_circle(100, 370, 10, 0, 'white')  # draw radio button

    if (x >= 90.0 and x <= 110.0 and y >= 360.0 and y <= 386.0):  # check whether bird radio button clicked
        print('inside bird click')
        draw_circle(0, 370, 10, 0, 'white')  # draw radio button
        draw_circle(100, 370, 10, 0, 'green')  # draw radio button
        turtle.penup()
        pos_x = -340
        pos_y = 370
        turtle.setpos(pos_x, pos_y)
        turtle.pendown()
        tree = False
        turtle.register_shape('bird', ((-22, -39), (-20, -7), (-7, 3), (-11, 7), (-12, 9), (-11, 10), (-9, 10), (-3, 7),
                                       (10, 24), (30, 16), (13, 18), (4, 0), (14, -6), (6, -13), (0, -4), (-14, -13),
                                       (-22, -39)))  # Register a new turtle shape
        turtle.shape('bird')
        turtle.fillcolor("brown")
        bird_clone = []
        astamp = turtle.stamp()
        turtle.penup()
        pos_x = -600
        pos_y = 600
        turtle.setpos(pos_x, pos_y)
        turtle.pendown()
        bird_clone.append(astamp)

    if tree is True:
        if (x >= -340.0 and y <= 349.0 and y >= -349.0 and x <= 360.0):  # check the clicke position is within the valid boundry
            triangle_one = y + 25
            triangle_overlap_one = triangle_one + (50 * 60 / 100.0)
            triangle_overlap_two = triangle_overlap_one + (50 * 60 / 100.0)

            draw_triangle(x, triangle_one, 100, 50, 'green', 'green')  # draw first triangle
            draw_triangle(x, triangle_overlap_one, 100, 50, 'green', 'green')  # draw second triangle
            draw_triangle(x, triangle_overlap_two, 100, 50, 'green', 'green')  # draw third triangle

            rectangle_one = y - 40
            draw_rectangle(x, rectangle_one, 15, 80, 'brown', 'brown')  # draw rectangle
    else :
        if (x >= -340.0 and y <= 349.0 and y >= -349.0 and x <= 360.0):  # check the clicke position is within the valid boundry
            if (x >= 90.0 and x <= 110.0 and y >= 360.0 and y <= 386.0):  # check whether tree radio button clicked
                print('do nothing')
            else:
                astamp  = turtle.stamp()
                bird_clone.append(astamp)
                turtle.penup()
                pos_x = x
                pos_y = y
                turtle.setpos(pos_x, pos_y)
                turtle.pendown()
                tree = False

    print('detected a click at', x, y)


def draw_triangle(centre_x, centre_y, width, height, pen_color, fill_color):  # draw a triangle
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.penup()
    pos_x = centre_x - width/2.0
    pos_y = centre_y - height/2.0
    turtle.setpos(pos_x, pos_y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(3) :
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()


def draw_rectangle(centre_x, centre_y, width, height, pen_color, fill_color):  # draw a rectangle
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.penup()
    pos_x = centre_x - width / 2.0
    pos_y = centre_y - height / 2.0
    turtle.setpos(pos_x, pos_y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()


def up():  # function call when the 'UP' arrow key pressed in the keyboard
    if tree is False:
        turtle.left(20)


def left():  # function call when the 'LEFT' arrow key pressed in the keyboard
    if tree is False:
        turtle.left(20)


def right():  # function call when the 'RIGHT' arrow key pressed in the keyboard
    if tree is False:
        turtle.right(20)


def down():  # function call when the 'DOWN' arrow key pressed in the keyboard
    if tree is False:
        turtle.right(20)


wn.onkey(up, 'Up')  # listen for 'UP' arrow key
wn.onkey(left, 'Left')  # listen for 'LEFT' arrow key
wn.onkey(right, 'Right')  # listen for 'RIGHT' arrow key
wn.onkey(down, 'Down')  # listen for 'DOWN' arrow key


wn.listen()  # listen to the key press

turtle.onscreenclick(handle_click)  # call handle_click when mouse click happens in the screen
