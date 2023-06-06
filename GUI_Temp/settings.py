from PIL import Image, ImageTk
import customtkinter

class Settings(customtkinter.CTkFrame):
    def __init__(self, controller):
      super().__init__()
      self.controller = controller
      self.config(bg="#072e0a", fg_color="#072e0a")
      self.create_widgets()

    def create_widgets(self):
      # self.grid_columnconfigure(0, weight=1)
      self.grid_columnconfigure(1, weight=1)
      self.grid_columnconfigure(2, weight=1)
      
      self.get_images()
      self.create_first_row()
      self.create_buttons_frame()
      self.create_settings_frame()
      self.create_time_row()


    def get_images(self):
      self.up_arrow = ImageTk.PhotoImage(Image.open("images/temp/down_arrow.png").resize((20, 20)).rotate(180))
      self.down_arrow = ImageTk.PhotoImage(Image.open("images/temp/down_arrow.png").resize((20, 20)))
      self.up_arrow_big = ImageTk.PhotoImage(Image.open("images/temp/down_arrow.png").resize((50, 40)).rotate(180))
      self.down_arrow_big = ImageTk.PhotoImage(Image.open("images/temp/down_arrow.png").resize((50, 40)))
      self.back_img =  ImageTk.PhotoImage(Image.open("images/temp/back.png").resize((40, 40)))
      self.check_img =  ImageTk.PhotoImage(Image.open("images/temp/check_mark.png").resize((40, 40)))
      self.temp_image = ImageTk.PhotoImage(Image.open("images/temp/Thermometer icon png.png").resize((24, 70)))

    def create_first_row(self):
      self.back_btn = customtkinter.CTkButton(self, image=self.back_img, text="", hover_color="#6fb574", command=self.button_click, bg_color="#072e0a", fg_color="#072e0a", border_width=0, width=10)
      self.back_btn.grid(row=0, column=0, sticky="w", padx=10, pady=5)  

      self.label = customtkinter.CTkLabel(self, text="Settings", bg_color="#072e0a", fg_color="#072e0a", text_font=("Arial", 26, "bold"), text_color="white")
      self.label.grid(row=0, column=1, sticky="nsew", padx=0, pady=5)
      self.check_btn = customtkinter.CTkButton(self, image=self.check_img, text="", hover_color="#6fb574", command=self.button_click, bg_color="#072e0a", fg_color="#072e0a", border_width=0, width=10)
      self.check_btn.grid(row=0, column=2, sticky="e", padx=10, pady=5)  
       
    def create_buttons_frame(self):
      self.settings_frame = customtkinter.CTkFrame(self, fg_color="#1c5b20")
      self.settings_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
      self.humidity_lbl = customtkinter.CTkLabel(self.settings_frame, text="Humidity", text_font="Arial 16 bold", text_color="white", fg_color="#39823e")
      self.humidity_lbl.grid(row=0, column=0, sticky="nsew", padx=10, pady=8, ipady=5)
      self.temp_lbl = customtkinter.CTkLabel(self.settings_frame, text="Temp", text_font="Arial 16 bold", text_color="white", fg_color="#39823e")
      self.temp_lbl.grid(row=1, column=0, sticky="nsew", padx=10, pady=8, ipady=5)
      self.light_lbl = customtkinter.CTkLabel(self.settings_frame, text="Brightness", text_font="Arial 16 bold", text_color="white", fg_color="#39823e")
      self.light_lbl.grid(row=2, column=0, sticky="nsew", padx=10, pady=8, ipady=5)
      self.fan_speed = customtkinter.CTkLabel(self.settings_frame, text="Fan Speed", text_font="Arial 16 bold", text_color="white", fg_color="#39823e")
      self.fan_speed.grid(row=3, column=0, sticky="nsew", padx=10, pady=8, ipady=5)
    
    def create_settings_frame(self):
      self.settings_frame = customtkinter.CTkFrame(self, fg_color="#1c5b20")
      self.settings_frame.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=10, pady=10)
      self.humidity_switch = customtkinter.CTkSwitch(self.settings_frame, text="On/Off Mist", text_font="Arial 16", text_color="white", fg_color="#39823e", button_color="white", button_hover_color="white", progress_color="light green")
      self.humidity_switch.grid(row=0, column=0, sticky="nsew", padx=10, pady=8, ipady=5)
      self.temp_switch = customtkinter.CTkSwitch(self.settings_frame, text="On/Off Heat", text_font="Arial 16", text_color="white", fg_color="#39823e", button_color="white", button_hover_color="white", progress_color="light green")
      self.temp_switch.grid(row=1, column=0, sticky="nsew", padx=10, pady=8, ipady=5)
      # self.light_switch = customtkinter.CTkSwitch(self.settings_frame, text="On/Off Light", text_font="Arial 16", text_color="white", fg_color="#39823e", button_color="white", button_hover_color="white", progress_color="light green")
      # self.light_switch.grid(row=2, column=0, sticky="nsew", padx=10, pady=8, ipady=5)

      self.light_slider = customtkinter.CTkSlider(self.settings_frame, fg_color="#39823e", button_color="white", button_hover_color="white", progress_color="light green")
      self.light_slider.grid(row=2, column=0, sticky="nsew", padx=10, pady=8, ipady=5)
      self.fan_speed_slider = customtkinter.CTkSlider(self.settings_frame, fg_color="#39823e", button_color="white", button_hover_color="white", progress_color="light green")
      self.fan_speed_slider.grid(row=3, column=0, sticky="nsew", padx=10, pady=8, ipady=5)
    

    def create_time_row(self):
      self.time_label = customtkinter.CTkLabel(self, text="4:00 PM", bg_color="#072e0a", fg_color="#072e0a", text_font=("Arial", 13, "bold"), text_color="white", width=80)
      self.time_label.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)
    
    def button_click(self):
      self.controller.show_frame("main")
    
    def increase_min_val(self):
      if self.min_value < self.max_value:
        self.min_value += 1
        self.min_value_lbl.config(text=str(self.min_value) + "%")

    def decrease_min_val(self):
      if self.min_value > 0:
        self.min_value -= 1
        self.min_value_lbl.config(text=str(self.min_value) + "%")

    def increase_max_val(self):
      if self.max_value < 100:
        self.max_value += 1
        self.max_value_lbl.config(text=str(self.max_value) + "%")

    def decrease_max_val(self):
      if self.max_value > self.min_value:
        self.max_value -= 1
        self.max_value_lbl.config(text=str(self.max_value) + "%")
    
    def increase_val(self):
      if self.value < self.max_value:
        self.value += 1
        self.value_lbl.config(text=str(self.value) + "%")

    def decrease_val(self):
      if self.value > self.min_value:
        self.value -= 1
        self.value_lbl.config(text=str(self.value) + "%")