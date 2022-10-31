from tkinter import *
from sql_interface import DbChinook
from logic import Search_engine

class Window(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = DbChinook()
        self.engine = Search_engine(self.db)
        self.create_widgets()
    def create_widgets(self):
        """Вікно наповнюється віджетами"""
        Label(self, text="Введіть частину назви треку:").grid(
            row=0, column=0, 
        )
    def search_track(self):
        """Пошук треків за назвою треку, або за автором
        або за жанром, в залежності від обраного режиму 
        radiobutton 
        """
        self.engine.select_name_tracks(text)
    
    def click_track(self):
        """Добуває детальну інформацію про обраний 
        трек
        """
        pass




if __name__=="__main__":
    root  = Window()
    root.geometry =("600x400")
    root.mainloop()