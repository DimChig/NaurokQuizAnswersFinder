# START THIS PROGRAM ONLY
# START THIS PROGRAM ONLY
# START THIS PROGRAM ONLY
# START THIS PROGRAM ONLY
# START THIS PROGRAM ONLY
# START THIS PROGRAM ONLY
# START THIS PROGRAM ONLY
# START THIS PROGRAM ONLY

from tkinter import *
import GoogleSearcher

win = Tk()
win.geometry("750x700+400+100")

query = ""

query_field = Entry(win, width=75, borderwidth=1, font=30)
query_field.grid(row=0, columnspan=2, pady=10, padx=5)

site_naurok = "naurok.com.ua"
site_pomahach = "pomahach.com"

site_filter = site_naurok


def handleQuery(query):
    global site_filter
    site_filter = ""
    if chechbox_naurok_var.get() == 1:    site_filter = "site:" + site_naurok
    if chechbox_pomahach_var.get() == 1:    site_filter = "site:" + site_pomahach
    s = GoogleSearcher.searchAnswers(query, site_filter)
    text_main.delete(1.0, END)
    text_main.insert(1.0, s)
    query_field.delete(0, END)


def onClickFind():
    global query
    query = query_field.get()
    if len(query) < 5:
        return
    # print("click ",query)
    text_main.delete(1.0, END)
    text_main.insert(1.0, "Loading...")
    handleQuery(query)


def onClickClear():
    global text_main
    query_field.delete(0, END)
    chechbox_naurok_var.set(0)
    chechbox_pomahach_var.set(0)
    text_main.delete(1.0, END)


def clickCheckboxNaurok():
    if chechbox_naurok_var.get() == 1:
        chechbox_pomahach_var.set(0)


def clickCheckboxPomahach():
    if chechbox_pomahach_var.get() == 1:
        chechbox_naurok_var.set(0)


Button(win, text="Clear", pady=5, width=45, command=onClickClear).grid(row=1, column=0)
Button(win, text="Find", pady=5, width=45, command=onClickFind).grid(row=1, column=1)

chechbox_naurok_var = IntVar()
chechbox_pomahach_var = IntVar()
checkbox_naurok = Checkbutton(win, text="Naurok.com.ua", command=clickCheckboxNaurok,
                              variable=chechbox_naurok_var).grid(row=2, column=0)
checkbox_pomahach = Checkbutton(win, text="Pomahach.com", command=clickCheckboxPomahach,
                                variable=chechbox_pomahach_var).grid(row=2, column=1)

text_main = Text(win, padx=5, pady=5, font=25)
text_main.grid(row=3, columnspan=2)

win.mainloop()
