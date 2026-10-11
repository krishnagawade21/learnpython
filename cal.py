import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#202124")

# Input field
expression = ""

display = tk.Entry(
    root,
    font=("Arial", 25),
    bg="#303134",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)
display.pack(fill="x", padx=15, pady=20, ipady=15)


# Button click function
def button_click(value):
    if value == "C":
        display.delete(0, tk.END)

    elif value == "=":
        try:
            result = eval(display.get())

            display.delete(0, tk.END)
            display.insert(tk.END, str(result))

        except ZeroDivisionError:
            display.delete(0, tk.END)
            display.insert(tk.END, "Cannot divide by zero")

        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Invalid Input")

    else:
        display.insert(tk.END, value)


# Calculator buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", ".", "+"],
    ["="]
]

# Create button frame
button_frame = tk.Frame(root, bg="#202124")
button_frame.pack(expand=True, fill="both", padx=10, pady=10)

# Button colors
number_color = "#3c4043"
operator_color = "#f9ab00"
clear_color = "#ea4335"
equal_color = "#34a853"

# Create buttons
for row_index, row in enumerate(buttons):

    for col_index, value in enumerate(row):

        if value == "C":
            color = clear_color
        elif value == "=":
            color = equal_color
        elif value in ["+", "-", "*", "/"]:
            color = operator_color
        else:
            color = number_color

        if value == "=":
            btn = tk.Button(
                button_frame,
                text=value,
                font=("Arial", 18, "bold"),
                bg=color,
                fg="white",
                bd=0,
                command=lambda v=value: button_click(v)
            )
            btn.grid(
                row=row_index,
                column=0,
                columnspan=4,
                sticky="nsew",
                padx=5,
                pady=5,
                ipady=8
            )

        else:
            btn = tk.Button(
                button_frame,
                text=value,
                font=("Arial", 18, "bold"),
                bg=color,
                fg="white",
                bd=0,
                activebackground="#5f6368",
                activeforeground="white",
                command=lambda v=value: button_click(v)
            )
            btn.grid(
                row=row_index,
                column=col_index,
                sticky="nsew",
                padx=5,
                pady=5,
                ipady=8
            )

# Configure grid layout
for i in range(5):
    button_frame.rowconfigure(i, weight=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)

# Run the application
root.mainloop()