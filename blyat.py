import tkinter as tk
import random

app = tk.Tk()
app.title("Island Generator")
app.geometry("600x600")

canvas = tk.Canvas(app, width=500, height=500, bg='blue')
canvas.place(x=50, y=50)

islands = []

def create_new_island():
    island_radius = 20
    overlap_threshold = 2 * island_radius
    new_island = None

    while new_island is None:
        x = random.randint(island_radius, 500 - island_radius)
        y = random.randint(island_radius, 500 - island_radius)
        is_overlapping = False

        for island in islands:
            x0, y0, x1, y1 = canvas.coords(island)
            distance = ((x - (x0 + x1) / 2)**2 + (y - (y0 + y1) / 2)**2)**0.5
            if distance < overlap_threshold:
                is_overlapping = True
                break

        if not is_overlapping:
            new_island = canvas.create_oval(x - island_radius, y - island_radius, x + island_radius, y + island_radius, fill='green')
            islands.append(new_island)

def create_new_island_button():
    button = tk.Button(app, text="Island", command=create_new_island)
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    button.place(x=x, y=y)
    islands.append(button)

new_island_button = tk.Button(app, text="NEW ISLAND", command=create_new_island_button)
new_island_button.place(x=10, y=10)

app.mainloop()
