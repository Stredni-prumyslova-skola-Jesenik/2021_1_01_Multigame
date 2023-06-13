import tkinter as tk
import subprocess

root = tk.Tk()
root.geometry('500x300')
root.title('Multigame')

menu = tk.Menu(root)

def ovladani_pong():
    subprocess.Popen(['python', 'ovladani_pong.txt'])
def ovladani_tetris():
    subprocess.Popen(['python', 'ovladani_tetris.txt'])
def open_tetris():
    subprocess.Popen(['python', 'tetris.py'])
def open_pong():
    subprocess.Popen(['python', 'pong.py'])
label = tk.Label(root, text='Choose your game!', font=('Arial', 18))
label.pack(padx=20, pady=20)

file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='Exit', command=quit)
menu.add_cascade(label='File', menu=file_menu)

ovladani_hry = tk.Menu(menu, tearoff=False)
ovladani_hry.add_command(label='Pong Ovládání', command=ovladani_pong)
ovladani_hry.add_command(label='Tetris Ovládání', command=ovladani_tetris)
menu.add_cascade(label='Ovládání Hry', menu=ovladani_hry)


button = tk.Button(root,
                text='Pong',
                command=open_pong,
                font=('Arial', 18))
button.pack(padx=10, pady=10)

button2 = tk.Button(root,
                    text='Tetris',
                    command=open_tetris,
                    font=('Arial', 18))
button2.pack(padx=10, pady=10)

button3 = tk.Button(root,
                text='Ovládání',
                command=open_pong,
                font=('Arial', 18))
button.pack(padx=10, pady=10)

root.configure(menu=menu)
root.mainloop()