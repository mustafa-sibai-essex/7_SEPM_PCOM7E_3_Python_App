from tkinter import *
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import json
from dataclasses import dataclass
import os

#Global variable that will be used throughout the application
@dataclass
class app_data:
    """A class to keep track of global variables used throughout the app"""
    keys: list
    entries_hw: list
    entries_sw: list
    total_hw: float
    total_sw: float
    total_widgets: dict

keys = ["type", "description", "count", "price", "man_cost", "des_cost", "cod_cost", "tes_cost", "total"]
global_data = app_data(keys, [], [], 0.0, 0.0, {})


# Functions
def clear_frame(frame):
    for child in frame.winfo_children():
        child.destroy()

def new_template():
    desc = "You can start adding components to your project below."
    push_desc(desc)

def push_desc(text):
    """Publishes a description text in the middle frame"""
    label_desc = tk.Label(middle_frame, text=text, font=("Arial", 15))
    label_desc.pack(pady=30)
def upload_json():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a .json file to open",
                                                 filetypes=((".json files", "*.json"), ("All files", "*.*")))
    clear_frame(middle_frame)
    clear_frame(bottom_frame)

    try:
        with open(filename, "r", encoding="utf-8") as file:
            raw_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "File not found.")

    hardware = raw_data["Hardware"]
    software = raw_data["Software"]
    global_data.total_hw = round(calculate(hardware),2)
    global_data.total_sw = round(calculate(software),2)
    push_data_hw(hardware, global_data.total_hw)
    length_hw = len(hardware)
    push_data_sw(software, global_data.total_sw, length_hw) # Length is passed to the function so that the table can be appended where previous one ended
    push_desc("You can see the total project cost broken down to Hardware and Software below.\n You can update your estimates by pressing 'Update' button below the table.")

    # Table headers
    i = 0
    headers = ["Type", "Description", "Count", "Price", "Mfg. Cost", "Design Cost", "Coding Cost", "Testing Cost", "Total"]
    for header in headers:
        label_headers = tk.Label(bottom_frame, text=header, font=("Arial Bold", 12), width=10)
        label_headers.grid(row=0, column=i)
        i +=1

    # Display grand total
    total_cost = round(global_data.total_hw + global_data.total_sw, 2)
    r = len(hardware) + len(software) + 6
    label_grand_total_text = tk.Label(bottom_frame, text="GRAND TOTAL", bg="red",font=("Arial Bold", 13))
    label_grand_total_text.grid(row=r, column=7, pady=10)
    label_grand_total = tk.Label(bottom_frame, text=f"£{total_cost}", bg="red", font=("Arial Bold", 13))
    label_grand_total.grid(row=r, column=8, pady=10)
    global_data.total_widgets["grand_total"] = label_grand_total


def push_data_hw(data_set, total):
    index = len(data_set)
    r = 1 # Because row 0 has the headers, table starts from row 1.
    rows = []
    for i in range(index):
        cols = []
        j=0
        for key in keys:
            e = Entry(bottom_frame, relief=GROOVE, width=10)
            e.grid(row=r, column=j)
            e.insert(END, data_set[i][key])
            cols.append(e)
            j += 1
        r += 1
        rows.append(cols)
    global_data.entries_hw = rows
    label_total_hw_text = tk.Label(bottom_frame, text="Hardware Total", bg="green", font=("Arial Bold", 12))
    label_total_hw_text.grid(row=index+1, column=7, pady=2)
    label_total_hw = tk.Label(bottom_frame, text=f"£{total}", bg="green", font=("Arial Bold", 12))
    label_total_hw.grid(row=index+1, column=8, pady=2)
    global_data.total_widgets["hw_total"] = label_total_hw

    # Add an update button
    button_update_hw = tk.Button(bottom_frame, text="Update Hardware", font=('Arial', 12), height=1, command=lambda: update_hw())
    button_update_hw.grid(row=index+2, column=8, pady=2)

def push_data_sw(data_set, total, length):
    index = len(data_set)
    r = length + 3 # Due to headers, total hardware cost and update button we need to add three rows
    rows = []
    for i in range(index):
        cols = []
        j = 0
        for key in keys:
            e = Entry(bottom_frame, relief=GROOVE, width=10)
            e.grid(row=r, column=j)
            e.insert(END, data_set[i][key])
            cols.append(e)
            j += 1
        r += 1
        rows.append(cols)
    global_data.entries_sw = rows # Updates the global variable
    label_total_sw_text = tk.Label(bottom_frame, text="Software Total", bg="green", font=("Arial Bold", 12))
    label_total_sw_text.grid(row=r+1, column=7, pady=2)
    label_total_sw = tk.Label(bottom_frame, text=f"£{total}", bg="green", font=("Arial Bold", 12))
    label_total_sw.grid(row=r+1, column=8, pady=2)
    global_data.total_widgets["sw_total"] = label_total_sw

    # Add an update button
    button_update_sw = tk.Button(bottom_frame, text="Update Software", font=('Arial', 12), height=1, command=lambda: update_sw())
    button_update_sw.grid(row=r+2, column=8, pady=2)

def calculate(data):
    total = 0
    index = len(data)
    for i in range(index):
        data[i]["total"] = round((data[i]["count"] * data[i]["price"]) + data[i]["man_cost"] + data[i]["des_cost"] + data[i]["cod_cost"] + data[i]["tes_cost"], 2)
        total += round(data[i]["total"],2)
    return total

def grand_total():
    # Calculating new grand total
    j = len(global_data.entries_hw) + len(global_data.entries_sw) + 6
    total_cost = round(global_data.total_hw + global_data.total_sw, 2)
    try:
        global_data.total_widgets["grand_total"].destroy()
    except KeyError:
        pass
    label_grand_total_text = tk.Label(bottom_frame, text="GRAND TOTAL", bg="red", font=("Arial Bold", 13))
    label_grand_total_text.grid(row=j, column=7, pady=10)
    label_grand_total = tk.Label(bottom_frame, text=f"£{total_cost}", bg="red", font=("Arial Bold", 13))
    label_grand_total.grid(row=j, column=8, pady=10)
    global_data.total_widgets["grand_total"] = label_grand_total

def update_hw():
    def update_entries():
        for row in global_data.entries_hw:
            for entry in row:
                entry.get()

    update_entries()

    # Calculating the new row totals
    try:
        for row in global_data.entries_hw:
            total = (float(row[2].get()) * float(row[3].get())) + float(row[4].get()) + float(row[5].get()) + float(row[6].get()) + float(row[7].get())
            row[8].delete(0,END)
            row[8].insert(END, round(total,2))
            update_entries()
        row
    except:
        messagebox.showinfo("Error", "Invalid input. Please check the values you entered.")

    # Calculating new overall totals
    total = 0
    for row in global_data.entries_hw:
        total += float(row[8].get())
    global_data.total_hw = round(total,2)

    i = len(global_data.entries_hw) + 1
    global_data.total_widgets["hw_total"].destroy()
    label_total_hw = tk.Label(bottom_frame, text=f"£{global_data.total_hw}", bg="green", font=("Arial Bold", 12))
    label_total_hw.grid(row=i, column=8, pady=2)
    global_data.total_widgets["hw_total"] = label_total_hw

    grand_total()

def update_sw():
    def update_entries():
        for row in global_data.entries_sw:
            for entry in row:
                entry.get()
    update_entries()

    # Calculating the new row totals
    try:
        for row in global_data.entries_sw:
            total = (float(row[2].get()) * float(row[3].get())) + float(row[4].get()) + float(row[5].get()) + float(
                row[6].get()) + float(row[7].get())
            row[8].delete(0, END)
            row[8].insert(END, round(total, 2))
            update_entries()
    except ValueError:
        messagebox.showinfo("Error", "Invalid value. Please enter a float data type.")

    # Calculating new overall totals
    total = 0
    for row in global_data.entries_sw:
        total += float(row[8].get())
    global_data.total_sw = round(total,2)

    i = len(global_data.entries_hw) + len(global_data.entries_sw) + 4
    global_data.total_widgets["sw_total"].destroy()
    label_total_sw = tk.Label(bottom_frame, text=f"£{global_data.total_sw}", bg="green", font=("Arial Bold", 12))
    label_total_sw.grid(row=i, column=8, pady=2)
    global_data.total_widgets["sw_total"] = label_total_sw

    grand_total()

def new_template():
    # Clears the screen
    clear_frame(middle_frame)
    clear_frame(bottom_frame)

    # Resets the global totals
    global_data.total_hw = 0
    global_data.total_sw = 0


    def new_hw(hw_count):
        r = 1  # Because row 0 has the headers, table starts from row 1.
        rows = []
        for i in range(hw_count):
            cols = []
            j = 0
            for key in keys:
                e = Entry(bottom_frame, relief=GROOVE, width=10)
                e.grid(row=r, column=j)
                cols.append(e)
                j += 1
            r += 1
            rows.append(cols)
        global_data.entries_hw = rows
        label_total_text = tk.Label(bottom_frame, text="Hardware Total", bg="green", font=("Arial Bold", 12))
        label_total_text.grid(row=hw_count + 1, column=7, pady=2)
        label_total_hw = tk.Label(bottom_frame, text=f"£{global_data.total_hw}", bg="green", font=("Arial Bold", 12))
        label_total_hw.grid(row=hw_count + 1, column=8, pady=2)
        global_data.total_widgets["hw_total"] = label_total_hw

        # Add an update button
        button_update_hw = tk.Button(bottom_frame, text="Update Hardware", font=('Arial', 12), height=1,
                                     command=lambda: update_hw())
        button_update_hw.grid(row=hw_count + 2, column=8, pady=2)
    def new_sw(sw_count):
        r = len(global_data.entries_hw) + 3  # Due to headers, total hardware cost and update button we need to add three rows
        rows = []
        for i in range(sw_count):
            cols = []
            j = 0
            for key in keys:
                e = Entry(bottom_frame, relief=GROOVE, width=10)
                e.grid(row=r, column=j)
                cols.append(e)
                j += 1
            r += 1
            rows.append(cols)
        global_data.entries_sw = rows  # Updates the global variable
        label_total_text = tk.Label(bottom_frame, text="Software Total", bg="green", font=("Arial Bold", 12))
        label_total_text.grid(row=r + 1, column=7, pady=2)
        label_total_sw = tk.Label(bottom_frame, text=f"£{global_data.total_sw}", bg="green", font=("Arial Bold", 12))
        label_total_sw.grid(row=r + 1, column=8, pady=2)
        global_data.total_widgets["sw_total"] = label_total_sw

        # Add an update button
        button_update_sw = tk.Button(bottom_frame, text="Update Software", font=('Arial', 12), height=1,
                                     command=lambda: update_sw())
        button_update_sw.grid(row=r + 2, column=8, pady=2)

    hw_count = simpledialog.askinteger(title="New template",
                                            prompt="How many hardware components does your project have?")
    sw_count = simpledialog.askinteger(title="New template",
                                            prompt="How many hardware components does your project have?")

    new_hw(hw_count)
    new_sw(sw_count)
    push_desc("You can use the empty template below to calculate the cost of your project.\nYou can also export your estimates by selecting 'Export .json' from file menu.")

    # Table headers
    i = 0
    headers = ["Type", "Description", "Count", "Price", "Mfg. Cost", "Design Cost", "Coding Cost", "Testing Cost",
               "Total"]
    for header in headers:
        label_headers = tk.Label(bottom_frame, text=header, font=("Arial Bold", 12), width=10)
        label_headers.grid(row=0, column=i)
        i += 1

    grand_total()

def export_json():
    hardware_list = []
    software_list = []
    keys = global_data.keys

    # Packing hardware components into a list of dictionaries
    for row in global_data.entries_hw:
        i = 0
        entry = {}
        for item in row:
            try: # Typecasts numeric values to float
                value = float(item.get())
            except ValueError:
                value = item.get()
            entry[keys[i]] = value
            i += 1
        hardware_list.append(entry)

    # Packing software components into a list of dictionaries
    for row in global_data.entries_sw:
        i = 0
        entry = {}
        for item in row:
            try:
                value = float(item.get())
            except ValueError:
                value = item.get()
            entry[keys[i]] = value
            i += 1
        software_list.append(entry)

    json_doc = {"Hardware": hardware_list, "Software": software_list}


    filename = filedialog.asksaveasfilename(defaultextension="*.json")
    with open(f"{filename}", "w") as save_file:
        json.dump(json_doc, save_file, indent=6)


def about():
    messagebox.showinfo("About the app", "Project Cost Calculator\n(c) 2023\nSibai & Associates")

def read_me():
    try:
        os.popen("open README.md")
    except:
        os.startfile("open README.md")

# Create a Tkinter window
root = tk.Tk()
root.title("Project Cost Calculator")
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))

# Home screen

top_frame = tk.Frame(root)
top_frame.pack()
middle_frame = tk.Frame(root)
middle_frame.pack(side=TOP)
#bottom_frame = tk.Frame(root)
#bottom_frame.pack(fill="y")
canvas = tk.Canvas(root)
canvas.pack()

# Scrollbar

scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
bottom_frame = tk.Frame(canvas)

bottom_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all"),
        width=e.width,
        height=e.height
    )
)

canvas.create_window(0, 0, window=bottom_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
#scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.place(relx=1, rely=0.5, anchor="e", height=200, width=20)

# Labels and description

label_top = tk.Label(top_frame, text="Project Cost Calculator", font=("Arial bold", 26))
label_top.pack(padx=20, pady=15)
desc_text = "Welcome to Project Cost Calculator.\n You can upload a .json file with your project data or you choose to start with an empty template to create your project from scratch.\nYou will also be able to export .json data of your project."
push_desc(desc_text)

# Home screen buttons
button_scratch = tk.Button(bottom_frame, text="Start with a new\ntemplate", font=('Arial', 14), height=4,
                           command=lambda: [clear_frame(middle_frame), clear_frame(bottom_frame), new_template()])
button_scratch.grid(column=0, row=0)
button_json = tk.Button(bottom_frame, text="Import a .json file", font=('Arial', 14), height=4, command=upload_json)
button_json.grid(column=1, row=0)



# Menu bar

menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(
    label='Import .json',
    command=lambda: upload_json()
)
file_menu.add_command(
    label='Export .json',
    command=lambda: export_json()
)
file_menu.add_command(
    label='New template',
    command=lambda: new_template()
)
file_menu.add_separator()
file_menu.add_command(
    label='Exit',
    command=root.destroy
)
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(
    label='About',
    command=lambda: about()
)
help_menu.add_command(
    label='Read me',
    command=lambda: read_me()
)
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Help", menu=help_menu)



# Start the Tkinter event loop
root.mainloop()

