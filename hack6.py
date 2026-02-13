#========== Mission 3 ==========
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

click = pygame.mixer.Sound("Audio/click.wav")
btn = pygame.mixer.Sound("Audio/btn.wav")

#========== data ==========
logs = ["connect.log || connect to old server"]
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

def btn_log_del():
    global log
    play_btn()
    logs.clear()

def show_tcpip():
    play_btn()
    output.config(text=textify(tcpip))

def copy_files():
    play_btn()
    messagebox.showinfo("Disk", "file ha copy shodand")

#========== story ==========
def mission_chat():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[red]================================[/red]")
    print("You : hala fahmidam...")  ;play_click(); time.sleep(3)
    print("You : un kanal ro faal karde bud")        ;play_click(); time.sleep(2)
    print("You : NOX ham khode jime")                 ;play_click(); time.sleep(3)
    print("")              ;play_click(); time.sleep(1)
    print("[green]+800$[/green]")                ;play_click(); time.sleep(2)
    db.add_money(800)
    print("[red]================================[/red]")
    sys.exit()

#========== start ==========
def start_hack():
    global root, output

    root = tk.Tk()
    root.geometry("420x300")
    root.title("jim johnson")
    root.configure(bg="black")

    messagebox.showinfo("System", "shoma varede system shodid")

    ttk.Button(root, text="disk.sys", command=show_disk).pack(pady=2)
    ttk.Button(root, text=".log", command=show_logs).pack(pady=2)
    ttk.Button(root, text="tcpip.sys", command=show_tcpip).pack(pady=2)
    ttk.Button(root, text="copy disk files", command=copy_files).pack(pady=10)
    button__log_del = ttk.Button(root, text="delete logs", command=btn_log_del).place(x=162,y=153)

    output = tk.Label(root, text="", bg="black", fg="white")
    output.pack(pady=5)

    root.mainloop()
