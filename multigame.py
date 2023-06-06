#Multigame-menu

#Hráč spustí menu a má na výběr mezi dvěma hrami: Tetris a Pong.

#Autoři:
# KamilKrivanek - Kamil Křivánek, PetrCrha - Petr Crha, PabloEmilioEscobarGaviria128482 - Daniel Bakeš, jafaktnevimnicmenenapada - Jan Mitašík, KubaKubiceek - Jakub Leskovjan

#Verze: 1.0.0

#Date: 06.06.2023

#import tkinter
import tkinter as tk
import subprocess

root = tk.Tk()

#velikost a název menu
root.geometry('500x300')
root.title('Multigame')

#definice otevření hry tetris
def open_tetris():
    subprocess.Popen(['python', 'tetris.py'])
 
#definice otevření hry pong
def open_pong():
    subprocess.Popen(['python', 'pong.py'])
    
#nadpis vybrání hry
label = tk.Label(root, text='Choose your game!', font=('Arial', 18))
label.pack(padx=20, pady=20)

#tlačítko hry pong
button = tk.Button(root,
                text='Pong',
                command=open_pong,
                font=('Arial', 18))
button.pack(padx=10, pady=10)

#tlačítko hry tetris
button2 = tk.Button(root,
                    text='Tetris',
                    command=open_tetris,
                    font=('Arial', 18))
button2.pack(padx=10, pady=10)

#ukončení menu
root.mainloop()
