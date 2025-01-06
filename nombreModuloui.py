#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
import pyperclip

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "laGUI.ui"
RESOURCE_PATHS = [PROJECT_PATH]


class nombreClaseUI:
    def __init__(self, master=None):
        self.builder = pygubu.Builder()
        self.builder.add_resource_paths(RESOURCE_PATHS)
        self.builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow: tk.Toplevel = self.builder.get_object("toplevel1", master)
        self.builder.connect_callbacks(self)

        self.furigana = self.builder.get_object("entry_furigana")
        self.kanji    = self.builder.get_object("text_kanji")
        self.meaning  = self.builder.get_object("entry_meaning")

    def run(self):
        self.mainwindow.mainloop()

    def on_limpiar_button_clicked(self):
        self.furigana.delete(0, tk.END)
        self.kanji.delete("1.0", tk.END)
        self.meaning.delete(0, tk.END)

    def on_ejecutar_button_clicked(self):
        cadenaUP = self.furigana.get()
        cadenaMID = self.kanji.get("1.0",tk.END).strip()
        cadenaDOWN = self.meaning.get()

        # "<ruby>日本語<rt>にほんご</rt><rtc>japones</rtc></ruby>"
        if cadenaDOWN != "":
            cadena = f'<ruby>{cadenaMID}<rt>{cadenaUP}</rt><rtc>{cadenaDOWN}</rtc></ruby>'
        else :
            cadena = f'<ruby>{cadenaMID}<rt>{cadenaUP}</rt></ruby>'
        
        self.kanji.delete("1.0",tk.END)
        self.kanji.insert("1.0",cadena)

        pyperclip.copy(cadena)


if __name__ == "__main__":
    app = nombreClaseUI()
    app.run()
