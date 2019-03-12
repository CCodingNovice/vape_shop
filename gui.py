from tkinter import *
import tkinter.ttk as ttk
import pandas as pd
from shop_database import load_csv_to_df


def destroy_widgets():
    for t in range(0, 6):
        for widget in main_window.grid_slaves(row=3, column=t):
            widget.destroy()
        for widget in main_window.grid_slaves(row=4, column=t):
            widget.destroy()
        for widget in main_window.grid_slaves(row=5, column=t):
            widget.destroy()


def form_table(data):
    rows = data.shape[0]
    cols = data.shape[1]
    table = ttk.Treeview(main_window)

    style = ttk.Style(main_window)
    style.theme_use("clam")
    style.configure("Treeview", background="#49464c",
                    fieldbackground="#49464c", foreground="orange")

    table["columns"] = ("one", "two", "three", "four", "five")
    table['show'] = 'headings'
    table.heading("one", text="id")
    table.heading("two", text="type")
    table.heading("three", text="name")
    table.heading("four", text="price")
    table.heading("five", text="amount")

    table.column("one", width=100, minwidth=100, stretch=False)
    table.column("two", width=170, minwidth=170, stretch=False)
    table.column("three", width=150, minwidth=150, stretch=False)
    table.column("four", width=100, minwidth=100, stretch=False)
    table.column("five", width=100, minwidth=100, stretch=False)

    for j in range(0, rows):
        lst = [data.index.tolist()[j]] + list(data.iloc[j])
        table.insert("", 'end', text=j, values=lst)
    table.grid(row=1, column=0, columnspan=6, sticky="nswe")
    Grid.columnconfigure(main_window, 0, weight=1)


def menu_pick(event):
    w = event.widget
    selection = int(w.curselection()[0])
    if selection == 0:
        destroy_widgets()
        # developing new bottom widgets
        ADD_BTN = Button(main_window, text="add", background="gray", foreground="black")
        INFO_LABEL = Label(main_window, text="Вставить в базу данных",
                           background="#1c0f21",
                           foreground="orange"
                           ).grid(row=3, column=0, columnspan=6, sticky="nwe")
        Grid.rowconfigure(main_window, 3, weight=1)
        id_etry = Entry(main_window, text="id", background="gray", justify=CENTER
                        ).grid(row=4, column=0, sticky="nwe", padx=5)
        type_entry = Entry(main_window, text="type", background="gray", justify=CENTER
                           ).grid(row=4, column=1, sticky="nwe", padx=5)
        name_entry = Entry(main_window, text="name", background="gray", justify=CENTER
                           ).grid(row=4, column=2, sticky="nwe", padx=5)
        price_entry = Entry(main_window, text="price", background="gray", justify=CENTER
                            ).grid(row=4, column=3, sticky="nwe", padx=5)
        amount_entry = Entry(main_window, text="amount", background="gray", justify=CENTER
                             ).grid(row=4, column=4, sticky="nwe", padx=5)
        ADD_BTN.grid(row=4, column=5, sticky="nwe")
        BOTTOM_EMPTY = Label(main_window, background="#49464c", height=1
                             ).grid(row=5, column=0, columnspan=5, sticky="nswe")
    if selection == 1:
        # destruction of others bottom widgets
        destroy_widgets()
        # developing new bottom widgets
        INFO_LABEL = Label(main_window, text="Удалить из базы данных",
                           background="#1c0f21",
                           foreground="orange"
                           ).grid(row=3, column=0, columnspan=6, sticky="nwe")
        Grid.rowconfigure(main_window, 3, weight=1)
        FIND_ENTRY = Entry(main_window, text="name", background="gray", justify=CENTER
                           ).grid(row=4, column=0, columnspan=2, sticky="nwe", padx=5, pady=5)
        variable = StringVar(main_window)
        variable.set("Все категории")
        find_in_col = OptionMenu(main_window, variable, "Все категории", "id", "type", "name", "amount", "price")
        find_in_col.config(bg="gray")
        find_in_col["menu"].config(bg="gray")
        find_in_col.grid(row=4, column=4, sticky="nwe", padx=5, pady=5)

        FIND_BTN = Button(main_window, background="gray", text="Найти", foreground="black"
                          ).grid(row=4, column=5, sticky="nwe", padx=5, pady=5)

        BOTTOM_EMPTY = Label(main_window, background="#49464c", height=1, text="\n\n"
                             ).grid(row=5, column=0, columnspan=5, sticky="nswe")

    if selection == 2:
        # destruction of others bottom widgets
        destroy_widgets()
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

df = load_csv_to_df(name='database_example')
form_table(df)

for i in MENU_LIST:
    RIGHT_MENU.insert(END, i)

RIGHT_MENU.grid(row=1, column=6, sticky="ns", rowspan=5)

Grid.rowconfigure(main_window, 1, weight=1)

RIGHT_MENU.bind("<Double-Button-1>", menu_pick)

main_window.mainloop()
