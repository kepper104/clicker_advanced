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
    text_header_down = tkinter.Label(root, text="Редактор сценариев",font=("Arial Bold", 16),bg='lightgray') 
    text_header_down.grid(row=2,column=1)
    # text_header = tkinter.Label(root, text="Кликер",font=("Arial Bold", 16),bg='lightgray') 
    # text_header.grid(row=1,column=1)

    button_create = tkinter.Button(root,text="Создать",command=lambda: create(root))
    button_create.grid(row=3,column=1,pady=5)

    button_delete = tkinter.Button(root,text="Удалить",command=delete)
    button_delete.grid(row=4,column=1)

    button_quit = tkinter.Button(root,text="Выйти",command=quit)
    button_quit.grid(row=5,column=1,pady=5)

    root.mainloop()

def create(root):
    var = tkinter.StringVar()
    createWindow = tkinter.Toplevel(root,padx=5,pady=5)     
    createWindow.title('Создание сценария')
    createWindow['bg'] = 'lightgray'
    
    text_header = tkinter.Label(createWindow, text="Создание сценария",font=("Arial Bold", 18),bg='lightgray') 
    text_header.grid(row=1,column=1,columnspan=2)

    text1 = tkinter.Label(createWindow, text="Название",font=("Arial Bold", 13),bg='lightgray') 
    text1.grid(row=2,column=1)

    name_entry = tkinter.Entry(createWindow,bg='lightgray')
    name_entry.grid(row=2,column=2)

    text2 = tkinter.Label(createWindow, text="Тип устройства",font=("Arial Bold", 13),bg='lightgray') 
    text2.grid(row=2,column=1)

    combo1 = ttk.Combobox(createWindow,bg='lightgray',textvariable=var)
    combo1['values'] = ('keyboard','mouse')
    combo1['state'] = 'readonly'
    combo1.grid(row=2,column=2)



    
    createWindow.mainloop()


def delete():
    print('deleted')

def quit():
    print('quit')
    exit(0)



if __name__ == "__main__":
    main()