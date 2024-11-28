import tkinter as tk
import csv
from tkinter import messagebox
from tkinter import ttk


def create_main_window():
    root = tk.Tk()
    root.title("Car Inventory System")
    root.geometry("1200x400")

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    notebook = ttk.Notebook(root)
    notebook.grid(row=0, column=0, sticky="ew")

    cars_tab = ttk.Frame(notebook)
    customers_tab = ttk.Frame(notebook)
    notebook.add(cars_tab, text="Cars")
    notebook.add(customers_tab, text="Customers")

    cars_tab.grid_rowconfigure(0, weight=1)
    cars_tab.grid_columnconfigure(0, weight=3)
    cars_tab.grid_columnconfigure(1, weight=1)

    display_frame = ttk.Frame(cars_tab, relief="raised", borderwidth=2)
    display_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    tree = ttk.Treeview(
        display_frame, columns=("ID", "Make", "Model", "Year", "Price"), show="headings"
    )
    tree.heading("ID", text="ID")
    tree.heading("Make", text="Make")
    tree.heading("Model", text="Model")
    tree.heading("Year", text="Year")
    tree.heading("Price", text="Price")
    tree.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    scrollbar = ttk.Scrollbar(display_frame, orient="vertical", command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    tree.configure(yscrollcommand=scrollbar.set)

    display_frame.grid_rowconfigure(0, weight=1)
    display_frame.grid_columnconfigure(0, weight=1)

    crud_frame = ttk.Frame(cars_tab)
    crud_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

    # def adding_car():
    #     return add_car(tree)

    ttk.Button(crud_frame, command= lambda: add_car(tree), text="Add New Car").grid(
        row=0, column=0, pady=10, padx=5, sticky="ew"
    )
    ttk.Button(crud_frame, text="Edit Selected Car").grid(
        row=1, column=0, pady=10, padx=5, sticky="ew"
    )
    ttk.Button(crud_frame, text="Delete Selected Car").grid(
        row=2, column=0, pady=10, padx=5, sticky="ew"
    )
    ttk.Button(crud_frame, text="Refresh List").grid(
        row=3, column=0, pady=10, padx=5, sticky="ew"
    )

    return root


def add_car(tree):
    window = tk.Toplevel()
    window.title("Add new car")
    window.geometry("300x250")

    ttk.Label(window, text="Make: ").grid(row=0, column=0, padx=5, pady=5)
    make_input = ttk.Entry(window)
    make_input.grid(row=0, column=1)

    ttk.Label(window, text="Model: ").grid(row=1, column=0, padx=5, pady=5)
    model_input = ttk.Entry(window)
    model_input.grid(row=1, column=1)

    ttk.Label(window, text="Year: ").grid(row=2, column=0, padx=5, pady=5)
    year_input = ttk.Entry(window)
    year_input.grid(row=2, column=1)

    ttk.Label(window, text="Price: ").grid(row=3, column=0, padx=5, pady=5)
    price_input = ttk.Entry(window)
    price_input.grid(row=3, column=1)

    def save_car():
        make = make_input.get()
        model = model_input.get()
        year = year_input.get()
        price = price_input.get()

        if not all([make, model, year, price]):
            messagebox.showerror("Error", "Fill all fields")
            return

        try:
            try:
                with open('cars.csv', 'r') as file:
                    reader = csv.reader(file)
                    next(reader)

                    cars = list(reader)
                    next_id = str(len(cars) + 1)
            except FileNotFoundError:
                with open('cars.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Make", "Model", "Year", "Price"])
                    next_id = "1"
            
            with open('cars.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([next_id, make, model, year, price])
            
            tree.insert('', 'end', values=(next_id, make, model, year, price))
            messagebox.showinfo("Succcess", "Car added successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error occured: {str(e)}")
    
    ttk.Button(window, text='Save car', command=save_car).grid(row=4, column=0,
        columnspan=2, pady=20)

def main():
    root = create_main_window()
    root.mainloop()


if __name__ == "__main__":
    main()
