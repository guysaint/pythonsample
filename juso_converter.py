import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "devU01TX0FVVEgyMDI1MDYwNDEzMDQzNjExNTgxNTY="

def convert_address(event=None):
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

        url = "https://business.juso.go.kr/addrlink/addrEngApi.do"
        response = requests.get(url, params=params)
        data = response.json()

        juso_list = data['results'].get('juso', [])

        if not juso_list:
            result_text.config(state='normal')
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, f"📌 [한글 주소]\n{korean_address}\n\n🌍 [영문 주소]\nN/A\n\n📦 [우편번호]\nN/A")
            result_text.config(state='disabled')
            return

        eng_addr = juso_list[0].get('engAddr')
        if not eng_addr:
            eng_addr = juso_list[0].get('roadAddr', 'N/A')

        zip_code = juso_list[0].get('zipNo', 'N/A')

        result_text.config(state='normal')
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"📌 [한글 주소]\n{korean_address}\n\n🌍 [영문 주소]\n{eng_addr}\n\n📦 [우편번호]\n{zip_code}")
        result_text.config(state='disabled')

        # 자동 복사
        root.clipboard_clear()
        root.clipboard_append(eng_addr)
        root.update()
        print(f"✅ 클립보드에 복사됨: {eng_addr}")

    except Exception as e:
        messagebox.showerror("에러", f"오류 발생: {str(e)}")

def exit_program():
    root.quit()

# ────────────── GUI ──────────────
root = tk.Tk()
root.title("한글 주소 → 영문 주소 변환기")
root.geometry("550x470")
root.resizable(False, False)
root.configure(bg="#f9f9f9")

tk.Label(root, text="📌 한글 주소 입력:", font=("맑은 고딕", 12), bg="#f9f9f9").pack(pady=(20, 5))

entry = tk.Entry(root, width=45, font=("맑은 고딕", 12))
entry.pack(pady=5)
entry.bind("<Return>", convert_address)
entry.focus()  # ✅ 자동 포커스

btn_frame = tk.Frame(root, bg="#f9f9f9")
btn_frame.pack(pady=10)

convert_btn = tk.Button(btn_frame, text="▶ 변환하기", font=("맑은 고딕", 11), width=15, bg="#ffffff", relief="groove", command=convert_address)
convert_btn.grid(row=0, column=0, padx=10)

exit_btn = tk.Button(btn_frame, text="⛔ 프로그램 종료", font=("맑은 고딕", 11), width=15, bg="#fff5f5", relief="groove", command=exit_program)
exit_btn.grid(row=0, column=1, padx=10)

frame = tk.Frame(root, bg="#eeeeee", bd=1, relief="solid", padx=10, pady=10)
frame.pack(padx=20, pady=5, fill="both", expand=True)

result_text = tk.Text(frame, font=("맑은 고딕", 11), wrap="word", bg="#eeeeee", relief="flat", height=8)
result_text.pack(fill="both", expand=True)
result_text.config(state='disabled', cursor='xterm')

root.mainloop()
