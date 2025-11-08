import tkinter as tk
import random
import os
import platform
import time

# -------------------- Config --------------------
username = os.getlogin()
root = tk.Tk()
root.title("Cool Fullscreen App")
root.attributes("-fullscreen", True)
root.configure(bg="black")

# -------------------- Settings --------------------
def settings():
    settings_win = tk.Toplevel(root)
    settings_win.geometry("400x300")
    settings_win.title("Settings")
    
    def change_bg():
        colors = ["black", "darkblue", "darkgreen", "purple", "gray"]
        root.configure(bg=random.choice(colors))
    
    tk.Button(settings_win, text="Change Background Color", command=change_bg, width=30).pack(pady=10)
    tk.Button(settings_win, text="Close", command=settings_win.destroy, width=30).pack(pady=10)

# -------------------- Loading Screen --------------------
loading_frame = tk.Frame(root, bg="black")
loading_frame.place(relwidth=1, relheight=1)
loading_label = tk.Label(loading_frame, text="LOADING...", font=("Arial", 40, "bold"), fg="cyan", bg="black")
loading_label.place(relx=0.5, rely=0.5, anchor="center")

def animate_loading(count=0):
    dots = "." * (count % 4)
    loading_label.config(text=f"LOADING{dots}")
    count += 1
    if count < 20:
        root.after(150, lambda: animate_loading(count))
    else:
        loading_frame.place_forget()
        show_welcome()

animate_loading()

# -------------------- Welcome Text --------------------
cool_text = tk.Label(root, text=f"WELCOME {username}!", font=("Comic Sans MS", 10, "bold"), fg="cyan", bg="black")
cool_text.place(relx=0.5, rely=0.5, anchor="center")

def animate_welcome(size=10):
    colors = ["cyan", "magenta", "yellow", "lime", "orange", "red", "blue", "white"]
    cool_text.config(fg=random.choice(colors), font=("Comic Sans MS", size, "bold"))
    if size < 50:
        root.after(100, lambda: animate_welcome(size + 2))
    else:
        root.after(3000, lambda: cool_text.place_forget())

def show_welcome():
    animate_welcome()

# -------------------- Start Menu --------------------
menu_frame = tk.Frame(root, bg="gray20", bd=2, relief="raised")
menu_frame.place(x=-250, y=50, width=200, height=350)  # start offscreen

menu_label = tk.Label(menu_frame, text="START MENU", font=("Arial", 16, "bold"), fg="white", bg="gray20")
menu_label.pack(pady=10)

# --- Funkce ---
def show_system_info():
    info = f"OS: {platform.system()} {platform.release()}\nUser: {username}"
    info_win = tk.Toplevel(root)
    info_win.geometry("300x150")
    info_win.title("System Info")
    tk.Label(info_win, text=info, font=("Arial", 12)).pack(pady=20)
    tk.Button(info_win, text="Close", command=info_win.destroy).pack()

def open_calculator():
    calc_win = tk.Toplevel(root)
    calc_win.title("Calculator")
    calc_win.geometry("250x350")
    entry = tk.Entry(calc_win, width=16, font=("Arial", 24), borderwidth=2, relief="ridge")
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    def press(num):
        entry.insert(tk.END, num)
    
    def clear():
        entry.delete(0, tk.END)
    
    def equal():
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")

    buttons = [
        ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
        ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
        ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
        ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
        ('C',5,0)
    ]
    for (text,row,col) in buttons:
        if text == "=":
            tk.Button(calc_win, text=text, width=5, height=2, command=equal).grid(row=row, column=col)
        elif text == "C":
            tk.Button(calc_win, text=text, width=5, height=2, command=clear).grid(row=row, column=col)
        else:
            tk.Button(calc_win, text=text, width=5, height=2, command=lambda t=text: press(t)).grid(row=row, column=col)

def show_time():
    time_win = tk.Toplevel(root)
    time_win.title("Clock")
    time_win.geometry("200x100")
    clock_label = tk.Label(time_win, font=("Arial", 24))
    clock_label.pack(pady=20)

    def update_clock():
        clock_label.config(text=time.strftime("%H:%M:%S"))
        clock_label.after(1000, update_clock)
    
    update_clock()

tk.Button(menu_frame, text="Shutdown", command=root.destroy, width=20).pack(pady=5)
tk.Button(menu_frame, text="Restart", command=lambda: print("Restart pressed"), width=20).pack(pady=5)
tk.Button(menu_frame, text="Settings", command=settings, width=20).pack(pady=5)
tk.Button(menu_frame, text="System Info", command=show_system_info, width=20).pack(pady=5)
tk.Button(menu_frame, text="Calculator", command=open_calculator, width=20).pack(pady=5)
tk.Button(menu_frame, text="Clock", command=show_time, width=20).pack(pady=5)

# -------------------- Start Button --------------------
start_btn = tk.Button(root, text="☰", font=("Arial", 25), bg="black", fg="white", bd=0)
start_btn.place(relx=0, rely=0)

menu_open = False
def toggle_menu():
    global menu_open
    if menu_open:
        # Animace zavření (slide out)
        def slide_out(x=-250):
            if x > -250:
                x -= 20
                menu_frame.place(x=x, y=50)
                root.after(10, lambda: slide_out(x))
            else:
                menu_frame.place(x=-250, y=50)
        slide_out()
        menu_open = False
    else:
        # Animace otevření (slide in)
        def slide_in(x=-250):
            if x < 50:
                x += 20
                menu_frame.place(x=x, y=50)
                root.after(10, lambda: slide_in(x))
            else:
                menu_frame.place(x=50, y=50)
        slide_in()
        menu_open = True

start_btn.config(command=toggle_menu)

root.mainloop()
