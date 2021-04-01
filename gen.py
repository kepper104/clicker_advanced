import tkinter
from tkinter import ttk
import pyautogui
import csv

def main():

    root = tkinter.Tk()
    root.title("Генератор сценариев")
    root['bg'] = 'lightgray'

    text_header_up = tkinter.Label(root, text="Кликер",font=("Arial Bold", 16),bg='lightgray') 
    text_header_up.grid(row=1,column=1)
    text_header_down = tkinter.Label(root, text="Создание сценариев",font=("Arial Bold", 16),bg='lightgray') 
    text_header_down.grid(row=2,column=1)
    # text_header = tkinter.Label(root, text="Кликер",font=("Arial Bold", 16),bg='lightgray') 
    # text_header.grid(row=1,column=1)

    button_create = tkinter.Button(root,text="Создать",command=create)
    button_create.grid(row=3,column=1,pady=5)

    button_delete = tkinter.Button(root,text="Удалить",command=delete)
    button_delete.grid(row=4,column=1)

    button_quit = tkinter.Button(root,text="Выйти",command=quit)
    button_quit.grid(row=5,column=1,pady=5)

    root.mainloop()

def create():
    print('created')

def delete():
    print('deleted')

def quit():
    print('quit')
    exit(0)



if __name__ == "__main__":
    main()