# Bacteria Program
# Date: April 21st, 2021
# Authors: Tyler Downey, Troy Green, Wesley Squires, Ciaran Kelly
""" This program is used to track bacteria samples that are being used to test new medications."""

""" Key Features:
- Date entry box (current date as default)
- ID number of the bacterial culture
- Dropdown menu to select the type of bacteria in that culture (options read from bacteria.dat)
- Dropdown menu for the type of medicine being tested on that culture (options read from medicine.dat)
- Morning (6 am) bacteria count entry box
- Evening (6 pm) bacteria count entry box
- "Confirm" button that adds data as an entry in a list box in following format:
    - date - culture id – bacteria type – medicine type – morning population reading – evening population
      reading – calculated rate of change  ((evening population reading)/(morning population reading)) -1).
    - We can use this button to also validate the entries
- "Save" button that writes the data to separate lines in a file of the user's choosing.
    - Need an entry box for filename.
- "Graph" button which plots a graph (matplotlib) of the bacteria's growth or decline.
    - Formula: y = a*x + b, where b = (morning population reading), and
      a = ((evening population reading) – (morning population reading))/12
    - When the “Graph” button is pressed, the user can be prompted to enter the starting x value for the
      plot, and the ending x value for the plot.
- "Add Bacteria" button: When this button is pressed, a window is opened, and a bacterial culture is added to the dropdown
  menu, as well as to the file bacteria.dat.
- “Add Medicine” button: opens a new window that allows the user to enter the name of a new bacteria, and upon hitting
  a confirm button then, it will be added to the appropriate dropdown menu and added to the file medicine.dat.
- "Exit" button: exits the program when user is finished.
"""

from tkinter import *
from tkinter import ttk, messagebox
import datetime

### FUNCTIONS ###
def confirm():
    pass

def save():
    pass

def graph():
    pass

def add_bacteria():
    #Creates Window for bacteria
    BacteriaWindow = Tk()
    #Creates title for window
    BacteriaWindow.title("Add Bacteria")
    #Sets dimensions of window
    BacteriaWindow.geometry("225x90")
    #Input Box and Variable
    BacteriaAddLabel = Label(BacteriaWindow, text="Bacteria Name: ", pady=2)
    BacteriaAddLabel.grid(row=0, column=0, sticky=E)
    BacteriaAddEntry = Entry(BacteriaWindow, width=16)
    BacteriaAddEntry.grid(row=0, column=1, sticky=W, pady=5, padx=5)

    def AddBacteriaButton():
        BacteriaList = open("bacteria.dat", 'a')
        BacteriaAdded = BacteriaAddEntry.get()
        BacteriaList.writelines("{}\n".format(BacteriaAdded))
        BacteriaList.close()

    #Add Button
    AddButton = Button(BacteriaWindow, text="Add", width=15, height=2, command=AddBacteriaButton)
    AddButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


def add_medicine():
    pass

def exit():
    quit()

### MAIN WINDOW ###
root = Tk()
root.geometry("550x355")
root.title("Medrix Database")
root.iconbitmap("pill.ico")

# FRAMES
frame1 = LabelFrame(root,  text="Culture Data")
frame1.grid(column=0, row=0, padx=5, pady=5, ipadx=10, ipady=10)

frame2 = LabelFrame(root, text="Bacteria Counts")
frame2.grid(row=1, column=0, padx=5, pady=5, ipadx=10, ipady=10)

frame3 = Frame(root)
frame3.grid(row=0, column=1, rowspan=2, padx=5, pady=5, ipadx=10, ipady=10)

frame4 = Frame(root)
frame4.grid(row=2, column=1, padx=5, pady=5, ipadx=10, ipady=10)

### LABELS AND BOXES ###
# DATE
current_date = datetime.datetime.today().strftime('%d-%m-%y')
date_var = StringVar()
date_label = Label(frame1, text="Date: ")
date_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")
date_entry = Entry(frame1, textvariable=date_var)
date_entry.grid(row=0, column=1, pady=5, padx=5)
date_var.set(current_date)

# ID NUMBER
id_number_var = StringVar()
id_number_label = Label(frame1, text="ID Number: ")
id_number_label.grid(row=1, column=0,  pady=5, padx=5, sticky="w")
id_number_entry = Entry(frame1, textvariable=id_number_var)
id_number_entry.grid(row=1, column=1, padx=5, pady=5)

# BACTERIA
bacteria_list = []
bacteria_file = open("bacteria.dat", "r")
for line in bacteria_file:
    bacteria_list.append(line.strip())
bacteria_var = StringVar()
bacteria_label = Label(frame1, text="Bacteria: ")
bacteria_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
bacteria_combobox = ttk.Combobox(frame1, values=bacteria_list, textvariable=bacteria_var, width=17)
bacteria_combobox.grid(row=2, column=1, padx=5, pady=5)

# MEDICINE
medicine_list = []
medicine_file = open("medicine.dat", "r")
for line in medicine_file:
    medicine_list.append(line.strip())
medicine_var = StringVar()
medicine_label = Label(frame1, text="Medicine: ")
medicine_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
medicine_combobox = ttk.Combobox(frame1, values=medicine_list, textvariable=medicine_var, width=17)
medicine_combobox.grid(row=3, column=1, padx=5, pady=5)

# MORNING COUNT
morning_var = StringVar()
morning_label = Label(frame2, text="Morning (6 AM) Count: ")
morning_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
morning_entry = Entry(frame2, textvariable=morning_var, width=10)
morning_entry.grid(row=0, column=1, padx=5, pady=5)

# EVENENING COUNT
evening_var = StringVar()
evening_label = Label(frame2, text="Evening (6 PM) Count: ")
evening_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
evening_entry = Entry(frame2, textvariable=evening_var, width=10)
evening_entry.grid(row=1, column=1, padx=5, pady=5)

# CONFIRM BUTTON
confirm_button = Button(root, text="CONFIRM", command=confirm)
confirm_button.grid(row=2, column=0, ipadx=15, ipady=5, sticky="n")

# BACTERIA LISTBOX TITLE
bacteria_listbox_label = Label(frame3, text="BACTERIA DATA")
bacteria_listbox_label.grid(row=0, column=0, padx=5)

# BACTERIA DATA LISTBOX
bacteria_listbox = Listbox(frame3, height=14, width=40)
bacteria_listbox.grid(row=1, column=0, padx=5, pady=5)

# SAVE BUTTON
save_button = Button(frame4, text="SAVE", command=save)
save_button.grid(row=0, column=0, padx=5, ipadx=15, ipady=5)

# SAVE BUTTON
graph_button = Button(frame4, text="GRAPH", command=graph)
graph_button.grid(row=0, column=1, padx=5, ipadx=10, ipady=5)

# EXIT BUTTON
exit_button = Button(frame4, text="EXIT", command=exit)
exit_button.grid(row=0, column=2, padx=5, ipadx=15, ipady=5)


### MENU ###
### MENUS ###
root_menu = Menu(root, tearoff=False)
root.config(menu=root_menu)

# File Menu
file_menu = Menu(root_menu, tearoff=False)
root_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=exit)

# Edit Menu
edit_menu = Menu(root_menu, tearoff=False)
root_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Add Bacteria", command=add_bacteria)
edit_menu.add_command(label="Add Medicine", command=add_medicine)



root.mainloop()
