'''
Created by Keenan Kalra
2022
This is a classic snake game with a twist. The user simply watches and presses nothing.
The program uses Almighty Move in which the snake just follows the same pattern throughout
the entire game. 
'''

import turtle
import time
import random

delay = 0

# Set up the Screen
window = turtle.Screen()    
window.title("Snake by Keenan K.")
window.bgcolor(0, 0.75, 0)
window.setup(width=680, height=680)
window.tracer(0)

background = turtle.Turtle()
background.speed(0)
background.shape("square")
background.color(0, 1, 0)
background.penup()
background.goto(10, 0)
background.shapesize(stretch_len=30 , stretch_wid=29)

score = 0
high_score = 0

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color(0, 0, 0.5)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(1, 0, 0)
food.penup()
food.goto(0, 100)

segments = []

# Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Times", 24, "bold")) 

#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        head.sety(head.ycor()+20)
    if head.direction == "down":
        head.sety(head.ycor()-20)
    if head.direction == "right":
        head.setx(head.xcor()+20)
    if head.direction == "left":
        head.setx(head.xcor()-20)

# Keyboard Bindings
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_right, "Right")
window.onkeypress(go_left, "Left")

# Main Game Loop
while True:
    window.update()


    if score >= 0:
        # Auto Movement for the Snake

        # Start at the center
        if head.xcor() == 0 and head.ycor() == 0:
            go_left()

        # Cycle of 4 movement to sweep the top area
        # Cycle 1
        if head.xcor() == -260 and head.ycor() == 0:
            go_up()
        
        if head.xcor() == -260 and head.ycor() == 20:
            go_right()
        
        if head.xcor() == 300 and head.ycor() == 20:
            go_up()
        
        if head.xcor() == 300 and head.ycor() == 40:
            go_left()
        
        # Cycle 2
        if head.xcor() == -260 and head.ycor() == 40:
            go_up()
        
        if head.xcor() == -260 and head.ycor() == 60:
            go_right()
        
        if head.xcor() == 300 and head.ycor() == 60:
            go_up()
        
        if head.xcor() == 300 and head.ycor() == 80:
            go_left()
        
        # Cycle 3
        if head.xcor() == -260 and head.ycor() == 80:
            go_up()
        
        if head.xcor() == -260 and head.ycor() == 100:
            go_right()
        
        if head.xcor() == 300 and head.ycor() == 100:
            go_up()
        
        if head.xcor() == 300 and head.ycor() == 120:
            go_left()

        # Cycle 4
        if head.xcor() == -260 and head.ycor() == 120:
            go_up()
        
        if head.xcor() == -260 and head.ycor() == 140:
            go_right()
        
        if head.xcor() == 300 and head.ycor() == 140:
            go_up()
        
        if head.xcor() == 300 and head.ycor() == 160:
            go_left()

        # Cycle 5
        if head.xcor() == -260 and head.ycor() == 160:
            go_up()
        
        if head.xcor() == -260 and head.ycor() == 180:
            go_right()
        
        if head.xcor() == 300 and head.ycor() == 180:
            go_up()
        
        if head.xcor() == 300 and head.ycor() == 200:
            go_left()
        
        # Cycle 6
        if head.xcor() == -260 and head.ycor() == 200:
            go_up()
        
        if head.xcor() == -260 and head.ycor() == 220:
            go_right()
        
        if head.xcor() == 300 and head.ycor() == 220:
            go_up()
        
        if head.xcor() == 300 and head.ycor() == 240:
            go_left()

        # Cycle 7
        if head.xcor() == -260 and head.ycor() == 240:
            go_up()
        
        if head.xcor() == -260 and head.ycor() == 260:
            go_right()
        
        if head.xcor() == 300 and head.ycor() == 260:
            go_up()
        
        if head.xcor() == 300 and head.ycor() == 280:
            go_left()

        # Top Left Corner
        if head.xcor() == -280 and head.ycor() == 280:
            go_down()
        
        # Cycle of 4 movement to sweep the bottom area
        # Cycle 1
        if head.xcor() == -280 and head.ycor() == -280:
            go_right()

        if head.xcor() == -260 and head.ycor() == -280:
            go_up()

        if head.xcor() == -260 and head.ycor() == -20:
            go_right()

        if head.xcor() == -240 and head.ycor() == -20:
            go_down()
        
        # Cycle 2
        if head.xcor() == -240 and head.ycor() == -280:
            go_right()

        if head.xcor() == -220 and head.ycor() == -280:
            go_up()

        if head.xcor() == -220 and head.ycor() == -20:
            go_right()
            
        if head.xcor() == -200 and head.ycor() == -20:
            go_down()
        
        # Cycle 3
        if head.xcor() == -200 and head.ycor() == -280:
            go_right()

        if head.xcor() == -180 and head.ycor() == -280:
            go_up()

        if head.xcor() == -180 and head.ycor() == -20:
            go_right()
            
        if head.xcor() == -160 and head.ycor() == -20:
            go_down()

        # Cycle 4
        if head.xcor() == -160 and head.ycor() == -280:
            go_right()

        if head.xcor() == -140 and head.ycor() == -280:
            go_up()

        if head.xcor() == -140 and head.ycor() == -20:
            go_right()
            
        if head.xcor() == -120 and head.ycor() == -20:
            go_down()
        
        # Cycle 5
        if head.xcor() == -120 and head.ycor() == -280:
            go_right()

        if head.xcor() == -100 and head.ycor() == -280:
            go_up()

        if head.xcor() == -100 and head.ycor() == -20:
            go_right()
            
        if head.xcor() == -80 and head.ycor() == -20:
            go_down()
        
        # Cycle 6
        if head.xcor() == -80 and head.ycor() == -280:
            go_right()

        if head.xcor() == -60 and head.ycor() == -280:
            go_up()

        if head.xcor() == -60 and head.ycor() == -20:
            go_right()
            
        if head.xcor() == -40 and head.ycor() == -20:
            go_down()

        # Cycle 7
        if head.xcor() == -40 and head.ycor() == -280:
            go_right()

        if head.xcor() == -20 and head.ycor() == -280:
            go_up()

        if head.xcor() == -20 and head.ycor() == -20:
            go_right()
            
        if head.xcor() == 0 and head.ycor() == -20:
            go_down()
        
        # Cycle 8
        if head.xcor() == 0 and head.ycor() == -280:
            go_right()

        if head.xcor() == 20 and head.ycor() == -280:
            go_up()

        if head.xcor() == 20 and head.ycor() == -20:
            go_right()
            
        if head.xcor() == 40 and head.ycor() == -20:
            go_down()

        # Cycle 9
        if head.xcor() == 40 and head.ycor() == -280:
            go_right()

        if head.xcor() == 60 and head.ycor() == -280:
            go_up()

        if head.xcor() == 60 and head.ycor() == -20:
            go_right()
            
        if head.xcor() == 80 and head.ycor() == -20:
            go_down()
        
        # Cycle 10
        if head.xcor() == 80 and head.ycor() == -280:
            go_right()

        if head.xcor() == 100 and head.ycor() == -280:
            go_up()

        if head.xcor() == 100 and head.ycor() == -20:
            go_right()
            
        if head.xcor() == 120 and head.ycor() == -20:
            go_down()
        
        # Cycle 11
        if head.xcor() == 120 and head.ycor() == -280:
            go_right()

        if head.xcor() == 140 and head.ycor() == -280:
            go_up()

        if head.xcor() == 140 and head.ycor() == -20:
            go_right()
            
        if head.xcor() == 160 and head.ycor() == -20:
            go_down()

        # Cycle 12
        if head.xcor() == 160 and head.ycor() == -280:
            go_right()

        if head.xcor() == 180 and head.ycor() == -280:
            go_up()

        if head.xcor() == 180 and head.ycor() == -20:
            go_right()
            
        if head.xcor() == 200 and head.ycor() == -20:
            go_down()
        
        # Cycle 13
        if head.xcor() == 200 and head.ycor() == -280:
            go_right()

        if head.xcor() == 220 and head.ycor() == -280:
            go_up()

        if head.xcor() == 220 and head.ycor() == -20:
            go_right()
            
        if head.xcor() == 240 and head.ycor() == -20:
            go_down()

        # Cycle 14
        if head.xcor() == 240 and head.ycor() == -280:
            go_right()

        if head.xcor() == 260 and head.ycor() == -280:
            go_up()

        if head.xcor() == 260 and head.ycor() == -20:
            go_right()
            
        if head.xcor() == 280 and head.ycor() == -20:
            go_down()
            
        # Bottom Right Corner
        if head.xcor() == 280 and head.ycor() == -280:
            go_right()
        
        if head.xcor() == 300 and head.ycor() == -280:
            go_up()

        if head.xcor() == 300 and head.ycor() == 0:
            go_left()

    # Check for Collision with Border
    if head.xcor() > 310 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        
        # Reset the Score
        score = 0

        # Reset the Delay
        delay = 0

        # Reset the Snake and Food
        head.goto(0, 0)
        head.direction = "stop"
        food.goto(0, 100)
        
        # Hide the Segments
        for segment in segments:
            segment.goto(1000000, 1000000)
        
        # Clear the Segment List
        segments.clear()


    # Check for Collision with Food
    if head.distance(food) < 20:
        # Move the Food to a Random Spot
        food.goto(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))
        
        for segment in segments:
            while segment.xcor() == food.xcor() and segment.ycor() == food.ycor():
                food.goto(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))
        # Shorten the Delay
        # delay -= 0.00001

        # Increase the Score
        score += 1

        if score > high_score:
            high_score = score
        
        # Write out the Score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Times", 24, "bold"))

        # Increase the Snake's Body Length
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(0.2, 0.2, 1)
        new_segment.penup()
        segments.append(new_segment)
    
    # Move the End Segments First in Reverse Order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        
        while food.xcor() == segments[index].xcor() and food.ycor() == segments[index].ycor:
            food.goto(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20)) 


    # Move segment 0 to where the Head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move() 

    # Check for Head Collisions with the Body Segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)

            # Reset the Score
            score = 0

            # Reset the Delay
            delay = 0

            # Reset the Snake and Food
            head.goto(0, 0)
            head.direction = "stop"
            food.goto(0, 100)
            
            # Hide the Segments
            for segment in segments:
                segment.goto(1000000, 1000000)
            
            # Clear the Segment List
            segments.clear()

    # Write out the Score
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Times", 24, "bold"))

    if score >= 760:
        delay = 0.05

    time.sleep(delay)

window.mainloop()
