import tkinter as tk
from PIL import Image, ImageTk, ImageOps

# 이미지 로드
original_img = Image.open("input.jpg")
current_img = original_img.copy()

# 윈도우 생성
window = tk.Tk()
window.title("이미지 수정 프로그램")
window.geometry("900x600")

# tkinter용 이미지로 변환
tk_img = ImageTk.PhotoImage(current_img)
label = tk.Label(window, image=tk_img)
label.pack(pady=20)

# 이미지 업데이트 함수
def update_image(new_img):
    global current_img, tk_img
    current_img = new_img
    tk_img = ImageTk.PhotoImage(current_img)
    label.config(image=tk_img)

# 흑백 필터 적용
def apply_grayscale():
    gray_img = ImageOps.grayscale(current_img)
    update_image(gray_img)

# 좌우 반전
def flip_horizontal():
    flipped_img = current_img.transpose(Image.FLIP_LEFT_RIGHT)
    update_image(flipped_img)

# 이미지 저장
def save_image():
    current_img.save("edited_image.jpg")
    print("이미지가 'edited_image.jpg'로 저장되었습니다.")

# 버튼 프레임
btn_frame = tk.Frame(window)
btn_frame.pack()

btn_gray = tk.Button(btn_frame, text="흑백 변환", command=apply_grayscale)
btn_gray.grid(row=0, column=0, padx=10)

btn_flip = tk.Button(btn_frame, text="좌우 반전", command=flip_horizontal)
btn_flip.grid(row=0, column=1, padx=10)

btn_save = tk.Button(btn_frame, text="이미지 저장", command=save_image)
btn_save.grid(row=0, column=2, padx=10)

# 실행
window.mainloop()

