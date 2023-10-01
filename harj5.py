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

pohteri = tk.Label(window, text="Pohteri", pady=8,
                   bg="white", font=("Arial", 10))
pohteri.place(x=550, y=230)
pohteri_message = []
seen_pohteri_messages = set()
pohteri_laiva_arrived = False
ernesti_monkey_survived = 0


def add_unique_message_to_pohteri(message):
    global ernesti_monkey_survived
    ernesti_monkey_survived += 1
    if message not in seen_pohteri_messages:
        pohteri_message.append(message)
        seen_pohteri_messages.add(message)


eteteri = tk.Label(window, text="Eteteri", pady=8,
                   bg="white", font=("Arial", 10))
eteteri.place(x=550, y=380)
eteteri_message = []
seen_eteteri_messages = set()
eteteri_laiva_arrived = False
kernesti_monkey_survived = 0


def add_unique_message_to_eteteri(message):
    global kernesti_monkey_survived
    kernesti_monkey_survived += 1
    if message not in seen_eteteri_messages:
        eteteri_message.append(message)
        seen_eteteri_messages.add(message)


def move_ernesti_monkey():
    random_word = random.choice(viesti)
    ernesti_monkey = canvas.create_oval(
        30, 30, 80, 80, fill="yellow")

    current_position = canvas.coords(ernesti_monkey)
    continent_coords = canvas.winfo_width()

    for i in range(100):

        current_position = canvas.coords(ernesti_monkey)
        canvas.move(ernesti_monkey, 3.5, 0)
        time.sleep(0.1)
        winsound.Beep(500, 100)
        result = random.randint(0, 150)

        if result == 150:

            winsound.Beep(300, 100)
            time.sleep(0.1)
            canvas.delete(ernesti_monkey)
            print("Shark has eaten one of Ernesti's monkeys")
            break

    if current_position[2] >= continent_coords:

        print("Ernesti monkey says:", random_word)
        add_unique_message_to_pohteri(random_word)
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
    random_word = random.choice(viesti)
    kernesti_monkey = canvas.create_oval(
        30, 130, 80, 180, fill="orange")

    current_position = canvas.coords(kernesti_monkey)
    continent_coords = canvas.winfo_width()

    for i in range(100):

        current_position = canvas.coords(kernesti_monkey)
        canvas.move(kernesti_monkey, 3.5, 0)
        time.sleep(0.1)
        winsound.Beep(700, 100)
        result = random.randint(0, 150)

        if result == 150:

            winsound.Beep(400, 100)
            time.sleep(0.1)
            canvas.delete(kernesti_monkey)
            print("Shark has eaten one of Kernesti's monkeys")
            break

    if current_position[2] >= continent_coords:

        print("Kernesti monkey says:", random_word)
        add_unique_message_to_eteteri(random_word)
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

pohteri_laiva = tk.Label(window, text="Pohteri laiva",
                         pady=8, bg="white", font=("Arial", 10))
pohteri_laiva.place(x=500, y=200)

eteteri_laiva = tk.Label(window, text="Eteteri laiva",
                         pady=8, bg="white", font=("Arial", 10))
eteteri_laiva.place(x=500, y=410)


def pohteri_watch():
    global pohteri_laiva_arrived
    global eteteri_laiva_arrived
    while True:
        pohteri_message_length = len(pohteri_message)

        if pohteri_message_length > 10:
            print("Pohteri understood the message")

            for i in range(0, 20):
                pohteri_laiva.place(
                    x=pohteri_laiva.winfo_x()-22, y=pohteri_laiva.winfo_y())
                time.sleep(1)

            pohteri_laiva_arrived = True

            if pohteri_laiva_arrived and eteteri_laiva_arrived == False:
                print("Ernesti won!")
                for i in range(0, 20):
                    pohteri_laiva.place(
                        x=pohteri_laiva.winfo_x()+22, y=pohteri_laiva.winfo_y())
                    time.sleep(1)

                break

            elif pohteri_laiva_arrived and eteteri_laiva_arrived:
                print("")
                for i in range(0, 20):
                    pohteri_laiva.place(
                        x=pohteri_laiva.winfo_x()+22, y=pohteri_laiva.winfo_y())
                    time.sleep(1)

                break

            elif pohteri_laiva_arrived == False and eteteri_laiva_arrived:
                print("")
                for i in range(0, 20):
                    pohteri_laiva.place(
                        x=pohteri_laiva.winfo_x()+22, y=pohteri_laiva.winfo_y())
                    time.sleep(1)

                break
        else:
            time.sleep(3)


def eteteri_watch():
    global pohteri_laiva_arrived
    global eteteri_laiva_arrived
    while True:
        eteteri_message_length = len(eteteri_message)

        if eteteri_message_length > 10:
            print("Eteteri understood the message")

            for i in range(0, 20):
                eteteri_laiva.place(
                    x=eteteri_laiva.winfo_x()-22, y=eteteri_laiva.winfo_y())
                time.sleep(1)

            eteteri_laiva_arrived = True

            if eteteri_laiva_arrived and pohteri_laiva_arrived == False:
                print("Kernesti won!")
                for i in range(0, 20):
                    eteteri_laiva.place(
                        x=eteteri_laiva.winfo_x()+22, y=eteteri_laiva.winfo_y())
                    time.sleep(1)

                break

            elif eteteri_laiva_arrived and pohteri_laiva_arrived:
                print("")
                for i in range(0, 20):
                    eteteri_laiva.place(
                        x=eteteri_laiva.winfo_x()+22, y=eteteri_laiva.winfo_y())
                    time.sleep(1)

                break

            elif eteteri_laiva_arrived == False and pohteri_laiva_arrived:
                print("")
                for i in range(0, 20):
                    eteteri_laiva.place(
                        x=eteteri_laiva.winfo_x()+22, y=eteteri_laiva.winfo_y())
                    time.sleep(1)

                break
        else:
            time.sleep(3)


def amount_of_food():
    global ernesti_monkey_survived
    global kernesti_monkey_survived

    north_food = ernesti_monkey_survived * 4
    south_food = kernesti_monkey_survived * 4

    if north_food > south_food:
        print(ernesti_monkey_survived,
              "of Ernesti's monkeys survived, they were enough to feed", north_food, "people")
        print(kernesti_monkey_survived,
              "of Kernesti's monkeys survived, they were enough to feed", south_food, "people")
        print("North had a bigger party!")

    elif north_food < south_food:
        print(ernesti_monkey_survived,
              "of Ernesti's monkeys survived, they were enough to feed", north_food, "people")
        print(kernesti_monkey_survived,
              "of Kernesti's monkeys survived, they were enough to feed", south_food, "people")
        print("South had a bigger party!")

    elif north_food == 0 and south_food == 0:
        print("No monkeys have survived/arrived yet!")

    else:
        print(ernesti_monkey_survived,
              "of Ernesti's monkeys survived, they were enough to feed", north_food, "people")
        print(kernesti_monkey_survived,
              "of Kernesti's monkeys survived, they were enough to feed", south_food, "people")
        print("Parties were equally big!")


amount_of_food_button = tk.Button(
    window, text="Check amount of food", command=amount_of_food)
amount_of_food_button.grid(row=5, column=2, columnspan=3)


pohteri_thread = threading.Thread(target=pohteri_watch)
pohteri_thread.start()

eteteri_thread = threading.Thread(target=eteteri_watch)
eteteri_thread.start()


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


i_suppose_i_have_earned_so_much_points(5)

window.mainloop()
