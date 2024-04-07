from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = '✓'
check_mark = ''
display_timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    global check_mark
    window.after_cancel(display_timer)
    timer.config(text='Timer', font=(FONT_NAME, 48, 'bold'), fg=fg, bg=YELLOW)
    canvas.itemconfig(timer_text, text='00:00')
    check_mark = ''
    check_label.config(text=check_mark)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global check
    global check_mark
    reps += 1

    if reps % 2 == 0:
        check_mark += check
        check_label.config(text=f'{check_mark}')

    if reps % 8 == 0:
        count_down(20*60)
        timer.config(text='Long Break!', fg=GREEN)
    elif reps % 2 == 0:
        count_down(5*60)
        timer.config(text='Short Break!', fg=PINK)
    else:
        count_down(25*60)
        timer.config(text='Work!', fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    minutes = count // 60
    seconds = count % 60
    if seconds % 60 < 10:
        seconds = f'0{seconds}'

    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        global display_timer
        display_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

fg = GREEN

canvas = Canvas(width=200, height=400, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 200, image=tomato_img)
timer_text = canvas.create_text(100, 220, text='25:00', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

timer = Label(text='Timer', font=(FONT_NAME, 48, 'bold'), fg=fg, bg=YELLOW)
timer.grid(row=0, column=1)

start = Button(text='Start', font=(FONT_NAME, 12, 'normal'), fg=fg, highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text='Reset', font=(FONT_NAME, 12, 'normal'), fg=fg, highlightthickness=0, command=reset)
reset.grid(row=2, column=2)

check_label = Label(bg=YELLOW, fg=fg, font=(FONT_NAME, 48, 'normal'))
check_label.grid(row=3, column=1)

window.mainloop()
