import tkinter as tk
from tkinter import filedialog
import pygame
import os

pygame.mixer.init()

class SoundboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Soundboard")
        self.root.geometry("600x400")
        self.root.configure(bg='#1e1e1e')

        self.button_frame = tk.Frame(self.root, bg='#1e1e1e')
        self.button_frame.pack(pady=20)

        self.add_button = tk.Button(self.root, text="Add Sound", command=self.add_sound_button, bg='#ff5733', fg='white', font=('Helvetica', 12, 'bold'), activebackground='#c70039', activeforeground='white')
        self.add_button.pack(pady=10)

        self.buttons = []
        self.sound_paths = []

    def play_sound(self, sound_path):
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()

    def add_sound_button(self):
        sound_path = filedialog.askopenfilename(title="Select Sound File", filetypes=[("WAV files", "*.wav"), ("MP3 files", "*.mp3")])
        if sound_path:
            sound_name = os.path.basename(sound_path)
            button = tk.Button(self.button_frame, text=sound_name, command=lambda sp=sound_path: self.play_sound(sp), bg='#33ff57', fg='white', font=('Helvetica', 10, 'bold'), width=20, height=2, activebackground='#28a745', activeforeground='white')
            self.buttons.append(button)
            self.sound_paths.append(sound_path)
            self.update_buttons(button)

    def update_buttons(self, button):
        index = len(self.buttons) - 1
        button.grid(row=index // 3, column=index % 3, padx=10, pady=10)

root = tk.Tk()
app = SoundboardApp(root)

root.mainloop()
