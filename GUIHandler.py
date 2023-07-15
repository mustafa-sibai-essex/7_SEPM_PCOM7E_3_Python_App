from tkinter import *
import tkinter as tk
from tkinter import simpledialog, messagebox
import os

class GUIHandler:
    def __init__(self, global_data, json_handler):
        self.global_data = global_data
        self.json_handler = json_handler

    def get_bottom_frame(self):
        return self.bottom_frame

    def start(self):
        # Create a Tkinter window

        root = tk.Tk()
        root.title("Project Cost Calculator")
        width, height = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (width, height))

        # Frames
        self.top_frame = tk.Frame(root)
        self.top_frame.pack()
        self.middle_frame = tk.Frame(root)
        self.middle_frame.pack(side=TOP)
        self.canvas = tk.Canvas(root)
        self.canvas.pack()

        # Scrollbar
        scrollbar = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.bottom_frame = tk.Frame(self.canvas)

        self.bottom_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(  # Extends the canvas to the size of the frame
                scrollregion=self.canvas.bbox("all"), width=e.width, height=e.height
            ),
        )

        self.canvas.create_window(0, 0, window=self.bottom_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(relx=1, rely=0.5, anchor="e", height=400, width=20)

        # Labels and description
        self.label_top = tk.Label(
            self.top_frame, text="Project Cost Calculator", font=("Arial bold", 26)
        )
        self.label_top.pack(padx=20, pady=15)
        self.push_desc(
            "Welcome to Project Cost Calculator.\nYou can upload a .json file with your project data or you choose to start with an empty template to create your project from scratch.\nYou will also be able to export .json data of your project."
        )

        # Home screen buttons
        self.button_scratch = tk.Button(
            self.bottom_frame,
            text="Start with a new\ntemplate",
            font=("Arial", 14),
            height=4,
            command=lambda: [
                self.clear_frame(self.middle_frame),
                self.clear_frame(self.bottom_frame),
                self.new_template(),
            ],
        )
        self.button_scratch.grid(column=0, row=0)
        self.button_json = tk.Button(
            self.bottom_frame,
            text="Import a .json file",
            font=("Arial", 14),
            height=4,
            command=self.json_handler.upload_json,
        )
        self.button_json.grid(column=1, row=0)

        # Menu bar
        menubar = Menu(root)
        root.config(menu=menubar)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(
            label="Import .json", command=self.json_handler.upload_json
        )
        file_menu.add_command(
            label="Export .json", command=self.json_handler.export_json
        )
        file_menu.add_command(
            label="Open & edit .json", command=self.json_handler.open_json
        )
        file_menu.add_command(label="New template", command=self.new_template)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.destroy)

        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.about)
        help_menu.add_command(label="Read me", command=self.read_me)
        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Help", menu=help_menu)

        # Start the Tkinter event loop
        root.mainloop()

    def push_desc(self, text):
        """Publishes a description text in the middle frame"""
        label_desc = tk.Label(self.middle_frame, text=text, font=("Arial", 15))
        label_desc.pack(pady=30)
        return label_desc  # For testing purposes only

    def clear_frame(self, frame):
        """Clears frame that passed as a parameter to clear the specified portions of screen"""
        for child in frame.winfo_children():
            child.destroy()

    def push_data_hw(self, data_set, total):
        """Pushes the initial (upon opening a .json file) Hardware data to the bottom frame"""
        index = len(data_set)
        r = 1  # Because row 0 has the headers, table starts from row 1.
        rows = []
        for i in range(index):
            cols = []
            j = 0
            for key in self.global_data.keys:
                e = Entry(self.bottom_frame, relief=GROOVE, width=10)
                e.grid(row=r, column=j)
                e.insert(END, data_set[i][key])
                cols.append(e)
                j += 1
            r += 1
            rows.append(cols)
        self.global_data.entries_hw = rows
        label_total_hw_text = tk.Label(
            self.bottom_frame,
            text="Hardware Total",
            bg="green",
            font=("Arial Bold", 12),
        )
        label_total_hw_text.grid(row=index + 1, column=7, pady=2)
        label_total_hw = tk.Label(
            self.bottom_frame, text=f"£{total}", bg="green", font=("Arial Bold", 12)
        )
        label_total_hw.grid(row=index + 1, column=8, pady=2)
        self.global_data.total_widgets["hw_total"] = label_total_hw

        # Add an update button
        button_update_hw = tk.Button(
            self.bottom_frame,
            text="Update Hardware",
            font=("Arial", 12),
            height=1,
            command=lambda: self.update_hw(),
        )
        button_update_hw.grid(row=index + 2, column=8, pady=2)

        return self.global_data.entries_hw  # For testing purposes only

    def push_data_sw(self, data_set, total, length):
        """Pushes the initial (upon opening a .json file) Software data to the bottom frame"""
        index = len(data_set)
        r = (
            length + 3
        )  # Due to headers, total hardware cost and update button we need to add three rows
        rows = []
        for i in range(index):
            cols = []
            j = 0
            for key in self.global_data.keys:
                e = Entry(self.bottom_frame, relief=GROOVE, width=10)
                e.grid(row=r, column=j)
                e.insert(END, data_set[i][key])
                cols.append(e)
                j += 1
            r += 1
            rows.append(cols)
        self.global_data.entries_sw = rows  # Updates the global variable
        label_total_sw_text = tk.Label(
            self.bottom_frame,
            text="Software Total",
            bg="green",
            font=("Arial Bold", 12),
        )
        label_total_sw_text.grid(row=r + 1, column=7, pady=2)
        label_total_sw = tk.Label(
            self.bottom_frame, text=f"£{total}", bg="green", font=("Arial Bold", 12)
        )
        label_total_sw.grid(row=r + 1, column=8, pady=2)
        self.global_data.total_widgets["sw_total"] = label_total_sw

        # Add an update button
        button_update_sw = tk.Button(
            self.bottom_frame,
            text="Update Software",
            font=("Arial", 12),
            height=1,
            command=lambda: self.update_sw(),
        )
        button_update_sw.grid(row=r + 2, column=8, pady=2)

    def calculate(self, data):
        """Calculates the total cost of each component in the data set passed in reference (e.g. Hardware and Software"""
        total = 0
        index = len(data)
        for i in range(index):
            data[i]["total"] = round(
                (data[i]["count"] * data[i]["price"])
                + data[i]["man_cost"]
                + data[i]["des_cost"]
                + data[i]["cod_cost"]
                + data[i]["tes_cost"],
                2,
            )
            total += round(data[i]["total"], 2)
        return total

    def grand_total(self):
        """Calculates the total cost of the project"""
        j = len(self.global_data.entries_hw) + len(self.global_data.entries_sw) + 6
        total_cost = round(self.global_data.total_hw + self.global_data.total_sw, 2)
        try:
            self.global_data.total_widgets["grand_total"].destroy()
        except KeyError:
            pass
        label_grand_total_text = tk.Label(
            self.bottom_frame,
            text="GRAND TOTAL",
            bg="red",
            font=("Arial Bold", 13),
        )
        label_grand_total_text.grid(row=j, column=7, pady=10)
        label_grand_total = tk.Label(
            self.bottom_frame,
            text=f"£{total_cost}",
            bg="red",
            font=("Arial Bold", 13),
        )
        label_grand_total.grid(row=j, column=8, pady=10)
        self.global_data.total_widgets["grand_total"] = label_grand_total
        return total_cost

    def update_hw(self):
        """Updates the hardware calculations upon user's amendment to data"""

        def update_entries():
            for row in self.global_data.entries_hw:
                for entry in row:
                    entry.get()

        update_entries()

        # Calculating the new row totals
        try:
            for row in self.global_data.entries_hw:
                total = (
                    (float(row[2].get()) * float(row[3].get()))
                    + float(row[4].get())
                    + float(row[5].get())
                    + float(row[6].get())
                    + float(row[7].get())
                )
                row[8].delete(0, END)
                row[8].insert(END, round(total, 2))
                update_entries()
        except:
            messagebox.showinfo(
                "Error", "Invalid input. Please check the values you entered."
            )

        # Calculating new overall totals
        total = 0
        for row in self.global_data.entries_hw:
            total += float(row[8].get())
        self.global_data.total_hw = round(total, 2)

        i = len(self.global_data.entries_hw) + 1
        self.global_data.total_widgets["hw_total"].destroy()
        label_total_hw = tk.Label(
            self.bottom_frame,
            text=f"£{self.global_data.total_hw}",
            bg="green",
            font=("Arial Bold", 12),
        )
        label_total_hw.grid(row=i, column=8, pady=2)
        self.global_data.total_widgets["hw_total"] = label_total_hw
        self.grand_total()

    def update_sw(self):
        """Updates the software calculations upon user's amendment to data"""

        def update_entries():
            for row in self.global_data.entries_sw:
                for entry in row:
                    entry.get()

        update_entries()

        # Calculating the new row totals
        try:
            for row in self.global_data.entries_sw:
                total = (
                    (float(row[2].get()) * float(row[3].get()))
                    + float(row[4].get())
                    + float(row[5].get())
                    + float(row[6].get())
                    + float(row[7].get())
                )
                row[8].delete(0, END)
                row[8].insert(END, round(total, 2))
                update_entries()
        except ValueError:
            messagebox.showinfo(
                "Error", "Invalid value. Please enter a float data type."
            )

        # Calculating new overall totals
        total = 0
        for row in self.global_data.entries_sw:
            total += float(row[8].get())
        self.global_data.total_sw = round(total, 2)

        i = len(self.global_data.entries_hw) + len(self.global_data.entries_sw) + 4
        self.global_data.total_widgets["sw_total"].destroy()
        label_total_sw = tk.Label(
            self.bottom_frame,
            text=f"£{self.global_data.total_sw}",
            bg="green",
            font=("Arial Bold", 12),
        )
        label_total_sw.grid(row=i, column=8, pady=2)
        self.global_data.total_widgets["sw_total"] = label_total_sw
        self.grand_total()

    def new_template(self):
        """Displays an empty template on the screen, based on user input (i.e. number of rows and columns)"""

        # Clears the screen
        self.clear_frame(self.middle_frame)
        self.clear_frame(self.bottom_frame)

        # Resets the global totals
        self.global_data.total_hw = 0
        self.global_data.total_sw = 0

        self.global_data.keys = [
            "Type",
            "Description",
            "Count",
            "Price",
            "Man. Cost",
            "Des. Cost",
            "Cod. Cost",
            "Tes. Cost",
            "Total",
        ]

        def new_hw(hw_count):
            """Displays the  empty hardware table"""
            r = 1  # Because row 0 has the headers, table starts from row 1.
            rows = []
            for i in range(hw_count):
                cols = []
                j = 0
                for key in self.global_data.keys:
                    e = Entry( self.bottom_frame, relief=GROOVE, width=10)
                    e.grid(row=r, column=j)
                    cols.append(e)
                    j += 1
                r += 1
                rows.append(cols)
            self.global_data.entries_hw = rows
            label_total_text = tk.Label(
                self.bottom_frame, text="Hardware Total", bg="green", font=("Arial Bold", 12)
            )
            label_total_text.grid(row=hw_count + 1, column=7, pady=2)
            label_total_hw = tk.Label(
                self.bottom_frame,
                text=f"£{self.global_data.total_hw}",
                bg="green",
                font=("Arial Bold", 12),
            )
            label_total_hw.grid(row=hw_count + 1, column=8, pady=2)
            self.global_data.total_widgets["hw_total"] = label_total_hw

            # Add an update button
            button_update_hw = tk.Button(
                self.bottom_frame,
                text="Update Hardware",
                font=("Arial", 12),
                height=1,
                command=lambda: self.update_hw(),
            )
            button_update_hw.grid(row=hw_count + 2, column=8, pady=2)

        def new_sw(sw_count):
            """Displays the  empty software table"""
            r = (
                len(self.global_data.entries_hw) + 3
            )  # Due to headers, total hardware cost and update button we need to add three rows
            rows = []
            for i in range(sw_count):
                cols = []
                j = 0
                for key in self.global_data.keys:
                    e = Entry(self.bottom_frame, relief=GROOVE, width=10)
                    e.grid(row=r, column=j)
                    cols.append(e)
                    j += 1
                r += 1
                rows.append(cols)
            self.global_data.entries_sw = rows  # Updates the global variable
            label_total_text = tk.Label(
                self.bottom_frame, text="Software Total", bg="green", font=("Arial Bold", 12)
            )
            label_total_text.grid(row=r + 1, column=7, pady=2)
            label_total_sw = tk.Label(
                self.bottom_frame,
                text=f"£{self.global_data.total_sw}",
                bg="green",
                font=("Arial Bold", 12),
            )
            label_total_sw.grid(row=r + 1, column=8, pady=2)
            self.global_data.total_widgets["sw_total"] = label_total_sw

            # Add an update button
            button_update_sw = tk.Button(
                self.bottom_frame,
                text="Update Software",
                font=("Arial", 12),
                height=1,
                command=lambda: self.update_sw(),
            )
            button_update_sw.grid(row=r + 2, column=8, pady=2)

        hw_count = simpledialog.askinteger(
            title="New template",
            prompt="How many hardware components does your project have?",
        )
        sw_count = simpledialog.askinteger(
            title="New template",
            prompt="How many hardware components does your project have?",
        )

        new_hw(hw_count)
        new_sw(sw_count)
        self.push_desc(
            "You can use the empty template below to calculate the cost of your project.\nYou can also export your estimates by selecting 'Export .json' from file menu."
        )

        # Table headers
        i = 0
        headers = [
            "Type",
            "Description",
            "Count",
            "Price",
            "Mfg. Cost",
            "Design Cost",
            "Coding Cost",
            "Testing Cost",
            "Total",
        ]
        for header in headers:
            label_headers = tk.Label(
                self.bottom_frame, text=header, font=("Arial Bold", 12), width=10
            )
            label_headers.grid(row=0, column=i)
            i += 1

        self.grand_total()

    def about(self):
        """Displays about message box"""
        messagebox.showinfo(
            "About the app", "Project Cost Calculator\n(c) 2023\nSibai & Associates"
        )

    def read_me(self):
        """Opens readme file with default application"""
        try:
            os.popen("open README.md")  # for MacOS
        except:
            os.startfile("open README.md")  # for Windows
