from tkinter import *
from shop_database import create_database

def add():
    pass

main_window = Tk()
MENU_LIST = ["Жидкость", "menu 2", "menu 3", "menu 4", "menu 5", "menu 6", "menu 7", "menu 8", "menu 9", "menu 10"]

# CONFIGURE MAIN WINDOW
main_window.title(u"Vape Shop app")
main_window.configure(background="#49464c")

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

RIGHT_MENU.grid(row=1, column=5, sticky="ns", rowspan=3)

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

id_entry = Entry(main_window, text="id", width=6, background="gray").grid(row=3, column=0, sticky="swe")
name_entry = Entry(main_window, text="name", width=10, background="gray").grid(row=3, column=1, sticky="swe")
price_entry = Entry(main_window, text="price", width=6, background="gray").grid(row=3, column=2, sticky="swe")
amount_entry = Entry(main_window, text="amount", width=10, background="gray").grid(row=3, column=3, sticky="swe")
ADD_BTN = Button(main_window, text="add",
                 background="gray",
                 foreground="orange"
                 ).grid(row=3, column=4, sticky="swe")
Grid.rowconfigure(main_window, 3, weight=1)


"""

LEFT_FRAME = Frame(main_window, background="#49464c")
LEFT_FRAME.grid(row=0, column=0, sticky="nwse")


RIGHT_MENU_FRAME = Frame(main_window, bg="#312b38")
RIGHT_MENU_FRAME.grid(row=0, column=1, sticky="nes")

# CONFIGURE GREETING LABEL
HELLO_USER = Label(LEFT_FRAME, text="Vape shop app\n"
                                     "Powered by biv184", font="Arial 14")
HELLO_USER.configure(background="#1c0f21", fg="orange", height=4)
HELLO_USER.pack(side="top")


#DATA_LISTBOX = Listbox(LEFT_FRAME, selectmode=SINGLE, fg="orange", side="top")


id_entry = Entry(LEFT_FRAME, text="id", width=6).pack(side="left")
name_entry = Entry(LEFT_FRAME, text="name", width=10).pack(side="left")
price_entry = Entry(LEFT_FRAME, text="price", width=6).pack(side="left")
amount_entry = Entry(LEFT_FRAME, text="amount", width=10).pack(side="left")




RIGHT_LABEL = Label(RIGHT_MENU_FRAME, text="\n", bg="#1c0f21", height=4, font="Arial 14")

RIGHT_LISTBOX = Listbox(RIGHT_MENU_FRAME, selectmode=BROWSE, bg="#312b38", fg="orange", relief=FLAT, width=20)
RIGHT_LISTBOX.config(highlightthickness=0)

for i in MENU_LIST:
    RIGHT_LISTBOX.insert(END, i)

RIGHT_LABEL.pack(side="top", fill=X)
HELLO_USER.pack(fill=X)
RIGHT_LISTBOX.pack(side="top", expand=FALSE)
RIGHT_LISTBOX.config(font="Arial 12")
"""
main_window.mainloop()
