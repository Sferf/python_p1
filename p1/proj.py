import pygame
import tkinter as tk
import time
#import keyboard


default_font_name = "Arial Bold"
default_font_size = "13"
default_source_file_name = "source.txt"
default_block_size = 40
default_font_settings = (default_font_name, default_font_size)
default_start_message = "Это клавиатурный тренажер"
default_button_message = "Нажмите для начала"
default_title_message = "Клавиатурный тренажер"
default_music_for_traine = "./music.mp3"
default_ready_message = "READY ...????" 
default_steady_message = "STEADY......" 
default_go_message = "GO!!!"
default_ready_time = 11
default_steady_time = 9
default_go_time = 2



def start_of_training():
    start_button.destroy()
    start_message.destroy()
    window.update()
    file = (open(default_source_file_name, 'r').read())

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(default_music_for_traine)
    pygame.mixer.music.play()

    ready = tk.Label(text = default_ready_message, font = default_font_settings)
    ready.pack()
    window.update()
    time.sleep(default_ready_time)
    ready.destroy()
    window.update()

    steady = tk.Label(text = default_steady_message, font = default_font_settings)
    steady.pack()
    window.update()
    time.sleep(default_steady_time)
    steady.destroy()
    window.update()

    go = tk.Label(text = default_go_message, font = default_font_settings)
    go.pack()
    window.update()
    time.sleep(default_go_time)
    go.destroy()
    window.update()

    for i in range(len(file) // default_block_size):
        left_border = i * default_block_size
        right_border = min(len(file), (i + 1) * default_block_size)
        substring = file[left_border: right_border]
        text = tk.Label(text = substring, font = default_font_settings)
        text.pack()

        for j in substring:
            t = 0
            while t < 1000:
            #not keyboard.is_pressed(j):
                t += 1
                time.sleep(0.01)
                print(t)
                window.update()
        text.destroy()
    

window = tk.Tk()
window.title(default_title_message)
window.geometry("500x400")

start_message = tk.Label(text = default_start_message, font = default_font_settings)
start_message.pack()

start_button = tk.Button(text = default_button_message, command=start_of_training)
start_button.pack()

window.mainloop()
