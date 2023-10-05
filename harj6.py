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
island = canvas.create_rectangle(100, 100, 500, 500, fill='green')

# add a swimming pool to the center of hte island the size of 60x20



# matetmatiikkaa...
oja = np.zeros((10, 1))
for i in range(10):
    oja[i] = 5


# perinteiseen tapaan ... piirretään kuvaaja "erilleen"...
fig1, ax1 = plt.subplots(figsize=(0.2, 2))
fig1.set_facecolor("#F0F0F0")
ax1.matshow(oja)
ax1.axis("off")
# remove padding around the figure
plt.tight_layout(pad=0)




# erikoisella tavalla...kuvaajan pitää näkyä käyttöliittymässä...
erikois_oja_kanvaasi = FigureCanvasTkAgg(fig1, master=ikkuna)
erikois_oja_kanvaasi.get_tk_widget().place(x=250, y=150)

erikois_oja_kanvaasi.draw()


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
