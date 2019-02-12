from tkinter import *
from shop_database import create_database


def add():
    pass


main_window = Tk()
MENU_LIST = ["Жидкость", "menu 2", "menu 3", "menu 4", "menu 5", "menu 6", "menu 7", "menu 8", "menu 9", "menu 10"]

# CONFIGURE MAIN WINDOW
main_window.title(u"Vape Shop app")
main_window.configure(background="#49464c")
main_window.geometry("800x600")

HELLO_USER = Label(main_window,
                   background="#1c0f21",
                   height=4,
                   text="Vape shop app\nPowered by biv184",
                   fg="orange"
                   ).grid(row=0, column=0, columnspan=5, sticky="we")

Grid.columnconfigure(main_window, 0, weight=1)
EMPTY_SLOT = Frame(main_window,
                   background="#1c0f21",
                   ).grid(row=0, column=5, sticky="wnse")
RIGHT_MENU = Listbox(main_window,
                     background="#312b38",
                     foreground="orange",
                     font="Arial 10",
                     width=25, relief=FLAT,
                     highlightthickness=0
                     )

for i in MENU_LIST:
    RIGHT_MENU.insert(END, i)

RIGHT_MENU.grid(row=1, column=5, sticky="ns", rowspan=5)

Grid.rowconfigure(main_window, 1, weight=1)

ID_LABEL = Label(main_window, text="id",
                 background="#49464c",
                 relief=GROOVE,
                 foreground="orange"
                 ).grid(row=1, column=0, sticky="nwe")
Grid.rowconfigure(main_window, 1, weight=1)

NAME_LABEL = Label(main_window, text="name",
                   background="#49464c",
                   relief=GROOVE,
                   foreground="orange"
                   ).grid(row=1, column=1, sticky="nwe")
Grid.columnconfigure(main_window, 1, weight=2)

PRICE_LABEL = Label(main_window, text="price",
                    background="#49464c",
                    relief=GROOVE,
                    foreground="orange"
                    ).grid(row=1, column=2, sticky="nwe")
Grid.columnconfigure(main_window, 2, weight=1)

AMOUNT_LABEL = Label(main_window, text="amount",
                     background="#49464c",
                     relief=GROOVE,
                     foreground="orange"
                     ).grid(row=1, column=3, sticky="nwe", columnspan=2)
Grid.columnconfigure(main_window, 3, weight=1)

INFO_LABEL = Label(main_window, text="Insertion into database",
                   background="#1c0f21",
                   foreground="orange"
                   ).grid(row=3, column=0, columnspan=5, sticky="swe")
Grid.rowconfigure(main_window, 3, weight=1)


name_entry = Entry(main_window, text="name", width=10, background="gray", justify=CENTER
                   ).grid(row=4, column=1, sticky="swe", padx=5)
price_entry = Entry(main_window, text="price", width=6, background="gray", justify=CENTER
                    ).grid(row=4, column=2, sticky="swe", padx=5)
amount_entry = Entry(main_window, text="amount", width=10, background="gray", justify=CENTER
                     ).grid(row=4, column=3, sticky="swe", padx=5)
ADD_BTN = Button(main_window, text="add",
                 background="gray",
                 foreground="black"
                 ).grid(row=4, column=4, sticky="swe")
BOTTOM_EMPTY = Label(main_window, background="#49464c", height=1
                     ).grid(row=5, column=0, columnspan=5, sticky="nwe")


main_window.mainloop()
