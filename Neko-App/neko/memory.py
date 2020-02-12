import tkinter
from PIL import Image, ImageTk

# windowを描画
window = tkinter.Tk()
# windowサイズを変更
# window.geometry("1500x1500")
# windowタイトルを設定
window.title("Welcome to the Tkinter")

# 画像を表示するための準備
img = Image.open('image0.jpeg')
img = ImageTk.PhotoImage(img)
# 画像を表示するためのキャンバスの作成（黒で表示）
canvas = tkinter.Canvas(bg = "black", width=1500, height=1500)
canvas.place(x=0, y=0) # 左上の座標を指定
# キャンバスに画像を表示する。第一引数と第二引数は、x, yの座標
canvas.create_image(0, 0, image=img, anchor=tkinter.NW)

window.mainloop()