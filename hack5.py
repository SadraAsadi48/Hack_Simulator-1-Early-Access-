#==========Mission 3==========
#=============================
#========== imports ==========
import time
import pygame
import os
from rich import print
from rich.progress import track
import os
import db
import random
import hack6

db.init_db()
money = db.get_money()
fire_hack = False

pygame.mixer.init()

#================= defs ===================
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_password():
    return str(random.randint(1000,1000000))

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

def hack_fire():
    global fire_hack
    for _ in track(range(100), description="[yellow]hacking firewall...[/yellow]"):
                time.sleep(0.4)
    print(f"[green]Firewall successfully hacked[/green]")
    fire_hack = True

#================= vars ===================
password = create_password()

#================= start ==================
clear_terminal()
def dastan():
    for _ in track(range(100), description="[yellow]loading mission...[/yellow]"):
                time.sleep(0.4)
    clear_terminal()
    print("[red]=========================New Email============================[/red]")
    print("Jim : [blue]hala bayad chikar konim?[/blue]")         ;play_click_sound(); time.sleep(3)
    print("You : ta feelan hichi")                               ;play_click_sound(); time.sleep(2.5)
    print("Jim : [blue]yani velesh konim?[/blue]")               ;play_click_sound(); time.sleep(3)
    print("You : chare digee nadarim")                           ;play_click_sound(); time.sleep(2)
    print("Jim : [blue]rast migi...[/blue]")                     ;play_click_sound(); time.sleep(2.5)
    print("You : age kary nadari man dige beram")                ;play_click_sound(); time.sleep(3)
    print("Jim : [blue]boro be karat beres...khodafez[/blue]")   ;play_click_sound(); time.sleep(4)
    print("You : khodafez")                                      ;play_click_sound(); time.sleep(2)
    print("[red]==============================================================[/red]");play_click_sound();time.sleep(2)
    print("You : man kheyli be jim mashkukam")                   ;play_click_sound(); time.sleep(3)
    print("You : un az hamun aval be man hasudi mikard")         ;play_click_sound(); time.sleep(3.5)
    print("You : bayad heme in ghazaya kare un bashe!")          ;play_click_sound(); time.sleep(3.5)
    print("You : bayad be systemesh nofuz konam ta bebinam chi mitunam peyda konam"); play_click_sound(); time.sleep(5)
    print("You : systeme un amniate ziadi dare");                                     play_click_sound(); time.sleep(3)
    print("You : hataman systemesh firewall dare");                                   play_click_sound(); time.sleep(3)
    print("You : mitunam ba dasture [yellow]hack_fire[/yellow] firewallesh ro az kar bendazam");play_click_sound(); time.sleep(5)
    print("You : bayad [yellow]log[/yellow] haye systemesh ro bebinam");play_click_sound(); time.sleep(5.5)
    print("[red]==============================================================[/red]");play_click_sound()
    cmd()

#================= prompt =================
def cmd():
    while True:
        prompt = input(">>")

        if prompt == "hack_pass" and fire_hack == True:
            hack_pass()

        elif prompt == "hack_pass" and fire_hack == False:
            print("[red]firewall is on[/red]")

        elif prompt == "login":
            play_click_sound()
            daryaft_pass = input("password: ")
            play_click_sound()

            if daryaft_pass == password:
                print("[green]login successful[/green]")
                play_click_sound()

                for _ in track(range(100), description="[yellow]connecting...[/yellow]"):
                    time.sleep(0.03)

           
                hack6.start_hack()
                break

            else:
                print("[red]password eshtebah ast[/red]")
                play_wrong_sound()

        elif prompt == "money":
            money = db.get_money()
            print(f"[green]money = {money}$[/green]")
            play_click_sound()


        elif prompt == "help":
            print("hack_pass | login | money | cls | help | hack_fire")
            play_click_sound()

        elif prompt == "cls":
            clear_terminal()
            play_click_sound()

        elif prompt == "hack_fire":
            hack_fire()

        else:
            print("[red]dasture eshtebah![/red]")
            play_wrong_sound()
