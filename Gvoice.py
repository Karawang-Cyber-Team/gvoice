# APABILA ADA YANG RE UPLOAD SC INI TANPA SEIZIN AUTHOR ASLI MOHON LAPORKAN SAYA VIA FB ATAU WA SAYA !!
# WA   : 085810753481
# FB   : True False
# INGIN BEKERJA SAMA MEMBUAT PROJECT?? WA/FB ME.
# FOLLOW MY GITHUB AND STARS MY REPOSITORY BRO :)
# THANXS TO MY TEAM : KARAWANG CYBER TEAM AND PYTHON TEAM OPEN SOURCE

#usr/bin/python3
import os, sys, time, requests
from gtts import gTTS

## PLEASE NO EDIT AUTHOR NAME!!
author = 'True False'
fb = 'True False'
github = 'github.com/TrueFalseID'

def mengetik(TrueFalseID):
    for im in TrueFalseID + '\n':
        sys.stdout.write(im)
        sys.stdout.flush()
        time.sleep(00.03) 
        
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
a = '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]'
b = '\x1b[1;97m[\x1b[1;91m?\x1b[1;97m]'
c = '\x1b[1;97m[\x1b[1;91m•\x1b[1;97m]'

def baner():
  print(f"""
\x1b[31m  ______    ____   ____        _
\x1b[31m.' ___  |  |_  _| |_  _|      (_)
\x1b[33m/ .'   \_|    \ \   / / .--.   __   .---.  .---.
\x1b[32m| |   ____     \ \ / // .'`\ \[  | / /'`\]/ /__\\
\x1b[32m\ `.___]  |     \ ' / | \__. | | | | \__. | \__.,
\x1b[34m `._____.'       \_/   '.__.' [___]'.___.' '.__.'
{c}-------------------------------------------------{c}
{c} Author : {author}                             {c}
{c} FB     : {fb}                             {c}
{c} github : {github}                 {c}
{c} Team   : Karawang Cyber Team                    {c}
{c}-------------------------------------------------{c}
{M}  >> {P}KETIK {M}HELP {P}UNTUK MELIHAT CARA PENGUNAAN TOOLS {M}<<
{M}  >>     {P}KETIK {M}BUG {P}UNTUK MELAPORKAN BUG TOOLS      {M}<<
  """)
def menu():
  os.system('clear');baner()
  mengetik(f"""\x1b[1;97m[\x1b[1;91m01\x1b[1;97m] Voice indonesia \x1b[1;97m[\x1b[1;91m02\x1b[1;97m] Voice inggris\n\x1b[1;97m[\x1b[1;91m03\x1b[1;97m] Voice arab      \x1b[1;97m[\x1b[1;91m04\x1b[1;97m] Voice albania\n\x1b[1;97m[\x1b[1;91m05\x1b[1;97m] Voice Jepang    \x1b[1;97m[\x1b[1;91m06\x1b[1;97m] Voice amhara\n\x1b[1;97m[\x1b[1;91m07\x1b[1;97m] Voice armenia   \x1b[1;97m[\x1b[1;91m08\x1b[1;97m] Voice assam\n\x1b[1;97m[\x1b[1;91m09\x1b[1;97m] Voice aymara    \x1b[1;97m[\x1b[1;91m10\x1b[1;97m] Voice azerbaijan\n\x1b[1;97m[\x1b[1;91m00\x1b[1;97m] Exit
  """)
  udud = input(f'{b} Choice >>: ')
  if udud in ['']:
      print(f'{a} \x1b[1;91mPlease input your menu{P}');time.sleep(2);os.system('clear');menu()
  if udud in ['00']:
    time.sleep(2);mengetik(f'{P}Thanxs using my tools bro. please follow and stars my repository:)');os.system('xdg-open https://github.com/TrueFalseID')
  if udud in ['help','HELP','ikehikeh','kimochisayang']:
   time.sleep(2);os.system('clear')
   print('\n\n')
   mengetik(f'{M}>> {P}CARA PENGGUNAAN TOOLS INI! {M}<<\n')
   mengetik(f'{M}>> {P}KETIK TEXT YANG INGIN MAU BUAT VOICE {M}<<')
   mengetik(f'{M}>> {P}SETELAH SELESAI MENGETIKAN TEXT LALU KLIK ENTER {M}<<')
   mengetik(f'{M}>> {P}KALO SUDAH DI ENTER OTOMATIS PROGRAM BAKAL MENCONVERT TEXT KE VOICE.MP3 {M}<<');time.sleep(7);exit()
  if udud in ['bug','BUG']:
    time.sleep(2);os.system('xdg-open https://wa.me/+6285810753481')
  if udud in ['1','01']:
    os.system('clear');baner()
    spet = input(f'{P}Enter Text To Spech : ')
    speech = gTTS(text=spet, lang='id', slow=False)
    speech.save('voice.mp3');time.sleep(3)
    mengetik(f'\n{H}Success file saved!{P}')
    kasep = input(f'{b} INGIN MENCOBA YANG LAIN Y/N :')
  if kasep in ['']:
    print(f'{a} \x1b[1;91mPlease input your menu{P}');time.sleep(2);os.system('clear');menu()
  if kasep in ['y','ya','YA','yes','YES']:
    time.sleep(1);os.system('clear');baner();menu()
  if kasep in ['n','N','no','NO','na','NI']:
    time.sleep(2);mengetik(f'{P}Thanxs using my tools bro. please follow and stars my repository:)');exit()
    
  if udud in ['2','02']:
    os.system('clear');baner()
    spet = input(f'{P}Enter Text To Spech : ')
    speech = gTTS(text=spet, lang='en', slow=False)
    speech.save('voice.mp3');time.sleep(3)
    mengetik(f'\n{H}Success file saved!{P}')
    geulis = input(f'{b} INGIN MENCOBA YANG LAIN Y/N :')
  if geulis in ['']:
    print(f'{a} \x1b[1;91mPlease input your menu{P}');time.sleep(2);os.system('clear');menu()
  if geulis in ['y','ya','YA','yes','YES']:
    time.sleep(1);os.system('clear');baner();menu()
  if geulis in ['n','N','no','NO','na','NI']:
    time.sleep(2);mengetik(f'{P}Thanxs using my tools bro. please follow and stars my repository:)');exit()
  
  if udud in ['3','03']:
    os.system('clear');baner()
    spet = input(f'{P}Enter Text To Spech : ')
    speech = gTTS(text=spet, lang='af', slow=False)
    speech.save('voice.mp3');time.sleep(3)
    mengetik(f'\n{H}Success file saved!{P}')
    ganteng = input(f'{b} INGIN MENCOBA YANG LAIN Y/N :')
  if ganteng in ['']:
    print(f'{a} \x1b[1;91mPlease input your menu{P}');time.sleep(2);os.system('clear');menu()
  if ganteng in ['y','ya','YA','yes','YES']:
    time.sleep(1);os.system('clear');baner();menu()
  if ganteng in ['n','N','no','NO','na','NI']:
    time.sleep(2);mengetik(f'{P}Thanxs using my tools bro. please follow and stars my repository:)');exit()
    
  if udud in ['4','04']:
    os.system('clear');baner()
    spet = input(f'{P}Enter Text To Spech : ')
    speech = gTTS(text=spet, lang='tl', slow=False)
    speech.save('voice.mp3');time.sleep(3)
    mengetik(f'\n{H}Success file saved!{P}')
    cantik = input(f'{b} INGIN MENCOBA YANG LAIN Y/N :')
  if cantik in ['']:
    print(f'{a} \x1b[1;91mPlease input your menu{P}');time.sleep(2);os.system('clear');menu()
  if cantik in ['y','ya','YA','yes','YES']:
    time.sleep(1);os.system('clear');baner();menu()
  if cantik in ['n','N','no','NO','na','NI']:
    time.sleep(2);mengetik(f'{P}Thanxs using my tools bro. please follow and stars my repository:)');exit()
    
  if udud in ['5','05']:
    os.system('clear');baner()
    spet = input(f'{P}Enter Text To Spech : ')
    speech = gTTS(text=spet, lang='ja', slow=False)
    speech.save('voice.mp3');time.sleep(3)
    mengetik(f'\n{H}Success file saved!{P}')
    cantik = input(f'{b} INGIN MENCOBA YANG LAIN Y/N :')
  if cantik in ['']:
    print(f'{a} \x1b[1;91mPlease input your menu{P}');time.sleep(2);os.system('clear');menu()
  if cantik in ['y','ya','YA','yes','YES']:
    time.sleep(1);os.system('clear');baner();menu()
  if cantik in ['n','N','no','NO','na','NI']:
    time.sleep(2);mengetik(f'{P}Thanxs using my tools bro. please follow and stars my repository:)');exit()
    
  if udud in ['6','06']:
    os.system('clear');baner()
    spet = input(f'{P}Enter Text To Spech : ')
    speech = gTTS(text=spet, lang='am', slow=False)
    speech.save('voice.mp3');time.sleep(3)
    mengetik(f'\n{H}Success file saved!{P}')
    ikehikeh = input(f'{b} INGIN MENCOBA YANG LAIN Y/N :')
  if ikehikeh in ['']:
    print(f'{a} \x1b[1;91mPlease input your menu{P}');time.sleep(2);os.system('clear');menu()
  if ikehikeh in ['y','ya','YA','yes','YES']:
    time.sleep(1);os.system('clear');baner();menu()
  if ikehikeh in ['n','N','no','NO','na','NI']:
    time.sleep(2);mengetik(f'{P}Thanxs using my tools bro. please follow and stars my repository:)');exit()
    
  if udud in ['7','07']:
    os.system('clear');baner()
    spet = input(f'{P}Enter Text To Spech : ')
    speech = gTTS(text=spet, lang='hy', slow=False)
    speech.save('voice.mp3');time.sleep(3)
    mengetik(f'\n{H}Success file saved!{P}')
    ewewe = input(f'{b} INGIN MENCOBA YANG LAIN Y/N :')
  if ewewe in ['']:
    print(f'{a} \x1b[1;91mPlease input your menu{P}');time.sleep(2);os.system('clear');menu()
  if ewewe in ['y','ya','YA','yes','YES']:
    time.sleep(1);os.system('clear');baner();menu()
  if ewewe in ['n','N','no','NO','na','NI']:
    time.sleep(2);mengetik(f'{P}Thanxs using my tools bro. please follow and stars my repository:)');exit()
    
  if udud in ['8','08']:
    os.system('clear');baner()
    spet = input(f'{P}Enter Text To Spech : ')
    speech = gTTS(text=spet, lang='as', slow=False)
    speech.save('voice.mp3');time.sleep(3)
    mengetik(f'\n{H}Success file saved!{P}')
    memek = input(f'{b} INGIN MENCOBA YANG LAIN Y/N :')
  if memek in ['']:
    print(f'{a} \x1b[1;91mPlease input your menu{P}');time.sleep(2);os.system('clear');menu()
  if memek in ['y','ya','YA','yes','YES']:
    time.sleep(1);os.system('clear');baner();menu()
  if memek in ['n','N','no','NO','na','NI']:
    time.sleep(2);mengetik(f'{P}Thanxs using my tools bro. please follow and stars my repository:)');exit()
    
  if udud in ['9','09']:
    os.system('clear');baner()
    spet = input(f'{P}Enter Text To Spech : ')
    speech = gTTS(text=spet, lang='ay', slow=False)
    speech.save('voice.mp3');time.sleep(3)
    mengetik(f'\n{H}Success file saved!{P}')
    kontol = input(f'{b} INGIN MENCOBA YANG LAIN Y/N :')
  if kontol in ['']:
    print(f'{a} \x1b[1;91mPlease input your menu{P}');time.sleep(2);os.system('clear');menu()
  if kontol in ['y','ya','YA','yes','YES']:
    time.sleep(1);os.system('clear');baner();menu()
  if kontol in ['n','N','no','NO','na','NI']:
    time.sleep(2);mengetik(f'{P}Thanxs using my tools bro. please follow and stars my repository:)');exit()
    
  if udud in ['10']:
    os.system('clear');baner()
    spet = input(f'{P}Enter Text To Spech : ')
    speech = gTTS(text=spet, lang='az', slow=False)
    speech.save('voice.mp3');time.sleep(3)
    mengetik(f'\n{H}Success file saved!{P}')
    kopienak = input(f'{b} INGIN MENCOBA YANG LAIN Y/N :')
  if kopienak in ['']:
    print(f'{a} \x1b[1;91mPlease input your menu{P}');time.sleep(2);os.system('clear');menu()
  if kopienak in ['y','ya','YA','yes','YES']:
    time.sleep(1);os.system('clear');baner();menu()
  if kopienak in ['n','N','no','NO','na','NI']:
    time.sleep(2);mengetik(f'{P}Thanxs using my tools bro. please follow and stars my repository:)');exit()
  
    
if __name__ == '__main__':
  menu()