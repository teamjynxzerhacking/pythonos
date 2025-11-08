import tkinter as tk
import random
import os

# -------------------- Config --------------------
username = os.getlogin()
root = tk.Tk()
root.title("Cool Fullscreen App")
root.attributes("-fullscreen", True)
root.configure(bg="black")

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
menu_frame.place(x=-250, y=50, width=200, height=250)  # start offscreen

menu_label = tk.Label(menu_frame, text="START MENU", font=("Arial", 16, "bold"), fg="white", bg="gray20")
menu_label.pack(pady=10)

tk.Button(menu_frame, text="Shutdown", command=root.destroy, width=20).pack(pady=5)
tk.Button(menu_frame, text="Restart", command=lambda: print("Restart pressed"), width=20).pack(pady=5)
tk.Button(menu_frame, text="Settings", command=lambda: print("Settings pressed"), width=20).pack(pady=5)

# -------------------- Console --------------------
console_win = None

def open_console():
    global console_win
    if console_win and console_win.winfo_exists():
        close_console()
        return

    console_win = tk.Toplevel(root)
    console_win.title("PythonOS Console")
    console_win.geometry("0x0+200+150")
    console_win.configure(bg="black")

    # Output text
    output = tk.Text(console_win, bg="black", fg="lime", insertbackground="lime", font=("Consolas", 12))
    output.pack(side="top", fill="both", expand=True)

    # Entry + Run button frame
    bottom_frame = tk.Frame(console_win, bg="black", height=40)
    bottom_frame.pack(side="bottom", fill="x")
    bottom_frame.pack_propagate(0)  # fix height

    entry = tk.Entry(bottom_frame, bg="black", fg="white", insertbackground="white", font=("Consolas", 12))
    entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)

    run_btn = tk.Button(bottom_frame, text="RUN", command=lambda: run_command(), bg="gray30", fg="white", font=("Arial", 12, "bold"))
    run_btn.pack(side="right", padx=5, pady=5)

    def run_command(event=None):
        cmd = entry.get().strip()
        if cmd == "":
            return
        output.insert(tk.END, f">>> {cmd}\n")
        if cmd.lower() == "help":
            output.insert(tk.END, "Available commands: help, cls, echo [text], dir\n")
        elif cmd.lower() == "cls":
            output.delete("1.0", tk.END)
        elif cmd.lower().startswith("echo "):
            output.insert(tk.END, cmd[5:] + "\n")
        elif cmd.lower() == "dir":
            output.insert(tk.END, "file1.txt\nfile2.txt\nfolder1\n")
        else:
            try:
                result = eval(cmd)
                output.insert(tk.END, str(result) + "\n")
            except Exception as e:
                output.insert(tk.END, str(e) + "\n")
        output.see(tk.END)
        entry.delete(0, tk.END)

    entry.bind("<Return>", run_command)

    # Animace otevření (slide)
    def animate_open(width=0, height=0):
        if width < 600 or height < 400:
            width = min(600, width + 20)
            height = min(400, height + 15)
            console_win.geometry(f"{width}x{height}+200+150")
            console_win.after(10, lambda: animate_open(width, height))
    animate_open()

def close_console():
    global console_win
    if not console_win or not console_win.winfo_exists():
        return

    def animate_close(width, height):
        if width > 0 or height > 0:
            width = max(0, width - 20)
            height = max(0, height - 15)
            console_win.geometry(f"{width}x{height}+200+150")
            console_win.after(10, lambda: animate_close(width, height))
        else:
            console_win.destroy()

    w = console_win.winfo_width()
    h = console_win.winfo_height()
    animate_close(w, h)

tk.Button(menu_frame, text="Console", command=open_console, width=20).pack(pady=5)

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
