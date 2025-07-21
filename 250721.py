import turtle
import random

s = turtle.getscreen()
t_one = turtle.Turtle()
t_one.color("green")
t_one.shape("turtle")
t_one.penup()
t_one.goto(-200, 100)
t_two = t_one.clone()
t_two.color("blue")
t_two.penup()
t_two.goto(-200,-100)
t_one.goto(300,60)
t_one.pendown()
t_one.circle(40)
t_one.penup()
t_one.goto(-200, 100)
t_two.goto(300,-140)
t_two.pendown()
t_two.circle(40)
t_two.penup()
t_two.goto(-200, -100)

die = [1,2,3,4,5,6]

for i in range(20):
    if t_one.pos() >= (300, 100):
        print("Player One Wins!")
        break
    elif t_two.pos() >= (300, -100):
        print("Player Two Wins!")
        break
    else:
        t_one_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        t_one.fd(20*die_outcome)
        t_two_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        t_two.fd(20*die_outcome)
    
