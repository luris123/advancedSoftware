import tkinter as tk
import random

def generate_button():
    # generate random x and y coordinates
    x = random.randint(10, 490)
    y = random.randint(10, 490)
    
    # check if there is already a button at the randomly generated spot
    overlapping = False
    for widget in canvas.winfo_children():
        if abs(widget.winfo_x() - x) < 50 and abs(widget.winfo_y() - y) < 50:
            overlapping = True
            break
    
    # if there is already a button at the spot, generate the button elsewhere
    if overlapping:
        generate_button()
    else:
        # create the button at the randomly generated spot
        button = tk.Button(canvas, text="Random Button")
        canvas.create_window(x, y, window=button)

# create the tkinter window and canvas
root = tk.Tk()
root.geometry("700x700")
canvas = tk.Canvas(root, width=600, height=600, bg='blue')
canvas.place(x=50, y=50)

# create the "Generate Button" button
generate_button_button = tk.Button(root, text="Generate Button", command=generate_button)
generate_button_button.place(x=50, y=10)

root.mainloop()


