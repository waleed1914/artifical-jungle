from PIL import Image, ImageTk
import customtkinter

class Main(customtkinter.CTkFrame):
    def __init__(self, controller):
      super().__init__()
      self.controller = controller
      self.config(bg="#072e0a", fg_color="#072e0a")
      self.create_widgets()


    def create_widgets(self):
      self.grid_columnconfigure(1, weight=1)
      self.grid_columnconfigure(2, weight=1)
      self.grid_rowconfigure(0, weight=1)
      
      self.create_buttons_frame()
      self.create_sensors_frame()
      self.create_ideal_val_frame()
      
    def create_buttons_frame(self):
      self.button_frame = customtkinter.CTkFrame(self, fg_color="#1c5b20")
      self.button_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
      self.humidity_btn = customtkinter.CTkButton(self.button_frame, text="Humidity", text_font="Arial 20 bold", text_color="white", hover_color="#6fb574", fg_color="#39823e", command=lambda: self.controller.show_frame("humidity"))
      self.humidity_btn.grid(row=0, column=0, sticky="nsew", padx=10, pady=13, ipady=7)
      self.temp_btn = customtkinter.CTkButton(self.button_frame, text="Temp", text_font="Arial 20 bold", text_color="white", fg_color="#39823e", hover_color="#6fb574", command=lambda: self.controller.show_frame("temp"))
      self.temp_btn.grid(row=1, column=0, sticky="nsew", padx=10, pady=13, ipady=7)
      self.light_btn = customtkinter.CTkButton(self.button_frame, text="Light", text_font="Arial 20 bold", text_color="white", fg_color="#39823e", hover_color="#6fb574", command=lambda: self.controller.show_frame("light"))
      self.light_btn.grid(row=2, column=0, sticky="nsew", padx=10, pady=13, ipady=7)
      self.setting_btn = customtkinter.CTkButton(self.button_frame, text="Setting", text_font="Arial 20 bold", text_color="white", fg_color="#39823e", hover_color="#6fb574", command=lambda: self.controller.show_frame("settings"))
      self.setting_btn.grid(row=3, column=0, sticky="nsew", padx=10, pady=13, ipady=7)

    def create_sensors_frame(self):
      self.sensors_frame = customtkinter.CTkFrame(self, fg_color="#072e0a")
      self.sensors_frame.grid(row=0, column=1, sticky="nsew")

      # configuration
      self.sensors_frame.grid_columnconfigure(0, weight=1)
      self.sensors_frame.grid_columnconfigure(1, weight=1)
      
      # containers
      self.container_1 = customtkinter.CTkFrame(self.sensors_frame, fg_color="#072e0a")
      self.container_1.grid(row=0, column=0, sticky="nsew", padx=2, pady=15)
      self.container_2 = customtkinter.CTkFrame(self.sensors_frame, fg_color="#072e0a")
      self.container_2.grid(row=1, column=0, sticky="nsew", padx=2, pady=13)
      self.container_3 = customtkinter.CTkFrame(self.sensors_frame, fg_color="#072e0a")
      self.container_3.grid(row=2, column=0, sticky="nsew", padx=2, pady=13)

      self.humidity_label = customtkinter.CTkLabel(self.container_1, text="45%", text_font="Arial 28 bold", text_color="white")
      self.humidity_label.grid(row=0, column=0, sticky="e", padx=0, pady=0)
      self.temp_label = customtkinter.CTkLabel(self.container_2, text=f"39°F", text_font="Arial 50 bold", text_color="white")
      self.temp_label.grid(row=1, column=0, sticky="e", padx=0, pady=0)
      self.light_label = customtkinter.CTkLabel(self.container_3, text="53%", text_font="Arial 25 bold", text_color="white")
      self.light_label.grid(row=2, column=0, sticky="e", padx=0, pady=0)
      self.time_label = customtkinter.CTkLabel(self.sensors_frame, text="04:50:09 pm", text_font="Arial 13", text_color="white")
      self.time_label.grid(row=3, column=0, sticky="e", padx=0, pady=25)
      # images 
      self.humidity_image = Image.open("images/main/Water Drop icon png.png").resize((20, 30))
      self.humidity_image = ImageTk.PhotoImage(self.humidity_image)
      
      self.sunrise_image = Image.open("images/main/Sun.png").resize((30, 30))
      self.sunrise_image = ImageTk.PhotoImage(self.sunrise_image)
      
      self.thermometer_image = Image.open("images/main/Thermometer icon png.png").resize((35, 100))
      self.thermometer_image = ImageTk.PhotoImage(self.thermometer_image)
      
      self.humidity_img = customtkinter.CTkLabel(self.container_1, image=self.humidity_image, width=10, height=10)
      self.humidity_img.grid(row=0, column=1, sticky="w", padx=0, pady=0)
      self.temp_img = customtkinter.CTkLabel(self.container_2, image=self.thermometer_image, width=10, height=10)
      self.temp_img.grid(row=1, column=1, sticky="w", padx=0, pady=0)
      self.light_img = customtkinter.CTkLabel(self.container_3, image=self.sunrise_image, width=10, height=10)
      self.light_img.grid(row=2, column=1, sticky="w", padx=0, pady=0)
      

    def create_ideal_val_frame(self):
      self.ideal_val_frame = customtkinter.CTkFrame(self, fg_color="#072e0a")
      self.ideal_val_frame.grid(row=0, column=2, sticky="nsew")
      self.humidity_ideal_label = customtkinter.CTkLabel(self.ideal_val_frame, text="60% - 80%", text_font="Arial 11 bold", text_color="white", width=30, fg_color="#072e0a")
      self.humidity_ideal_label.grid(row=0, column=0, sticky="nsew", padx=0, pady=20)
      self.temp_ideal_label = customtkinter.CTkLabel(self.ideal_val_frame, text="80°F - 65°F", text_font="Arial 11 bold", text_color="white", width=30, fg_color="#072e0a")
      self.temp_ideal_label.grid(row=1, column=0, sticky="nsew", padx=0, pady=40)
      self.light_ideal_label = customtkinter.CTkLabel(self.ideal_val_frame, text="8:00am-6:00pm", text_font="Arial 9 bold", text_color="white", width=30, fg_color="#072e0a")
      self.light_ideal_label.grid(row=2, column=0, sticky="nsew", padx=0, pady=25)

    def button_click(self):
      print("Button clicked")

