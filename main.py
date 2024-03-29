from Side import Side
from UI import Main
from tkinter import *


def main():

    print("Hello world!")


if __name__ == "__main__":
    window = Tk()
    Side(window, title = "Foo", size = 2, value_matrix = [[1, 3], [1, 4]], value_number = 1)

    window.mainloop()
    #Main()
