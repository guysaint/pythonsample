from tkinter import *

window = Tk()
window.title("간단 계산기")
window.geometry("350x200")
window.resizable(False, False)

# 스타일용 기본 폰트
FONT = ("Arial", 12)

# 입력 안내 라벨
Label(window, text='숫자 1', font=FONT).grid(column=0, row=0, padx=10, pady=10, sticky="e")
Label(window, text='숫자 2', font=FONT).grid(column=0, row=1, padx=10, pady=10, sticky="e")

# 결과 표시 라벨
res_label = Label(window, text="결과", font=("Arial", 12, "bold"))
res_label.grid(column=0, row=2, columnspan=3, pady=10)

# 입력창
num1 = Entry(window, width=15, font=FONT)
num2 = Entry(window, width=15, font=FONT)
num1.grid(column=1, row=0, padx=5)
num2.grid(column=1, row=1, padx=5)

# 기능 함수들
def add():
    try:
        answer = float(num1.get()) + float(num2.get())
        res_label.config(text=f"결과 = {answer}")
    except:
        res_label.config(text="유효한 숫자를 입력하세요")

def subtract():
    try:
        answer = float(num1.get()) - float(num2.get())
        res_label.config(text=f"결과 = {answer}")
    except:
        res_label.config(text="유효한 숫자를 입력하세요")

def multiplication():
    try:
        answer = float(num1.get()) * float(num2.get())
        res_label.config(text=f"결과 = {answer}")
    except:
        res_label.config(text="유효한 숫자를 입력하세요")

def division():
    try:
        answer = float(num1.get()) / float(num2.get())
        res_label.config(text=f"결과 = {round(answer, 2)}")
    except ZeroDivisionError:
        res_label.config(text="0으로 나눌 수 없습니다")
    except:
        res_label.config(text="유효한 숫자를 입력하세요")

# 버튼들 (가로 정렬)
btn_frame = Frame(window)
btn_frame.grid(column=0, row=3, columnspan=3, pady=10)

Button(btn_frame, text='+', width=5, font=FONT, command=add).grid(row=0, column=0, padx=5)
Button(btn_frame, text='-', width=5, font=FONT, command=subtract).grid(row=0, column=1, padx=5)
Button(btn_frame, text='*', width=5, font=FONT, command=multiplication).grid(row=0, column=2, padx=5)
Button(btn_frame, text='/', width=5, font=FONT, command=division).grid(row=0, column=3, padx=5)

window.mainloop()
