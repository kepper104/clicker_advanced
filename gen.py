import tkinter
from tkinter import ttk
import pyautogui
import csv


def close_window(window):
    window.destroy()

def main():
    root = tkinter.Tk()
    root.title("Генератор сценариев")
    root['bg'] = 'lightgray'

    text_header_up = tkinter.Label(root, text="Кликер", font=("Arial Bold", 16), bg='lightgray')
    text_header_up.grid(row=1, column=1)
    text_header_down = tkinter.Label(root, text="Редактор сценариев", font=("Arial Bold", 16), bg='lightgray')
    text_header_down.grid(row=2, column=1)
    # text_header = tkinter.Label(root, text="Кликер",font=("Arial Bold", 16),bg='lightgray') 
    # text_header.grid(row=1,column=1)

    button_create = tkinter.Button(root, text="Создать", command=lambda: create(root))
    button_create.grid(row=3, column=1, pady=5)

    button_delete = tkinter.Button(root, text="Удалить", command=delete)
    button_delete.grid(row=4, column=1)

    button_quit = tkinter.Button(root, text="Выйти", command=lambda: close_window(root))
    button_quit.grid(row=5, column=1, pady=5)

    root.mainloop()

def instruct(window):
    var = tkinter.StringVar()
    instruct_window = tkinter.Toplevel(window, padx=5, pady=5)
    instruct_window.title('Инструкция по пользованию генератором сценариев')
    instruct_window['bg'] = 'lightgray'

    text_header = tkinter.Label(instruct_window, text='Инструкция по пользованию генератором сценариев', font=("Arial Bold", 20), bg='lightgray')
    text_header.grid(row=1, column=1)

    text_body0 = tkinter.Label(instruct_window,text='Если вы нажали сюда, то вам вероятно необходимо создать кликер-сценарий', font=("Arial Bold", 12), bg='lightgray')
    text_body0.grid(row=2,column=1,sticky='w')

    text_body1 = tkinter.Label(instruct_window,text='Кликер-сценарий создается путем последовательного добавления действий', font=("Arial Bold", 12), bg='lightgray')
    text_body1.grid(row=3,column=1,sticky='w')

    text_body2 = tkinter.Label(instruct_window,text='Для начала, вам нужно выбрать устройство - клавиатура или мышь', font=("Arial Bold", 12), bg='lightgray')
    text_body2.grid(row=4,column=1,sticky='w')

    text_body3 = tkinter.Label(instruct_window,text='После этого у вас откроется окно в котором вы должны ввести все параметры действия', font=("Arial Bold", 12), bg='lightgray')
    text_body3.grid(row=5,column=1,sticky='w')

    text_body4 = tkinter.Label(instruct_window,text='Далее нажимаете на кнопку "добавить действие"', font=("Arial Bold", 12), bg='lightgray')
    text_body4.grid(row=6,column=1,sticky='w')

    text_body5 = tkinter.Label(instruct_window,text='Повторяете цикл сколько требуется', font=("Arial Bold", 12), bg='lightgray')
    text_body5.grid(row=7,column=1,sticky='w')

    text_body6 = tkinter.Label(instruct_window,text='В конце нажимаете "создать сценарий"', font=("Arial Bold", 12), bg='lightgray')
    text_body6.grid(row=8,column=1,sticky='w')

    close_button = tkinter.Button(instruct_window,text='Выйти',command=lambda: close_window(instruct_window))
    close_button.grid(row=10,column=1,pady=5)


    instruct_window.mainloop()


def keyboard_add(window):
    keyboard_window = tkinter.Toplevel(window, padx=5, pady=5)
    keyboard_window.title('Добавление действия (клавиатура)')
    keyboard_window['bg'] = 'lightgray'

    close_button = tkinter.Button(keyboard_window,text='Выйти',command=lambda: close_window(keyboard_window))
    close_button.grid(row=10,column=1,pady=5,columnspan=2)

    keyboard_window.mainloop()

def mouse_add(window):
    mouse_window = tkinter.Toplevel(window, padx=5, pady=5)
    mouse_window.title('Добавление действия (мышь)')
    mouse_window['bg'] = 'lightgray'

    close_button = tkinter.Button(mouse_window,text='Выйти',command=lambda: close_window(mouse_window))
    close_button.grid(row=10,column=1,pady=5,columnspan=2)

    mouse_window.mainloop()

def create_scenario(label):
    file_name = 'лол'
    label.configure(text=('Создан клик-сценарий: ' + file_name))


def create(root):
    create_window = tkinter.Toplevel(root, padx=5, pady=5)
    create_window.title('Создание сценария')
    create_window['bg'] = 'lightgray'

    text_header = tkinter.Label(create_window, text="Создание сценария", font=("Arial Bold", 18), bg='lightgray')
    text_header.grid(row=1,column=1,columnspan=2)

    button_quit = tkinter.Button(create_window, text="Инструкция", command=lambda: instruct(create_window))
    button_quit.grid(row=2,column=1,pady=5,columnspan=2)

    keyboard_button = tkinter.Button(create_window,text='Клавиатура',command=lambda: keyboard_add(create_window))
    keyboard_button.grid(row=3,column=1)

    mouse_button = tkinter.Button(create_window,text='Мышка',command=lambda: mouse_add(create_window))
    mouse_button.grid(row=3,column=2,pady=5)

    created_label = tkinter.Label(create_window,text='', font=("Arial Bold", 10), bg='lightgray')
    created_label.grid(row=5,column=1,columnspan=2)

    create_button = tkinter.Button(create_window,text='Создать клик-сценарий',command=lambda: create_scenario(created_label))
    create_button.grid(row=4,column=1,columnspan=2)

    close_button = tkinter.Button(create_window,text='Выйти',command=lambda: close_window(create_window))
    close_button.grid(row=10,column=1,pady=5,columnspan=2)

    # text1 = tkinter.Label(create_window, text="Название", font=("Arial Bold", 13), bg='lightgray')
    # text1.grid(row=2, column=1)

    # name_entry = tkinter.Entry(create_window, bg='lightgray')
    # name_entry.grid(row=2, column=2)

    # text2 = tkinter.Label(create_window, text="Тип устройства", font=("Arial Bold", 13), bg='lightgray')
    # text2.grid(row=2, column=1)

    # combo1 = ttk.Combobox(create_window, textvariable=var)
    # combo1['values'] = ('Keyboard', 'Mouse')
    # combo1['state'] = 'readonly'
    # combo1.grid(row=2, column=2)

    # text2 = tkinter.Label(create_window, text="Тип действия", font=("Arial Bold", 13), bg='lightgray')
    # text2.grid(row=3, column=1)

    # combo1 = ttk.Combobox(create_window, textvariable=var)
    # combo1['values'] = ('Нажатие(Для клавиатуры)', 'Фраза(Для клавиатуры)', 'Хоткей(Для клавиатуры)', 'Зажать(Для клавиатуры)', 'Отпустить(Для клавиатуры)','Кликнуть(Для мышки)', 'Передвинуть(Для мышки)')
    # combo1['state'] = 'readonly'
    # combo1.grid(row=3, column=2)

    create_window.mainloop()

def delete():
    print('deleted')

if __name__ == "__main__":
    main()