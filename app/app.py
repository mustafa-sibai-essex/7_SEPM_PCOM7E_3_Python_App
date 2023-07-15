


keys = [
    "type",
    "description",
    "count",
    "price",
    "man_cost",
    "des_cost",
    "cod_cost",
    "tes_cost",
    "total",
]






def new_template():
    """Displays an empty template on the screen, based on user input (i.e. number of rows and columns)"""

    # Clears the screen
    clear_frame(middle_frame)
    clear_frame(bottom_frame)

    # Resets the global totals
    global_data.total_hw = 0
    global_data.total_sw = 0

    def new_hw(hw_count):
        """Displays the  empty hardware table"""
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
        label_total_text = tk.Label(
            bottom_frame, text="Hardware Total", bg="green", font=("Arial Bold", 12)
        )
        label_total_text.grid(row=hw_count + 1, column=7, pady=2)
        label_total_hw = tk.Label(
            bottom_frame,
            text=f"£{global_data.total_hw}",
            bg="green",
            font=("Arial Bold", 12),
        )
        label_total_hw.grid(row=hw_count + 1, column=8, pady=2)
        global_data.total_widgets["hw_total"] = label_total_hw

        # Add an update button
        button_update_hw = tk.Button(
            bottom_frame,
            text="Update Hardware",
            font=("Arial", 12),
            height=1,
            command=lambda: update_hw(),
        )
        button_update_hw.grid(row=hw_count + 2, column=8, pady=2)

    def new_sw(sw_count):
        """Displays the  empty software table"""
        r = (
            len(global_data.entries_hw) + 3
        )  # Due to headers, total hardware cost and update button we need to add three rows
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
        label_total_text = tk.Label(
            bottom_frame, text="Software Total", bg="green", font=("Arial Bold", 12)
        )
        label_total_text.grid(row=r + 1, column=7, pady=2)
        label_total_sw = tk.Label(
            bottom_frame,
            text=f"£{global_data.total_sw}",
            bg="green",
            font=("Arial Bold", 12),
        )
        label_total_sw.grid(row=r + 1, column=8, pady=2)
        global_data.total_widgets["sw_total"] = label_total_sw

        # Add an update button
        button_update_sw = tk.Button(
            bottom_frame,
            text="Update Software",
            font=("Arial", 12),
            height=1,
            command=lambda: update_sw(),
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
    push_desc(
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
            bottom_frame, text=header, font=("Arial Bold", 12), width=10
        )
        label_headers.grid(row=0, column=i)
        i += 1

    grand_total()











