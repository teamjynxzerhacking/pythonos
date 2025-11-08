import tkinter as tk
import random
import os
import time

# Získání jména uživatele Windows
username = os.getlogin()

# Tkinter okno fullscreen
root = tk.Tk()
root.title("Cool Fullscreen App")
root.attributes("-fullscreen", True)
root.configure(bg="black")

# ---------- Loading Screen ----------
loading_frame = tk.Frame(root, bg="black")
loading_frame.place(relwidth=1, relheight=1)

loading_label = tk.Label(loading_frame, text="LOADING...", font=("Arial", 40, "bold"), fg="cyan", bg="black")
loading_label.place(relx=0.5, rely=0.5, anchor="center")

def animate_loading(count=0):
    dots = "." * (count % 4)
    loading_label.config(text=f"LOADING{dots}")
    root.update()
    count += 1
    if count < 20:  # cca 3 sekundy animace
        root.after(150, lambda: animate_loading(count))
    else:
        loading_frame.place_forget()
        show_welcome()

animate_loading()

# ---------- Welcome Text ----------
cool_text = tk.Label(root, text=f"WELCOME {username}!", font=("Comic Sans MS", 50, "bold"), fg="cyan", bg="black")

def animate_text():
    colors = ["cyan", "magenta", "yellow", "lime", "orange", "red", "blue", "white"]
    cool_text.config(fg=random.choice(colors))
    root.after(500, animate_text)

def show_welcome():
    cool_text.place(relx=0.5, rely=0.5, anchor="center")
    animate_text()
    root.after(5000, lambda: cool_text.place_forget())  # zmizí po 5 sekundách

# ---------- Start Menu ----------
menu_frame = tk.Frame(root, bg="gray20", bd=2, relief="raised")
tk.Label(menu_frame, text="START MENU", font=("Arial", 16, "bold"), fg="white", bg="gray20").pack(pady=10)
tk.Button(menu_frame, text="Shutdown", command=root.destroy, width=20).pack(pady=5)
tk.Button(menu_frame, text="Restart", command=lambda: print("Restart pressed"), width=20).pack(pady=5)
tk.Button(menu_frame, text="Settings", command=lambda: print("Settings pressed"), width=20).pack(pady=5)

# ---------- Start Button ----------
start_btn = tk.Button(root, text="☰", font=("Arial", 25), bg="black", fg="white", bd=0)
start_btn.place(relx=0, rely=0)

def toggle_menu():
    if menu_frame.winfo_ismapped():
        menu_frame.place_forget()
    else:
        menu_frame.place(x=50, y=50)

start_btn.config(command=toggle_menu)

# ---------- Make Start Menu Draggable ----------
def start_move(event):
    menu_frame.startX = event.x
    menu_frame.startY = event.y

def stop_move(event):
    menu_frame.startX = None
    menu_frame.startY = None

def do_move(event):
    x = menu_frame.winfo_x() - menu_frame.startX + event.x
    y = menu_frame.winfo_y() - menu_frame.startY + event.y
    menu_frame.place(x=x, y=y)

menu_frame.bind("<Button-1>", start_move)
menu_frame.bind("<ButtonRelease-1>", stop_move)
menu_frame.bind("<B1-Motion>", do_move)

# ---------- Hide menu when clicking outside ----------
def click_outside(event):
    if menu_frame.winfo_ismapped() and not menu_frame.winfo_containing(event.x_root, event.y_root):
        menu_frame.place_forget()

root.bind("<Button-1>", click_outside)

root.mainloop()
