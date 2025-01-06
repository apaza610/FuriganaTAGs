#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
from nombreModuloui import nombreClaseUI


class nombreClase(nombreClaseUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = nombreClase()
    app.run()
