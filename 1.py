import pandas as pd
d1=pd.read_csv("C:\Users\babu\Desktop\project\Book2.csv")
def accept():
    a=input("enter product name")
    b=float(input("enter gst"))
    c=int(input("unit price"))
    d=int(input("enter qty"))
def add():
    accept()
    m=pd.DataFrame([a,b,c,d])
    print(m)
a=input("enter function")
if a="add":
    add()
    
