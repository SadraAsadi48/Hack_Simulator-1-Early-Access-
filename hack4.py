#========== Mission 2 ==========
import tkinter as tk
from tkinter import ttk, messagebox
import pygame
import os
import db
import time
from rich import print
import sys

#========== init ==========
pygame.mixer.init()
db.init_db()

click = pygame.mixer.Sound("audio/click.wav")
btn = pygame.mixer.Sound("audio/btn.wav")

#========== data ==========
logs = ["connect.log || login","=== NOX ==="]
disk = ["program.exe", "readme.txt", "config.sys", "bootmgr", "data.bin"]
tcpip = ["127.0.0.1", "192.168.1.1"]

#========== utils ==========
def play_click():
    click.play()

def play_btn():
    btn.play()

def textify(data):
    return "\n".join(data) if data else "(Empty)"

#========== buttons ==========
def show_disk():
    play_btn()
    output.config(text=textify(disk))
    logs.insert(0, "disk.log || open disk")

def show_logs():
    play_btn()
    output.config(text=textify(logs))
    log = True
    time.sleep(2)
    root.after(3000,destroy)

def destroy():
    root.destroy()
    after_mission_chat()

def show_tcpip():
    play_btn()
    output.config(text=textify(tcpip))

def copy_files():
    play_btn()
    messagebox.showinfo("Disk", "file ha copy shodand")

#========== story ==========
def after_mission_chat():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[red]================================[/red]")
    print("You : log ha chizi ro neshun midan")  ;play_click(); time.sleep(3)
    print("Jim : [blue]chi didi?[/blue]")        ;play_click(); time.sleep(2)
    print("You : ye esm... NOX")                 ;play_click(); time.sleep(3)
    print("Jim : [blue]...[/blue]")              ;play_click(); time.sleep(1)
    print("[green]+800$[/green]")                ;play_click(); time.sleep(2)
    db.add_money(800)
    print("[red]================================[/red]")
    sys.exit()

#========== start ==========
def start_hack():
    global root, output

    root = tk.Tk()
    root.geometry("420x300")
    root.title("Old Server")
    root.configure(bg="black")

    messagebox.showinfo("System", "shoma varede server shodid")

    ttk.Button(root, text="disk.sys", command=show_disk).pack(pady=2)
    ttk.Button(root, text=".log", command=show_logs).pack(pady=2)
    ttk.Button(root, text="tcpip.sys", command=show_tcpip).pack(pady=2)
    ttk.Button(root, text="copy disk files", command=copy_files).pack(pady=10)

    output = tk.Label(root, text="", bg="black", fg="white")
    output.pack(pady=5)

    root.mainloop()
