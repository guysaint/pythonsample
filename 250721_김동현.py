import turtle
import random
import time

# 화면 설정
win = turtle.Screen()
win.title("똥 피하기 게임")
win.bgcolor("skyblue")
win.setup(width=600, height=600)
win.tracer(0)

# 플레이어 설정
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.lt(90)
player.penup()
player.goto(0, -250)
player.speed(0)

# 이동 함수
def go_left():
    x = player.xcor()
    x -= 20
    if x > -280:
        player.setx(x)

def go_right():
    x = player.xcor()
    x += 20
    if x < 280:
        player.setx(x)

# 키 입력
win.listen()
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

# 똥 생성
poops = []
fall_speeds = []  # 각 똥의 낙하 속도
for _ in range(20):
    poop = turtle.Turtle()
    poop.shape("circle")
    poop.color("brown")
    poop.penup()
    poop.speed(0)
    poop.goto(random.randint(-280, 280), random.randint(100, 400))
    poops.append(poop)
    fall_speeds.append(random.randint(10, 30))  # 각 똥마다 다른 속도 부여

# 타이머 텍스트 설정
timer = turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(200, 260)
timer.color("black")

start_time = time.time()

# 게임 루프
game_over = False

while not game_over:
    win.update()
        
    # 현재 시간 표시
    elapsed = time.time() - start_time
    timer.clear()
    timer.write(f"Time: {elapsed:.2f}", align="right", font=("Arial", 16, "bold"))

    for i in range(len(poops)):
        poop = poops[i]
        speed = fall_speeds[i]

        y = poop.ycor()
        y -= speed
        poop.sety(y)

        # 다시 위로 보내기
        if y < -300:
            poop.goto(random.randint(-280, 280), random.randint(300, 400))
            fall_speeds[i] = random.randint(10, 30)

        # 충돌 검사
        if player.distance(poop) < 20:
            game_over = True
            print(f"💥 Game Over 💥\n⏱️ 생존 시간: {elapsed:.2f}초")
            timer.goto(0, 0)
            timer.write(f"Game Over\nTime: {elapsed:.2f}초", align="center", font=("Arial", 20, "bold"))
            break

    time.sleep(0.03)

# 종료 처리
turtle.done()
