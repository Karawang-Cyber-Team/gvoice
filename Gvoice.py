# APABILA ADA YANG RE UPLOAD SC INI TANPA SEIZIN AUTHOR ASLI MOHON LAPORKAN SAYA VIA FB ATAU WA SAYA. Terima Kasih!!
# WA   : 085810753481
# FB   : True False
# INGIN BEKERJA SAMA MEMBUAT PROJECT?? WA/FB ME.
# FOLLOW MY GITHUB AND STARS MY REPOSITORY BRO :)
# THANXS TO MY TEAM : KARAWANG CYBER TEAM AND PYTHON TEAM OPEN SOURCE
#!user/bin/python3.10

import os, sys
from sys import stdout as st
from time import sleep
from os import system as shell
from random import uniform as unif, choice as ch

def clear(): #cleaning the terminal
    if os.name == "nt":
        shell("cls")
    else:
        shell("clear")
#checking modulee        
try:
    import rich, requests
    from rich.panel import Panel
    from gtts import gTTS
    from io import BytesIO as BIO
except ModuleNotFoundError:
    clear()
    print ("installing modules..")
    print ("please waiting for a minutes.."); sleep(1)
    shell("python3 -m pip install requests rich gtts gTTS ")
    clear()
    print ("done!"); sleep(1)
# okay we start to coding! mangatse..
def picture (clr, color_):
    return f"""
        [default][on black red]  ______    ____   ____        _                     [not on black]
        [on black red].' ___  |  |_  _| |_  _|      (_)                    [not on black]
        [on black green]/ .'   \_|  \ \   / / .--.   __   .---.  .---.       [not on black]
        [on black green]| |   ____   \ \ / // .'`\ \[  | / /'`\]/ /__\\      [not on black]
        [on black blue] `.___]  |   \ ' / | \__. | | | | \__. | \__.,      [not on black]
        [on black blue]`._____.'      \_/   '.__.' [___]'.___.' '.__.'      [not on black]
        [default]-------------------------------------------------    [not on black]
        [red] Author : [italic white]True False[not italic]
        [red] FB     : [italic white]true false        [not italic]
        [red] github : [italic white]github.com/TrueFalseID    [not italic]
        [red] Team   : [italic white]None                              [not italic]

        -------------------------------------------------
        [bold blue]  >> [default]KETIK [bold italic green]HELP [default not italic] UNTUK MELIHAT CARA PENGUNAAN TOOLS [bold blue]<<
        [bold blue]  >> [default]    [underline]KETIK BUG UNTUK MELAPORKAN BUG TOOLS[not underline]      [bold blue]<<[default]

        (01) Voice Indonesian  (06) Voice Afghanistan
        (02) Voice English     (07) Voice Malaysia
        (03) Voice Arabian     (08) Voice Uzbekistan
        (04) Voice Albania     (09) Voice Yaman
        (05) Voice Japan       (10) Voice Brazil 
        (11) Voice Bambara     (12) Voice Basque
        (13) Voice Belanda     (14) Voice BellaRusia
        (15) Voice Bengali     (16) Voice Bhojpuri
        (17) Voice Bosnia      (18) Voice Bulgaria
        (19) Voice Burma       (20) Voice Cebuano
        (21) Voice RepCeko     (22) Voice Chicewa
        (23) Voice Denmark     (24) Voice Divehi
        (25) Voice Dogri       (26) Voice Esparanto
        (27) Voice Estonia     (28) Voice Ewe
        (29) Voice Farsi       (30) Voice Finlandia
        (00) Exit"""
def Animation(txt):
    for i in txt:
        st.write(i)
        st.flush()
        sleep(round(unif(0.03,0.01),2))
def colors():
    global clr, color_
    # [0] = default         [6] = cyan
    # [1] = red             [7] = white   
    # [2] = green           [8] = black
    # [3] = yellow
    # [4] = blue
    # [5] = Magenta/pink
    clr = [   "\x1b[0m",      "\x1b[31;1m",   "\x1b[32;1m",  
                "\x1b[33;1m",   "\x1b[34;1m",   "\x1b[35;1m",
                "\x1b[36;1m",   "\x1b[37;1m",   "\x1b[30;1m"    ]
    color_ = [  "\x1b[44;1m",   "\x1b[41;1m",   "\x1b[40;1m"    ]
def design():
    clear(); colors()
    rich.print(Panel(Panel(picture(clr,color_),style="on black"),style="on cyan"))
class Voice:
    def __init__(self, msg, country) -> str:
        self.coun = country
        self.file = "voice"
        self.msg = msg    
    def voicer(self):
        try:
            get = gTTS(self.msg, lang=self.coun, slow=False)
        except:
            rich.print(Panel("(!) sistem tidak support",style="red"))
            sys.exit(0)
        with open(self.file + f"_{self.coun}.mp3", "wb") as f:
            get.write_to_fp(f)
        return "sukses to save file " + self.file + "_{self.coun}.mp3"
def PROGRAMMER_TURU():
    colors(); Animation(f"\n{color_[2]}enter your choice{clr[0]} ")
    count = input(": ")
    if count == "1" or  "01": coun = "id"
    elif count == "2" or "02": coun = "en"
    elif count == "3" or "03": coun = "ar"
    elif count == "4" or "04": coun = "al"
    elif count == "5" or "05": coun = "ja"
    elif count == "6" or "06": coun = "af"
    elif count == "7" or "07": coun = "my"
    elif count == "8" or "08": coun = "us"
    elif count == "9" or "09": coun = "ye"
    elif count == "10": coun = "br"
    elif count == "11": coun = "bm"
    elif count == "12": coun = "eu"
    elif count == "13": coun = "nl"
    elif count == "14": coun = "be"
    elif count == "15": coun = "bn"
    elif count == "16": coun = "bho"
    elif count == "17": coun = "bs"
    elif count == "18": coun = "bg"
    elif count == "19": coun = "my"
    elif count == "20": coun = "ceb"
    elif count == "21": coun = "cs"
    elif count == "22": coun = "ny"
    elif count == "23": coun = "da"
    elif count == "24": coun = "dv"
    elif count == "25": coun = "doi"
    elif count == "26": coun = "eo"
    elif count == "27": coun = "et"
    elif count == "28": coun = "ee"
    elif count == "29": coun = "fa"
    elif count == "30": coun = "fi"
    elif count == "00": exit()
    Animation(f"\n{color_[2]}enter the message{clr[0]} ")
    msg = input(": ")
    x = Voice(msg, coun).voicer();
    rich.print(Panel(x, style="bold green"))
    shell(f"xdg-open voice{coun}.mp3")
    def REUSE():
        try:
            y = input(f"{clr[0]}try again?[y/n] ")
            if y == "y":
                PROGRAMMER_TURU()
            else:
                sys.exit("\n[program finshed]\n")
        except KeyboardInterrupt: print ("{}jangan menekan ctrl+c").format(clr[1]); REUSE()
        except EOFError: print ("{}jangan menekan ctrl+d").format(clr[1]);REUSE()
    REUSE()
      
if __name__ == "__main__":
    design()  
    PROGRAMMER_TURU()
    os.system("git pull")
