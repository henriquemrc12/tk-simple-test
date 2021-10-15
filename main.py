import sqlite3 
import os, time
from datetime import datetime
from tkinter import *

title = "Comida majestosa Gestão"
now = datetime.now()
root = Tk()
width = 800
height = 800

class User:
    id: 1
    name: "default"
    email: "email"

class Sale:
    id: 1
    date: "default"
    total: 0

def migrations():
    connection = sqlite3.connect("comida_majestosa_gestao")
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sale (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                date DATETIME NOT NULL,
                total DECIMAL(19,2) NOT NULL);
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(45) NOT NULL,
                email VARCHAR(45) NOT NULL,
                password VARCHAR(45) NOT NULL);
        """)
        print("[ " + now.strftime("%H:%M:%S") + " ] - " + "Migrations executada com sucesso")
    except NameError:
        print("[ " + now.strftime("%H:%M:%S") + " ] - " + "Erro ao executar as migrations")
        raise
    finally:
        connection.close()

def createUser(name, email, password):
    connection = sqlite3.connect("comida_majestosa_gestao")
    try:  
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO users (name, email, password)
            VALUES (?,?,?)
        """, (name, email, password))
        connection.commit()
    except NameError:
        print("[ " + now.strftime("%H:%M:%S") + " ] - " + "Erro ao criar usuarios")
        raise
    finally:
        connection.close()

def getAllUsers():
    connection = sqlite3.connect("comida_majestosa_gestao")
    users = list()

    try:  
        cursor = connection.cursor()
        cursor.execute(""" 
            SELECT * FROM users;
        """)
        for line in cursor.fetchall():
            user = User()
            user.id = line[0]
            user.name = line[1]
            user.email = line[2]
            
            users.append(user)
        return users
    except NameError:
        print("[ " + now.strftime("%H:%M:%S") + " ] - " + "Erro ao buscar usuarios")
        raise
    finally:
        connection.close()

def getAllSales():
    connection = sqlite3.connect("comida_majestosa_gestao")
    sales = list()

    try:  
        cursor = connection.cursor()
        cursor.execute(""" 
            SELECT * FROM sale;
        """)
        for line in cursor.fetchall():
            sale = Sale()
            sale.id = line[0]
            sale.date = line[1]
            sale.total = line[2]
            
            sales.append(sale)
        return sales
    except NameError:
        print("[ " + now.strftime("%H:%M:%S") + " ] - " + "Erro ao buscar vendas")
        raise
    finally:
        connection.close()

def createSale(total):
    connection = sqlite3.connect("comida_majestosa_gestao")
    try:  
        cursor = connection.cursor()
        date = now.strftime("%d/%m/%Y - %H:%M:%S")
        cursor.execute("""
            INSERT INTO sale (total, date)
            VALUES (?,?)
        """, (total, date))
        connection.commit()
    except NameError:
        print("[ " + now.strftime("%H:%M:%S") + " ] - " + "Erro ao criar venda")
        raise
    finally:
        connection.close()

def createNewUserScreen():
    newWindow = Tk()
    newWindow.geometry( str(width) + "x" + str(height))

    buttonExample = Button(newWindow, 
              text="Salvar usuario",
              command=createSale)
    buttonExample.pack()
    buttonExample.place(x=(width/2), y=(height/2))
    newWindow.mainloop()

def init():
    migrations()

class Application:
    def __init__(self, master=None):
        buttonExample = Button(root, 
              text="Create new window",
              command=createNewUserScreen)
        buttonExample.pack()

Application(root)
root.title(title)
root.geometry( str(width) + "x" + str(height))
root.mainloop()