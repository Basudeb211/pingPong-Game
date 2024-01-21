import turtle
import winsound

win = turtle.Screen()
win.title("Pong Game by @Rocky")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("green")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("blue")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 | Player B: 0", align="center", font=("Algerian", 24, "italic"))

# Button for starting a new game
new_game_button = turtle.Turtle()
new_game_button.speed(0)
new_game_button.shape("square")
new_game_button.color("white")
new_game_button.shapesize(stretch_wid=1, stretch_len=6)
new_game_button.penup()
new_game_button.goto(-150, -290)
new_game_button.hideturtle()  # Hide the button initially

# Button for exiting the game
exit_button = turtle.Turtle()
exit_button.speed(0)
exit_button.shape("square")
exit_button.color("white")
exit_button.shapesize(stretch_wid=1, stretch_len=6)
exit_button.penup()
exit_button.goto(150, -290)
exit_button.hideturtle()  # Hide the button initially

# Functions to operate the paddle using the keyboard
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y < 250:
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y > -240:
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y < 250:
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if y > -240:
        paddle_b.sety(y)

# Function to start a new game
def start_new_game():
    global score_a, score_b
    pen.clear()
    score_a = 0
    score_b = 0
    pen.goto(0, 260)
    pen.write("Player A: 0 | Player B: 0", align="center", font=("Algerian", 24, "italic"))
    ball.goto(0, 0)
    ball.dx = 0.1
    ball.dy = 0.1
    win.update()
    new_game_button.hideturtle()
    exit_button.hideturtle()
   

# Function to exit the game
def exit_game():
    win.bye()

# Keyboard Binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Button Click Events
def on_new_game_click(x, y):
    start_new_game()

def on_exit_click(x, y):
    exit_game()

new_game_button.onclick(on_new_game_click)
exit_button.onclick(on_exit_click)

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boundary
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        score_a += 1
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("Algerian", 24, "italic"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        score_b += 1
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("Algerian", 24, "italic"))

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 35 and ball.ycor() > paddle_b.ycor() - 35):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dx *= 1.03
        ball.dy *= 1.03

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 35 and ball.ycor() > paddle_a.ycor() - 35):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dx *= 1.03
        ball.dy *= 1.03

    # Check for player wins
    if score_a == 1 or score_b == 1:  # Adjusted the winning score to 5
        ball.goto(0, 0)
        ball.dx = 0
        ball.dy = 0

        if score_a == 1:
            pen.goto(0, 100)
            pen.write("Player A Wins! ", align="center", font=("Times New Roman", 15, "normal"))
            new_game_button.showturtle()
            exit_button.showturtle()
           
        else:
            pen.goto(0, 100)
            pen.write("Player B Wins! ", align="center", font=("Times New Roman", 15, "normal"))
            new_game_button.showturtle()
            exit_button.showturtle()
            
