#==========Mission 1==========
#=============================
#===========Imports==========
import tkinter as tk
import pygame
import random
from tkinter import ttk, messagebox
from rich import print
import time
import sys
import os
import db
import hack3

pygame.mixer.init()

#====================== Data =============================
first_names = ["John", "Emily", "Michael", "Sarah", "Daniel"]
last_names = ["Smith", "Johnson", "Brown", "Davis", "Miller"]

logs = []
disk = ["program.exe", "readme.txt", "config.sys", "bootmgr", "data.bin"]
tcpip = []

copy = False
score = 0
log = False

#====================== Functions ========================
def random_full_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def play_click_sound():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audio/click.wav")
    pygame.mixer.music.play()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_btn():
    try:
        pygame.mixer.music.load("audio/btn.wav")
        pygame.mixer.music.play()
    except:
        pass

def textify(data, empty="(Empty)"):
    return "\n".join(data) if data else empty

def btn_disk():
    play_btn()
    label_output.config(text=textify(disk))
    logs.insert(0, "disk.log||enter disk")

def btn_log():
    play_btn()
    label_output.config(text=textify(logs))

def btn_tcpip():
    play_btn()
    label_output.config(text=textify(tcpip))

def btn_log_del():
    global log
    play_btn()
    logs.clear()
    log = True

    if copy and log:
        clear_terminal()
        time.sleep(1)
        play_click_sound()
        root.destroy()
        print("[red]========================New Email===========================[/red]")
        print("[blue]karet khub bud[/blue]"),time.sleep(2.5),play_click_sound()
        print("[blue]to bakhshe amuzeshi ro tamum kardi[/blue]"),time.sleep(3.5),play_click_sound()
        print("[green]800$[/green][blue]zadam be kartet[/blue]"),time.sleep(2.5),play_click_sound()
        print("[blue]hala mituni varede bakhsh dastani beshi[/blue]"),time.sleep(4.5),play_click_sound()
        print("[red]============================================================[/red]"),time.sleep(2)

        clear_terminal()        
        hack3.dastan()
        sys.exit()

def btn_copy_files():
    global copy, score,log
    copy = True
    db.add_money(800)
    messagebox.showinfo("Disk", "file ha copy shodand")
    if copy and log:
        clear_terminal()
        time.sleep(1)
        play_click_sound()
        root.destroy()
        print("[red]========================New Email===========================[/red]")
        print("[blue]karet khub bud[/blue]"),time.sleep(2.5),play_click_sound()
        print("[blue]to bakhshe amuzeshi ro tamum kardi[/blue]"),time.sleep(3.5),play_click_sound()
        print("[green]800$[/green][blue]zadam be kartet[/blue]"),time.sleep(2.5),play_click_sound()
        print("[blue]hala mituni varede bakhsh dastani beshi[/blue]"),time.sleep(4.5),play_click_sound()
        print("[red]============================================================[/red]"),time.sleep(2)

        clear_terminal()        
        hack3.dastan()
        sys.exit()

#====================== START ============================
def start_hack2():
    global label_output,button_disk,button__log ,button__tcpip,button__copy,root

    root = tk.Tk()
    root.geometry("400x250")
    root.title(random_full_name())
    root.config(bg="black")

    messagebox.showinfo("System", "shoma varede system shodid")
    logs.insert(0, "connect.log||login")

    tk.Label(root, text="Windows Files", bg="black", fg="white").pack()

    button_disk = ttk.Button(root, text="disk.sys", command=btn_disk).pack(pady=2)
    button__log = ttk.Button(root, text=".log", command=btn_log).pack(pady=2)
    button__tcpip = ttk.Button(root, text="tcpip.sys", command=btn_tcpip).pack(pady=2)
    button__copy = ttk.Button(root, text="copy disk files", command=btn_copy_files).pack(pady=20)
    button__log_del = ttk.Button(root, text="delete logs", command=btn_log_del).place(x=162,y=153)

    label_output = tk.Label(root, text="", bg="black", fg="white")
    label_output.pack(pady=5)

#================run=================
    root.mainloop()
