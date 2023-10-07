import tkinter as tk
import winsound
import time
import threading
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ikkuna = tk.Tk()
ikkuna.title("Exercise 6")
ikkuna.geometry("950x950")

canvas = tk.Canvas(ikkuna, width=850, height=850, bg='blue')
canvas.place(x=50, y=50)

island = canvas.create_rectangle(100, 100, 750, 750, fill='burlywood1')


ernesti_oja = np.ones((100, 1))
ernesti_monkey_stop_digging = threading.Event()

ernesti_oja_fig, ernesti_oja_ax = plt.subplots(figsize=(0.3, 4.5))
ernesti_oja_fig.set_facecolor("none")
ernesti_oja_ax.matshow(ernesti_oja)
ernesti_oja_ax.axis("off")
ernesti_oja_fig.tight_layout(pad=0)

ernesti_oja_canvas = FigureCanvasTkAgg(ernesti_oja_fig, master=ikkuna)
ernesti_oja_canvas.get_tk_widget().place(x=250, y=150)

# function for updating the ernesti_oja_ax showing numbers
def update_ernesti_oja_ax():
    for i in range(len(ernesti_oja)):
        ernesti_oja_ax.text(0, i, int(ernesti_oja[i]), fontsize=7)
    ernesti_oja_canvas.draw()


for i in range(len(ernesti_oja)):
    ernesti_oja_ax.text(0, i, int(ernesti_oja[i]), fontsize=7)

exit_flag = threading.Event()

def add_ernesti_monkey():
    ernesti_monkey = canvas.create_oval(175, 530, 195, 550, fill='brown')
    random_number = random.randint(0, 100)
    for i in range(random_number):
        canvas.move(ernesti_monkey, 0, -4.4)
        canvas.update()
        time.sleep(0.01)
    while True:
        if ernesti_monkey_stop_digging.is_set() == False:
            digging_speed = 1
            digging_left = 100 - random_number
            for i in range(digging_left, -1, -1):
                ernesti_oja[i] -= 1
                update_ernesti_oja_ax()
                canvas.move(ernesti_monkey, 0, -4.2)
                canvas.update()
                print(digging_speed)
                time.sleep(digging_speed)
                digging_speed *= 2
            time.sleep(3)
            canvas.delete(ernesti_monkey)
            break
        else:
            print("Ernesti monkey not digging")
            time.sleep(3)

def ernesti_monkey_start_or_stop_digging():
    if ernesti_monkey_stop_digging.is_set():
        ernesti_monkey_stop_digging.clear()
    else:
        ernesti_monkey_stop_digging.set()

def ernesti_monkey_thread():
    threading.Thread(target=add_ernesti_monkey).start()
ernesti_monkey_stop_digging.set()


kernesti_oja = np.ones((100, 1))
kernesti_monkey_stop_digging = threading.Event()

kernesti_oja_fig, kernesti_oja_ax = plt.subplots(figsize=(0.3, 4.5))
kernesti_oja_fig.set_facecolor("none")
kernesti_oja_ax.matshow(kernesti_oja)
kernesti_oja_ax.axis("off")
kernesti_oja_fig.tight_layout(pad=0)

kernesti_oja_canvas = FigureCanvasTkAgg(kernesti_oja_fig, master=ikkuna)
kernesti_oja_canvas.get_tk_widget().place(x=670, y=150)

def update_kernesti_oja_ax():
    for i in range(len(kernesti_oja)):
        kernesti_oja_ax.text(0, i, int(kernesti_oja[i]), fontsize=7)
    kernesti_oja_canvas.draw()

for i in range(len(kernesti_oja)):
    kernesti_oja_ax.text(0, i, int(kernesti_oja[i]), fontsize=7)
    
def add_kernesti_monkey():
    kernesti_monkey = canvas.create_oval(655, 530, 675, 550, fill='brown')
    random_number = random.randint(0, 100)
    for i in range(random_number):
        canvas.move(kernesti_monkey, 0, -4.2)
        canvas.update()
        time.sleep(0.01)
    while True:
        if kernesti_monkey_stop_digging.is_set() == False:
            digging_speed = 1
            digging_left = 100 - random_number
            for i in range(digging_left, -1, -1):

                kernesti_oja[i] -= 1
                update_kernesti_oja_ax()
                canvas.move(kernesti_monkey, 0, -4.2)
                canvas.update()
                print(digging_speed)
                time.sleep(digging_speed)
                digging_speed *= 2
            time.sleep(3)
            canvas.delete(kernesti_monkey)
            break
        else:
            print("Kernesti monkey not digging")
            time.sleep(3)
            
def kernesti_monkey_thread():
    threading.Thread(target=add_kernesti_monkey).start()
kernesti_monkey_stop_digging.set()

def kernesti_monkey_start_or_stop_digging():
    if kernesti_monkey_stop_digging.is_set():
        kernesti_monkey_stop_digging.clear()
    else:
        kernesti_monkey_stop_digging.set()
        
# function that resets both ojas and delete monkeys and clear threads
def reset_oja():
    pass

    
    
def reset_oja_thread():
    threading.Thread(target=reset_oja).start()

reset_oja_button = tk.Button(
    ikkuna, text="Reset oja", command=reset_oja_thread)
reset_oja_button.place(x=450, y=100)

pool = np.zeros((20, 60))
pool_fig, pool_ax = plt.subplots(figsize=(4.5, 1.5))
pool_ax.matshow(pool)
pool_ax.axis("off")
pool_fig.set_facecolor("none")
pool_fig.tight_layout(pad=0)
pool_fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
pool_in_canvas = FigureCanvasTkAgg(pool_fig, master=ikkuna)
pool_in_canvas.get_tk_widget().place(x=250, y=600)

for i in range(len(pool)):
    for j in range(len(pool[i])):
        pool_ax.text(j, i, int(pool[i][j]),
                     va="center", ha="center", fontsize=6)

ernesti_monkey_button = tk.Button(
    ikkuna, text="Add monkey to Ernesti Oja", command=ernesti_monkey_thread)
ernesti_monkey_button.place(x=250, y=70)
ernesti_monkey_digging_button = tk.Button(
    ikkuna, text="Start/Stop digging", command=ernesti_monkey_start_or_stop_digging)
ernesti_monkey_digging_button.place(x=250, y=100)

kernesti_monkey_button = tk.Button(
    ikkuna, text="Add monkey to Kernesti Oja", command=kernesti_monkey_thread)
kernesti_monkey_button.place(x=670, y=70)
kernesti_monkey_digging_button = tk.Button(
    ikkuna, text="Start/Stop digging", command=kernesti_monkey_start_or_stop_digging)
kernesti_monkey_digging_button.place(x=670, y=100)

# add five buttons to the top line of the window
koristetta = tk.Label(ikkuna, text="").grid(row=0, column=0)
point_button = []
for i in range(5):
    button_temp = tk.Button(ikkuna, text="Points: "+str(i+1), padx=40)
    button_temp.grid(row=0, column=i+1)
    point_button.append(button_temp)


def i_suppose_i_have_earned_so_much_points(amount_of_points):
    for i in range(5):
        point_button[i].configure(bg='gray')
    time.sleep(1)
    for i in range(amount_of_points):
        point_button[i].configure(bg='green')
        winsound.Beep(440+i*100, 500)
# example ...
# i_suppose_i_have_earned_so_much_points(3)


ikkuna.mainloop()
