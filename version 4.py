import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import Listbox
from tkinter import *
import re


# Create a connection to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='project'  # Use the 'project' database
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

common_style = {"font": ("Arial", 25), "bg": "black","fg":"white", "padx": 10, "pady": 10}
bg_image = tk.PhotoImage(file=r"C:\Users\babu\Desktop\project\bg1.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)


 
# Add image file 


# Function to log in as an administrator
def login_administrator():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "kumar the great":
        messagebox.showinfo("Success", "Administrator logged in successfully.")
        show_admin_menu()
        
    else:
        messagebox.showinfo("Error", "Invalid username or password.")
def customer_portal():
    def show_customer_menu():
        pass
    login_frame.destroy()
    def sign_up():
        usr = username_entry.get()
        pswd = password_entry.get()
        email = email_entry.get()

        # Check username and password conditions
        username_pattern = r"^(?=.*[A-Z]).{5,}$"  # At least one uppercase letter and minimum length of 5 characters
        password_pattern = r"^(?=.*[A-Z])(?=.*[@*$%#]).+$"  # At least one uppercase letter and one of the specified special characters

        if not re.match(username_pattern, usr):
            messagebox.showinfo("Error", "Invalid username. It should contain one uppercase letter and have a minimum length of 5 characters.")
        elif not re.match(password_pattern, pswd):
            messagebox.showinfo("Error", "Invalid password. It should contain one uppercase letter and one of the characters '@', '*', '$', '%', or '#'.")
        else:
            show_customer_menu_
            cursor.execute("CREATE TABLE IF NOT EXISTS USER DETAILS(USERNAME VARCHAR(90) PRIMARY KEY,PASSWORD VARCHAR(90),EMAIL_ID VARCHAR(90))")
            query="insert into USER DETAILS VALUES(%s,%s,%s)"
            values=(usr,pswd,email)
            cursor.execute(query,values)

    def sign_in():
        usr = username_entry.get()
        pswd = password_entry.get()

        cursor.execute("SELECT * FROM USER DETAILS WHERE USERNAME = %s", (usr,))
        result = cursor.fetchone()

        if result is None:
            messagebox.showinfo("Error", "Invalid username. Please try again.")
        elif not result[1] == pswd:
            messagebox.showinfo("Error", "Invalid password. Please try again.")
        else:
            show_customer_menu()
        def show_customer_menu():
            menu = Toplevel(root)
            menu.title("Customer Menu")
            menu.geometry("1000x700")

        def view_account_details():
            cursor.execute("SELECT * FROM USER DETAILS WHERE USERNAME = %s", (usr,))
            result = cursor.fetchone()
            view_account_details_label.config(text=f"Username: {result[0]}\nPassword: {result[1]}\nEmail ID: {result[2]}")

        def update_account_details():
            cursor.execute("UPDATE USER DETAILS SET PASSWORD = %s, EMAIL_ID = %s WHERE USERNAME = %s", (new_password_entry.get(), new_email_entry.get(), usr))
            messagebox.showinfo("Success", "Account details updated successfully.")

        def delete_account():
            cursor.execute("DELETE FROM USER DETAILS WHERE USERNAME = %s", (usr,))
            messagebox.showinfo("Success", "Account deleted successfully.")
            sign_out()

    b1=tk.Button(root,text="sign in",command=sign_in)
    b1.pack()

def customer_login_frame():
    customer_portal_button = tk.Button(root, text="Customer Portal", command=customer_portal)
    customer_portal_button.grid(pady=40)
username_entry=None
password_entry=None
email_entry=None
def admin_login_frame():
    
    
    
    
    global username_entry
    global password_entry
    username_label = ttk.Label(login_frame, text="Username:")
    username_label.grid(row=0, column=0, padx=10, pady=5)
    username_entry = ttk.Entry(login_frame)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = ttk.Label(login_frame, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=5)
    password_entry = ttk.Entry(login_frame, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    login_button = ttk.Button(login_frame, text="Login", command=login_administrator)
    login_button.grid(row=2, columnspan=2, pady=10)                           
                           
        
    
        
      

# Function to set the background image


# Create the login frame


# Create widgets for logging in
login_frame = ttk.Frame(root)
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
button1=tk.Button(login_frame,text="administrator portal",command=admin_login_frame,bg='black',fg='white')
button2=tk.Button(login_frame,text="customer portal",command=customer_login_frame)
button1.grid(row=2, column=0, padx=100, pady=40)
button2.grid(row=3, column=1, padx=60, pady=60)


# Function to show the administrator's menu
def show_admin_menu():
    login_frame.destroy()
    
    


    # Create a Notebook widget to organize different sections
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand='yes')

    # Create widgets for adding items
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

    quantity_remove_label = ttk.Label(remove_item_frame, text="Quantity to Remove:")
    quantity_remove_label.grid(row=1, column=0, padx=10, pady=5)
    quantity_remove_entry = ttk.Entry(remove_item_frame)
    quantity_remove_entry.grid(row=1, column=1, padx=10, pady=5)

    remove_button = ttk.Button(remove_item_frame, text="Remove Item", command=remove_item)
    remove_button.grid(row=2, columnspan=2, pady=10)


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


    

# Create a table for billing information if it doesn't exist
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS bills (
        bill_id INT AUTO_INCREMENT PRIMARY KEY,
        item_no INT,
        item_name VARCHAR(255),
        quantity INT,
        unit_price FLOAT,
        total_price FLOAT
      )
    ''')

# Create a new frame for billing
    billing_frame = ttk.Frame(root)
    notebook.add(billing_frame, text='Billing')

# Create a Listbox to display the bill
    bill_listbox = Listbox(billing_frame, width=60, height=20)
    bill_listbox.grid(row=0, column=0, padx=10, pady=10)

# Create variables to keep track of the current bill
    current_bill = []

# Function to add items to the bill
    def add_to_bill():
        item_no = int(item_no_bill_entry.get())
        quantity = int(quantity_bill_entry.get())
    
        # Fetch item information from the database
        cursor.execute("SELECT item_name, sale_price FROM items WHERE itemno = %s", (item_no,))
        item_info = cursor.fetchone()
    
        if item_info:
            item_name, unit_price = item_info
            total_price = unit_price * quantity
            current_bill.append((item_no, item_name, quantity, unit_price, total_price))
            update_bill_display()
        else:
            messagebox.showinfo("Error", "Item not found in stock.")

# Function to update the bill display
    def update_bill_display():
        bill_listbox.delete(0, 'end')
        total_amount = 0
        for item in current_bill:
            item_no, item_name, quantity, unit_price, total_price = item
            bill_listbox.insert('end', f"{item_name} x{quantity} - ${total_price:.2f}")
            total_amount += total_price
        bill_listbox.insert('end', f"Total: ${total_amount:.2f}")

# Function to clear the current bill
    def clear_bill():
        current_bill.clear()
        update_bill_display()

# Function to save the current bill in the SQL table
    def save_bill():
        for item in current_bill:
            item_no, item_name, quantity, unit_price, total_price = item
            cursor.execute("INSERT INTO bills (item_no, item_name, quantity, unit_price, total_price) VALUES (%s, %s, %s, %s, %s)", (item_no, item_name, quantity, unit_price, total_price))
            conn.commit()
        clear_bill()
        messagebox.showinfo("Success", "Bill saved successfully.")

# Create widgets for billing
    item_no_bill_label = ttk.Label(billing_frame, text="Item No:")
    item_no_bill_label.grid(row=1, column=0, padx=10, pady=5)
    item_no_bill_entry = ttk.Entry(billing_frame)
    item_no_bill_entry.grid(row=1, column=1, padx=10, pady=5)

    quantity_bill_label = ttk.Label(billing_frame, text="Quantity:")
    quantity_bill_label.grid(row=2, column=0, padx=10, pady=5)
    quantity_bill_entry = ttk.Entry(billing_frame)
    quantity_bill_entry.grid(row=2, column=1, padx=10, pady=5)

    add_to_bill_button = ttk.Button(billing_frame, text="Add to Bill", command=add_to_bill)
    add_to_bill_button.grid(row=3, columnspan=2, pady=10)

    clear_bill_button = ttk.Button(billing_frame, text="Clear Bill", command=clear_bill)
    clear_bill_button.grid(row=4, columnspan=2, pady=10)

    save_bill_button = ttk.Button(billing_frame, text="Save Bill", command=save_bill)
    save_bill_button.grid(row=5, columnspan=2, pady=10)

    # Create widgets for sales billing
    
        # Define the add_item_to_bill function in a broader scope
    

# ... (Rest of your code)

# Run the main tkinter loop
root.mainloop()






# Create the sales billing function

# ... (Rest of the code)

# Run the main tkinter loop
root.mainloop()



# Set the background image

# Run the main tkinter loop
root.mainloop()
