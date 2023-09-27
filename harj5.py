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

ernesti_monkey = canvas.create_oval(20, 20, 80, 80, fill="yellow")
kernesti_monkey = canvas.create_oval(20, 120, 80, 180, fill="orange")


def move_ernesti_monkey():

    current_position = canvas.coords(ernesti_monkey)
    continent_coords = canvas.winfo_width()

    if current_position[2] >= continent_coords:
        print("Ernesti monkey has reached the continent. \n Apina sanoo: tarvitaan! \n")
        winsound.Beep(800, 100)
    else:
        for i in range(12):
            canvas.move(ernesti_monkey, 10, 0)
            time.sleep(0.1)
            winsound.Beep(500, 100)
            result = random.randint(0, 100)
            if result == 100:
                winsound.Beep(300, 100)
                time.sleep(0.1)
                canvas.coords(ernesti_monkey, 20, 20, 80, 80)
                print("Shark has eaten the monkey")
                break
                
            print("Ernesti monkey has not reached the continent.")


def ernesti_monkey_thread():
    t = threading.Thread(target=move_ernesti_monkey)
    t.start()


def move_kernesti_monkey():
    current_position = canvas.coords(kernesti_monkey)
    continent_coords = canvas.winfo_width()

    if current_position[2] >= continent_coords:
        print("Kernesti monkey has reached the continent. \n Apina sanoo: apua! \n")
        winsound.Beep(1000, 100)
    else:
        for i in range(12):
            canvas.move(kernesti_monkey, 10, 0)
            time.sleep(0.1)
            winsound.Beep(700, 100)
            result = random.randint(0, 100)
            if result == 100:
                winsound.Beep(300, 100)
                time.sleep(0.1)
                canvas.coords(kernesti_monkey, 20, 120, 80, 180)
                print("Shark has eaten the monkey")
                break
                
            print("Kernesti monkey has not reached the continent.")
            
            
def kernesti_monkey_thread():
    t = threading.Thread(target=move_kernesti_monkey)
    t.start()


ernesti_move_button = tk.Button(window, text="Move ernesti monkey to Continent",
                                command=ernesti_monkey_thread)
ernesti_move_button.grid(row=3, column=1, columnspan=3)

kernesti_move_button = tk.Button(window, text="Move kernesti monkey to Continent",
                                 command=kernesti_monkey_thread)
kernesti_move_button.grid(row=3, column=3, columnspan=3)

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


i_suppose_i_have_earned_so_much_points(2)


window.mainloop()
