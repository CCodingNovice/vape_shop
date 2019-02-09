from tkinter import *

main_window = Tk()
MENU_LIST = ["menu 1", "menu 2", "menu 3", "menu 4", "menu 5", "menu 6", "menu 7", "menu 8", "menu 9", "menu 10"]

# CONFIGURE MAIN WINDOW
main_window.title(u"Vape Shop app")
main_window.geometry("800x600")
main_window.configure(background="#49464c")

LEFT_FRAME = Frame(main_window)

# CONFIGURE GREETING LABEL
HELLO_USER = Label(main_window, text="Welcome to the club, buddy!\n"
                                     "There are a lot of vape stuff, just check our database")
HELLO_USER.configure(background="white")


LEFT_FRAME.pack(side="top", anchor="nw", fill=BOTH, expand=FALSE)

RIGHT_MENU_FRAME = Frame(main_window, bg="#312b38")

RIGHT_LABEL = Label(RIGHT_MENU_FRAME, text="\n", bg="white")

RIGHT_LISTBOX = Listbox(RIGHT_MENU_FRAME, selectmode=BROWSE, bg="#312b38", fg="orange", relief=FLAT)
RIGHT_LISTBOX.config(highlightthickness=0)

for i in MENU_LIST:
    RIGHT_LISTBOX.insert(END, i)

RIGHT_LABEL.pack(side="top", fill=X)
RIGHT_MENU_FRAME.pack(side=RIGHT, fill=Y, expand=FALSE)
HELLO_USER.pack(fill=X)
RIGHT_LISTBOX.pack(side="top", expand=FALSE)
RIGHT_LISTBOX.config(font="Monospaced 10")

main_window.mainloop()
