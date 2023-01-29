from tkinter import *
from model3 import Asmenys
from PIL import ImageTk, Image
from tkinter_input_box.input_box import InputBox


langas = Tk()
ui = Tk()
langas.title("Asmenu sarasas")
langas.geometry("500x500")

pasirinkta = IntVar()

asmuo_edit = False
get_all_records_list()

def update_fields():
    box_asmenys.delete(0, END)
    box_asmenys.insert(END, *get_all_records_list())
    e_vardas.delete(0, "end")
    e_pavarde.delete(0, "end")
    e_amzius.delete(0, "end")
    e_pavarde.delete(0, "end")
    e_vardas.focus()

def ui_add(event):
    global asmuo_edit
    if asmuo_edit:
        update_record(asmuo_edit.id, e_vardas.get(), e_pavarde.get(), e_amzius.get(), e_pareigos.get())
        asmuo_edit = False
    else:
        add_record(e_vardas.get(), e_pavarde.get(), e_amzius.get(), e_pareigos.get())
    update_fields()

def ui_delete():
    aktyvus = get_all_records_list()[box_asmenys.curselection()[0]]
    delete_record(aktyvus.id)
    update_fields()

def ui_edit():
    global asmuo_edit 
    asmuo_edit = get_all_records_list()[box_asmenys.curselection()[0]]
    update_fields()
    e_vardas.insert(0, asmuo_edit.vardas)
    e_pavarde.insert(0, asmuo_edit.pavarde)
    e_amzius.insert(0, asmuo_edit.amzius)
    e_pareigos.insert(0, asmuo_edit.pareigos)


top_frame = Frame(langas)
button_frame = Frame(langas)
box_asmenys = Listbox(button_frame, selectmode=SINGLE, width=40)
box_asmenys.insert(END)
status = Label(top_frame, text="Iveskite asmeni", width=40)
e_vardas = Entry(top_frame)
e_vardas_laukas = Label(top_frame, text="Vardas")
e_pavarde = Entry(top_frame)
e_pavarde_laukas = Label(top_frame, text="Pavarde")
e_amzius = Entry(top_frame)
e_amzius_laukas = Label(top_frame, text="Amzius")
e_pareigos = Entry(top_frame)
e_pareigos_laukas = Label(top_frame, text="Pareigos")
b_ivesti = Button(top_frame, text="Ivesti")
b_redaguoti = Button(top_frame, text="Redaguoti", command=ui_edit)
b_istrinti = Button(top_frame, text="Istrinti", command=ui_delete)

e_vardas.bind("<Return>", ui_add)
e_pavarde.bind("<Return>", ui_add)
e_amzius.bind("<Return>", ui_add)
e_pareigos.bind("<Return>", ui_add)


status.grid(row=0, columnspan=2)
e_vardas_laukas.grid(row=1, column=0)
e_vardas.grid(row=1, column=1)
e_pavarde_laukas.grid(row=2, column=0)
e_pavarde.grid(row=2, column=1)
e_amzius_laukas.grid(row=3, column=0)
e_amzius.grid(row=3, column=1)
e_pareigos_laukas.grid(row=4, column=0)
e_pareigos.grid(row=4, column=1)
b_ivesti.grid(row=5, columnspan=2, sticky=E)
b_redaguoti.grid(row=2, columnspan=2)
b_istrinti.grid(row=2, columnspan=2, sticky=W)

e1 = Entry(ui)
box_asmenys.pack()
top_frame.pack()
button_frame.pack()
e1.pack()

langas.mainloop()
ui.mainloop()

