import turtle
import random
import time

s = turtle.getscreen()

# 레이싱 선수 세팅 (1번부터 6번까지)
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-300, 250)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-300, 150)
player_three = player_one.clone()
player_three.color("red")
player_three.penup()
player_three.goto(-300, 50)
player_four = player_one.clone()
player_four.color("yellow")
player_four.penup()
player_four.goto(-300, -50)
player_five = player_one.clone()
player_five.color("orange")
player_five.penup()
player_five.goto(-300, -150)
player_six = player_one.clone()
player_six.color("purple")
player_six.penup()
player_six.goto(-300, -250)

# 트랙 만들기
player_one.goto(300, 300)
player_one.pendown()
player_one.rt(90)
player_one.fd(600)
player_one.penup()
player_one.goto(-300, 250)
player_one.lt(90)

speed = [1, 2, 3, 4, 5, 6]

bet_winner = input("Please enter the number of player you think will win(1 ~ 6): ")

while True:
    # 0.5초마다 기다림
    time.sleep(0.5)

    # 플레이어마다 랜덤 스피드를 줌
    player_one.fd(20 * random.choice(speed))
    player_two.fd(20 * random.choice(speed))
    player_three.fd(20 * random.choice(speed))
    player_four.fd(20 * random.choice(speed))
    player_five.fd(20 * random.choice(speed))
    player_six.fd(20 * random.choice(speed))
    
    if player_one.pos() == (300, 250):
        print("Player 1 wins!")
        if bet_winner == 1:
            print("You earned the money, Congratuation!")
        else: print("You lost... Sorry for that.")
        break
    elif player_two.pos() == (300, 150):
        print("Player 2 wins!")
        if bet_winner == 2:
            print("You earned the money, Congratuation!")
        else: print("You lost... Sorry for that.")
        break
    elif player_three.pos() == (300, 50):
        print("Player 3 wins!")
        if bet_winner == 3:
            print("You earned the money, Congratuation!")
        else: print("You lost... Sorry for that.")
        break
    elif player_four.pos() == (300, -50):
        print("Player 4 wins!")
        if bet_winner == 4:
            print("You earned the money, Congratuation!")
        else: print("You lost... Sorry for that.")
        break
    elif player_five.pos() == (300, -150):
        print("Player 5 wins!")
        if bet_winner == 5:
            print("You earned the money, Congratuation!")
        else: print("You lost... Sorry for that.")
        break
    elif player_six.pos() == (300, -250):
        print("Player 6 wins!")
        if bet_winner == 6:
            print("You earned the money, Congratuation!")
        else: print("You lost... Sorry for that.")
        break
    