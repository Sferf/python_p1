import pygame
import tkinter as tk
import time
import math

class Default:
    font_name = "Arial Bold"
    font_size = "13"
    source_file_name = "source.txt"
    block_size = 40
    font_settings = (font_name, font_size)
    start_message = "Это клавиатурный тренажер"
    button_message = "Нажмите для начала"
    title_message = "Клавиатурный тренажер"
    music_for_traine = "./music.mp3"
    ready_message = "READY...????" 
    steady_message = "STEADY......zzz" 
    go_message = "GO!!!(^_^)"
    ready_time = 8
    steady_time = 11
    go_time = 2.3
    sleep_time = 0.04
    current_statistcs_message = "Current statistcs"
    module_statistics = 10000
    statistics_file = "best_time.txt"
    statistics_message = "You best time: "
    funny_mode_value = "off"
    separator_left = "|>"
    separator_right = "<|"
    reboot = "Reboot"
    heatmap_file = "heatmap.txt"


class Training:
    def __init__(self):
        self.heatmap = None
        self.heatmap_button = None
        self.key_number = None
        self.key_need_to_pres = None
        self.block = None
        self.window = None
        self.statistics_file = None
        self.file = None
        self.start_message = None
        self.start_button = None
        self.you_best_time = None
        self.start_button = None
        self.text = None
        self.result_string = None
        self.substring = None
        self.current_passed_number = None
        self.statistics_str = None
        self.start_time = None
        self.reboot_button = None
        self.result_time = None
        self.result_time_label = None

    def print_result_time(self):
        self.result_time_label = tk.Label(text = result_time, 
                                          font = getattr(Default, "font_settings")) 
        self.result_time_label.pack()

    def initialize_window(self):
        self.window = tk.Tk()
        self.window.title(getattr(Default, "title_message"))
        self.window.geometry("500x400")

    def initialize_start_message(self):
        self.start_message = tk.Label(text = getattr(Default, "start_message"), 
                                 font = getattr(Default, "font_settings"))
        self.start_message.pack()

    def show_heat_map(self):
        result_string = ""
        for [i, j, k] in self.heatmap:
            result_string += i + ' ' + j + ' ' + k + ' ' + float(int(j) / int(k)) + '%\n'
        result = tk.Label(text = result_string, font = getattr(Default, "font_settings"))
        result.pack()

#    def initialize_heat_map_button(self):
#        self.heatmap = []
#        self.heatmap_button = tk.Button(text = getattr(Default, "heat_map_button_text"), 
#                                        font = getattr(Default, "font_settings"),
#                                        command = self.show_heat_map)

    def initialize_start_button(self):
        self.start_button = tk.Button(text = getattr(Default, "button_message"), 
                                 command=self.start_of_training)
        self.start_button.pack()

    def initialize_reboot_button(self):
        self.reboot_button = tk.Button(text = getattr(Default, "reboot"), 
                                 command=self.reboot_training)
        self.reboot_button.pack()

    def initialize_statistics_message(self):
        self.statistics_file = open(getattr(Default, "statistics_file"), 'r')
        self.statistics_str = self.statistics_file.read()
        statistics_message = (
            getattr(Default, "statistics_message") + self.statistics_str)
        self.you_best_time = tk.Label(text = statistics_message, 
                                 font = getattr(Default, "font_settings"))
        self.you_best_time.pack()

    def reboot_training(self):
        self.window.destroy()
        pygame.mixer.music.stop()#getattr(Default, "music_for_traine"))
        self.main_window()

    def main_window(self):
        self.initialize_window()
        self.initialize_start_message()
        self.initialize_start_button()
        self.initialize_reboot_button()
        self.initialize_statistics_message()
#        self.initialize_heat_map_button()

    def print_ready_steady_go_message(self, message, message_time):
        my_message = tk.Label(text = message, 
                              font = getattr(Default, "font_settings"))
        my_message.pack()
        self.window.update()
        time.sleep(message_time)
        my_message.destroy()
        self.window.update()

    def continue_key(self, entry = None):
        self.key_number += 1
        if entry.char == self.key_need_to_pres:
            self.block = False

    def funny_mode(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(getattr(Default, "music_for_traine"))
        pygame.mixer.music.play()
        self.print_ready_steady_go_message(getattr(Default, "ready_message"), 
                                      getattr(Default, "ready_time"))
        self.print_ready_steady_go_message(getattr(Default, "steady_message"), 
                                      getattr(Default, "steady_time"))
        self.print_ready_steady_go_message(getattr(Default, "go_message"), 
                                      getattr(Default, "go_time"))

    def get_percent_statistics(self):
        return round(self.current_passed_number / self.key_number, 2)

    def start_of_training(self):
        self.start_button.destroy()
        self.start_message.destroy()
        self.window.update()
        self.file = (open(getattr(Default, "source_file_name"), 'r').read())
        if getattr(Default, "funny_mode_value") == "on":
            self.funny_mode()

        self.main_training()

    def main_training(self):
        self.start_time = time.time()
        size = int(getattr(Default, "block_size"))
        for i in range((len(self.file) + size - 1) // size):
            left_border = i * getattr(Default, "block_size")
            right_border = min(len(self.file), (i + 1) * getattr(Default, "block_size"))
            self.substring = self.file[left_border: right_border]
            self.text = tk.Label(
                text = getattr(Default, "separator_left") + 
                       self.substring + 
                       getattr(Default, "separator_right"),
                font = getattr(Default, "font_settings"))
            self.text.pack()
            self.result_string = ""
            self.key_number = 0
            self.one_iteration(i)
            self.text.destroy()
        end_time = time.time()

        self.result_time = end_time - self.start_time
        print(self.result_time)
        if (self.result_time < float(self.statistics_str) or len(self.statistics_file.read()) == 0):
            self.statistics_file.close()
            self.statistics_file = open(getattr(Default, "statistics_file"), 'w')
            self.statistics_file.write(str(self.result_time))
            self.statistics_file.close()
            self.statistics_file = open(getattr(Default, "statistics_file"), 'r')
    
    def print_statistics(self, i, j):
        self.current_passed_number = i * getattr(Default, "block_size") + j
        statistics_text = getattr(Default, "current_statistcs_message")
        statistics_text += str(self.current_passed_number) 
        statistics_text += '/' + str(self.key_number)
        if self.key_number != 0:
            statistics_text += (' ' + str(self.get_percent_statistics()) + "%")
        statistics_text += " time -> "
        statistics_text += str(math.trunc(time.time() - self.start_time))
        self.statistics = tk.Label(text = statistics_text, 
                              font = getattr(Default, "font_settings"))
        self.statistics.pack()
        self.window.update()

    def one_iteration(self, i):
        for j in range(len(self.substring) - 1):
            result_message = tk.Label(text = self.result_string, 
                                      font = getattr(Default, "font_settings"))
            result_message.pack()
            self.key_need_to_pres = self.substring[j]
            self.block = True
            while self.block:
                self.window.bind_all("<KeyPress>", self.continue_key)
                self.print_statistics(i, j)
                time.sleep(getattr(Default, "sleep_time"))
                self.statistics.destroy()
            self.result_string += self.substring[j]
            result_message.destroy()
        self.text.destroy()

def main():
    my_traininig = Training()
    my_traininig.main_window()
    my_traininig.window.mainloop()

main()
