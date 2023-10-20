import tkinter as tk
import threading
import winsound
import numpy as np
import time
import random


monkeys_on_island_S1 = 10
travel_awareness_S1 = 1


class Island:
    def __init__(self, canvas, x, y, value, monkeys, travel_awareness):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.value = value
        self.monkeys = monkeys

        self.travel_awareness = travel_awareness
        self.port_e = None
        self.port_w = None
        self.port_n = None
        self.port_s = None

        self.color = "yellow"

        self.button = tk.Button(self.canvas, text=str(
            self.value) + "\n" + str(self.monkeys), command=self.show_info, bg=(self.color))
        self.canvas.create_window(self.x, self.y, window=self.button)

        # Initialize the thread for monkey noises
        self.thread = None
        self.thread_send_monkey_to_swim = None
        self._stop_thread = False
        self._stop_thread_send_monkey_to_swim = False
        self.start_monkeys_make_noise()
        self.start_send_monkey_to_swim()

    def show_info(self):
        print("x:", self.x, "y:", self.y, "value:",
              self.value, "monkeys:", self.monkeys, "travel_awareness:", self.travel_awareness)

    def set_travel_awareness(self, new_value):
        self.travel_awareness = new_value
        if new_value == 1:
            self.start_send_monkey_to_swim()

    def delete_ports(self):
        if self.port_e:
            self.port_e.destroy()
        if self.port_w:
            self.port_w.destroy()
        if self.port_n:
            self.port_n.destroy()
        if self.port_s:
            self.port_s.destroy()

    def delete(self):
        self.delete_ports()
        if self.thread:
            self.stop_monkeys_make_noise()
        if self.thread_send_monkey_to_swim:
            self.stop_send_monkey_to_swim()
        self.delete_ports()
        
        self.button.destroy()
        del self

    def send_monkey_to_swim(self):
        while not self._stop_thread_send_monkey_to_swim:
            while True:
                if self.travel_awareness == 1 and self.monkeys > 0:
                    winsound.Beep(1200, 100)
                    print("A monkey has been sent from", self.value, "...")
                    self.monkeys -= 1
                    self.update_island_text()
                    print("...Now there are", self.monkeys,
                          "monkeys on", self.value)
                    self.choose_random_port()
                time.sleep(10)
                if self._stop_thread_send_monkey_to_swim:
                    return

    def choose_random_port(self):
        global monkeys_on_island_S1
        global island_S1
        island_S1_geometry = island_S1.winfo_geometry()
        # get the coordinates of the island S1
        x1 = int(island_S1_geometry.split("+")[1])
        y1 = int(island_S1_geometry.split("+")[2])
        x2 = x1 + 50
        y2 = y1 + 50
        
        random_port = random.randint(0, 3)
        break_loop = False
        # create ports to the island similar to island S1
        self.port_e = tk.Button(self.canvas, text="===")
        self.port_e.place(x=self.x+10, y=self.y-10)
        self.port_w = tk.Button(self.canvas, text="===")
        self.port_w.place(x=self.x-40, y=self.y-10)
        self.port_n = tk.Button(self.canvas, text="||")
        self.port_n.place(x=self.x-10, y=self.y-40)
        self.port_s = tk.Button(self.canvas, text="||")
        self.port_s.place(x=self.x-10, y=self.y+20)

        if random_port == 0:
            monkey = canvas.create_oval(
                self.x+50, self.y+20, self.x+50+10, self.y+20+10, fill="brown")
            # move oval to the right until it reaches the edge of the canvas
            while canvas.coords(monkey)[0] < 590:
                canvas.move(monkey, 10, 0)
                time.sleep(0.1)
                random_number = random.randint(1, 100)
                if random_number == 1:
                    canvas.delete(monkey)
                    print("A monkey was eaten by a shark")
                    winsound.Beep(100, 100)
                    break
                # check if there is an island at the spot
                overlaps = canvas.find_overlapping(
                    canvas.coords(monkey)[0], canvas.coords(monkey)[1], canvas.coords(monkey)[2], canvas.coords(monkey)[3])
                if len(overlaps) > 1:
                    for island in generated_islands:
                        if abs(island.x - canvas.coords(monkey)[0]) < 50 and abs(island.y - canvas.coords(monkey)[1]) < 50:
                            print("A monkey arrived on island", island.value)
                            island.monkeys += 1
                            island.travel_awareness = 1
                            island.update_island_text()
                            canvas.delete(monkey)
                            break_loop = True
                            break
                if canvas.coords(monkey):
                    monkey_x = canvas.coords(monkey)[0]
                    monkey_y = canvas.coords(monkey)[1]
                    
                    if (monkey_x > x1 and monkey_x < x2 and monkey_y > y1 and monkey_y < y2):
                        print("A monkey arrived on island S1")
                        monkeys_on_island_S1 += 1
                        island_S1.configure(text="S1\n" +
                                            str(monkeys_on_island_S1))
                        canvas.delete(monkey)
                        break_loop = True
                        break
                if break_loop:
                    break
            canvas.delete(monkey)

        elif random_port == 1:
            monkey = canvas.create_oval(
                self.x-20, self.y+20, self.x-20+10, self.y+20+10, fill="brown")
            # move oval to the left until it reaches the edge of the canvas
            while canvas.coords(monkey)[0] > 10:
                canvas.move(monkey, -10, 0)
                time.sleep(0.1)
                random_number = random.randint(1, 100)
                if random_number == 1:
                    canvas.delete(monkey)
                    print("A monkey was eaten by a shark")
                    winsound.Beep(100, 100)
                    break
                # check if there is an island at the spot
                overlaps = canvas.find_overlapping(
                    canvas.coords(monkey)[0], canvas.coords(monkey)[1], canvas.coords(monkey)[2], canvas.coords(monkey)[3])
                if len(overlaps) > 1:
                    for island in generated_islands:
                        if abs(island.x - canvas.coords(monkey)[0]) < 50 and abs(island.y - canvas.coords(monkey)[1]) < 50:
                            print("A monkey arrived on island", island.value)
                            island.monkeys += 1
                            island.travel_awareness = 1
                            island.update_island_text()
                            canvas.delete(monkey)
                            break_loop = True
                            break
                if canvas.coords(monkey):
                    monkey_x = canvas.coords(monkey)[0]
                    monkey_y = canvas.coords(monkey)[1]
                    
                    if (monkey_x > x1 and monkey_x < x2 and monkey_y > y1 and monkey_y < y2):
                        print("A monkey arrived on island S1")
                        monkeys_on_island_S1 += 1
                        island_S1.configure(text="S1\n" +
                                            str(monkeys_on_island_S1))
                        canvas.delete(monkey)
                        break_loop = True
                        break
                if break_loop:
                    break
            canvas.delete(monkey)

        elif random_port == 2:
            monkey = canvas.create_oval(
                self.x+20, self.y-20, self.x+20+10, self.y-20+10, fill="brown")
            # move oval up until it reaches the edge of the canvas
            while canvas.coords(monkey)[1] > 10:
                canvas.move(monkey, 0, -10)
                time.sleep(0.1)
                random_number = random.randint(1, 100)
                if random_number == 1:
                    canvas.delete(monkey)
                    print("A monkey was eaten by a shark")
                    winsound.Beep(100, 100)
                    break
                # check if there is an island at the spot
                overlaps = canvas.find_overlapping(
                    canvas.coords(monkey)[0], canvas.coords(monkey)[1], canvas.coords(monkey)[2], canvas.coords(monkey)[3])
                if len(overlaps) > 1:
                    for island in generated_islands:
                        if abs(island.x - canvas.coords(monkey)[0]) < 50 and abs(island.y - canvas.coords(monkey)[1]) < 50:
                            print("A monkey arrived on island", island.value)
                            island.monkeys += 1
                            island.travel_awareness = 1
                            island.update_island_text()
                            canvas.delete(monkey)
                            break_loop = True
                            break
                if canvas.coords(monkey):
                    monkey_x = canvas.coords(monkey)[0]
                    monkey_y = canvas.coords(monkey)[1]
                    
                    if (monkey_x > x1 and monkey_x < x2 and monkey_y > y1 and monkey_y < y2):
                        print("A monkey arrived on island S1")
                        monkeys_on_island_S1 += 1
                        island_S1.configure(text="S1\n" +
                                            str(monkeys_on_island_S1))
                        canvas.delete(monkey)
                        break_loop = True
                        break
                if break_loop:
                    break
            canvas.delete(monkey)

        elif random_port == 3:
            monkey = canvas.create_oval(
                self.x+20, self.y+60, self.x+20+10, self.y+60+10, fill="brown")
            # move oval down until it reaches the edge of the canvas
            while canvas.coords(monkey)[1] < 590:
                canvas.move(monkey, 0, 10)
                time.sleep(0.1)
                random_number = random.randint(1, 100)
                if random_number == 1:
                    canvas.delete(monkey)
                    print("A monkey was eaten by a shark")
                    winsound.Beep(100, 100)
                    break
                # check if there is an island at the spot
                overlaps = canvas.find_overlapping(
                    canvas.coords(monkey)[0], canvas.coords(monkey)[1], canvas.coords(monkey)[2], canvas.coords(monkey)[3])
                if len(overlaps) > 1:
                    for island in generated_islands:
                        if abs(island.x - canvas.coords(monkey)[0]) < 50 and abs(island.y - canvas.coords(monkey)[1]) < 50:
                            print("A monkey arrived on island", island.value)
                            island.monkeys += 1
                            island.travel_awareness = 1
                            island.update_island_text()
                            canvas.delete(monkey)
                            break_loop = True
                            break
                if canvas.coords(monkey):
                    monkey_x = canvas.coords(monkey)[0]
                    monkey_y = canvas.coords(monkey)[1]
                    
                    if (monkey_x > x1 and monkey_x < x2 and monkey_y > y1 and monkey_y < y2):
                        print("A monkey arrived on island S1")
                        monkeys_on_island_S1 += 1
                        island_S1.configure(text="S1\n" +
                                            str(monkeys_on_island_S1))
                        canvas.delete(monkey)
                        break_loop = True
                        break
                if break_loop:
                    break
            canvas.delete(monkey)

    def start_send_monkey_to_swim(self):
        if not self.thread_send_monkey_to_swim:
            self._stop_thread_send_monkey_to_swim = False  # Reset the flag
            self.thread_send_monkey_to_swim = threading.Thread(
                target=self.send_monkey_to_swim)
            self.thread_send_monkey_to_swim.daemon = True
            self.thread_send_monkey_to_swim.start()

    def stop_send_monkey_to_swim(self):
        self._stop_thread_send_monkey_to_swim = True
        if self.thread_send_monkey_to_swim and self.thread_send_monkey_to_swim.is_alive():
            self.thread_send_monkey_to_swim.join()
        self.thread_send_monkey_to_swim = None

    def update_island_text(self):
        self.button.configure(text=str(self.value) + "\n" + str(self.monkeys))
        if self.travel_awareness == 1:
            self.button.configure(bg="green")

    def monkeys_make_noise(self):
        sound_value = self.value[1:]
        hertz_multiplier = int(sound_value)
        while not self._stop_thread:
            for i in range(self.monkeys):
                if self._stop_thread:
                    return
                if random.random() <= 0.01:
                    print("A monkey died from laughter on island", self.value)
                    winsound.Beep(1000, 100)
                    self.monkeys -= 1
                else:
                    winsound.Beep(200 + hertz_multiplier * 8, 100)
                self.update_island_text()
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
            island = Island(canvas, x, y, button_text, 10, 0)
            generated_islands.append(island)


def delete_all_islands():
    # Stop and join all the island threads
    global generated_islands
    for island in generated_islands:
        island.stop_monkeys_make_noise()
        island.stop_send_monkey_to_swim()
        island.delete_ports()

    # Delete all island objects
    for island in generated_islands:
        island.delete()
        island.delete_ports()
    generated_islands = []
    print(generated_islands)


def delete_all_islands_thread():
    thread = threading.Thread(target=delete_all_islands)
    thread.start()


def show_info_of_every_island():
    for island in generated_islands:
        island.show_info()


def show_info_of_every_island_thread():
    thread = threading.Thread(target=show_info_of_every_island)
    thread.start()


ikkuna = tk.Tk()
ikkuna.geometry("700x700")
canvas = tk.Canvas(ikkuna, width=600, height=600, bg='blue')
canvas.place(x=50, y=50)

generated_islands = []


island_S1 = tk.Button(canvas, text="S1\n" +
                      str(monkeys_on_island_S1), width=7, height=4)
island_S1.place(x=200, y=200)

s1_overlaps = canvas.find_overlapping(
    200, 200, 200+50, 200+50)

port_e = tk.Button(canvas, text="===")
port_e.place(x=200+50, y=200+20)

port_w = tk.Button(canvas, text="===")
port_w.place(x=200-20, y=200+20)

port_n = tk.Button(canvas, text="||")
port_n.place(x=200+20, y=200-20)

port_s = tk.Button(canvas, text="||")
port_s.place(x=200+20, y=200+60)


if travel_awareness_S1 == 1:
    island_S1.configure(bg="green")
else:
    island_S1.configure(bg="yellow")


def send_monkey_from_S1():
    global monkeys_on_island_S1, travel_awareness_S1
    while 1:
        time.sleep(10)
        if travel_awareness_S1 == 1 and monkeys_on_island_S1 > 0:
            if random.random() <= 0.01:
                print("A monkey died from laughter on island S1")
                winsound.Beep(1000, 100)
                monkeys_on_island_S1 -= 1
                island_S1.configure(text="S1\n" + str(monkeys_on_island_S1))

            winsound.Beep(1200, 100)
            print("A monkey has been sent from S1...")
            monkeys_on_island_S1 -= 1
            island_S1.configure(text="S1\n" + str(monkeys_on_island_S1))
            print("...Now there are", monkeys_on_island_S1, "monkeys on S1")
            choose_random_port_S1()


def choose_random_port_S1():
    random_port = random.randint(0, 3)
    break_loop = False

    if random_port == 0:
        monkey = canvas.create_oval(
            200+50, 200+20, 200+50+10, 200+20+10, fill="brown")
        # move oval to the right until it reaches the edge of the canvas
        while canvas.coords(monkey)[0] < 590:
            canvas.move(monkey, 10, 0)
            time.sleep(0.1)
            random_number = random.randint(1, 100)
            if random_number == 1:
                canvas.delete(monkey)
                print("A monkey was eaten by a shark")
                winsound.Beep(100, 100)
                break
            # check if there is an island at the spot
            overlaps = canvas.find_overlapping(
                canvas.coords(monkey)[0], canvas.coords(monkey)[1], canvas.coords(monkey)[2], canvas.coords(monkey)[3])
            if len(overlaps) > 1:
                for island in generated_islands:
                    if abs(island.x - canvas.coords(monkey)[0]) < 50 and abs(island.y - canvas.coords(monkey)[1]) < 50:
                        print("A monkey arrived on island", island.value)
                        island.monkeys += 1
                        island.update_island_text()
                        island.travel_awareness = 1
                        canvas.delete(monkey)
                        break_loop = True
                        break
            if break_loop:
                break
        canvas.delete(monkey)

    elif random_port == 1:

        monkey = canvas.create_oval(
            200-20, 200+20, 200-20+10, 200+20+10, fill="brown")
        # move oval to the left until it reaches the edge of the canvas
        while canvas.coords(monkey)[0] > 10:
            canvas.move(monkey, -10, 0)
            time.sleep(0.1)
            random_number = random.randint(1, 100)
            if random_number == 1:
                canvas.delete(monkey)
                print("A monkey was eaten by a shark")
                winsound.Beep(100, 100)
                break
            # check if there is an island at the spot
            overlaps = canvas.find_overlapping(
                canvas.coords(monkey)[0], canvas.coords(monkey)[1], canvas.coords(monkey)[2], canvas.coords(monkey)[3])
            if len(overlaps) > 1:
                for island in generated_islands:
                    if abs(island.x - canvas.coords(monkey)[0]) < 50 and abs(island.y - canvas.coords(monkey)[1]) < 50:
                        print("A monkey arrived on island", island.value)
                        island.monkeys += 1
                        island.update_island_text()
                        island.travel_awareness = 1
                        canvas.delete(monkey)
                        break_loop = True
                        break
            if break_loop:
                break
        canvas.delete(monkey)

    elif random_port == 2:

        monkey = canvas.create_oval(
            200+20, 200-20, 200+20+10, 200-20+10, fill="brown")
        # move oval up until it reaches the edge of the canvas
        while canvas.coords(monkey)[1] > 10:
            canvas.move(monkey, 0, -10)
            time.sleep(0.1)
            random_number = random.randint(1, 100)
            if random_number == 1:
                canvas.delete(monkey)
                print("A monkey was eaten by a shark")
                winsound.Beep(100, 100)
                break
            # check if there is an island at the spot
            overlaps = canvas.find_overlapping(
                canvas.coords(monkey)[0], canvas.coords(monkey)[1], canvas.coords(monkey)[2], canvas.coords(monkey)[3])
            if len(overlaps) > 1:
                for island in generated_islands:
                    if abs(island.x - canvas.coords(monkey)[0]) < 50 and abs(island.y - canvas.coords(monkey)[1]) < 50:
                        print("A monkey arrived on island", island.value)
                        island.monkeys += 1
                        island.update_island_text()
                        island.travel_awareness = 1
                        canvas.delete(monkey)
                        break_loop = True
                        break
            if break_loop:
                break
        canvas.delete(monkey)

    elif random_port == 3:

        monkey = canvas.create_oval(
            200+20, 200+60, 200+20+10, 200+60+10, fill="brown")
        # move oval down until it reaches the edge of the canvas
        while canvas.coords(monkey)[1] < 590:
            canvas.move(monkey, 0, 10)
            time.sleep(0.1)
            random_number = random.randint(1, 100)
            if random_number == 1:
                canvas.delete(monkey)
                print("A monkey was eaten by a shark")
                winsound.Beep(100, 100)
                break
            # check if there is an island at the spot
            overlaps = canvas.find_overlapping(
                canvas.coords(monkey)[0], canvas.coords(monkey)[1], canvas.coords(monkey)[2], canvas.coords(monkey)[3])
            if len(overlaps) > 1:
                for island in generated_islands:
                    if abs(island.x - canvas.coords(monkey)[0]) < 50 and abs(island.y - canvas.coords(monkey)[1]) < 50:
                        print("A monkey arrived on island", island.value)
                        island.monkeys += 1
                        island.update_island_text()
                        island.travel_awareness = 1
                        canvas.delete(monkey)
                        break_loop = True
                        break
            if break_loop:
                break
        canvas.delete(monkey)


def check_if_new_monkeys_on_S1():
    global monkeys_on_island_S1
    global s1_overlaps
    while 1:

        time.sleep(1)
        island_S1.configure(text="S1\n" + str(monkeys_on_island_S1))
        print("Amount of monkeys on S1 after checking:", monkeys_on_island_S1)


island_S1_thread = threading.Thread(target=send_monkey_from_S1)
island_S1_thread.start()

monkeys_arriving_on_island_S1 = threading.Thread(
    target=check_if_new_monkeys_on_S1)
monkeys_arriving_on_island_S1.start()

generate_button_button = tk.Button(
    ikkuna, text="NEW ISLAND", command=generate_island)
generate_button_button.place(x=50, y=660)

delete_all_islands_button = tk.Button(
    ikkuna, text="DELETE ALL ISLANDS", command=delete_all_islands_thread)
delete_all_islands_button.place(x=150, y=660)

show_info_of_every_island_button = tk.Button(
    ikkuna, text="SHOW INFO OF EVERY ISLAND", command=show_info_of_every_island_thread)
show_info_of_every_island_button.place(x=290, y=660)

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
    # time.sleep(1)
    point_button[0].configure(bg='green')
    for i in range(points_mod):
        point_button[i+1].configure(bg='green')
        winsound.Beep(440+i*100, 500)
# example ...


i_suppose_i_have_earned_so_much_points(20)

ikkuna.mainloop()
