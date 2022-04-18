import pygame
import tkinter as tk
import time

default_font_name = "Arial Bold"
default_font_size = "13"
default_source_file_name = "source.txt"
default_block_size = 40
default_font_settings = (default_font_name, default_font_size)
default_start_message = "Это клавиатурный тренажер"
default_button_message = "Нажмите для начала"
default_title_message = "Клавиатурный тренажер"
default_music_for_traine = "./music.mp3"
default_ready_message = "READY...????" 
default_steady_message = "STEADY......zzz" 
default_go_message = "GO!!!(^_^)"
default_ready_time = 8
default_steady_time = 11
default_go_time = 2.3
funny_mode_value = "on"


def print_ready_steady_go_message(message, message_time):
    my_message = tk.Label(text = message, font = default_font_settings)
    my_message.pack()
    window.update()
    time.sleep(message_time)
    my_message.destroy()
    window.update()


key_number = None
key_need_to_pres = None
block = None
def continue_key(entry = None):
    #print(entry)
    global key_number
    key_number += 1
    if entry.char == key_need_to_pres:
        global block
        block = False

def funny_mode():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(default_music_for_traine)
    pygame.mixer.music.play()

    print_ready_steady_go_message(default_ready_message, default_ready_time)
    print_ready_steady_go_message(default_steady_message, default_steady_time)
    print_ready_steady_go_message(default_go_message, default_go_time)

def start_of_training():
    start_button.destroy()
    start_message.destroy()
    window.update()
    file = (open(default_source_file_name, 'r').read())

    if funny_mode_value == "on":
        funny_mode()

    for i in range(len(file) // default_block_size):
        left_border = i * default_block_size
        right_border = min(len(file), (i + 1) * default_block_size)
        substring = file[left_border: right_border]
        text = tk.Label(text = substring, font = default_font_settings)
        text.pack()

        result_string = ""
        global key_number
        key_number = 0
        for j in substring:
            result_message = tk.Label(text = result_string, font = default_font_settings)
            result_message.pack()
            global key_need_to_pres
            key_need_to_pres = j
            global block
            block = True
            while block:
                window.bind_all("<KeyPress>", continue_key)
                statistics = tk.Label(text = key_number, font = default_font_settings)
                statistics.pack()
                window.update()
                statistics.destroy()
            result_string += j
            result_message.destroy()
        text.destroy()
    

window = tk.Tk()
window.title(default_title_message)
window.geometry("500x400")

start_message = tk.Label(text = default_start_message, font = default_font_settings)
start_message.pack()

start_button = tk.Button(text = default_button_message, command=start_of_training)
start_button.pack()

window.mainloop()
