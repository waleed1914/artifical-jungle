from tkinter import font
from PIL import Image, ImageTk
import customtkinter

class Humidity(customtkinter.CTkFrame):
    def __init__(self, controller):
      super().__init__()
      self.controller = controller
      self.config(bg="#072e0a", fg_color="#072e0a")
      self.create_widgets()

    def create_widgets(self):
      self.grid_columnconfigure(1, weight=1)
      self.min_value = 20
      self.value = 50
      self.max_value = 60
      self.get_images()
      self.create_first_row()
      self.create_max_frame_row()
      self.create_min_frame_row()
      self.create_middle_frame()
      self.create_time_row()
      self.increase_max_val()
      self.increase_min_val()
      self.increase_val()

    def get_images(self):
      self.up_arrow = ImageTk.PhotoImage(Image.open("images/humidity/down_arrow.png").resize((20, 20)).rotate(180))
      self.down_arrow = ImageTk.PhotoImage(Image.open("images/humidity/down_arrow.png").resize((20, 20)))
      self.up_arrow_big = ImageTk.PhotoImage(Image.open("images/humidity/down_arrow.png").resize((50, 40)).rotate(180))
      self.down_arrow_big = ImageTk.PhotoImage(Image.open("images/humidity/down_arrow.png").resize((50, 40)))
      self.back_img =  ImageTk.PhotoImage(Image.open("images/humidity/back.png").resize((40, 40)))
      self.check_img =  ImageTk.PhotoImage(Image.open("images/humidity/check_mark.png").resize((40, 40)))
      self.humidity_image = ImageTk.PhotoImage(Image.open("images/humidity/Water Drop icon png.png").resize((32, 50)))

    def create_first_row(self):
      self.back_btn = customtkinter.CTkButton(self, image=self.back_img, text="", hover_color="#6fb574", command=self.button_click, bg_color="#072e0a", fg_color="#072e0a", border_width=0, width=10)
      self.back_btn.grid(row=0, column=0, sticky="w", padx=10, pady=10)  

      self.label = customtkinter.CTkLabel(self, text="Humidity", bg_color="#072e0a", fg_color="#072e0a", text_font=("Arial", 26, "bold"), text_color="white")
      self.label.grid(row=0, column=1, sticky="nsew", padx=0, pady=10)
      self.check_btn = customtkinter.CTkButton(self, image=self.check_img, text="", hover_color="#6fb574", command=self.button_click, bg_color="#072e0a", fg_color="#072e0a", border_width=0, width=10)
      self.check_btn.grid(row=0, column=2, sticky="e", padx=10, pady=10)  
    

    def create_max_frame_row(self):
      self.max_frame = customtkinter.CTkFrame(self, bg_color="#072e0a", fg_color="#1c5b20", corner_radius=10)
      self.max_frame.grid(row=2, column=2, sticky="nsew", padx=10, pady=10)

      self.min_label = customtkinter.CTkLabel(self.max_frame, text="Max", bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 25, "bold"), text_color="white", width=80)
      self.min_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=0)
      self.up_btn = customtkinter.CTkButton(self.max_frame, image=self.up_arrow, text="", hover_color="#6fb574", command=self.increase_max_val, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.up_btn.grid(row=1, column=0, sticky="nsew", padx=10, pady=0)
      self.max_value_lbl = customtkinter.CTkLabel(self.max_frame, text=f"{self.max_value}%", bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 25, "bold"), text_color="white", width=10)
      self.max_value_lbl.grid(row=2, column=0, sticky="nsew", padx=10, pady=0)
      self.down_btn = customtkinter.CTkButton(self.max_frame, image=self.down_arrow, text="", hover_color="#6fb574", command=self.decrease_max_val, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.down_btn.grid(row=3, column=0, sticky="nsew", padx=10, pady=0)

    def create_min_frame_row(self):
      self.min_frame = customtkinter.CTkFrame(self, bg_color="#072e0a", fg_color="#1c5b20", corner_radius=10)
      self.min_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

      self.min_label = customtkinter.CTkLabel(self.min_frame, text="Min", bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 25, "bold"), text_color="white", width=80)
      self.min_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=0)
      self.up_btn = customtkinter.CTkButton(self.min_frame, image=self.up_arrow, text="", hover_color="#6fb574", command=self.increase_min_val, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.up_btn.grid(row=1, column=0, sticky="nsew", padx=10, pady=0)
      self.min_value_lbl = customtkinter.CTkLabel(self.min_frame, text=f"{self.min_value}%", bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 25, "bold"), text_color="white", width=10)
      self.min_value_lbl.grid(row=2, column=0, sticky="nsew", padx=10, pady=0)
      self.down_btn = customtkinter.CTkButton(self.min_frame, image=self.down_arrow, text="", hover_color="#6fb574", command=self.decrease_min_val, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.down_btn.grid(row=3, column=0, sticky="nsew", padx=10, pady=0)

    def create_middle_frame(self):
      self.mid_frame = customtkinter.CTkFrame(self, bg_color="#072e0a", fg_color="#1c5b20", corner_radius=10)
      self.mid_frame.grid(row=2, column=1, padx=10, pady=10, ipady=10)

      self.up_btn = customtkinter.CTkButton(self.mid_frame, image=self.up_arrow_big, text="", hover_color="#6fb574", command=self.increase_val, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.up_btn.grid(row=1, column=0, sticky="nsew", padx=10, pady=0)
      self.value_frame = customtkinter.CTkFrame(self.mid_frame, bg_color="#1c5b20", fg_color="#1c5b20", corner_radius=10)
      self.value_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=0)
      self.value_lbl = customtkinter.CTkLabel(self.value_frame, text=f"{self.value}%", bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 35, "bold"), text_color="white", width=10)
      self.value_lbl.grid(row=2, column=0, sticky="nsew", padx=0, pady=0)
      self.value_image = customtkinter.CTkLabel(self.value_frame, image=self.humidity_image, text="", bg_color="#1c5b20", fg_color="#1c5b20", width=10)
      self.value_image.grid(row=2, column=1, sticky="nsew", padx=0, pady=0)
      self.down_btn = customtkinter.CTkButton(self.mid_frame, image=self.down_arrow_big, text="", hover_color="#6fb574", command=self.decrease_val, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.down_btn.grid(row=3, column=0, sticky="nsew", padx=10, pady=0)

    def create_time_row(self):
      self.time_label = customtkinter.CTkLabel(self, text="4:00 PM", bg_color="#072e0a", fg_color="#072e0a", text_font=("Arial", 13, "bold"), text_color="white", width=80)
      self.time_label.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

    def button_click(self):
      self.controller.show_frame("main")
    
    def increase_min_val(self):
      if self.min_value < self.max_value:
        self.min_value += 1
        self.min_value_lbl.config(text=f" {self.min_value}%")

    def decrease_min_val(self):
      if self.min_value > 0:
        self.min_value -= 1
        self.min_value_lbl.config(text=f" {self.min_value}%")

    def increase_max_val(self):
      if self.max_value < 99:
        self.max_value += 1
        self.max_value_lbl.config(text=f" {self.max_value}%")
      if self.max_value == 99:
        self.max_value += 1
        self.max_value_lbl.config(text=f" {self.max_value}%")

    def decrease_max_val(self):
      if self.max_value > self.min_value:
        self.max_value -= 1
        self.max_value_lbl.config(text=f" {self.max_value}%")
    
    def increase_val(self):
      if self.value == 99:
        self.value += 1
        self.value_lbl.config(text=f" {self.value}%")
        
      elif self.value < self.max_value:
        self.value += 1
        self.value_lbl.config(text=f" {self.value}%")

    def decrease_val(self):
      if self.value > self.min_value:
        self.value -= 1
        self.value_lbl.config(text=f" {self.value}%")