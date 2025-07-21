# 과정 시각화 겸 복습
# 동작방식
# 1. 최대 구간이 나올 때 까지 다음 클릭
# 2. 최종 최대 구간이 나오면 닫기
import tkinter as tk
import collections

class SlidingWindow:
    def __init__(self, root, s, k):
        self.s = s
        self.k = k
        self.left = 0          # 윈도우의 시작
        self.right = 0         #    ''     끝
        self.counts = collections.Counter()
        self.max_len = 0
        self.best_left = 0
        self.best_right = 0

        self.label = tk.Label(root, text=self.s, font=("Arial", 16))
        self.label.pack(pady=10)

        self.info = tk.Label(root, text="", font=("Arial", 12))
        self.info.pack()

        self.next_button = tk.Button(root, text="다음", command=self.step)
        self.next_button.pack(pady=10)

        self.finished = False

    def step(self):
        if self.finished:
            return

        if self.right == len(self.s):
            self.finished = True
            display_str = ""
            for i, ch in enumerate(self.s):
                if self.best_left <= i < self.best_right:
                    display_str += f"[{ch}]"
                else:
                    display_str += f" {ch} "
            self.label.config(text=display_str)
            self.info.config(text=f"최종 최대 구간: {self.best_left}~{self.best_right-1} → 길이: {self.max_len}")
            return

        self.counts[self.s[self.right]] += 1
        max_char_n = self.counts.most_common(1)[0][1]

        while (self.right - self.left + 1) - max_char_n > self.k:
            self.counts[self.s[self.left]] -= 1
            self.left += 1

        window_str = self.s[self.left:self.right+1]
        if len(window_str) > self.max_len:
            self.max_len = len(window_str)
            self.best_left = self.left
            self.best_right = self.right + 1

        self.right += 1

        display_str = ""
        for i, ch in enumerate(self.s):
            if self.left <= i < self.right:
                display_str += f"[{ch}]"
            else:
                display_str += f" {ch} "
        self.label.config(text=display_str)
        self.info.config(text=f"윈도우: '{window_str}' 길이: {len(window_str)} / 최대 길이: {self.max_len}")

root = tk.Tk()
root.title("슬라이딩 윈도우 시각화")
app = SlidingWindow(root, "AASDQEW", 2)
root.mainloop()
