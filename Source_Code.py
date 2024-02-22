import tkinter as tk
import random
# Setting Main Frame
window = tk.Tk()
window.title("Cricket")
window.geometry("700x600+20+20")
window.iconbitmap("./imgIcon.ico")
window.configure(bg="white")
# window.attributes("-topmost",1)


score1 = 0
score2 = 0
batting=True


def buttons_clicked(txt):
    global score2,lb22, lb25,lb
    lb.place_forget()
    score2 += int(txt)
    lb25.config(text=txt)
    #lb22.config(text="Score: "+str(score2))
    print(txt)
    play(txt)


def play(txt):
    global batting,score1, lb14
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random_num = random.choice(numbers)
    lb14.config(text=random_num)
    num=int(txt)
    if not batting:
        score1 += random_num
    if num == random_num:
        lb.place(relx=0.5, rely=0.821, anchor=tk.CENTER)
        frame4.place(relx=0.5, rely=0.53, anchor=tk.CENTER, width=700, height=700)
        if batting:
            print("Player out")
            batting = False
        else:
            print("System Out")
            batting = True
    else:
        if batting:
            lb22.config(text="Score: " + str(score2))

        else:
            lb12.config(text="Score: " + str(score1))


def reset():
    global lb12, lb22, score1, score2, lb13, lb24, lb14, lb25, frame4
    frame4.place_forget()
    lb12.config(text="Score: " + "0")
    lb22.config(text="Score: " + "0")
    lb24.config(text="")
    lb13.config(text="")
    lb14.config(text="")
    lb25.config(text="")
    score1 = 0
    score2 = 0
    if random.choice([1, 2]) == 1:
        lb24.config(text=" You are Bowling ")
        lb13.config(text="System is Batting")
    else:
        lb24.config(text=" You are Batting ")
        lb13.config(text="System is Bowling")


# Creating Frames
# frame = tk.Frame(window)
# frame.pack(fill=tk.BOTH, expand=True,padx=10,pady=10)

frame1 = tk.Frame(window, bg="lightskyblue")
frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
lb1 = tk.Label(frame1, text="SYSTEM", bg="lightskyblue", fg="white", font=("Arial",22,"bold","underline"))
lb1.pack(side=tk.TOP, expand=False, pady=10)
lb11 = tk.Label(frame1, text="", bg="lightskyblue", font=("Arial",15,""))
lb11.pack()
lb12 = tk.Label(frame1, text="Score: "+"0", bg="lightskyblue", font=("Arial", 18, "bold"))
lb12.pack()
lb13 = tk.Label(frame1, text="System is Batting", bg="lightskyblue", font=("Arial", 15, "bold"))
lb13.pack(side=tk.BOTTOM, pady=10)
lb14 = tk.Label(frame1,text="", bg="lightskyblue", font=("Arial", 25, "bold"))
lb14.place(relx=0.5,rely=0.8, anchor=tk.CENTER)
img= tk.PhotoImage(file="img.png")
lb15 = tk.Label(image=img,width=250, height=250,bg="lightskyblue")
lb15.place(relx=0.25,rely=0.52,anchor=tk.CENTER)

frame2 = tk.Frame(window, bg="lightgreen")
frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
lb2 = tk.Label(frame2,text="PLAYER",bg="lightgreen",fg="white",font=("Arial",22,"bold","underline"))
lb2.pack(side=tk.TOP, expand=False, pady=10)
lb21 = tk.Label(frame2, text="", bg="lightgreen", font=("Arial",15,""))
lb21.pack()
lb22 = tk.Label(frame2, text="Score: "+"5", bg="lightgreen", font=("Arial", 18, "bold"))
lb22.pack()
lb22.config(text="Score: "+"0")
lb23 = tk.Label(frame2, text="Click any of the button", bg="lightgreen", font=("Arial", 12))
lb23.place(relx=0.5, rely=0.4, anchor=tk.S)
lb24 = tk.Label(frame2, text=" You are Batting ", bg="lightgreen", font=("Arial", 15, "bold"))
lb24.pack(side=tk.BOTTOM, pady=10)
lb25 = tk.Label(frame2,text="", bg="lightgreen", font=("Arial", 25, "bold"))
lb25.place(relx=0.5,rely=0.8, anchor=tk.CENTER)

frame3 = tk.Frame(frame2, bg="lightgreen")
frame3.pack(side=tk.TOP, fill=tk.X, expand=True)  # Expand horizontally to fill available space
frame3.place(relx=0.5, rely=0.53, anchor=tk.CENTER)
b = []
j = 1
k = 0
for i in range(10):
    b.append(tk.Button(frame3, text=i+1, command=lambda num=i+1: buttons_clicked(num),
               width=3, height=2,  # Set width and height of the button
                fg="black",  # Set background and foreground (text) colors
               font=("Arial", 12,"bold"),  # Set font family and size
               relief=tk.RAISED,  # Set relief style (BORDER, FLAT, RAISED, SUNKEN)
               borderwidth=4,  # Set border width
               padx=2, pady=5) )
    b[i].grid(row=j, column=k)
    k=k+1
    if i==4:
        j=2
        k=0

frame4=tk.Frame(window, bg="black")
#frame4.place(relx=0.5, rely=0.53, anchor=tk.CENTER, width=600, height=600)


button = tk.Button(window, text="RESET", width=7, height=1, font=("Courier",12,"bold"), fg="black", command=lambda: reset())
button.pack(side=tk.TOP, fill=tk.X, expand=True)  # Expand horizontally to fill available space
button.place(relx=0.5, rely=0.21, anchor=tk.CENTER)
lb =tk.Label(window,text="OUT !!!",width=8, height=1, font=("Courier",20,"bold"), fg="white",bg="red")
#lb.place(relx=0.5, rely=0.821, anchor=tk.CENTER)
window.mainloop()
