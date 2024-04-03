# NOTE: THIS PROJECT IS MISSING LOTS OF REQUIREMENTS FOR PROJECT
# THIS IS JUST AN EXAMPLE TO SHOW OFF A TKINTER PROJECT


import tkinter as tk
from tkinter import messagebox


def calculate_area(length, width=None):
    if width is not None:
        try:
            length = float(length)
            width = float(width)
            if length <= 0 or width <= 0:
                raise ValueError("Dimensions must be positive numbers")
            return length * width
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return None


def calculate_perimeter(length, sides):
    try:
        length = float(length)
        sides = int(sides)
        if length <= 0 or sides < 3:
            raise ValueError("Length must be positive and sides must be at least 3")
        return length * sides
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return None


def create_main_window():
    root = tk.Tk()
    root.title("Polygon Calculator")

    nav_bar = tk.Frame(root)
    nav_bar.pack(side="top", fill="x")

    area_button = tk.Button(nav_bar, text="Calculate Area", command=switch_to_area)
    area_button.pack(side="left", padx=10, pady=5)

    perimeter_button = tk.Button(nav_bar, text="Calculate Perimeter", command=switch_to_perimeter)
    perimeter_button.pack(side="left", padx=10, pady=5)

    return root


def create_area_frame(root):
    area_frame = tk.Frame(root)

    length_label = tk.Label(area_frame, text="Length:")
    length_label.grid(row=0, column=0)
    length_entry_area = tk.Entry(area_frame)
    length_entry_area.grid(row=0, column=1)

    width_label = tk.Label(area_frame, text="Width:")
    width_label.grid(row=1, column=0)
    width_entry_area = tk.Entry(area_frame)
    width_entry_area.grid(row=1, column=1)

    submit_button = tk.Button(area_frame, text="Calculate Area", command=area_submit_callback)
    submit_button.grid(row=3, columnspan=2)

    area_result_label = tk.Label(area_frame, text="")
    area_result_label.grid(row=4, columnspan=2)

    return area_frame, length_entry_area, width_entry_area, area_result_label


def create_perimeter_frame(root):
    perimeter_frame = tk.Frame(root)

    length_label = tk.Label(perimeter_frame, text="Length:")
    length_label.grid(row=0, column=0)
    length_entry_perimeter = tk.Entry(perimeter_frame)
    length_entry_perimeter.grid(row=0, column=1)

    sides_label = tk.Label(perimeter_frame, text="Number of Sides:")
    sides_label.grid(row=1, column=0)
    sides_entry_perimeter = tk.Entry(perimeter_frame)
    sides_entry_perimeter.grid(row=1, column=1)

    submit_button = tk.Button(perimeter_frame, text="Calculate Perimeter", command=perimeter_submit_callback)
    submit_button.grid(row=2, columnspan=2)

    perimeter_result_label = tk.Label(perimeter_frame, text="")
    perimeter_result_label.grid(row=3, columnspan=2)

    return perimeter_frame, length_entry_perimeter, sides_entry_perimeter, perimeter_result_label


def switch_to_area():
    perimeter_frame.pack_forget()
    area_frame.pack()


def switch_to_perimeter():
    area_frame.pack_forget()
    perimeter_frame.pack()


def area_submit_callback():
    length = length_entry_area.get()
    width = width_entry_area.get()
    if not length:
        messagebox.showerror("Error", "Please enter length")
        return
    if width:
        area = calculate_area(length, width=width)
        if area is not None:
            area_result_label.config(text=f"Area: {area}")


def perimeter_submit_callback():
    length = length_entry_perimeter.get()
    sides = sides_entry_perimeter.get()
    if not length:
        messagebox.showerror("Error", "Please enter length")
        return
    if not sides:
        messagebox.showerror("Error", "Please enter number of sides")
        return
    perimeter = calculate_perimeter(length, sides)
    if perimeter is not None:
        perimeter_result_label.config(text=f"Perimeter: {perimeter}")


main_window = create_main_window()
global perimeter_frame, length_entry_perimeter, sides_entry_perimeter, perimeter_result_label
global area_frame, length_entry_area, width_entry_area, area_result_label

area_frame, length_entry_area, width_entry_area, area_result_label = create_area_frame(main_window)
perimeter_frame, length_entry_perimeter, sides_entry_perimeter, perimeter_result_label = create_perimeter_frame(
    main_window)

switch_to_area()

main_window.mainloop()
