from tkinter import *


def menu_pick(event):
    w = event.widget
    selection = int(w.curselection()[0])
    if selection == 0:
        for t in range(0, 5):
            for widget in main_window.grid_slaves(row=3, column=t):
                widget.destroy()
            for widget in main_window.grid_slaves(row=4, column=t):
                widget.destroy()
            for widget in main_window.grid_slaves(row=5, column=t):
                widget.destroy()
        # developing new bottom widgets

        INFO_LABEL = Label(main_window, text="Вставить в базу данных",
                           background="#1c0f21",
                           foreground="orange"
                           ).grid(row=3, column=0, columnspan=6, sticky="swe")
        Grid.rowconfigure(main_window, 3, weight=1)
        id_etry = Entry(main_window, text="name", background="gray", justify=CENTER
                        ).grid(row=4, column=0, sticky="swe", padx=5)
        type_entry = Entry(main_window, text="name", background="gray", justify=CENTER
                           ).grid(row=4, column=1, sticky="swe", padx=5)
        name_entry = Entry(main_window, text="name", background="gray", justify=CENTER
                           ).grid(row=4, column=2, sticky="swe", padx=5)
        price_entry = Entry(main_window, text="price", background="gray", justify=CENTER
                            ).grid(row=4, column=3, sticky="swe", padx=5)
        amount_entry = Entry(main_window, text="amount", background="gray", justify=CENTER
                             ).grid(row=4, column=4, sticky="swe", padx=5)
        ADD_BTN = Button(main_window, text="add",
                         background="gray",
                         foreground="black"
                         ).grid(row=4, column=5, sticky="swe")
        BOTTOM_EMPTY = Label(main_window, background="#49464c", height=1
                             ).grid(row=5, column=0, columnspan=5, sticky="nwe")
    if selection == 1:
        # destruction of others bottom widgets
        for t in range(0, 6):
            for widget in main_window.grid_slaves(row=3, column=t):
                widget.destroy()
            for widget in main_window.grid_slaves(row=4, column=t):
                widget.destroy()
            for widget in main_window.grid_slaves(row=5, column=t):
                widget.destroy()
        # developing new bottom widgets
        INFO_LABEL = Label(main_window, text="Удалить из базы данных",
                           background="#1c0f21",
                           foreground="orange"
                           ).grid(row=3, column=0, columnspan=6, sticky="swe")
        Grid.rowconfigure(main_window, 3, weight=1)
        FIND_ENTRY = Entry(main_window, text="name", background="gray", justify=CENTER
                           ).grid(row=4, column=0, sticky="nswe", padx=5, pady=5)
        variable = StringVar(main_window)
        variable.set("Все категории")
        FIND_IN_COL = OptionMenu(main_window, variable, "Все категории", "id", "type", "name", "amount", "price")
        FIND_IN_COL.config(bg="gray")
        FIND_IN_COL["menu"].config(bg="gray")
        FIND_IN_COL.grid(row=4, column=1, sticky="swe", padx=5, pady=5)

        FIND_BTN = Button(main_window, background="gray", text="Найти", foreground="black"
                          ).grid(row=4, column=2, sticky="swe", padx=5, pady=5)

        BOTTOM_EMPTY = Label(main_window, background="#49464c", height=1
                             ).grid(row=5, column=0, columnspan=5, sticky="nwe")

    if selection == 2:
        # destruction of others bottom widgets
        for t in range(0, 6):
            for widget in main_window.grid_slaves(row=3, column=t):
                widget.destroy()
            for widget in main_window.grid_slaves(row=4, column=t):
                widget.destroy()
            for widget in main_window.grid_slaves(row=5, column=t):
                widget.destroy()
        # developing new bottom widgets


main_window = Tk()
BOTTOM_FRAME = Frame(main_window, bg="#49464c", relief=FLAT).grid(row=3, column=0, columnspan=5, sticky="swe")

MENU_LIST = ["Вставить в БД", "Удалить из БД", "Редактировать БД"]

# CONFIGURE MAIN WINDOW
main_window.title(u"Vape Shop app")
main_window.configure(background="#49464c")
main_window.geometry("800x600")

HELLO_USER = Label(main_window,
                   background="#1c0f21",
                   height=4,
                   text="Vape shop app\nPowered by biv184",
                   fg="orange"
                   ).grid(row=0, column=0, columnspan=6, sticky="we")

Grid.columnconfigure(main_window, 0, weight=1)
EMPTY_SLOT = Frame(main_window,
                   background="#1c0f21",
                   ).grid(row=0, column=6, sticky="wnse")
RIGHT_MENU = Listbox(main_window,
                     background="#312b38",
                     foreground="orange",
                     font="Arial 10",
                     width=25, relief=FLAT,
                     highlightthickness=0
                     )

for i in MENU_LIST:
    RIGHT_MENU.insert(END, i)

RIGHT_MENU.grid(row=1, column=6, sticky="ns", rowspan=5)

Grid.rowconfigure(main_window, 1, weight=1)

ID_LABEL = Label(main_window, text="id",
                 background="#49464c",
                 relief=GROOVE,
                 foreground="orange"
                 ).grid(row=1, column=0, sticky="nwe")
Grid.rowconfigure(main_window, 1, weight=1)

TYPE_LABEL = Label(main_window, text="type",
                   background="#49464c",
                   relief=GROOVE,
                   foreground="orange"
                   ).grid(row=1, column=1, sticky="nwe")
Grid.columnconfigure(main_window, 1, weight=1)

NAME_LABEL = Label(main_window, text="name",
                   background="#49464c",
                   relief=GROOVE,
                   foreground="orange"
                   ).grid(row=1, column=2, sticky="nwe")
Grid.columnconfigure(main_window, 2, weight=2)

PRICE_LABEL = Label(main_window, text="price",
                    background="#49464c",
                    relief=GROOVE,
                    foreground="orange"
                    ).grid(row=1, column=3, sticky="nwe")
Grid.columnconfigure(main_window, 3, weight=1)

AMOUNT_LABEL = Label(main_window, text="amount",
                     background="#49464c",
                     relief=GROOVE,
                     foreground="orange"
                     ).grid(row=1, column=4, sticky="nwe", columnspan=2)
Grid.columnconfigure(main_window, 4, weight=1)

RIGHT_MENU.bind("<Double-Button-1>", menu_pick)
main_window.mainloop()
