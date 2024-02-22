import tkinter as tk
import random

# Setting Main Frame
window = tk.Tk()
window.title("Let's Cricket")
window.geometry("700x600+20+20")
window.iconbitmap("./imgIcon.ico")
window.configure(bg="white")

score1 = 0
score2 = 0
highscore = 0
Sys_batting = 0
Plr_batting = 0


def buttons_clicked(txt):
    global score2, lb22, lb25, lb, Sys_batting, Plr_batting
    lb.place_forget()
    if Plr_batting:
        score2 += int(txt)
    lb25.config(text=txt)
    print(txt, end=" ")
    play(txt)


def play(txt):
    global score1, lb14, Sys_batting, Plr_batting
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random_num = random.choice(numbers)
    lb14.config(text=random_num)
    num = int(txt)
    if Sys_batting == 1:
        score1 += random_num
    if num == random_num:
        lb.place(relx=0.5, rely=0.821, anchor=tk.CENTER)
        if Plr_batting == 1:
            print("Player out")
            Plr_batting = 2
            if Sys_batting == 0:
                Sys_batting = 1
                lb24.config(text=" You are Bowling🏐 ")
                lb13.config(text="System is Batting🦇")
        elif Sys_batting == 1:
            print("System Out")
            Sys_batting = 2
            if Plr_batting == 0:
                Plr_batting = 1
                lb24.config(text=" You are Batting🦇 ")
                lb13.config(text="System is Bowling🏐")
    else:
        if Plr_batting:
            lb22.config(text="Score: " + str(score2))
        else:
            lb12.config(text="Score: " + str(score1))

    if (score1 > 0) and (score2 > 0):
        if (Sys_batting == 1) and (score1 > score2):
            print("GAME OVERR")
            lb.place_forget()
            button.place_forget()
            frame4.place(relx=0.5, rely=0.53, anchor=tk.CENTER, width=700, height=700)
            lb.config(text="System Won")
            return
        elif (Plr_batting == 1) and (score1 < score2):
            print("GAME OVERR")
            lb.place_forget()
            button.place_forget()
            frame4.place(relx=0.5, rely=0.53, anchor=tk.CENTER, width=700, height=700)
            lb.config(text="Player Won")
            return

    if Plr_batting == 2 and Sys_batting == 2:
        print("GAME OVER")
        lb.place_forget()
        button.place_forget()
        frame4.place(relx=0.5, rely=0.53, anchor=tk.CENTER, width=700, height=700)


def reset():
    global lb12, lb22, score1, score2, lb14, lb25, frame4, Sys_batting, Plr_batting, highscore
    frame4.place_forget()
    Sys_batting = 0
    Plr_batting = 0
    lb12.config(text="Score: " + "0")
    lb22.config(text="Score: " + "0")
    lb14.config(text="")
    lb25.config(text="")
    score1 = 0
    score2 = 0
    if random.choice([1, 2]) == 1:
        Sys_batting = 1
        lb24.config(text=" You are Bowling🏐 ")
        lb13.config(text="System is Batting🦇")
    else:
        Plr_batting = 1
        lb24.config(text=" You are Batting🦇 ")
        lb13.config(text="System is Bowling🏐")


def restart():
    global frame4, score1, score2, Sys_batting, Plr_batting, highscore, lb12, lb22, lb, lb26
    frame4.place_forget()
    if highscore < score2:
        highscore = score2
        lb26.config(text="HighScore: " + str(highscore))
    lb12.config(text="Score: " + "0")
    lb22.config(text="Score: " + "0")
    lb = tk.Label(window, text="OUT !!!", width=8, height=1, font=("Courier", 20, "bold"), fg="white", bg="red")
    button.place(relx=0.5, rely=0.21, anchor=tk.CENTER)
    reset()


# Creating Frames
frame1 = tk.Frame(window, bg="#00FFFF")
frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
lb1 = tk.Label(frame1, text="SYSTEM", bg="#00FFFF", fg="#040406", font=("Arial", 22, "bold", "underline"))
lb1.pack(side=tk.TOP, expand=False, pady=10)
lb11 = tk.Label(frame1, text="", bg="#00FFFF", font=("Arial", 15, ""))
lb11.pack()
lb12 = tk.Label(frame1, text="Score: "+"0", bg="#00FFFF", font=("Arial", 18, "bold"))
lb12.pack()
lb13 = tk.Label(frame1, text="System is Bowling🏐", bg="#00FFFF", font=("Arial", 15, "bold"))
lb13.pack(side=tk.BOTTOM, pady=10)
lb14 = tk.Label(frame1, text="", bg="#00FFFF", font=("Arial", 25, "bold"))
lb14.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
img = tk.PhotoImage(file="img.png")
lb15 = tk.Label(image=img, width=250, height=250, bg="#00FFFF")
lb15.place(relx=0.25, rely=0.52, anchor=tk.CENTER)

frame2 = tk.Frame(window, bg="#FC46AA")
frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
lb2 = tk.Label(frame2, text="PLAYER", bg="#FC46AA", fg="white", font=("Arial", 22, "bold", "underline"))
lb2.pack(side=tk.TOP, expand=False, pady=10)
lb21 = tk.Label(frame2, text="", bg="#FC46AA", font=("Arial", 15, ""))
lb21.pack()
lb22 = tk.Label(frame2, text="Score: "+"5", bg="#FC46AA", font=("Arial", 18, "bold"))
lb22.pack()
lb22.config(text="Score: "+"0")
lb23 = tk.Label(frame2, text="Click any of the button", bg="#FC46AA", font=("Arial", 12))
lb23.place(relx=0.5, rely=0.42, anchor=tk.S)
lb24 = tk.Label(frame2, text=" You are Batting🦇 ", bg="#FC46AA", font=("Arial", 15, "bold"))
lb24.pack(side=tk.BOTTOM, pady=10)
lb25 = tk.Label(frame2, text="", bg="#FC46AA", font=("Arial", 25, "bold"))
lb25.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
lb26 = tk.Label(frame2, text="HighScore: "+str(highscore), bg="#FC46AA", font=("Arial", 12))
lb26.place(relx=0.5, rely=0.26, anchor=tk.S)

frame3 = tk.Frame(frame2, bg="#FC46AA")
frame3.pack(side=tk.TOP, fill=tk.X, expand=True)
frame3.place(relx=0.5, rely=0.53, anchor=tk.CENTER)
b = []
j = 1
k = 0
for i in range(10):
    b.append(tk.Button(frame3, text=i+1, command=lambda num=i+1: buttons_clicked(num),
             width=3, height=2, fg="black", bg="#FEC5E5", font=("Arial", 12, "bold"),
             relief=tk.RAISED, borderwidth=4, padx=2, pady=2))
    b[i].grid(row=j, column=k)
    k = k+1
    if i == 4:
        j = 2
        k = 0

frame4 = tk.Frame(window, bg="black")
lb41 = tk.Label(frame4, text="GAME OVER !\n Click RESTART to continue", font=("Arial", 20, "bold"), bg="black",
                fg="white")
lb41.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
b41 = tk.Button(frame4, text="RESTART", font=("Arial", 15, "bold"), bg="#4CBB17", fg="black", command=lambda: restart())
b41.place(relx=0.5, rely=0.51, anchor=tk.CENTER)


button = tk.Button(window, text="RESET", width=7, height=1, font=("Courier", 12, "bold"), fg="black",
                   command=lambda: reset())
button.pack(side=tk.TOP, fill=tk.X, expand=True)  # Expand horizontally to fill available space
button.place(relx=0.5, rely=0.21, anchor=tk.CENTER)
lb = tk.Label(window, text="OUT !!!", width=8, height=1, font=("Courier", 20, "bold"), fg="white", bg="red")
reset()
window.mainloop()
