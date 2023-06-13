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
<<<<<<< HEAD
root.geometry('500x300')
root.title('Multigame')

menu = tk.Menu(root)

def ovladani_pong():
    subprocess.Popen(['python', 'ovladani_pong.txt'])
def ovladani_tetris():
    subprocess.Popen(['python', 'ovladani_tetris.txt'])
=======

#velikost a název menu
root.geometry('500x300')
root.title('Multigame')

#definice otevření hry tetris
>>>>>>> 322b0025b8fd530c90506eef527654ace51fbc84
def open_tetris():
    subprocess.Popen(['python', 'tetris.py'])
 
#definice otevření hry pong
def open_pong():
    subprocess.Popen(['python', 'pong.py'])
    
#nadpis vybrání hry
label = tk.Label(root, text='Choose your game!', font=('Arial', 18))
label.pack(padx=20, pady=20)

<<<<<<< HEAD
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='Exit', command=quit)
menu.add_cascade(label='File', menu=file_menu)

ovladani_hry = tk.Menu(menu, tearoff=False)
ovladani_hry.add_command(label='Pong Ovládání', command=ovladani_pong)
ovladani_hry.add_command(label='Tetris Ovládání', command=ovladani_tetris)
menu.add_cascade(label='Ovládání Hry', menu=ovladani_hry)


=======
#tlačítko hry pong
>>>>>>> 322b0025b8fd530c90506eef527654ace51fbc84
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

<<<<<<< HEAD
button3 = tk.Button(root,
                text='Ovládání',
                command=open_pong,
                font=('Arial', 18))
button.pack(padx=10, pady=10)

root.configure(menu=menu)
root.mainloop()
=======
#ukončení menu
root.mainloop()
>>>>>>> 322b0025b8fd530c90506eef527654ace51fbc84
