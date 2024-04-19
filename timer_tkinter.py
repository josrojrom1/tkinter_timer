###############
### IMPORTS ###
from tkinter import Tk, Label, Button, RIDGE
import pygame
import pyglet
import os
##################
### MAIN CLASS ###
class Timer:
    def __init__(self):
        ############################
        ### INITIALIZE VARIABLES ###
        self.hrs = 0
        self.mins = 0
        self.secs = 0
        ####################
        ### TIMER LABELS ###
        self.hours_label = Label(root, text="hours", font=("Arial", 12))
        self.minutes_label = Label(root, text="min", font=("Arial", 12))
        self.seconds_label = Label(root, text="sec", font=("Arial", 12))
        #####################
        ### TIMER DISPLAY ###
        self.display_h = Label(root, text="00", font=("Seven Segment", 52))
        self.display_m = Label(root, text="00", font=("Seven Segment", 52))
        self.display_s = Label(root, text="00", font=("Seven Segment", 52))
        #####################
        ### TIMER BUTTONS ###
        #----------------------- Start
        self.start_btn = Button(root, text="Start", width=12, height=2, font=("Arial", 12), command=lambda: (self.startTimer(), self.playSound()))
        #----------------------- Stop
        self.stop_btn = Button(root, text="Stop", width=12, height=2, font=("Arial", 12), command=lambda: (self.stopTimer(), self.playSound()))
        #----------------------- Reset
        self.reset_btn = Button(root, text="Reset", width=12, height=2, font=("Arial", 12), command=lambda: (self.resetTimer(), self.playSound()))
        #----------------------- Initial state
        self.stop_btn["state"] = "disabled"
        self.reset_btn["state"] = "disabled"
        #----------------------- Customize timer buttons
        self.customize_cake_btn = Button(root, text="Cake", font=("Arial", 9), command=lambda: self.customizeTimer(self.customize_cake_btn))
        self.customize_coffee_btn = Button(root, text="Coffee", font=("Arial", 9), command=lambda: self.customizeTimer(self.customize_coffee_btn))
        self.customize_dark_btn = Button(root, text="Dark", font=("Arial", 9), command=lambda: self.customizeTimer(self.customize_dark_btn))
        self.customize_hacker_btn = Button(root, text="Hacker", font=("Arial", 9), command=lambda: self.customizeTimer(self.customize_hacker_btn))
        self.customize_light_btn = Button(root, text="Light", font=("Arial", 9), command=lambda: self.customizeTimer(self.customize_light_btn))
        ############
        ### GRID ###
        #---------------- Labels
        self.hours_label.grid(row=0, column=0)
        self.minutes_label.grid(row=0, column=1)
        self.seconds_label.grid(row=0, column=2)
        #---------------- Display
        self.display_h.grid(row=1, column=0)
        self.display_m.grid(row=1, column=1)
        self.display_s.grid(row=1, column=2)
        #---------------- Buttons
        self.start_btn.grid(row=2, column=0)
        self.stop_btn.grid(row=2, column=1)
        self.reset_btn.grid(row=2, column=2)
        self.customize_coffee_btn.place(x=25, y=202)
        self.customize_cake_btn.place(x=75, y=202)
        self.customize_dark_btn.place(x=120, y=202)
        self.customize_hacker_btn.place(x=162, y=202)
        self.customize_light_btn.place(x=217, y=202)
        #---------------- Grid configure
        self.hours_label.grid_configure(padx=60, pady=10)
        self.minutes_label.grid_configure(padx=60, pady=10)
        self.seconds_label.grid_configure(padx=60, pady=10)
        self.start_btn.grid_configure(pady=18)
        self.stop_btn.grid_configure(pady=18)
        self.reset_btn.grid_configure(pady=18)
        #############
        ### STYLE ###
        #---------------- Display
        self.display_h.config(background=background_color, fg=font_color)
        self.display_m.config(background=background_color, fg=font_color)
        self.display_s.config(background=background_color, fg=font_color)
        #---------------- Labels
        self.hours_label.config(background=background_color, fg=font_color)
        self.minutes_label.config(background=background_color, fg=font_color)
        self.seconds_label.config(background=background_color, fg=font_color)
        #---------------- Buttons
        self.start_btn.config(background=background_color, fg=font_color, relief=RIDGE)
        self.stop_btn.config(background=background_color, fg=font_color, relief=RIDGE)
        self.reset_btn.config(background=background_color, fg=font_color, relief=RIDGE)
        #................ Cusomize buttons
        self.customize_coffee_btn.config(background=background_color, fg=font_color, relief=RIDGE)
        self.customize_cake_btn.config(background=background_color, fg=font_color, relief=RIDGE)
        self.customize_dark_btn.config(background=background_color, fg=font_color, relief=RIDGE)
        self.customize_hacker_btn.config(background=background_color, fg=font_color, relief=RIDGE)
        self.customize_light_btn.config(background=background_color, fg=font_color, relief=RIDGE)
    ############################
    ### START TIMER FUNCTION ###
    def startTimer(self):
        self.secs = self.secs + 1
        if self.secs == 60:
            self.secs = 00
            self.mins = self.mins + 1
            if self.mins ==59:
                self.mins = 00
                self.hrs = self.hrs + 1
            if self.hrs == 59:
                self.stopTimer
                pygame.mixer.music.load("resources/sounds/end_timer.wav")
                pygame.mixer.music.play(loops=0)                
        # 1000 miliseconds = 1 second
        self.contar = self.start_btn.after(1000, self.startTimer)
        self.display_s.config(text= "{0:02d}".format(self.secs))
        self.display_m.config(text= "{0:02d}".format(self.mins))
        self.display_h.config(text= "{0:02d}".format(self.hrs))
        self.start_btn["state"] = "disabled"
        self.stop_btn["state"] = "normal"
        self.reset_btn["state"] = "normal"
    ###########################
    ### STOP TIMER FUNCTION ###
    def stopTimer(self):
            self.start_btn.after_cancel(self.contar)
            self.stop_btn["state"] = "disabled"
            self.start_btn["state"] = "normal"
    ############################
    ### RESET TIMER FUNCTION ###
    def resetTimer(self):
        self.hrs = 0
        self.mins = 0
        self.secs = 0
        self.start_btn.after_cancel(self.contar)	
        self.display_s.config(text="00")
        self.display_m.config(text="00")
        self.display_h.config(text="00")
        self.stop_btn["state"] = "disabled"
        self.reset_btn["state"] = "disabled"
        self.start_btn["state"] = "normal" 
    ###########################
    ### PLAY SOUND FUNCTION ###
    def playSound(self):
        pygame.mixer.music.load("resources/sounds/click.wav")
        pygame.mixer.music.play(loops=0)
    ################################
    ### CUSTOMIZE TIMER FUNCTION ###
    def customizeTimer(self, button_pressed):
        #------------------------- Cofee theme
        if button_pressed == self.customize_coffee_btn:
            self.display_h.config(background=brown_color_light, fg=brown_color_dark)
            self.display_m.config(background=brown_color_light, fg=brown_color_dark)
            self.display_s.config(background=brown_color_light, fg=brown_color_dark)
            self.hours_label.config(background=brown_color_light, fg=brown_color_dark)
            self.minutes_label.config(background=brown_color_light, fg=brown_color_dark)
            self.seconds_label.config(background=brown_color_light, fg=brown_color_dark)
            self.start_btn.config(background=brown_color_light, fg=brown_color_dark)
            self.stop_btn.config(background=brown_color_light, fg=brown_color_dark)
            self.reset_btn.config(background=brown_color_light, fg=brown_color_dark)
            self.customize_coffee_btn.config(background=brown_color_light, fg=brown_color_dark)
            self.customize_cake_btn.config(background=brown_color_light, fg=brown_color_dark)
            self.customize_hacker_btn.config(background=brown_color_light, fg=brown_color_dark)
            self.customize_dark_btn.config(background=brown_color_light, fg=brown_color_dark)
            self.customize_light_btn.config(background=brown_color_light, fg=brown_color_dark)
            root.config(bg=brown_color_light)
        #------------------------- Cake theme
        if button_pressed == self.customize_cake_btn:
            self.display_h.config(background=pink_color_1, fg=blue_color_1)
            self.display_m.config(background=pink_color_1, fg=blue_color_1)
            self.display_s.config(background=pink_color_1, fg=blue_color_1)
            self.hours_label.config(background=pink_color_1, fg=background_color)
            self.minutes_label.config(background=pink_color_1, fg=background_color)
            self.seconds_label.config(background=pink_color_1, fg=background_color)
            self.start_btn.config(background=pink_color_1, fg=background_color)
            self.stop_btn.config(background=pink_color_1, fg=background_color)
            self.reset_btn.config(background=pink_color_1, fg=background_color)
            self.customize_coffee_btn.config(background=pink_color_1, fg=background_color)
            self.customize_cake_btn.config(background=pink_color_1, fg=background_color)
            self.customize_hacker_btn.config(background=pink_color_1, fg=background_color)
            self.customize_dark_btn.config(background=pink_color_1, fg=background_color)
            self.customize_light_btn.config(background=pink_color_1, fg=background_color)
            root.config(bg=pink_color_1)
        #------------------------- Dark theme
        if button_pressed == self.customize_dark_btn:
            self.display_h.config(background=background_color, fg=font_color)
            self.display_m.config(background=background_color, fg=font_color)
            self.display_s.config(background=background_color, fg=font_color)
            self.hours_label.config(background=background_color, fg=font_color)
            self.minutes_label.config(background=background_color, fg=font_color)
            self.seconds_label.config(background=background_color, fg=font_color)
            self.start_btn.config(background=background_color, fg=font_color)
            self.stop_btn.config(background=background_color, fg=font_color)
            self.reset_btn.config(background=background_color, fg=font_color)
            self.customize_coffee_btn.config(background=background_color, fg=font_color)
            self.customize_cake_btn.config(background=background_color, fg=font_color)
            self.customize_hacker_btn.config(background=background_color, fg=font_color)
            self.customize_dark_btn.config(background=background_color, fg=font_color)
            self.customize_light_btn.config(background=background_color, fg=font_color)
            root.config(bg=background_color)
        #------------------------- Hacker theme
        if button_pressed == self.customize_hacker_btn:    
            self.display_h.config(background=background_color, fg=hacker_color)
            self.display_m.config(background=background_color, fg=hacker_color)
            self.display_s.config(background=background_color, fg=hacker_color)
            self.hours_label.config(background=background_color, fg=hacker_color)
            self.minutes_label.config(background=background_color, fg=hacker_color)
            self.seconds_label.config(background=background_color, fg=hacker_color)
            self.start_btn.config(background=background_color, fg=hacker_color)
            self.stop_btn.config(background=background_color, fg=hacker_color)
            self.reset_btn.config(background=background_color, fg=hacker_color)
            self.customize_coffee_btn.config(background=background_color, fg=hacker_color)
            self.customize_cake_btn.config(background=background_color, fg=hacker_color)
            self.customize_hacker_btn.config(background=background_color, fg=hacker_color)
            self.customize_dark_btn.config(background=background_color, fg=hacker_color)
            self.customize_light_btn.config(background=background_color, fg=hacker_color)
            root.config(bg=background_color)
        #------------------------- Light theme
        if button_pressed == self.customize_light_btn:
            self.display_h.config(background=font_color, fg=background_color)
            self.display_m.config(background=font_color, fg=background_color)
            self.display_s.config(background=font_color, fg=background_color)
            self.hours_label.config(background=font_color, fg=background_color)
            self.minutes_label.config(background=font_color, fg=background_color)
            self.seconds_label.config(background=font_color, fg=background_color)
            self.start_btn.config(background=font_color, fg=background_color)
            self.stop_btn.config(background=font_color, fg=background_color)
            self.reset_btn.config(background=font_color, fg=background_color)
            self.customize_coffee_btn.config(background=font_color, fg=background_color)
            self.customize_cake_btn.config(background=font_color, fg=background_color)
            self.customize_hacker_btn.config(background=font_color, fg=background_color)
            self.customize_dark_btn.config(background=font_color, fg=background_color)
            self.customize_light_btn.config(background=font_color, fg=background_color)
            root.config(bg=font_color)
        
if __name__ == "__main__":
    os.system('clear')
    ####################
    ### COLOR SCHEMA ###
    background_color = "#313338"
    hacker_color = "#3CF317"
    font_color = "#FFFFFF"
    pink_color_1 = "#FEF1FF"
    blue_color_1 = "#31EEE6"
    brown_color_dark = "#6C4C0E"
    brown_color_light = "#FFDB96"
    ###########################
    ### MAIN FRAME SETTINGS ###
    root = Tk()
    root.resizable(False,False)
    root.geometry("475x240")
    root.config(bg=background_color)
    root.title("Timer with tkinter")
    root.iconbitmap("resources/images/icon.ico")
    pygame.mixer.init()
    # Custom font
    pyglet.font.add_file('resources/fonts/Seven Segment.ttf')
    ############################
    ### TIMER CLASS INSTANCE ###
    root_instance = Timer()
    #################
    ### MAIN LOOP ###
    root.mainloop()