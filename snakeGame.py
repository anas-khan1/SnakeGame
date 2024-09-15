import turtle
import time
import random 

#SCREEN FOR SNAKE GAME
screen = turtle.Screen()     
screen.setup(width=1000,height=720)
screen.title("Snake Game (CREATED BY - ANAS KHAN)")
screen.bgcolor("black")
screen.tracer(0)          #TO TURN OFF ANIMATION

#THE VERY FIRST TURTLE, HEAD OF SNAKE 
head = turtle.Turtle()      
head.shape("square")
head.color("orange")
head.penup()

#TURTLE FOR GENERATING FOOD
food = turtle.Turtle()      
food.shape("circle")
food.shapesize(0.5)
food.color("red")
food.up()

segment = [head]            #LIST TO STORE SNAKE BODY OBJECTS
score = 0                   #VARIABLE TO COUNT SCORE OF A PERSON

# Create a turtle for displaying the score
score_display = turtle.Turtle()
score_display.color("yellow")
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 320)  # Position it at the top of the screen

# Function to display the score
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 25, "normal"))

def addbody(p,pos):
    segment.append(p)
    p.shape("circle")
    p.color("blue")
    p.penup()
    p.goto(pos)

#THIS FUNCTION CHECKS IF THE GAME IS OVER OR NOT 
def check_game_over(): 
    #WHEN HIT WALL     
    if head.xcor() > 490 or head.xcor() < -490 or head.ycor() > 350 or head.ycor() < -350:    #WILL TERMINATE WHEN REACHES 500 OR 360
        return True
    #WHEN HIT ITS OWN TAIL
    for el in segment[1:]:  # Start from segment[1], skipping the head itself
        if head.distance(el) < 10:  # Check if head is within 10 pixels of any body segment
            return True
    return False  # SEND FALSE IF NONE ABOVE CASES ARE TRUE

#THIS FUNCTION GENERATES FOOD AT RANDOM PLACES
def generateFood():        
    food.goto(random.randrange(-460,460,20),random.randrange(-320,320,20))

#THIS FUNCTIONS MAKES THE SNAKE WHOLE BODY MOVE FORWARD BY 20
def snakeforward():        
    for segment_number in range(len(segment)-1,0,-1):
        pos = segment[segment_number-1].position()
        segment[segment_number].goto(pos)
    head.forward(20)

# KEYBINDING FUNCTIONS TO CONTROL SNAKE DIRECTION
def setheading0():
    if head.heading()!=180:
        head.setheading(0)
def setheading90():
    if head.heading()!=270:
        head.setheading(90)
def setheading180():
    if head.heading()!=0:
        head.setheading(180)
def setheading270():
    if head.heading()!=90:
        head.setheading(270)

#THIS FUNCTION ENABLES THE KEYBOARD KEYS TO WORK
def makeKeyWork():           
    screen.listen()
    screen.onkeypress(setheading90,"Up")
    screen.onkeypress(setheading270,"Down") 
    screen.onkeypress(setheading0,"Right")
    screen.onkeypress(setheading180,"Left")

#THIS FUNCTION WORKS WHEN SNAKE EATS FOOD AND NEW FOOD IS GENERATED AND SNAKE LENGTH INCREASES
def if_eaten_food():         
    if head.distance(food) < 10:      
        generateFood()
        global score
        score+=1
        update_score()     # UPDATE THE SCORE AFTER EATING FOOD
        new_body_memeber = turtle.Turtle()
        last_body_turtle = segment[-1]
        if head.heading()==0:
            pos = (last_body_turtle.xcor()-20,last_body_turtle.ycor())
        elif head.heading()==90:
            pos = (last_body_turtle.xcor(),last_body_turtle.ycor()-20)
        elif head.heading()==180:
            pos = (last_body_turtle.xcor()+20,last_body_turtle.ycor())
        elif head.heading()==270:
            pos = (last_body_turtle.xcor(),last_body_turtle.ycor()+20)
        addbody(new_body_memeber,pos)    #ADDING NEW TURTLE AT BACK OF SNAKE

 #MAIN FUNCTION THAT CONINUOSLY MOVES THE SNAKE AND CHECK OTHER CONDITIONS AND COMBINE ALL OTHER IMP FUNCTIONS
def move():             
    while True:
        time.sleep(0.1)
        screen.update()
        if check_game_over():
            score_display.goto(0,0)
            score_display.clear()
            score_display.write(f"GAME OVER\nSCORE: {score}", align="center", font=("Arial", 50,"normal"))
            break
        makeKeyWork()
        snakeforward()
        if_eaten_food()


p1 = turtle.Turtle()       #TO CREATE SECOND SNAKE BODY TURTLE AFTER HEAD
addbody(p1,(-20,0))

generateFood()             #TO GENERATE FOOD FOR THE FIRST TIME
update_score()             #TO WRITE INITIAL SCORE
move()                     #TO MAKE SNAKE WORK AND START GAME LOOP

screen.exitonclick()