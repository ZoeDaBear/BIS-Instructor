import turtle
import time

# Create screen
sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)


# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(5)
left_pad.shape("square")
left_pad.color("red")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)


# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(5)
right_pad.shape("square")
right_pad.color("blue")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)


# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("black")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Initialize the score
left_player = 0
right_player = 0

# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player: 0  Right_player: 0",
             align="center", font=("Courier", 24, "normal"))


# Functions to move paddles
def paddleaup():
    y = left_pad.ycor()
    if y < 250:   # Limit paddle movement
        y += 20
        left_pad.sety(y)


def paddleadown():
    y = left_pad.ycor()
    if y > -240:  # Limit paddle movement
        y -= 20
        left_pad.sety(y)


def paddlebup():
    y = right_pad.ycor()
    if y < 250:  # Limit paddle movement
        y += 20
        right_pad.sety(y)


def paddlebdown():
    y = right_pad.ycor()
    if y > -240:  # Limit paddle movement
        y -= 20
        right_pad.sety(y)


# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

# Get player names before starting
left_player_name = turtle.textinput("Player Name", "Enter Left Player's name:")
right_player_name = turtle.textinput("Player Name", "Enter Right Player's name:")

def show_start_screen():
    start_turtle = turtle.Turtle()
    start_turtle.hideturtle()
    start_turtle.penup()
    start_turtle.goto(0, 0)
    start_turtle.write(
        f"{left_player_name} vs {right_player_name}\nPress SPACE to start",
        align="center", font=("Courier", 32, "bold")
    )
    return start_turtle

def start_game():
    start_turtle.clear()
    game_loop()

def game_loop():
    global left_player, right_player
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write(f"{left_player_name}: {left_player}  {right_player_name}: {right_player}",
                     align="center", font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write(f"{left_player_name}: {left_player}  {right_player_name}: {right_player}",
                     align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370 and
            (hit_ball.ycor() < right_pad.ycor() + 50 and hit_ball.ycor() > right_pad.ycor() - 50)):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370 and
            (hit_ball.ycor() < left_pad.ycor() + 50 and hit_ball.ycor() > left_pad.ycor() - 50)):
        hit_ball.setx(-360)
        hit_ball.dx *= -1

    sc.update()
    sc.ontimer(game_loop, 10)

# Show start screen and bind SPACE to start
start_turtle = show_start_screen()
sc.onkeypress(start_game, "space")
sc.listen()
turtle.mainloop()
