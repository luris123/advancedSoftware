import tkinter as tk
import threading
import winsound
import numpy as np
import time
import random


class Island:
    def __init__(self, canvas, x, y, value, monkeys):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.value = value
        self.monkeys = monkeys

        self.button = tk.Button(self.canvas, text=str(
            self.value), command=self.show_info)
        self.canvas.create_window(self.x, self.y, window=self.button)

        # Initialize the thread for monkey noises
        self.thread = None
        self._stop_thread = False
        self.start_monkeys_make_noise()

    def show_info(self):
        print("x:", self.x, "y:", self.y, "value:",
              self.value, "monkeys:", self.monkeys)

    def delete(self):
        if self.thread:
            self.stop_monkeys_make_noise()
        self.button.destroy()
        del self

    def monkeys_make_noise(self):
        sound_value = self.value[1:]
        hertz_multiplier = int(sound_value)
        while not self._stop_thread:
            for i in range(self.monkeys):
                winsound.Beep(200 + hertz_multiplier * 8, 100)
                time.sleep(0.5)
            time.sleep(10)

    def start_monkeys_make_noise(self):
        if not self.thread:
            self._stop_thread = False  # Reset the flag
            self.thread = threading.Thread(target=self.monkeys_make_noise)
            self.thread.daemon = True
            self.thread.start()

    def stop_monkeys_make_noise(self):
        self._stop_thread = True
        if self.thread and self.thread.is_alive():
            self.thread.join()
        self.thread = None

def generate_island():
    # generate random x and y coordinates
    global generated_islands
    x = random.randint(10, 590)
    y = random.randint(10, 590)

    # check if there is already a button at the randomly generated spot
    overlapping = False
    for widget in canvas.winfo_children():
        if abs(widget.winfo_x() - x) < 50 and abs(widget.winfo_y() - y) < 50:
            overlapping = True
            break

    # if there is already a button at the spot, generate the button elsewhere
    if overlapping:
        generate_island()
    else:
        # create the button at the randomly generated spot
        if 125 <= x <= 250 and 125 <= y <= 250:
            generate_island()
        else:
            button_text = "S"+str(len(generated_islands)+2)
            island = Island(canvas, x, y, button_text, 10)
            generated_islands.append(island)


def delete_all_islands():
    # Stop and join all the island threads
    global generated_islands
    for island in generated_islands:
        island.stop_monkeys_make_noise()
    
    # Delete all island objects
    for island in generated_islands:
        island.delete()
    generated_islands = []
    print(generated_islands)

def delete_all_islands_thread():
    thread = threading.Thread(target=delete_all_islands)
    thread.start()
    


ikkuna = tk.Tk()
ikkuna.geometry("700x700")
canvas = tk.Canvas(ikkuna, width=600, height=600, bg='blue')
canvas.place(x=50, y=50)

generated_islands = []

island_S1 = tk.Button(ikkuna, text="S1", width=7, height=4)
island_S1.place(x=200, y=200)

port_e = tk.Button(ikkuna, text="===")
port_e.place(x=200+50, y=200+20)

port_w = tk.Button(ikkuna, text="===")
port_w.place(x=200-20, y=200+20)

port_n = tk.Button(ikkuna, text="||")
port_n.place(x=200+20, y=200-20)

port_s = tk.Button(ikkuna, text="||")
port_s.place(x=200+20, y=200+60)

generate_button_button = tk.Button(
    ikkuna, text="NEW ISLAND", command=generate_island)
generate_button_button.place(x=50, y=660)

delete_all_islands_button = tk.Button(
    ikkuna, text="DELETE ALL ISLANDS", command=delete_all_islands_thread)
delete_all_islands_button.place(x=150, y=660)


# add five buttons to the top line of the window
koristetta = tk.Label(ikkuna, text="").grid(row=0, column=0)

point_button = []

for i in range(5):
    button_temp = tk.Button(ikkuna, text="Points: "+str(5*(i)), padx=40)
    button_temp.grid(row=0, column=i+1)
    point_button.append(button_temp)


def i_suppose_i_have_earned_so_much_points(amount_of_points):
    points_mod = int(amount_of_points/5)
    for i in range(5):
        point_button[i].configure(bg='gray')
    time.sleep(1)
    point_button[0].configure(bg='green')
    for i in range(points_mod):
        point_button[i+1].configure(bg='green')
        winsound.Beep(440+i*100, 500)
# example ...


i_suppose_i_have_earned_so_much_points(0)

ikkuna.mainloop()
