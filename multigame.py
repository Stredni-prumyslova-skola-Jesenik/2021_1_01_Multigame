import tkinter as tk
import subprocess

root = tk.Tk()

root.geometry('500x300')
root.title('Multigame')
def open_tetris():
    subprocess.Popen(['python', 'tetris.py'])
def open_pong():
    subprocess.Popen(['python', 'pong.py'])
label = tk.Label(root, text='Choose your game!', font=('Arial', 18))
label.pack(padx=20, pady=20)

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
    
root.mainloop()