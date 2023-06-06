from PIL import Image, ImageTk
import customtkinter

class Light(customtkinter.CTkFrame):
    def __init__(self, controller):
      super().__init__()
      self.controller = controller
      self.config(bg="#072e0a", fg_color="#072e0a")
      self.create_widgets()

    def create_widgets(self):
      self.grid_columnconfigure(1, weight=1)
      self.min_value_1 = 0
      self.min_value_2 = 0
      self.value = 50
      self.max_value_1 = 12
      self.max_value_2 = 12
      self.get_images()
      self.create_first_row()
      self.create_max_frame_row()
      self.create_min_frame_row()
      self.create_middle_frame()
      self.create_time_row()
      self.increase_max_val_1()
      self.increase_max_val_2()
      self.increase_min_val_1()
      self.increase_min_val_2()
      self.increase_val()

    def get_images(self):
      self.up_arrow = ImageTk.PhotoImage(Image.open("images/light/down_arrow.png").resize((20, 20)).rotate(180))
      self.down_arrow = ImageTk.PhotoImage(Image.open("images/light/down_arrow.png").resize((20, 20)))
      self.right_arrow = ImageTk.PhotoImage(Image.open("images/light/down_arrow.png").resize((20, 20)).rotate(90))
      self.left_arrow = ImageTk.PhotoImage(Image.open("images/light/down_arrow.png").resize((20, 20)).rotate(270))
      self.up_arrow_big = ImageTk.PhotoImage(Image.open("images/light/down_arrow.png").resize((50, 40)).rotate(180))
      self.down_arrow_big = ImageTk.PhotoImage(Image.open("images/light/down_arrow.png").resize((50, 40)))
      self.back_img =  ImageTk.PhotoImage(Image.open("images/light/back.png").resize((40, 40)))
      self.check_img =  ImageTk.PhotoImage(Image.open("images/light/check_mark.png").resize((40, 40)))
      self.sunrise = ImageTk.PhotoImage(Image.open("images/light/sunrise.png").resize((40, 40)))
      self.light_image = ImageTk.PhotoImage(Image.open("images/light/sun.png").resize((20, 20)))
      self.sunset = ImageTk.PhotoImage(Image.open("images/light/sunset.png").resize((40, 40)))
      self.gap_image = ImageTk.PhotoImage(Image.open("images/light/gap.jpeg").resize((80,5)))

    def create_first_row(self):
      self.back_btn = customtkinter.CTkButton(self, image=self.back_img, text="", command=self.back_to_main, bg_color="#072e0a",  hover_color="#6fb574", fg_color="#072e0a", border_width=0, width=10)
      self.back_btn.grid(row=0, column=0, sticky="w", padx=10, pady=10)  

      self.label = customtkinter.CTkLabel(self, text="Light", bg_color="#072e0a", fg_color="#072e0a", text_font=("Arial", 23, "bold"), text_color="white")
      self.label.grid(row=0, column=1, sticky="nsew", padx=0, pady=10)
      self.check_btn = customtkinter.CTkButton(self, image=self.check_img, text="", command=self.back_to_main, bg_color="#072e0a",  hover_color="#6fb574", fg_color="#072e0a", border_width=0, width=10)
      self.check_btn.grid(row=0, column=2, sticky="e", padx=10, pady=10)  

    def create_max_frame_row(self):
      self.max_frame = customtkinter.CTkFrame(self, bg_color="#072e0a", fg_color="#1c5b20", corner_radius=10)
      self.max_frame.grid(row=2, column=2, sticky="nsew", padx=10, pady=10, ipadx=2, ipady=2)

      self.min_label = customtkinter.CTkLabel(self.max_frame, text="Sunset", bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 15, "bold"), text_color="white", width=80)
      self.min_label.grid(row=0, column=0, sticky="nsew", padx=0, pady=10, columnspan=3)
      
      self.left_btn_1 = customtkinter.CTkButton(self.max_frame, image=self.left_arrow, text="", hover_color="#6fb574", command=self.decrease_max_val_1, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.left_btn_1.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
      self.max_value_lbl_1 = customtkinter.CTkLabel(self.max_frame, text=f"{self.max_value_1}:00am", bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 15, "bold"), text_color="white", width=10)
      self.max_value_lbl_1.grid(row=1, column=1, sticky="nsew", padx=0, pady=0)
      self.right_btn_1 = customtkinter.CTkButton(self.max_frame, image=self.right_arrow, text="", hover_color="#6fb574", command=self.increase_max_val_1, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.right_btn_1.grid(row=1, column=2, sticky="nsew", padx=0, pady=0)

      self.gap = customtkinter.CTkLabel(self.max_frame, text="", image=self.gap_image, bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 25, "bold"), text_color="white", width=10)
      self.gap.grid(row=2, column=0, sticky="nsew", padx=0, pady=5,columnspan=3)

      self.left_btn_2 = customtkinter.CTkButton(self.max_frame, image=self.left_arrow, text="", hover_color="#6fb574", command=self.decrease_max_val_2, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.left_btn_2.grid(row=3, column=0, sticky="nsew", padx=0, pady=0)
      self.max_value_lbl_2 = customtkinter.CTkLabel(self.max_frame, text=f"{self.max_value_2}:00am", bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 15, "bold"), text_color="white", width=10)
      self.max_value_lbl_2.grid(row=3, column=1, sticky="nsew", padx=0, pady=0)
      self.right_btn_2 = customtkinter.CTkButton(self.max_frame, image=self.right_arrow, text="", hover_color="#6fb574", command=self.increase_max_val_2, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.right_btn_2.grid(row=3, column=2, sticky="nsew", padx=0, pady=0)

      self.sunset_label = customtkinter.CTkLabel(self.max_frame, text="", image=self.sunset, bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 25, "bold"), text_color="white", width=80)
      self.sunset_label.grid(row=4, column=1, sticky="nsew", padx=0, pady=0)

    def create_min_frame_row(self):
      self.min_frame = customtkinter.CTkFrame(self, bg_color="#072e0a", fg_color="#1c5b20", corner_radius=10)
      self.min_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10, ipadx=2, ipady=2)

      self.min_label = customtkinter.CTkLabel(self.min_frame, text="Sunrise", bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 15, "bold"), text_color="white", width=80)
      self.min_label.grid(row=0, column=0, sticky="nsew", padx=0, pady=10, columnspan=3)

      self.left_btn_1 = customtkinter.CTkButton(self.min_frame, image=self.left_arrow, text="", hover_color="#6fb574", command=self.decrease_min_val_1, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.left_btn_1.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
      self.min_value_lbl_1 = customtkinter.CTkLabel(self.min_frame, text=f"{self.min_value_1}:00am", bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 15, "bold"), text_color="white", width=10)
      self.min_value_lbl_1.grid(row=1, column=1, sticky="nsew", padx=0, pady=0)
      self.right_btn_1 = customtkinter.CTkButton(self.min_frame, image=self.right_arrow, text="", hover_color="#6fb574", command=self.increase_min_val_1, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.right_btn_1.grid(row=1, column=2, sticky="nsew", padx=0, pady=0)

      self.gap = customtkinter.CTkLabel(self.min_frame, text="", image=self.gap_image, bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 25, "bold"), text_color="white", width=10)
      self.gap.grid(row=2, column=0, sticky="nsew", padx=0, pady=5,columnspan=3)
      
      self.left_btn_2 = customtkinter.CTkButton(self.min_frame, image=self.left_arrow, text="", hover_color="#6fb574", command=self.decrease_min_val_2, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.left_btn_2.grid(row=3, column=0, sticky="nsew", padx=0, pady=0)
      self.min_value_lbl_2 = customtkinter.CTkLabel(self.min_frame, text=f"{self.min_value_2}:00am", bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 15, "bold"), text_color="white", width=10)
      self.min_value_lbl_2.grid(row=3, column=1, sticky="nsew", padx=0, pady=0)
      self.right_btn_2 = customtkinter.CTkButton(self.min_frame, image=self.right_arrow, text="", hover_color="#6fb574", command=self.increase_min_val_2, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.right_btn_2.grid(row=3, column=2, sticky="nsew", padx=0, pady=0)
      
      self.sunrise_label = customtkinter.CTkLabel(self.min_frame, text="", image=self.sunrise, bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 25, "bold"), text_color="white", width=10)
      self.sunrise_label.grid(row=4, column=1, sticky="nsew", padx=0, pady=0)

    def create_middle_frame(self):
      self.mid_frame = customtkinter.CTkFrame(self, bg_color="#072e0a", fg_color="#1c5b20", corner_radius=10)
      self.mid_frame.grid(row=2, column=1, padx=10, pady=10)

      self.up_btn = customtkinter.CTkButton(self.mid_frame, image=self.up_arrow_big, text="", hover_color="#6fb574", command=self.increase_val, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.up_btn.grid(row=1, column=0, sticky="nsew", padx=5, pady=15)
      self.value_frame = customtkinter.CTkFrame(self.mid_frame, bg_color="#1c5b20", fg_color="#1c5b20", corner_radius=10, width=100)
      self.value_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=0)
      self.value_lbl = customtkinter.CTkLabel(self.value_frame, text=f" {self.value}%", bg_color="#1c5b20", fg_color="#1c5b20", text_font=("Arial", 27, "bold"), text_color="white", width=10)
      self.value_lbl.grid(row=2, column=0, sticky="nsew", padx=0, pady=0)
      self.value_image = customtkinter.CTkLabel(self.value_frame, image=self.light_image, text="", bg_color="#1c5b20", fg_color="#1c5b20", width=10)
      self.value_image.grid(row=2, column=1, sticky="nsew", padx=0, pady=0)
      self.down_btn = customtkinter.CTkButton(self.mid_frame, image=self.down_arrow_big, text="", hover_color="#6fb574", command=self.decrease_val, bg_color="#1c5b20", fg_color="#1c5b20", border_width=0, width=10)
      self.down_btn.grid(row=3, column=0, sticky="nsew", padx=5, pady=15)

    def create_time_row(self):
      self.time_label = customtkinter.CTkLabel(self, text="4:00 PM", bg_color="#072e0a", fg_color="#072e0a", text_font=("Arial", 13, "bold"), text_color="white", width=80)
      self.time_label.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

    def button_click(self):
      print("button clicked")

    def back_to_main(self):
      self.controller.show_frame("main")
    
    def increase_min_val_1(self):
      if self.min_value_1 < 11:
        self.min_value_1 += 1
        self.min_value_lbl_1.config(text=f"{self.min_value_1:02}:00am")
      elif self.min_value_1 == 11:
        self.min_value_1 += 1
        self.min_value_lbl_1.config(text=f"{self.min_value_1:02}:00pm")
      elif self.min_value_1 < 23 and self.min_value_1 > 0:
        self.min_value_1 += 1
        self.min_value_lbl_1.config(text=f"{self.min_value_1-12:02}:00pm")
      elif self.min_value_1 == 23:
        self.min_value_1 = 0
        self.min_value_lbl_1.config(text=f"{self.min_value_1:02}:00am")

    def decrease_min_val_1(self):
      if self.min_value_1 > 12:
        self.min_value_1 -= 1
        self.min_value_lbl_1.config(text=f"{self.min_value_1-12:02}:00pm")
      elif self.min_value_1 == 12:
        self.min_value_1 -= 1
        self.min_value_lbl_1.config(text=f"{self.min_value_1:02}:00am")
      elif self.min_value_1 < 12 and self.min_value_1 > 0:
        self.min_value_1 -= 1
        self.min_value_lbl_1.config(text=f"{self.min_value_1:02}:00am")
      elif self.min_value_1 == 0:
        self.min_value_1 = 23
        self.min_value_lbl_1.config(text=f"{self.min_value_1-12:02}:00pm")

    def increase_min_val_2(self):
      if self.min_value_2 < 11:
        self.min_value_2 += 1
        self.min_value_lbl_2.config(text=f"{self.min_value_2:02}:00am")
      elif self.min_value_2 == 11:
        self.min_value_2 += 1
        self.min_value_lbl_2.config(text=f"{self.min_value_2:02}:00pm")
      elif self.min_value_2 < 23 and self.min_value_2 > 0:
        self.min_value_2 += 1
        self.min_value_lbl_2.config(text=f"{self.min_value_2-12:02}:00pm")
      elif self.min_value_2 == 23:
        self.min_value_2 = 0
        self.min_value_lbl_2.config(text=f"{self.min_value_2:02}:00am")

    def decrease_min_val_2(self):
      if self.min_value_2 > 12:
        self.min_value_2 -= 1
        self.min_value_lbl_2.config(text=f"{self.min_value_2-12:02}:00pm")
      elif self.min_value_2 == 12:
        self.min_value_2 -= 1
        self.min_value_lbl_2.config(text=f"{self.min_value_2:02}:00am")
      elif self.min_value_2 < 12 and self.min_value_2 > 0:
        self.min_value_2 -= 1
        self.min_value_lbl_2.config(text=f"{self.min_value_2:02}:00am")
      elif self.min_value_2 == 0:
        self.min_value_2 = 23
        self.min_value_lbl_2.config(text=f"{self.min_value_2-12:02}:00pm")

    def increase_max_val_1(self):
      if self.max_value_1 < 11:
        self.max_value_1 += 1
        self.max_value_lbl_1.config(text=f"{self.max_value_1:02}:00am")
      elif self.max_value_1 == 11:
        self.max_value_1 += 1
        self.max_value_lbl_1.config(text=f"{self.max_value_1:02}:00pm")
      elif self.max_value_1 < 23 and self.max_value_1 > 0:
        self.max_value_1 += 1
        self.max_value_lbl_1.config(text=f"{self.max_value_1-12:02}:00pm")
      elif self.max_value_1 == 23:
        self.max_value_1 = 0
        self.max_value_lbl_1.config(text=f"{self.max_value_1:02}:00am")


    def decrease_max_val_1(self):
      if self.max_value_1 > 12:
        self.max_value_1 -= 1
        self.max_value_lbl_1.config(text=f"{self.max_value_1-12:02}:00pm")
      elif self.max_value_1 == 12:
        self.max_value_1 -= 1
        self.max_value_lbl_1.config(text=f"{self.max_value_1:02}:00am")
      elif self.max_value_1 < 12 and self.max_value_1 > 0:
        self.max_value_1 -= 1
        self.max_value_lbl_1.config(text=f"{self.max_value_1:02}:00am")
      elif self.max_value_1 == 0:
        self.max_value_1 = 23
        self.max_value_lbl_1.config(text=f"{self.max_value_1-12:02}:00pm")
    
    def increase_max_val_2(self):
      if self.max_value_2 < 11:
        self.max_value_2 += 1
        self.max_value_lbl_2.config(text=f"{self.max_value_2:02}:00am")
      elif self.max_value_2 == 11:
        self.max_value_2 += 1
        self.max_value_lbl_2.config(text=f"{self.max_value_2:02}:00pm")
      elif self.max_value_2 < 23 and self.max_value_2 > 0:
        self.max_value_2 += 1
        self.max_value_lbl_2.config(text=f"{self.max_value_2-12:02}:00pm")
      elif self.max_value_2 == 23:
        self.max_value_2 = 0
        self.max_value_lbl_2.config(text=f"{self.max_value_2:02}:00am")


    def decrease_max_val_2(self):
      if self.max_value_2 > 12:
        self.max_value_2 -= 1
        self.max_value_lbl_2.config(text=f"{self.max_value_2-12:02}:00pm")
      elif self.max_value_2 == 12:
        self.max_value_2 -= 1
        self.max_value_lbl_2.config(text=f"{self.max_value_2:02}:00am")
      elif self.max_value_2 < 12 and self.max_value_2 > 0:
        self.max_value_2 -= 1
        self.max_value_lbl_2.config(text=f"{self.max_value_2:02}:00am")
      elif self.max_value_2 == 0:
        self.max_value_2 = 23
        self.max_value_lbl_2.config(text=f"{self.max_value_2-12:02}:00pm")
    
    def increase_val(self):
      if self.value < 100:
        self.value += 1
        self.value_lbl.config(text=f" {self.value:02}%")

    def decrease_val(self):
      if self.value > 0:
        self.value -= 1
        self.value_lbl.config(text=f" {self.value:02}%")