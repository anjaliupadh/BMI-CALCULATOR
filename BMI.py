from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("BMI CALCULATOR")
root.geometry("480x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

def BMI():
    h = float(Height.get())
    w = float(Weight.get())
    
    # convert height to meters
    m = h / 100
    bmi = round(float(w / m**2), 1)
    print(bmi)
    Label1.config(text=f"BMI = {bmi}")
    
    # change the value
    if bmi <= 18.5:
        Label2.config(text="Underweight")
        Label3.config(text="You have lower weight than normal body!")
    elif 18.5 < bmi <= 24.9:
        Label2.config(text="Normal")
        Label3.config(text="It indicates that you are healthy!😍")
    elif 25 <= bmi <= 29.9:
        Label2.config(text="Overweight!")
        Label3.config(text="It indicates that a person is\nslightly overweight.\nA doctor may advise to lose some\nweight for health!")
    else:
        Label2.config(text="Obese!")
        Label3.config(text="Health may be at risk if they do not\nlose weight!")

# icon
image_icon = PhotoImage(file="images/logo2.png")
root.iconphoto(False, image_icon)

# top heading
Label(root, text="BMI CALCULATOR", font='arial 30 bold', bg="#f0f1f5").place(x=60, y=30)

# bottom box
Label(root, width=72, height=18, bg="lightblue").pack(side=BOTTOM)

# two boxes
box = PhotoImage(file="images/happy.png")
Label(root, image=box).place(x=20, y=135)
Label(root, image=box).place(x=240, y=135)

# scale
scale = PhotoImage(file="images/hoja.png")
Label(root, image=scale, bg="lightblue").place(x=10, y=315)

# Slider1
current_value = tk.DoubleVar()

def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    size = int(float(get_current_value()))
    img = (Image.open("images/mennn.png"))
    resized_image = img.resize((60, 10 + size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=90, y=550 - size)
    secondimage.image = photo2

# change background
style = ttk.Style()
style.configure("TScale", background="white")
slider = ttk.Scale(root, from_=0, to=220, orient="horizontal", style="TScale", command=slider_changed, variable=current_value)
slider.place(x=80, y=250)

# Slider2
current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{:.2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

# change background
style2 = ttk.Style()
style2.configure("TScale", background="white")
slider2 = ttk.Scale(root, from_=0, to=200, orient="horizontal", style="TScale", command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)

# entry box
Height = StringVar()
Weight = StringVar()

# Height and Weight labels with units
Label(root, text="Height (m)", font='arial 15', bg="lightgrey").place(x=30, y=154)
Label(root, text="Weight (kg)", font='arial 15', bg="lightgrey").place(x=250, y=154)

height = Entry(root, textvariable=Height, width=5, font='arial 50', bg="lightgrey", fg="#000", bd=0, justify=CENTER)
height.place(x=27, y=180)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=5, font='arial 50', bg="lightgrey", fg="#000", bd=0, justify=CENTER)
weight.place(x=245, y=180)
Weight.set(get_current_value2())

# man image
secondimage = Label(root, bg="lightblue")
secondimage.place(x=90, y=530)

Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(x=280, y=340)
Label1 = Label(root, font="arial 40 bold", bg="lightblue", fg="black")
Label1.place(x=180, y=400)

Label2 = Label(root, font="arial 20 bold", bg="lightblue", fg="#3b3a3a")
Label2.place(x=180, y=470)

Label3 = Label(root, font="arial 10 bold", bg="lightblue")
Label3.place(x=180, y=500)

root.mainloop()
