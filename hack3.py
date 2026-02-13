#==========Mission 2==========
#=============================
#========== imports ==========
import time
import pygame
import os
from rich import print
from rich.progress import track
import hack4
import os
import db

db.init_db()
money = db.get_money()

pygame.mixer.init()

#================= defs ===================
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_password():
    return str(4848)

def play_click_sound():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audio/click.wav")
    pygame.mixer.music.play()

def play_wrong_sound():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audio/wrong.wav")
    pygame.mixer.music.play()

def hack_pass():
    for _ in track(range(100), description="[yellow]hacking...[/yellow]"):
        time.sleep(0.05)
    print(f"password: [bold green]{password}[/bold green]")
    play_click_sound()

#================= vars ===================
password = create_password()

#================= start ==================
clear_terminal()
def dastan():
    for _ in track(range(100), description="[yellow]loading mission...[/yellow]"):
                time.sleep(0.1)
    clear_terminal()
    print("[red]=====================================================[/red]")
    print("Jim : [blue]in kanal faal shode!bavaret mishe?[/blue]")                      ;play_click_sound(); time.sleep(4)
    print("You : yani ki in karo karde?")                                         ;play_click_sound(); time.sleep(3)
    print("Jim : [blue]nemidunam...bayad kasi ke in karo karde ro peyda konim[/blue]")  ;play_click_sound(); time.sleep(4)
    print("You : are vali chetori?")                                              ;play_click_sound(); time.sleep(2)
    print("Jim : [blue]bayad soraghe server ghadimi mun berim[/blue]")                  ;play_click_sound(); time.sleep(3)
    print("You : man miram va [yellow]log[/yellow] haye server ro baresi mikonam");play_click_sound(); time.sleep(5)
    print("Jim : [blue]khube[/blue]")                                                   ;play_click_sound(); time.sleep(1)
    print("You : ramze server chand bud?")                                        ;play_click_sound(); time.sleep(3)
    print("Jim : [blue]nemidunam[/blue]")                                                    ;play_click_sound(); time.sleep(1)
    print("[red]=====================================================[/red]")     ;play_click_sound(); play_click_sound()
    cmd()
#================= prompt =================
def cmd():
    while True:
        prompt = input(">>")

        if prompt == "hack_pass":
            hack_pass()

        elif prompt == "login":
            play_click_sound()
            daryaft_pass = input("password: ")
            play_click_sound()

            if daryaft_pass == password:
                print("[green]login successful[/green]")
                play_click_sound()

                for _ in track(range(100), description="[yellow]connecting...[/yellow]"):
                    time.sleep(0.03)

           
                hack4.start_hack()
                break

            else:
                print("[red]password eshtebah ast[/red]")
                play_wrong_sound()

        elif prompt == "money":
            money = db.get_money()
            print(f"[green]money = {money}$[/green]")
            play_click_sound()


        elif prompt == "help":
            print("hack_pass | login | money | cls | help")
            play_click_sound()

        elif prompt == "cls":
            clear_terminal()
            play_click_sound()

        else:
            print("[red]dasture eshtebah![/red]")
            play_wrong_sound()
