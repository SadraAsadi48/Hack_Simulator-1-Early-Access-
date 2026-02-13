#========== Mission 1 ==========
#========== imports ==========
import time
import random
import os
import pygame
from rich import print
from rich.progress import track

import hack2
import db

#========== init ==========
db.init_db()
pygame.mixer.init()

#========== sounds ==========
click_sound = pygame.mixer.Sound("audio/click.wav")
wrong_sound = pygame.mixer.Sound("audio/wrong.wav")

def play_click():
    click_sound.play()

def play_wrong():
    wrong_sound.play()

#========== utils ==========
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_password():
    return str(random.randint(1000, 9999))

def hack_pass(password):
    for _ in track(range(100), description="[yellow]hacking...[/yellow]"):
        time.sleep(0.05)
    print(f"[bold green]password:[/bold green] {password}")
    play_click()

#========== game vars ==========
password = create_password()
hacked = False

#========== start ==========
clear_terminal()

print("[red]========================= New Email =========================[/red]")
print("[blue]salam duste man. man jim hastam[/blue]"); play_click(); time.sleep(3)
print("[blue]be bakhshe amuzeshi khosh umadi[/blue]"); play_click(); time.sleep(3)
print("[blue]tuye in mamuriat faghat bayad ramze dorost ro hads bezani va vared system shi[/blue]"); play_click(); time.sleep(5)
print("[blue]ba dasture [yellow]hack_pass[/yellow] password ro hack kon[/blue]"); play_click(); time.sleep(3)
print("[blue]ba [yellow]login[/yellow] vared system sho[/blue]"); play_click(); time.sleep(3)
print("[blue]ba [yellow]help[/yellow] hame command ha ro bebin [/blue]"); play_click()
print("[red]============================================================[/red]")
play_click()

#========== prompt loop ==========
while True:
    prompt = input(">> ")

    if prompt == "hack_pass":
        hack_pass(password)
        hacked = True

    elif prompt == "login":
        if not hacked:
            print("[red]aval bayad hack_pass bezani[/red]")
            play_wrong()
            continue

        play_click()
        daryaft_pass = input("password: ").strip()
        play_click()

        if daryaft_pass == password:
            print("[green]login successful[/green]")
            play_click()

            for _ in track(range(100), description="[yellow]connecting...[/yellow]"):
                time.sleep(0.03)

            hack2.start_hack2()
            break
        else:
            print("[red]password eshtebah ast[/red]")
            play_wrong()

    elif prompt == "money":
        money = db.get_money()
        print(f"[green]money = {money}$[/green]")
        play_click()

    elif prompt == "help":
        print("[cyan]hack_pass | login | money | cls | help[/cyan]")
        play_click()

    elif prompt == "cls":
        clear_terminal()
        play_click()

    else:
        print("[red]dasture eshtebah![/red]")
        play_wrong()
