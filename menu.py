#=============  بسم الله الرحمان الرحيم  ===============
import tkinter as tk
from tkinter import messagebox
import sys
import pygame as pg
import subprocess
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#=========================window===========================
root = tk.Tk()
root.title("Hack Simulator")
root.geometry("800x600")
root.resizable(False, False)

#=========================audio============================
pg.mixer.init()
pg.mixer.music.load("hack sim 1.2/Audio/menu.wav")
pg.mixer.music.play(-1)

#======================canvas (background)=================
WIDTH = 800
HEIGHT = 600
FONT_SIZE = 16
SPEED = 6

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black", highlightthickness=0)
canvas.place(x=0, y=0)

drops = []
for x in range(0, WIDTH, FONT_SIZE):
    y = random.randint(-HEIGHT, 0)
    drops.append([x, y])

def matrix_animation():
    canvas.delete("matrix")
    for drop in drops:
        x, y = drop
        char = random.choice(["0", "1"])
        canvas.create_text(x, y, text=char, fill="lime",
                           font=("Consolas", FONT_SIZE, "bold"), tag="matrix")
        drop[1] += SPEED
        if drop[1] > HEIGHT:
            drop[1] = random.randint(-100, 0)
    root.after(50, matrix_animation)

matrix_animation()

#========================= LABELS =========================
label = tk.Label(root, text="Hack Simulator", bg="black", fg="lime", font=("Arial", 30))
label2 = tk.Label(root, text="1", bg="black", fg="red", font=("Arial", 30))

label.place(x=30, y=12)
label2.place(x=309, y=12)

#================= LOADING (CENTER) =================
BAR_W = 300
BAR_X1 = 250
BAR_Y1 = 300
BAR_X2 = BAR_X1 + BAR_W
BAR_Y2 = 325

loading_bg = canvas.create_rectangle(
    BAR_X1, BAR_Y1, BAR_X2, BAR_Y2,
    outline="lime", width=2, state="hidden"
)

loading_bar = canvas.create_rectangle(
    BAR_X1+2, BAR_Y1+2, BAR_X1+2, BAR_Y2-2,
    fill="lime", width=0, state="hidden"
)

loading_text = canvas.create_text(
    400, 270,
    text="SYSTEM BOOTING...",
    fill="lime",
    font=("Consolas", 14, "bold"),
    state="hidden"
)

loading_percent = canvas.create_text(
    400, 340,
    text="0%",
    fill="lime",
    font=("Consolas", 12),
    state="hidden"
)

scanline = canvas.create_rectangle(
    BAR_X1, BAR_Y1, BAR_X2, BAR_Y1+4,
    fill="#00aa00", outline="", state="hidden"
)

loading_progress = 0
scan_y = BAR_Y1

#================= BUTTON STYLE =================
BTN_BG = "#0f0f0f"
BTN_FG = "lime"
BTN_FONT = ("Consolas", 16, "bold")

def hacky_button(text, command, x, y, hover_bg, hover_fg):
    btn = tk.Button(root, text=text, bg=BTN_BG, fg=BTN_FG,
                    font=BTN_FONT, width=22, height=2,
                    relief="flat", activebackground=hover_bg,
                    activeforeground=hover_fg, command=command,
                    cursor="hand2")
    btn.place(x=x, y=y)

    btn.bind("<Enter>", lambda e: btn.config(bg=hover_bg, fg=hover_fg))
    btn.bind("<Leave>", lambda e: btn.config(bg=BTN_BG, fg=BTN_FG))
    return btn

#================= CREDITS =================
credits_visible = False
def toggle_credits():
    global credits_visible
    if not credits_visible:
        credits_label.place(x=250, y=400)
        credits_visible = True
    else:
        credits_label.place_forget()
        credits_visible = False

credits_label = tk.Label(
    root,
    text="=== CREDITS ===\n\nGame Developer:\nSadra Asadi\n\nHack Simulator v1.2",
    bg="black", fg="lime",
    font=("Consolas", 14),
    justify="center"
)

#================= BUTTONS =================
btn_start = hacky_button(">>> START HACK <<<", lambda: start(), 310, 210, "lime", "black")
btn_credits = hacky_button(">>> CREDITS <<<", toggle_credits, 310, 270, "cyan", "black")
btn_exit = hacky_button(">>> EXIT <<<", lambda: exit_game(), 310, 330, "red", "black")

buttons = [btn_start, btn_credits, btn_exit]

def hide_buttons():
    for b in buttons:
        b.place_forget()

#================= START / EXIT =================
def start():
    pg.mixer.music.fadeout(6000)
    hide_buttons()
    show_loading()
    loading_animation()
    scanline_animation()

def exit_game():
    if messagebox.askyesno("SYSTEM ALERT",
                           "[!] TERMINATE SESSION?\n\nUNSAVED DATA WILL BE LOST."):
        root.destroy()

#================= LOADING ANIMATION =================
def show_loading():
    for item in (loading_bg, loading_bar, loading_text,
                 loading_percent, scanline):
        canvas.itemconfigure(item, state="normal")

def loading_animation():
    global loading_progress

    if loading_progress < BAR_W - 4:
        loading_progress += 1

        canvas.coords(
            loading_bar,
            BAR_X1 + 2, BAR_Y1 + 2,
            BAR_X1 + 2 + loading_progress, BAR_Y2 - 2
        )

        percent = int((loading_progress / (BAR_W - 4)) * 100)
        canvas.itemconfigure(loading_percent, text=f"{percent}%")

        root.after(50, loading_animation)
    else:
        root.destroy()
        subprocess.call([sys.executable, os.path.join(BASE_DIR, "hack.py")])


def scanline_animation():
    global scan_y
    scan_y += 4
    if scan_y > BAR_Y2:
        scan_y = BAR_Y1
    canvas.coords(scanline, BAR_X1, scan_y, BAR_X2, scan_y+4)
    root.after(30, scanline_animation)

#================= run =================
root.mainloop()
