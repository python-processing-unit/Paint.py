import turtle
from PIL import ImageGrab

# Setup Statements and Variables
print("Left/Right = Color change")
print("Up/Down = Size change")
print("Mouse Click = Pen Up/Down")
print("S = Save Image")
print("Place the Turtle Window on Fullscreen.")

screen = turtle.Screen()
screen.bgcolor("White")

# Set the screen to fullscreen
screen.setup(width=1.0, height=1.0)
wi, he = screen.screensize()
fsize = int(wi/20)
t = turtle.Turtle()
t.speed(0)
size = 5
t.pensize(size)
t.penup()  # Start with pen up
colors = ["Black", "Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Gray", "Brown", "White"]
t.color(colors[0])
tcol = 0

numsplay = turtle.Turtle()
numsplay.color("Black")
numsplay.speed(0)
numsplay.hideturtle()
numsplay.penup()
numsplay.goto(-int(1.7*wi), int(1.1*he))
numsplay.pendown()
# Initial display of the Turtle's pensize
numsplay.write(f"Size: {size}",font=("Helvetica",fsize,"normal"))

csplay = turtle.Turtle()
csplay.color("Black")
csplay.speed(0)
csplay.hideturtle()
csplay.penup()
csplay.goto(int(1.65*wi), int(he))
csplay.pendown()
csplay.begin_fill()
csplay.circle(2.5)
csplay.end_fill()

def cir():
    csplay.clear()
    csplay.color(colors[tcol])
    csplay.begin_fill()
    csplay.circle(size/2)
    csplay.end_fill()

# Key Up function, raises the pensize by two
def ku():
    global size
    size += 2
    t.pensize(size)
    numsplay.clear()
    numsplay.write(f"Size: {size}",font=("Helvetica",fsize,"normal"))
    cir()

# Key Down function, lowers the pensize by two
def kd():
    global size
    if size > 2:
        size -= 2
        t.pensize(size)
    numsplay.clear()
    numsplay.write(f"Size: {size}",font=("Helvetica",fsize,"normal"))
    cir()

# Key Right function, changes the pencolor
def kr():
    global tcol
    tcol = (tcol + 1) % len(colors)
    t.color(colors[tcol])
    cir()

# Key Left function, changes the pencolor
def kl():
    global tcol
    tcol = (tcol - 1) % len(colors)
    t.color(colors[tcol])
    cir()

# Function to follow mouse movement.
def follow_mouse(x, y):
    t.goto(x - screen.window_width() // 2, screen.window_height() // 2 - y)

# Mouse button state variable
is_left_button_down = False

# Mouse button press event to toggle pen state
def mouse_toggle(x, y):
    global is_left_button_down
    is_left_button_down = not is_left_button_down
    if is_left_button_down:
        t.pendown()  # Put pen down when mouse is pressed
    else:
        t.penup()  # Lift pen up when mouse is released

# Sets delay to 0 for smoother movement
screen.delay(0)

def update_turtle_position():
    x, y = screen.getcanvas().winfo_pointerxy()
    
    # Update position based on mouse movement.
    follow_mouse(x, y)  
    
    # Check if the left mouse button is down and set pen state accordingly.
    if is_left_button_down:
        t.pendown()
    else:
        t.penup()

    screen.ontimer(update_turtle_position, 10)

def screenshot():
    numsplay.clear()
    csplay.clear()
    # Get the underlying Tkinter window
    root = screen.getcanvas().winfo_toplevel()
    
    # Capture the entire screen
    img = ImageGrab.grab()
    
    # Get the position and size of the turtle window
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    width = root.winfo_width()
    height = root.winfo_height()
    
    # Crop the image to the turtle window
    img = img.crop((x, y, x+width, y+height))
    
    # Save as PNG
    png_file = "screenshot.png"
    img.save(png_file, "PNG")
    numsplay.write(f"Size: {size}",font=("Helvetica",fsize,"normal"))
    cir()
    print("Image saved")

update_turtle_position()

# Key bindings for user controls
screen.onkey(ku, "Up")
screen.onkey(kd, "Down")
screen.onkey(kr, "Right")
screen.onkey(kl, "Left")
screen.onkey(screenshot, "s")
screen.listen()

# Bind mouse events for pressing and toggling pen state
screen.onscreenclick(mouse_toggle)   # Toggle pen state on mouse click

turtle.done()
