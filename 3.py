import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Label, PhotoImage# Import Label and PhotoImage
from PIL import Image, ImageTk




# Create a connection to MySQL
conn = mysql.connector.connect(
  host='localhost',
  user='root',
  password='root',
  database='project' # Use the 'project' database
)

# Create a cursor object
cursor = conn.cursor()

# Create the 'items' table if it doesn't exist
cursor.execute('''
  CREATE TABLE IF NOT EXISTS items (
    itemno INT PRIMARY KEY,
    item_name VARCHAR(255),
    quantity INT,
    unit_price FLOAT,
    expiry_date DATE,
    sale_price FLOAT
  )
''')

# Create the main tkinter window
root = tk.Tk()
root.title("Grocery Store Management")
root.geometry("1000x700")

# Create a login frame
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0, padx=10, pady=10)
bg=tk.PhotoImage(file="xyz.png")
x=tk.Label(root,image=bg)
x.place()


# Function to log in as an administrator
def login_administrator():
  username = username_entry.get()
  password = password_entry.get()

  if username == "admin" and password == "admin":
    messagebox.showinfo("Success", "Administrator logged in successfully.")
    show_admin_menu()
  else:
    messagebox.showinfo("Error", "Invalid username or password.")

# Create widgets for logging in
username_label = ttk.Label(main_frame, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = ttk.Entry(main_frame)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = ttk.Label(main_frame, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = ttk.Entry(main_frame, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

login_button = ttk.Button(main_frame, text="Login", command=login_administrator)
login_button.grid(row=2, columnspan=2, pady=10)

# Function to show the administrator's menu
# Create widgets for adding items
show_billed_frame = ttk.Frame(root)
show_billed_frame.grid(row=1, column=0, padx=10, pady=10)

def show_admin_menu():
    main_frame.destroy()

  # Create a Notebook widget to organize different sections
    notebook = ttk.Notebook(root)
    notebook.place( expand='yes')



    

    def add_item():
        item_name = item_name_entry.get()
        quantity = quantity_entry.get()
        unit_price = unit_price_entry.get()
        item_no = item_no_entry.get()
        exp_date = exp_date_entry.get()
        sale_price = sale_price_entry.get()

        query = "INSERT INTO items VALUES (%s, %s, %s, %s, %s, %s)"
        values = (item_no, item_name, quantity, unit_price, exp_date, sale_price)

        try:
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Success", "Item added successfully.")
        except mysql.connector.IntegrityError:
            messagebox.showinfo("Warning", "Item already exists. Updating quantity...")
            cursor.execute("UPDATE items SET quantity = quantity + %s WHERE itemno = %s", (quantity, item_no))
            conn.commit()

    add_item_frame = ttk.Frame(root)
    notebook.add(add_item_frame, text='Add Item')

    item_name_label = ttk.Label(add_item_frame, text="Product Name:")
    item_name_label.grid(row=0, column=0, padx=10, pady=5)
    item_name_entry = ttk.Entry(add_item_frame)
    item_name_entry.grid(row=0, column=1, padx=10, pady=5)

    quantity_label = ttk.Label(add_item_frame, text="Quantity:")
    quantity_label.grid(row=1, column=0, padx=10, pady=5)
    quantity_entry = ttk.Entry(add_item_frame)
    quantity_entry.grid(row=1, column=1, padx=10, pady=5)

    unit_price_label = ttk.Label(add_item_frame, text="Unit Price:")
    unit_price_label.grid(row=2, column=0, padx=10, pady=5)
    unit_price_entry = ttk.Entry(add_item_frame)
    unit_price_entry.grid(row=2, column=1, padx=10, pady=5)

    item_no_label = ttk.Label(add_item_frame, text="Item No:")
    item_no_label.grid(row=3, column=0, padx=10, pady=5)
    item_no_entry = ttk.Entry(add_item_frame)
    item_no_entry.grid(row=3, column=1, padx=10, pady=5)

    exp_date_label = ttk.Label(add_item_frame, text="Expiry Date (yy/mm/dd):")
    exp_date_label.grid(row=4, column=0, padx=10, pady=5)
    exp_date_entry = ttk.Entry(add_item_frame)
    exp_date_entry.grid(row=4, column=1, padx=10, pady=5)

    sale_price_label = ttk.Label(add_item_frame, text="Sale Price:")
    sale_price_label.grid(row=5, column=0, padx=10, pady=5)
    sale_price_entry = ttk.Entry(add_item_frame)
    sale_price_entry.grid(row=5, column=1, padx=10, pady=5)

    add_button = ttk.Button(add_item_frame, text="Add Item", command=add_item)
    add_button.grid(row=6, columnspan=2, pady=10)

    # Create widgets for showing stock
    # Create a Treeview widget to display stock in a table
    stock_treeview = ttk.Treeview(notebook, columns=("itemno", "item_name", "quantity", "unit_price", "expiry_date", "sale_price"))
    notebook.add(stock_treeview, text='Show Stock')

    # Define columns for the table
    stock_treeview.heading("#1", text="Item No")
    stock_treeview.heading("#2", text="Item Name")
    stock_treeview.heading("#3", text="Quantity")
    stock_treeview.heading("#4", text="Unit Price")
    stock_treeview.heading("#5", text="Expiry Date")
    stock_treeview.heading("#6", text="Sale Price")

    # Set column widths
    stock_treeview.column("#1", width=100)
    stock_treeview.column("#2", width=200)
    stock_treeview.column("#3", width=100)
    stock_treeview.column("#4", width=100)
    stock_treeview.column("#5", width=150)
    stock_treeview.column("#6", width=100)

    # Function to populate the table with stock data
    def show_stock():
        stock_treeview.delete(*stock_treeview.get_children())  # Clear the table
        cursor.execute("SELECT * FROM items")
        result = cursor.fetchall()
        for row in result:
            stock_treeview.insert("", "end", values=row)

    show_stock_button = ttk.Button(stock_treeview, text="Show Stock", command=show_stock)
    show_stock_button.grid(row=0, column=0, pady=10)

    # Function to remove items from the database
    def remove_item():
        item_no = int(item_no_remove_entry.get())
        qty = int(quantity_remove_entry.get())

        cursor.execute("SELECT quantity FROM items WHERE itemno = %s", (item_no,))
        current_qty = cursor.fetchone()

        if current_qty and current_qty[0] >= qty:
            cursor.execute("UPDATE items SET quantity = quantity - %s WHERE itemno = %s", (qty, item_no))
            conn.commit()
            messagebox.showinfo("Success", "Item removed successfully.")
        else:
            messagebox.showinfo("Warning", "Item does not exist or quantity is insufficient.")

    remove_item_frame = ttk.Frame(root)
    notebook.add(remove_item_frame, text='Remove Item')

    item_no_remove_label = ttk.Label(remove_item_frame, text="Item No to Remove:")
    item_no_remove_label.grid(row=0, column=0, padx=10, pady=5)
    item_no_remove_entry = ttk.Entry(remove_item_frame)
    item_no_remove_entry.grid(row=0, column=1, padx=10, pady=5)

# ... (previous code)

# Function to modify an item by itemno
    def modify_item():
        item_no = item_no_modify_entry.get()
        new_quantity = new_quantity_entry.get()
        new_unit_price = new_unit_price_entry.get()
        new_exp_date = new_exp_date_entry.get()
        new_sale_price = new_sale_price_entry.get()

        query = "UPDATE items SET quantity = %s, unit_price = %s, expiry_date = %s, sale_price = %s WHERE itemno = %s"
        values = (new_quantity, new_unit_price, new_exp_date, new_sale_price, item_no)

        cursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Success", f"Item {item_no} modified successfully.")

# Create widgets for modifying items
    modify_item_frame = ttk.Frame(root)
    notebook.add(modify_item_frame, text='Modify Item')

    item_no_modify_label = ttk.Label(modify_item_frame, text="Item No to Modify:")
    item_no_modify_label.grid(row=0, column=0, padx=10, pady=5)
    item_no_modify_entry = ttk.Entry(modify_item_frame)
    item_no_modify_entry.grid(row=0, column=1, padx=10, pady=5)

    new_quantity_label = ttk.Label(modify_item_frame, text="New Quantity:")
    new_quantity_label.grid(row=1, column=0, padx=10, pady=5)
    new_quantity_entry = ttk.Entry(modify_item_frame)
    new_quantity_entry.grid(row=1, column=1, padx=10, pady=5)

    new_unit_price_label = ttk.Label(modify_item_frame, text="New Unit Price:")
    new_unit_price_label.grid(row=2, column=0, padx=10, pady=5)
    new_unit_price_entry = ttk.Entry(modify_item_frame)
    new_unit_price_entry.grid(row=2, column=1, padx=10, pady=5)

    new_exp_date_label = ttk.Label(modify_item_frame, text="New Expiry Date (yy/mm/dd):")
    new_exp_date_label.grid(row=3, column=0, padx=10, pady=5)
    new_exp_date_entry = ttk.Entry(modify_item_frame)
    new_exp_date_entry.grid(row=3, column=1, padx=10, pady=5)

    new_sale_price_label = ttk.Label(modify_item_frame, text="New Sale Price:")
    new_sale_price_label.grid(row=4, column=0, padx=10, pady=5)
    new_sale_price_entry = ttk.Entry(modify_item_frame)
    new_sale_price_entry.grid(row=4, column=1, padx=10, pady=5)

    modify_button = ttk.Button(modify_item_frame, text="Modify Item", command=modify_item)
    modify_button.grid(row=5, columnspan=2, pady=10)
    


    
# Create a new frame for displaying billed items
  

# Function to show previously billed items


# ... (remaining code)

# Run the main tkinter loop
root.mainloop()


# Run the main tkinter loop
root.mainloop()



