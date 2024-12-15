import turtle
import time 
import random 

lp= turtle.Turtle()


wn= turtle.Screen()
wn.screensize(400,400)
wn.title("scribble pong")
wn.bgcolor("black")


wn.listen()


bordergen= turtle.Turtle()
bordergen.speed(0)
bordergen.penup()

bordergen.goto(400,0)
bordergen.pendown()
bordergen.pensize(5)
bordergen.color("white")

#loop optimization 
bordergen.right(90)
bordergen.forward(280)
bordergen.right(90)
bordergen.forward(800)
bordergen.right(90)
bordergen.forward(560)
bordergen.right(90)
bordergen.forward(800)
bordergen.right(90)
bordergen.forward(280)

bordergen.hideturtle()

# paddle left

lp.color("white")
lp.shape("square")
lp.penup()
lp.shapesize(stretch_wid=6, stretch_len= 1)
lp.goto(280,0)

#paddle right 

rp= turtle.Turtle()

rp.color("light blue")
rp.shape("square")
rp.shapesize(stretch_wid=6, stretch_len= 1)
rp.penup()
rp.goto(-280, 0)


#pong ball

ball= turtle.Turtle()

ball.goto(0,0)
ball.shape("circle")
ball.penup()
ball.color("white")


s=random.randint(10,15)

print (s)
ball.speed(2)

def ballmove():
    
    s=random.randint(1,8)
    if s%2==0 :
        ball.right(s)
        ball.forward(400)
        ball.setx()
        ball.sety()
    elif s%2 !=0:
        ball.left(s)
        ball.back(400)
        

    # if ((lp.ycor()-40) >= (ball.ycor()) >= (lp.ycor()+40)) and



if (-275 <= ball.xcor() <= -285):
    print (ball.xcor())
        
        
        


player1=0
player2 =0

score1= turtle.Turtle()
score1.penup()
score1.goto(-500, -150)
score1.pendown()
score1.color("white")
score1.pensize(5)
score1.write("Score: ")
score1.hideturtle()


score2= turtle.Turtle()
score2.penup()
score2.goto(500, -150)
score2.pendown()
score2.pensize(6)
score2.color("light blue")
score2.write("Score: ")
score2.hideturtle()






wn.update()

time.sleep(0.01)



    
def leftpadmoveup():
    y = lp.ycor()
    if y < 216:  
        y += 20
        lp.sety(y)  
        
        
def rightpadmovedown():
    y = rp.ycor()
    if y > -216:  
        y -= 20
        rp.sety(y) 
   
   
def rightpadmoveup():
    y = rp.ycor()
    if y < 216:  
        y += 20
        rp.sety(y)  
        
        
def leftpadmovedown():
    y = lp.ycor()
    if y > -216:  
        y -= 20
        lp.sety(y)  
        
        
leftpadmoveup()
leftpadmovedown()
rightpadmovedown()
rightpadmoveup()

wn.listen()
wn.onkeypress(leftpadmoveup, "w")
wn.onkeypress(leftpadmovedown,"s")
wn.onkeypress(rightpadmoveup, "i")
wn.onkeypress(rightpadmovedown,"k")
wn.onkeypress(ballmove(), "b")
        
        
if ball.xcor()>=390 or ball.xcor()<=-395:
        ball.teleport(0,0)
        player1=player1+1
       
if ball.ycor()>=300 or  ball.ycor()<=-300:
        ball.teleport(0,0)
        player2=player2 +1



#time.sleep()

wn.exitonclick()