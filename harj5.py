import tkinter as tk
import threading
import winsound
import time
import random

window = tk.Tk()
window.title("Harjoitus 5")
window.geometry("700x700")

island_label = tk.Label(window, text="Island",
                        pady=80, bg="red", font=("Arial", 20))
island_label.grid(row=2, column=0, columnspan=3, sticky="w")

continent_label = tk.Label(window, text="Continent",
                           pady=80, bg="green", font=("Arial", 20))
continent_label.grid(row=2, column=3, columnspan=3, sticky="e")

window.grid_rowconfigure(2, weight=1)

canvas = tk.Canvas(window, width=400, height=200, bg="blue")
canvas.grid(row=2, column=2, columnspan=3)

viesti = ["Ernesti", "ja", "Kernesti", "tässä", "terve!", "Olemme", "autiolla", "saarella,", "ja",
          "voisitteko", "tulla", "sieltä", "sivistyksestä", "joku", "hakemaan", "meidät", "pois!", "Kiitos!"]


def move_ernesti_monkey():
    ernesti_monkey = canvas.create_oval(30, 30, 80, 80, fill="yellow")
    random_word = random.choice(viesti)
    current_position = canvas.coords(ernesti_monkey)
    continent_coords = canvas.winfo_width()

    for i in range(100):

        current_position = canvas.coords(ernesti_monkey)
        canvas.move(ernesti_monkey, 3.5, 0)
        time.sleep(0.1)
        winsound.Beep(500, 100)
        result = random.randint(0, 100)

        if result == 100:

            winsound.Beep(300, 100)
            time.sleep(0.1)
            canvas.delete(ernesti_monkey)
            print("Shark has eaten one of Ernesti's monkeys")
            break

    if current_position[2] >= continent_coords:
        print("Ernesti apina sanoo: ", random_word)
        winsound.Beep(800, 100)
        canvas.delete(ernesti_monkey)


def ernesti_monkey_thread():
    t = threading.Thread(target=move_ernesti_monkey)
    t.start()


def ten_ernesti_monkeys():
    for i in range(10):
        ernesti_monkey_thread()
        time.sleep(1)


def ten_ernesti_monkeys_thread():
    t = threading.Thread(target=ten_ernesti_monkeys)
    t.start()


def move_kernesti_monkey():
    kernesti_monkey = canvas.create_oval(30, 130, 80, 180, fill="orange")
    random_word = random.choice(viesti)

    current_position = canvas.coords(kernesti_monkey)
    continent_coords = canvas.winfo_width()

    for i in range(100):

        current_position = canvas.coords(kernesti_monkey)
        canvas.move(kernesti_monkey, 3.5, 0)
        time.sleep(0.1)
        winsound.Beep(700, 100)
        result = random.randint(0, 100)

        if result == 100:

            winsound.Beep(400, 100)
            time.sleep(0.1)
            canvas.delete(kernesti_monkey)
            print("Shark has eaten one of Kernesti's monkeys")
            break

    if current_position[2] >= continent_coords:
        print("Kernesti apina sanoo: ", random_word)
        winsound.Beep(1000, 100)
        canvas.delete(kernesti_monkey)


def kernesti_monkey_thread():
    t = threading.Thread(target=move_kernesti_monkey)
    t.start()


def ten_kernesti_monkeys():
    for i in range(10):
        kernesti_monkey_thread()
        time.sleep(1)


def ten_kernesti_monkeys_thread():
    t = threading.Thread(target=ten_kernesti_monkeys)
    t.start()


ernesti_move_button = tk.Button(window, text="Move ernesti monkey to Continent",
                                command=ernesti_monkey_thread)
ernesti_move_button.grid(row=3, column=1, columnspan=3)

ten_ernesti_monkeys_button = tk.Button(window, text="Move ten ernesti monkeys to Continent",
                                       command=ten_ernesti_monkeys_thread)
ten_ernesti_monkeys_button.grid(row=4, column=1, columnspan=3)

kernesti_move_button = tk.Button(window, text="Move kernesti monkey to Continent",
                                 command=kernesti_monkey_thread)
kernesti_move_button.grid(row=3, column=3, columnspan=3)

ten_kernesti_monkeys_button = tk.Button(window, text="Move ten kernesti monkeys to Continent",
                                        command=ten_kernesti_monkeys_thread)
ten_kernesti_monkeys_button.grid(row=4, column=3, columnspan=3)

pohteri = canvas.create_oval(370, 10, 400, 40, fill="white")
pohteri_text = canvas.create_text(385, 25, text="Pohteri", fill="black")

point_button = []

for i in range(5):
    button_temp = tk.Button(window, text="Points: " + str(i+1), padx=40)
    button_temp.grid(row=0, column=i + 1)
    point_button.append(button_temp)


def i_suppose_i_have_earned_so_much_points(amount_of_points):
    for i in range(5):
        point_button[i].configure(bg='gray')
    time.sleep(1)
    for i in range(amount_of_points):
        point_button[i].configure(bg='green')
        winsound.Beep(440+i*100, 500)


i_suppose_i_have_earned_so_much_points(3)

window.mainloop()
