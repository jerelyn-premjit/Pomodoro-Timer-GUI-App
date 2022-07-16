from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def hitreset():
    window.after_cancel(timer)
    canvas.itemconfig(timertxt,text = "00:00")
    l.config(text="Timer")
    check_marks.config(text="")
    global rep
    rep=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def hitstart():
    global rep
    rep = rep + 1

    worktimer = WORK_MIN*60
    shortbreaktimer = SHORT_BREAK_MIN*60
    longbreaktimer = LONG_BREAK_MIN*60

    if(rep%8==0):
        currentrep = longbreaktimer
        l.config(text="Break",fg=RED)
    elif(rep%2==0):
        currentrep = shortbreaktimer
        l.config(text="Break",fg=PINK)
    else:
        currentrep = worktimer
        l.config(text = "Work",fg=GREEN)
    count_down(currentrep)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    mins_left = math.floor(count/60)
    seconds_left = count%60
    if seconds_left<10:
        seconds_left = f"0{seconds_left}"
    if mins_left<10:
        mins_left = f"0{mins_left}"

    canvas.itemconfig(timertxt, text=f"{mins_left}:{seconds_left}")
    if(count>0):
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        hitstart()
        marks = ""
        work_sessions = math.floor(rep / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Jerelyn's Pomodoro")
window.config(width=200,height=400,padx=70,pady=50,bg=YELLOW)
#TITLE
l = Label(text = "Timer", font=(FONT_NAME,40,"bold"), bg= YELLOW, fg=GREEN)
l.grid(column = 1,row=0)

#TOMATO
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timertxt = canvas.create_text(103,132,text="00:00",font=(FONT_NAME,30,"bold"))
canvas.grid(column =1 ,row=1)

#RESET AND START BUTTONS
start = Button(text = "Start",bg=YELLOW, command = hitstart ,highlightthickness=0, highlightcolor=YELLOW)
start.grid(column=0,row=3)


reset = Button(text = "Reset",bg=YELLOW, command = hitreset,highlightthickness=0, highlightcolor=YELLOW)
reset.grid(column=2,row=3)

#TICK LABEL
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()