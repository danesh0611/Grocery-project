

import mysql.connector
a = mysql.connector.connect(host="localhost", user="root", passwd="root")
m = a.cursor()
m.execute("use grocery")



def add():
    while True:
        y=input("enter product name")
        jxx=y.get()
        z=int(input("enter itemno"))
        b=int(input("enter quantity"))
        c=float(input("enter unit price"))
        query = "INSERT INTO items(sno, item_name, quantity, unit_price) VALUES (%s, %s, %s, %s)"
        jxx=tkinter.Entry(width=100)
        values = (z, y, b, c)
        m.execute(query, values)
        a.commit()
        print("if you want to continue")
        n=input()
        if n=='yes':
            continue
        if n=='no':
            break
def show_stock():
    m.execute("select*from items")
    r=m.fetchall()
    print('sno, item_name, quantity, unit_price')
    column_names = [desc[0] for desc in m.description]
    print(column_names)
    print(r)
   
import tkinter as tk
root = tk.Tk()
root.title("grocery manager")
label=tk.Label(root,text='welcome to grocery manager the one and only best app')
label.pack()



button = tk.Button(root, text="add", command=add)
button.pack()
button2 = tk.Button(root, text="show stock", command=show_stock)
button2.pack()


    
    

    
    





