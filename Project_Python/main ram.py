from Tkinter import *
root=Tk()
root.geometry('900x600')
root.title("Ram marriage bureau")
def theFunction(e=0):
    root.destroy()
    import ramram
root.configure(background="light blue")
Label(root, text="Welcome to Matrimonial spot", font=("algerian", 40), fg="white",bg="#ff2299" ,width=27).place(x=0,y=0)
Label(root, text="Presented By: Udaya Sri", font=("algerian", 14), fg="blue", bg="green").place(x=10,y=80)
Label(root, text="Enroll No.: 171B084", font=("algerian", 15), fg="blue", bg="green").place(x=10,y=120)
Label(root, text="Batch: B7", font=("algerian", 15), fg="blue", bg="green").place(x=10,y=160)
Label(root, text="University: JNTUN", font=("algerian", 15), fg="blue", bg="green").place(x=10,y=200)
Label(root, text="Email: udayaguttikonda@gmail.com", font=("Comic Sans MS", 15), fg="blue", bg="green").place(x=10,y=240)
Label(root, text="Mob.: +919575794665", font=("Comic Sans MS", 15), fg="blue", bg="green").place(x=10,y=280)
a=PhotoImage (file="ram.gif")
l=Label(root, image=a)
l.place (x=550, y=120)
l.bind('<Motion>',theFunction)
root.mainloop()
