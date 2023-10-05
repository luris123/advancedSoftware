import tkinter as tk
import winsound
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ikkuna = tk.Tk()
ikkuna.title("Exercise 6")
ikkuna.geometry("700x700")

canvas = tk.Canvas(ikkuna, width=600, height=600, bg='blue')
canvas.place(x=50, y=50)

# add an island to the center of canvas the size of 400x400
island = canvas.create_rectangle(100, 100, 500, 500, fill='burlywood1')


ernesti_oja = np.zeros((10, 1))

ernesti_oja_fig, ernesti_oja_ax = plt.subplots(figsize=(0.2, 2))
ernesti_oja_fig.set_facecolor("none")
ernesti_oja_ax.matshow(ernesti_oja)
ernesti_oja_ax.axis("off")
ernesti_oja_fig.tight_layout(pad=0)

ernesti_oja_canvas = FigureCanvasTkAgg(ernesti_oja_fig, master=ikkuna)
ernesti_oja_canvas.get_tk_widget().place(x=250, y=150)

# fill ernesti_oja with 1's
for i in range(len(ernesti_oja)):
    ernesti_oja_ax.text(0, i, 1, va="center", ha="center",
                        color="white", fontsize=10)


kernesti_oja = np.zeros((10, 1))

kernesti_oja_fig, kernesti_oja_ax = plt.subplots(figsize=(0.2, 2))
kernesti_oja_fig.set_facecolor("none")
kernesti_oja_ax.matshow(kernesti_oja)
kernesti_oja_ax.axis("off")
kernesti_oja_fig.tight_layout(pad=0)

kernesti_oja_canvas = FigureCanvasTkAgg(kernesti_oja_fig, master=ikkuna)
kernesti_oja_canvas.get_tk_widget().place(x=430, y=150)

for i in range(len(kernesti_oja)):
    kernesti_oja_ax.text(0, i, 1, va="center", ha="center",
                         color="white", fontsize=10)

pool = np.zeros((2, 6))
pool_fig, pool_ax = plt.subplots(figsize=(2, 0.67))
pool_ax.matshow(pool, cmap="viridis")
pool_ax.axis("off")
pool_fig.tight_layout(pad=0)
pool_fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
pool_in_canvas = FigureCanvasTkAgg(pool_fig, master=ikkuna)
pool_in_canvas.get_tk_widget().place(x=250, y=350)

for i in range(len(pool)):
    for j in range(len(pool[i])):
        pool_ax.text(j, i, int(pool[i][j]), va="center",
                     ha="center", color="white", fontsize=10)


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
