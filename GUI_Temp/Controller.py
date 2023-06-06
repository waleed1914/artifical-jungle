import customtkinter

from settings import Settings
from temp import Temp
from humidity import Humidity
from light import Light
from main import Main

class Controller(customtkinter.CTk):
  def __init__(self):
    super().__init__()
    self.title("GUI")
    self.geometry("480x320")
    self.config(bg="#072e0a")
    self.resizable(False, False)
    self.initialize_frames()
    self.show_frame("main")
    self.mainloop()

  def initialize_frames(self):
    main = Main(self)
    settings = Settings(self)
    temp = Temp(self)
    humidity = Humidity(self)
    light = Light(self)
    self.frames = {
      "main": main,
      "settings": settings,
      "temp": temp,
      "humidity": humidity,
      "light": light
    }

    self.rowconfigure(0, weight=1)
    self.columnconfigure(0, weight=1)
    
    for frame in self.frames.values():
      frame.grid(row=0, column=0, sticky="nsew")
    
  def show_frame(self, frame_name):
      self.next_frame = self.frames[frame_name]
      self.next_frame.tkraise()

Controller()