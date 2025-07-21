import tkinter as tk
from tkinter import messagebox
import requests
import urllib.parse

# ★★ 발급받은 CONFIRM_KEY 입력 ★★
API_KEY = "여기에_발급받은_우정사업본부_API_KEY_입력"

def convert_address():
    korean_address = entry.get()
    if not korean_address.strip():
        messagebox.showwarning("입력 오류", "한글 주소를 입력해주세요.")
        return

    try:
        params = {
            "currentPage": 1,
            "countPerPage": 10,
            "keyword": korean_address,
            "confmKey": API_KEY,
            "resultType": "json"
        }

        url = "https://www.juso.go.kr/addrlink/addrEngApi.do"
        response = requests.get(url, params=params)
        data = response.json()

        juso_list = data['results']['juso']
        if not juso_list:
            result_label.config(text="❗ 영문 주소를 찾을 수 없습니다.")
            return

        kor_addr = juso_list[0]['jibunAddr']
        eng_addr = juso_list[0]['engAddr']
        result_label.config(text=f"[한글 주소]\n{kor_addr}\n\n[영문 주소]\n{eng_addr}")

    except Exception as e:
        messagebox.showerror("에러", f"오류 발생: {str(e)}")

# GUI 구성
root = tk.Tk()
root.title("한글 주소 → 영문 주소 변환기 (우정사업본부 API)")
root.geometry("500x300")
root.resizable(False, False)

tk.Label(root, text="🔎 한글 주소 입력:", font=("맑은 고딕", 12)).pack(pady=10)

entry = tk.Entry(root, width=50, font=("맑은 고딕", 11))
entry.pack(pady=5)

convert_btn = tk.Button(root, text="▶ 변환하기", font=("맑은 고딕", 11), command=convert_address)
convert_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("맑은 고딕", 10), justify="left", wraplength=460)
result_label.pack(pady=10)

root.mainloop()
