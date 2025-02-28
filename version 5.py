import tkinter as tk
from tkinter import messagebox
import mysql.connector



    # Create the main window (root)
root = tk.Tk()

    # ... (rest of your code)

    # Start the Tkinter event loop
root.mainloop()



def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def submit_login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showinfo("Error", "Please fill in all fields.")

    else:
        # Verify the login credentials with the database
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            # Login successful, destroy the login frame and show the administrator's menu
            login_frame.destroy()
            show_admin_menu()

        else:
            messagebox.showinfo("Error", "Invalid username or password.")

def show_admin_menu():
    global admin_menu_frame
   
    admin_menu_frame = tk.Frame(root, bg="white")
    admin_menu_frame.place(relx=0.5, rely=0.2, relwidth=0.4, relheight=0.6, anchor="n")

    # Create buttons for adding a purchase entry, adding a sale entry, showing stock, and going back to the login menu
    purchase_entry_button = tk.Button(admin_menu_frame, text="Add Purchase Entry", command=add_purchase_entry, **common_style)
    purchase_entry_button.pack(pady=10)

    sale_entry_button = tk.Button(admin_menu_frame, text="Add Sale Entry", command=add_sale_entry, **common_style)
    sale_entry_button.pack(pady=10)

    show_stock_button = tk.Button(admin_menu_frame, text="Show Stock", command=show_stock, **common_style)
    show_stock_button.pack(pady=10)

    # No back button since the administrator should always be able to log out and go back to the login menu

    frames.append(admin_menu_frame)


def add_purchase_entry():
    # Your code for adding a purchase entry
    pass

def add_sale_entry():
    pass
   # Your code for adding a sale entry


def show_stock():
    # Your code for showing stock
    pass





# Function to run the program
def run_program():
    
    root.mainloop()


if __name__ == "__main__":
    run_program()

# Create widgets for the customer portal
def show_customer_menu():
    customer_login_frame.destroy() # Destroy the login frame
    customer_menu_frame = tk.Frame(root, bg="xyz.png")
    customer_menu_frame.place(relx=0.5, rely=0.2, relwidth=0.4, relheight=0.6, anchor="n")

    # Create a back button for the customer menu
   

    # Add other customer-related functionality here

    frames.append(customer_menu_frame) # Add the customer menu frame to the frames list

    # ... (Customer portal code)

      # Add the customer menu frame to the frames list



root.mainloop()





# Function to add a purchase entry


# ... (Rest of your code)

root.mainloop()
