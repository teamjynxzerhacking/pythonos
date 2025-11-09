import tkinter as tk
import random
import os
import platform
import time
import webbrowser
import pathlib
import pygame  # 🔊 nově používáme pygame pro zvuky

# -------------------- Inicializace --------------------
username = os.getlogin()
base_path = pathlib.Path(__file__).parent

pygame.mixer.init()  # inicializace zvukového systému

root = tk.Tk()
root.title("Cool Fullscreen App")
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.config(cursor="arrow")

# -------------------- Zvuková funkce --------------------
def play_sound(name):
    """Najde a přehraje click.mp3 / close.mp3 apod."""
    sound_path = base_path / name
    if sound_path.exists():
        try:
            pygame.mixer.Sound(str(sound_path)).play()
        except Exception as e:
            print(f"Chyba přehrávání {name}: {e}")
    else:
        print(f"Soubor {name} nebyl nalezen v {sound_path.parent}")

# -------------------- Open Website --------------------
def open_website():
    play_sound("click.mp3")
    path = base_path / "main.html"
    if path.exists():
        webbrowser.open(path.resolve().as_uri())
    else:
        print("Soubor main.html nebyl nalezen!")

# -------------------- Settings --------------------
def settings():
    play_sound("click.mp3")
    settings_win = tk.Toplevel(root)
    settings_win.geometry("400x300")
    settings_win.title("Settings")

    def change_bg():
        play_sound("click.mp3")
        colors = ["black", "darkblue", "darkgreen", "purple", "gray"]
        root.configure(bg=random.choice(colors))

    def close_settings():
        play_sound("close.mp3")
        settings_win.destroy()

    tk.Button(settings_win, text="Change Background Color", command=change_bg, width=30).pack(pady=10)
    tk.Button(settings_win, text="Close", command=close_settings, width=30).pack(pady=10)

# -------------------- Welcome Text --------------------
cool_text = tk.Label(root, text=f"WELCOME {username}!", font=("Comic Sans MS", 10, "bold"), fg="cyan", bg="black")
cool_text.place(relx=0.5, rely=0.5, anchor="center")

def animate_welcome(size=10):
    if size <= 80:
        colors = ["cyan", "magenta", "yellow", "lime", "orange", "red", "blue", "white"]
        cool_text.config(fg=random.choice(colors), font=("Comic Sans MS", size, "bold"))
        root.after(100, lambda: animate_welcome(size + 2))
    else:
        root.after(3000, lambda: cool_text.place_forget())

def show_welcome():
    animate_welcome()

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

# -------------------- Start Menu --------------------
menu_frame = tk.Frame(root, bg="gray20", bd=2, relief="raised")
menu_frame.place(x=-250, y=50, width=200, height=350)

menu_label = tk.Label(menu_frame, text="START MENU", font=("Arial", 16, "bold"), fg="white", bg="gray20")
menu_label.pack(pady=10)

# --- System Info ---
def show_system_info():
    play_sound("click.mp3")
    info = f"OS: {platform.system()} {platform.release()}\nUser: {username}"
    info_win = tk.Toplevel(root)
    info_win.geometry("300x150")
    info_win.title("System Info")
    tk.Label(info_win, text=info, font=("Arial", 12)).pack(pady=20)
    tk.Button(info_win, text="Close", command=lambda: [play_sound("close.mp3"), info_win.destroy()]).pack()

# --- Calculator ---
def open_calculator():
    play_sound("click.mp3")
    if hasattr(open_calculator, 'win') and open_calculator.win.winfo_exists():
        open_calculator.win.lift()
        return
    open_calculator.win = tk.Toplevel(root)
    calc_win = open_calculator.win
    calc_win.title("Calculator")
    calc_win.geometry("250x350")

    entry = tk.Entry(calc_win, width=16, font=("Arial", 24), borderwidth=2, relief="ridge")
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    def press(num):
        play_sound("click.mp3")
        entry.insert(tk.END, num)

    def clear():
        play_sound("click.mp3")
        entry.delete(0, tk.END)

    def equal():
        play_sound("click.mp3")
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
        cmd = equal if text == "=" else clear if text == "C" else lambda t=text: press(t)
        tk.Button(calc_win, text=text, width=5, height=2, command=cmd).grid(row=row, column=col)

    calc_win.protocol("WM_DELETE_WINDOW", lambda: [play_sound("close.mp3"), calc_win.destroy()])

# --- Clock ---
def show_time():
    play_sound("click.mp3")
    if hasattr(show_time, 'win') and show_time.win.winfo_exists():
        show_time.win.lift()
        return
    show_time.win = tk.Toplevel(root)
    time_win = show_time.win
    time_win.title("Clock")
    time_win.geometry("200x100")

    clock_label = tk.Label(time_win, font=("Arial", 24))
    clock_label.pack(pady=20)

    def update_clock():
        clock_label.config(text=time.strftime("%H:%M:%S"))
        clock_label.after(1000, update_clock)

    update_clock()
    time_win.protocol("WM_DELETE_WINDOW", lambda: [play_sound("close.mp3"), time_win.destroy()])

# --- Menu Buttons ---
tk.Button(menu_frame, text="Shutdown", command=lambda: [play_sound("close.mp3"), root.destroy()], width=20).pack(pady=5)
tk.Button(menu_frame, text="Restart", command=lambda: play_sound("click.mp3"), width=20).pack(pady=5)
tk.Button(menu_frame, text="Settings", command=settings, width=20).pack(pady=5)
tk.Button(menu_frame, text="System Info", command=show_system_info, width=20).pack(pady=5)
tk.Button(menu_frame, text="Calculator", command=open_calculator, width=20).pack(pady=5)
tk.Button(menu_frame, text="Clock", command=show_time, width=20).pack(pady=5)
tk.Button(menu_frame, text="Website", command=open_website, width=20).pack(pady=5)

# -------------------- Start Button --------------------
start_btn = tk.Button(root, text="☰", font=("Arial", 25), bg="black", fg="white", bd=0)
start_btn.place(relx=0, rely=0, anchor="nw")

menu_open = False
def toggle_menu():
    global menu_open
    play_sound("click.mp3")
    if menu_open:
        def slide_out(x=0):
            if x > -250:
                x -= 20
                menu_frame.place(x=x, y=50)
                root.after(10, lambda: slide_out(x))
            else:
                menu_frame.place(x=-250, y=50)
        slide_out()
        menu_open = False
    else:
        def slide_in(x=-250):
            if x < 0:
                x += 20
                menu_frame.place(x=x, y=50)
                root.after(10, lambda: slide_in(x))
            else:
                menu_frame.place(x=0, y=50)
        slide_in()
        menu_open = True

start_btn.config(command=toggle_menu)

root.mainloop()
