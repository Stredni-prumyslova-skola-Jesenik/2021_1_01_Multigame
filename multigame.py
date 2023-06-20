#Multigame-menu

#Hráč spustí menu a má na výběr mezi dvěma hrami: Tetris a Pong.

#Autoři:
# KamilKrivanek - Kamil Křivánek, PetrCrha - Petr Crha, PabloEmilioEscobarGaviria128482 - Daniel Bakeš, jafaktnevimnicmenenapada - Jan Mitašík, KubaKubiceek - Jakub Leskovjan

#Verze: 1.0.0

#Date: 06.06.2023

#import tkinter
import customtkinter
import subprocess

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry('500x350')
root.title('Multigame')

def games_controls():
    subprocess.Popen(['python', 'ovladani.py'])

def open_tetris():
    subprocess.Popen(['python', 'tetris.py'])
 
#definice otevření hry pong
def open_pong():
    subprocess.Popen(['python', 'pong.py'])
    
#nadpis vybrání hry
label = customtkinter.CTkLabel(root, text='Choose your game!', font=('Arial', 18))
label.pack(padx=20, pady=20)

button = customtkinter.CTkButton(root,
                text='Pong',
                command=open_pong,
                font=('Arial', 18))
button.pack(padx=10, pady=10)

#tlačítko hry tetris
button2 = customtkinter.CTkButton(root,
                    text='Tetris',
                    command=open_tetris,
                    font=('Arial', 18))
button2.pack(padx=10, pady=10)

button3 = customtkinter.CTkButton(root,
                text='Exit',
                command=exit,
                font=('Arial', 18))
button3.pack(padx=10, pady=10)


root.mainloop()
