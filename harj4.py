print("...")

import tkinter as tk
import time
import winsound
import threading
import numpy as np
import psutil as psutil

ikkuna=tk.Tk()
ikkuna.title("Käyttöliittymä, jossa on säikeystoiminnallisuutta")
ikkuna.geometry("650x300")


koriste={}
for i in range(10):
    koriste[i] = tk.Label(ikkuna,text="")
    koriste[i].grid(row=i, column=i)
    
ernestin_muuttuja_naytolla=tk.StringVar()
ernestin_muuttuja_naytolla.set("-------")

kernestin_muuttuja_naytolla=tk.StringVar()
kernestin_muuttuja_naytolla.set("-------")



cpu_muuttuja=tk.StringVar()
cpu_muuttuja.set("---------")

thread_muuttuja=tk.StringVar()
thread_muuttuja.set("---------")

def use_only_certain_amount_of_CPU():
    print("...")
    if slider.get() == 0:
        psutil.IDLE_PRIORITY_CLASS



def nayta_cpu():
    cpu_muuttuja.set(f"CPU: {psutil.cpu_percent()}%")
    
    ikkuna.after(1000, nayta_cpu)

def aja_cpu_thread():
    t=threading.Thread(target=nayta_cpu)
    t.start()
    
def nayta_thread():
    pid = psutil.Process().pid
    thread_muuttuja.set(f"Threads: {psutil.Process(pid).num_threads()}")
    ikkuna.after(1000, nayta_thread)

def aja_thread_thread():
    t=threading.Thread(target=nayta_thread)
    t.start()

def ernesti_heita_tomaatti():
    for i in range(10):
        print("o-", i)
        temp=np.random.randint(0, 100)
        ernestin_muuttuja_naytolla.set(f"{temp}+{temp*'-'}->")
        A=np.ones((1000,1000))
        B=np.matmul(A,A)
        time.sleep(0.1)
        winsound.Beep(500,100)
    print("heitto")
    winsound.Beep(300,500)

def luo_ja_aja_thread_tomaatinheittoa_varten_ernestille():
    t=threading.Thread(target=ernesti_heita_tomaatti)
    t.start()
    
cpu_teksti = tk.Label(ikkuna, textvariable=cpu_muuttuja,bg='green', width=40,anchor='w')
cpu_teksti.grid(row=5, column=2)

thread_teksti = tk.Label(ikkuna, textvariable=thread_muuttuja,bg='yellow', width=40,anchor='w')
thread_teksti.grid(row=6, column=2)
  
ernesti_painike=tk.Button(ikkuna,text="Ernesti", command=luo_ja_aja_thread_tomaatinheittoa_varten_ernestille)
ernesti_painike.grid(row=1,column=1)

ernesti_teksti=tk.Label(ikkuna, textvariable=ernestin_muuttuja_naytolla,bg='purple', width=80,anchor='w')
ernesti_teksti.grid(row=1, column=2)



def kernesti_heita_tomaatti():
    for i in range(10):
        print("o-", i)
        temp=np.random.randint(0, 100)
        kernestin_muuttuja_naytolla.set(f"{temp}+{temp*'-'}->")
        time.sleep(0.1)
        winsound.Beep(700,100)
    print("heitto")
    winsound.Beep(500,500)
    
def luo_ja_aja_thread_tomaatinheittoa_varten_kernestille():
    t=threading.Thread(target=kernesti_heita_tomaatti)
    t.start()
  
  
kernesti_painike=tk.Button(ikkuna,text="Kernesti", command=luo_ja_aja_thread_tomaatinheittoa_varten_kernestille)
kernesti_painike.grid(row=3,column=1)

kernesti_teksti=tk.Label(ikkuna, textvariable=kernestin_muuttuja_naytolla,bg='blue', width=80,anchor='w')
kernesti_teksti.grid(row=3, column=2)


aja_cpu_thread()
aja_thread_thread()

slider = tk.Scale(ikkuna, from_= 0, to = 100, orient=tk.HORIZONTAL, length=400, )
slider.grid(row=11, column=2)

def ohjauskeskus():
    print("ohjaus")
    tavoite_maara=slider.get()
    print("tavoite: ", tavoite_maara)
    cpu = psutil.cpu_percent()
    print("CPU: ", cpu)
    if tavoite_maara < cpu:
        print("limittiä")

ohjaus=tk.Button(ikkuna,text="Ohjaa", command=ohjauskeskus)
ohjaus.grid(row=9,column=1)

ikkuna.mainloop()
