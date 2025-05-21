import tkinter as tk
from tkinter import messagebox
import os

def shutdown():
    confirm = messagebox.askyesno("확인", "정말로 컴퓨터를 종료하시겠습니까?")
    if confirm:
        os.system("shutdown /s /t 0")

def restart():
    confirm = messagebox.askyesno("확인", "정말로 재시작하시겠습니까?")
    if confirm:
        os.system("shutdown /r /t 0")

def schedule_shutdown():
    try:
        minutes = int(entry.get())
        seconds = minutes * 60
        confirm = messagebox.askyesno("확인", f"{minutes}분 후 컴퓨터를 종료할까요?")
        if confirm:
            os.system(f"shutdown /s /t {seconds}")
    except ValueError:
        messagebox.showerror("오류", "정수를 입력해주세요 (예: 10)")

def cancel_shutdown():
    os.system("shutdown /a")
    messagebox.showinfo("취소됨", "예약된 종료가 취소되었습니다.")

# GUI 세팅
root = tk.Tk()
root.title("전원 관리 도구")
root.geometry("300x300")
root.resizable(False, False)

label = tk.Label(root, text="전원 관리", font=("Arial", 16))
label.pack(pady=10)

btn_shutdown = tk.Button(root, text="전원 끄기", command=shutdown, width=25, height=2, bg="tomato")
btn_shutdown.pack(pady=5)

btn_restart = tk.Button(root, text="재시작", command=restart, width=25, height=2, bg="skyblue")
btn_restart.pack(pady=5)

entry_label = tk.Label(root, text="전원 끄기 예약 (분 단위):")
entry_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

btn_schedule = tk.Button(root, text="예약 종료 실행", command=schedule_shutdown, width=25, height=2, bg="lightgreen")
btn_schedule.pack(pady=5)

btn_cancel = tk.Button(root, text="예약 종료 취소", command=cancel_shutdown, width=25, height=2, bg="orange")
btn_cancel.pack(pady=5)

root.mainloop()
