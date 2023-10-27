import tkinter as tk
from tkinter import messagebox
from tkinter import *
import base64
import os
def main_screen():
    global root
    global code
    global text1
    root=tk.Tk()
    root.geometry("800x300")
    root.title("SECRET MESSAGE")

    def decrypt():
        password = code.get()
        if password == "1234":
            root2 = Toplevel(root)
            root2.title("decryption")
            root2.geometry("400x200")
            root2.configure(bg="#ed3833")
            message = text1.get(1.0, END)
            decode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decode_message)
            decrypt = base64_bytes.decode("ascii")
            Label(root2, text="DECRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
            text2 = Text(root2, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(END, decrypt)
        elif password == "":
            messagebox.showerror("decryption", "Input Password")
        elif password != "1234":
            messagebox.showerror("decryption","Invalid Password")

    def encrypt():
        password = code.get()
        if password == "1234":
            root1 = Toplevel(root)
            root1.title("encryption")

            root1.geometry("400x200")
            root1.configure(bg="#1089ff")
            message = text1.get(1.0, END)
            encode_message = message.encode("ascii")
            base64_bytes = base64.b64encode(encode_message)
            encrypt=base64_bytes
            Label(root1, text="ENCRYPT",font="arial",fg="white",bg="#1089ff").place(x=10, y=0)
            text2 = Text(root1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(END,encrypt)
        elif password == "":
            messagebox.showerror("encryption", "Input Password")
        elif password != "1234":
            messagebox.showerror("encryption", "Invalid Password")

    def reset():
        code.set("")
        text1.delete(1.0, END)
    Label(text="enter text for encryption and decryption",fg="black",font=("arial",13)).place(x=10,y=10)
    text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)
    Label(text="enter secret key for encryption and decryption", fg="black", font=("calbri", 13)).place(x=10,y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25),show="*").place(x=10, y=200)
    Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white",bd=0,command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0,command=reset).place(x=10, y=300)
    root.mainloop()
main_screen()