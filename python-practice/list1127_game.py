import tkinter

def click_btn():
  button["text"] ="購入しました"

root =tkinter.Tk()
root .title("New window")
root .geometry("800x600")
button = tkinter.Button(root, text="購入する", font=("Times New Roman",24), command=click_btn)
button.place(x=200,y=100)
root.mainloop()