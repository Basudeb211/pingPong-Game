# Pong Game by @Rocky

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
paddle_a.shape("turtle")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("green")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("turtle")
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
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 | Player B: 0", align="center", font=("Algerian", 24, "italic"))


# Functions to operate the paddle using keyboard
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Function to start a new game
def start_new_game():
    global score_a, score_b
    pen.clear()  # Clear the previous messages
    score_a = 0
    score_b = 0
    pen.goto(0, 260)
    pen.write("Player A: 0 | Player B: 0", align="center", font=("Algerian", 24, "italic"))

# Function to exit the game
def exit_game():
    win.bye()
    
# Keyboard Binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")
win.onkeypress(start_new_game, "n")
win.onkeypress(exit_game, "q")

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
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center",
                  font=("Algerian", 24, "italic"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        score_b += 1
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center",
                  font=("Algerian", 24, "italic"))
       

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

    if score_a == 1:
        pen.goto(0, 100)
        pen.write("Player A Win ! Enter twice n for start new game or q for quit game", align="center", font=("Times New Roman", 15, "normal"))

    elif score_b == 1:
        pen.goto(0, 100)
        pen.write("Player B Win ! Enter twice n for start new game or q for quit game", align="center", font=("Times New Roman", 15, "normal"))