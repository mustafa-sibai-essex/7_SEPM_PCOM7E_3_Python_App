import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

class JSONHandler:
    def __init__(self, global_data):
        self.global_data = global_data
        self.gui_handler = None

    def set_gui_handler(self, gui_handler):
        self.gui_handler = gui_handler

    def export_json(self):
        """Exports data as a j.son file"""

        hardware_list = []
        software_list = []
        keys = self.global_data.keys

        # Packing hardware components into a list of dictionaries
        for row in self.global_data.entries_hw:
            i = 0
            entry = {}
            for item in row:
                try:  # Typecasts numeric values to float
                    value = float(item.get())
                except ValueError:
                    value = item.get()
                entry[keys[i]] = value
                i += 1
            hardware_list.append(entry)

        for row in self.global_data.entries_sw:
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

    def open_json(self):
        """Opens .json file with default application for editing"""

        filetypes = (("Json files", "*.json"), ("All files", "*.*"))

        filename = filedialog.askopenfilename(
            title="Open a file", initialdir="/", filetypes=filetypes
        )

        try:
            os.popen(f"open {filename}")  # for MacOS
        except:
            os.startfile(f"open {filename}")  # for Windows

    def load_json(self):
        """Opens .json file and reads the content to memory"""

        filename = filedialog.askopenfilename(
            initialdir="/",
            title="Select a .json file to open",
            filetypes=((".json files", "*.json"), ("All files", "*.*")),
        )

        try:
            with open(filename, "r", encoding="utf-8") as file:
                raw_data = json.load(file)
                return raw_data
        except FileNotFoundError:
            return None
    
    def upload_json(self):
        """Opens .json file and reads the content to memory"""

        raw_data = self.load_json()

        if raw_data == None:
            return messagebox.showinfo("Error", "File not found.")

        self.gui_handler.clear_frame(self.gui_handler.middle_frame)
        self.gui_handler.clear_frame(self.gui_handler.bottom_frame)

        hardware = raw_data["Hardware"]
        software = raw_data["Software"]
        self.global_data.total_hw = round(self.gui_handler.calculate(hardware), 2)
        self.global_data.total_sw = round(self.gui_handler.calculate(software), 2)
        self.gui_handler.push_data_hw(hardware, self.global_data.total_hw)
        length_hw = len(hardware)
        self.gui_handler.push_data_sw(
            software, self.global_data.total_sw, length_hw
        )  # Length is passed to the function so that the table can be appended where previous one ended
        self.gui_handler.push_desc(
            "You can see the total project cost broken down to Hardware and Software below.\n You can update your estimates by pressing 'Update' button below the table."
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
                self.gui_handler.bottom_frame,
                text=header,
                font=("Arial Bold", 12),
                width=10,
            )
            label_headers.grid(row=0, column=i)
            i += 1

        # Display grand total
        total_cost = round(self.global_data.total_hw + self.global_data.total_sw, 2)
        r = len(hardware) + len(software) + 6
        label_grand_total_text = tk.Label(
            self.gui_handler.bottom_frame,
            text="GRAND TOTAL",
            bg="red",
            font=("Arial Bold", 13),
        )
        label_grand_total_text.grid(row=r, column=7, pady=10)
        label_grand_total = tk.Label(
            self.gui_handler.bottom_frame,
            text=f"£{total_cost}",
            bg="red",
            font=("Arial Bold", 13),
        )
        label_grand_total.grid(row=r, column=8, pady=10)
        self.global_data.total_widgets["grand_total"] = label_grand_total