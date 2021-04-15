import tkinter
from tkinter import ttk
from tkinter import messagebox
import pyautogui
import csv

all = {'0','1','2','3','4','5','6','7','8','9'}
global_list = []


def callbackFunc(event):
    global type_var_button
    button_type = tkinter.StringVar()
    if type_var_button.get() == 'Клик':

        num_label = tkinter.Label(mouse_window,text='Кнопка', font=("Arial Bold", 13), bg='lightgray')
        num_label.grid(row=2,column=1)

        button_combo = ttk.Combobox(mouse_window,textvariable=button_type)
        button_combo['values'] = ('Правая','Левая','Колесико')
        button_combo['state'] = 'readonly'
        button_combo.grid(row=2,column=2)

        x_label = tkinter.Label(mouse_window,text='Координата x', font=("Arial Bold", 13), bg='lightgray')
        x_label.grid(row=3,column=1)

        size = pyautogui.size()

        x_spin = tkinter.Spinbox(mouse_window,from_=-1,to=size[0],bg='lightgray')
        x_spin.grid(row=3,column=2)

        y_label = tkinter.Label(mouse_window,text='Координата y', font=("Arial Bold", 13), bg='lightgray')
        y_label.grid(row=4,column=1)
        
        y_spin = tkinter.Spinbox(mouse_window,from_=-1,to=size[1],bg='lightgray')
        y_spin.grid(row=4,column=2)

        add_button = tkinter.Button(mouse_window,text='Добавить действие',command=lambda: add_action(mouse_window,type_var_button.get(),button_type.get(),x_spin.get(),y_spin.get()))
        add_button.grid(row=5,column=1,columnspan=2)

    if type_var_button.get() == 'Сдвинуть':

        x_label = tkinter.Label(mouse_window,text='Координата x', font=("Arial Bold", 13), bg='lightgray')
        x_label.grid(row=2,column=1)

        size = pyautogui.size()

        x_spin = tkinter.Spinbox(mouse_window,from_=0,to=size[0],bg='lightgray')
        x_spin.grid(row=2,column=2)

        y_label = tkinter.Label(mouse_window,text='Координата y', font=("Arial Bold", 13), bg='lightgray')
        y_label.grid(row=3,column=1)
        
        y_spin = tkinter.Spinbox(mouse_window,from_=0,to=size[1],bg='lightgray')
        y_spin.grid(row=3,column=2)

        add_button = tkinter.Button(mouse_window,text='Добавить действие',command=lambda: add_action(mouse_window,type_var_button.get(),'move',x_spin.get(),y_spin.get()))
        add_button.grid(row=4,column=1,columnspan=2)

def pause_add(window):
    pause_window = tkinter.Toplevel(window, padx=5, pady=5)
    pause_window.title('Добавление паузы')
    pause_window['bg'] = 'lightgray'

    num_label = tkinter.Label(pause_window,text='Продолжительность паузы', font=("Arial Bold", 13), bg='lightgray')
    num_label.grid(row=1,column=1)

    num_spin = tkinter.Spinbox(pause_window,from_=0,to=9999,bg='lightgray')
    num_spin.grid(row=1,column=2)

    add_button = tkinter.Button(pause_window,text='Добавить действие',command=lambda: add_action(pause_window,'pause',' ',num_spin.get(),' '))
    add_button.grid(row=2,column=1,columnspan=2)

def close_window(window):
    window.destroy()

def main():
    root = tkinter.Tk()
    root.title("Генератор сценариев")
    root['bg'] = 'lightgray'


    text_header_up = tkinter.Label(root, text="Кликер", font=("Arial Bold", 20), bg='lightgray')
    text_header_up.grid(row=1, column=1)
    text_header_down = tkinter.Label(root, text="Редактор сценариев", font=("Arial Bold", 16), bg='lightgray')
    text_header_down.grid(row=2, column=1)

    button_create = tkinter.Button(root, text="Создать", command=lambda: create(root))
    button_create.grid(row=3, column=1, pady=5)

    button_delete = tkinter.Button(root, text="Удалить", command=lambda: delete(root))
    button_delete.grid(row=4, column=1)

    button_quit = tkinter.Button(root, text="Выйти", command=lambda: close_window(root))
    button_quit.grid(row=5, column=1, pady=5)


    root.mainloop()

def instruct(window):
    instruct_window = tkinter.Toplevel(window, padx=5, pady=5)
    instruct_window.title('Инструкция по пользованию генератором сценариев')
    instruct_window['bg'] = 'lightgray'

    text_header = tkinter.Label(instruct_window, text='Инструкция по пользованию генератором сценариев', font=("Arial Bold", 20), bg='lightgray')
    text_header.grid(row=1, column=1)

    text_body0 = tkinter.Label(instruct_window,text='Если вы нажали сюда, то вам вероятно необходимо создать кликер-сценарий', font=("Arial Bold", 12), bg='lightgray')
    text_body0.grid(row=2,column=1,sticky='w')

    text_body1 = tkinter.Label(instruct_window,text='Кликер-сценарий создается путем последовательного добавления действий', font=("Arial Bold", 12), bg='lightgray')
    text_body1.grid(row=3,column=1,sticky='w')

    text_body2 = tkinter.Label(instruct_window,text='Для начала, вам нужно выбрать устройство - клавиатура или мышь (или пауза)', font=("Arial Bold", 12), bg='lightgray')
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


def add_action(window,type,symbol,num,delay):
    global global_list
    close_window(window)
    print('added')
    if type == 'Нажатие':
        type = 'press'
    elif type == 'Фраза':
        type = 'phrase'
    elif type == 'Хоткей':
        type = 'hotkey'
    elif type == 'Зажать':
        type = 'hold'
    elif type == 'Отпустить':
        type = 'unhold'
    elif type == 'Сдвинуть':
        type = 'move'
    elif type == 'Клик':
        type = 'click'
    if symbol == 'Правая':
        symbol = 'right'
    elif symbol == 'Левая':
        symbol = 'left'
    elif symbol == 'Колесико':
        symbol = 'wheel'
    cur_row = [type,symbol,num,delay]
    global_list.append(cur_row)

def keyboard_add(window):
    type_var = tkinter.StringVar()
    keyboard_window = tkinter.Toplevel(window, padx=5, pady=5)
    keyboard_window.title('Добавление действия (клавиатура)')
    keyboard_window['bg'] = 'lightgray'

    type_label = tkinter.Label(keyboard_window,text='Тип действия', font=("Arial Bold", 13), bg='lightgray')
    type_label.grid(row=1,column=1)

    type_combo = ttk.Combobox(keyboard_window,textvariable=type_var)
    type_combo['values'] = ('Нажатие', 'Фраза', 'Хоткей', 'Зажать', 'Отпустить')
    type_combo['state'] = 'readonly'
    type_combo.grid(row=1,column=2)

    symbol_label = tkinter.Label(keyboard_window,text='Клавиша', font=("Arial Bold", 13), bg='lightgray')
    symbol_label.grid(row=2,column=1)

    symbol_entry = tkinter.Entry(keyboard_window,bg='lightgray')
    symbol_entry.grid(row=2,column=2)

    num_label = tkinter.Label(keyboard_window,text='Количество повторов', font=("Arial Bold", 13), bg='lightgray')
    num_label.grid(row=3,column=1)

    num_spin = tkinter.Spinbox(keyboard_window,from_=0,to=9999,bg='lightgray')
    num_spin.grid(row=3,column=2)

    delay_label = tkinter.Label(keyboard_window,text='Задержка', font=("Arial Bold", 13), bg='lightgray')
    delay_label.grid(row=4,column=1)

    delay_spin = tkinter.Spinbox(keyboard_window,from_=0,to=60,bg='lightgray')
    delay_spin.grid(row=4,column=2)

    add_button = tkinter.Button(keyboard_window,text='Добавить действие',command=lambda: add_action(keyboard_window,type_var.get(),symbol_entry.get(),num_spin.get(),delay_spin.get()))
    add_button.grid(row=5,column=1,columnspan=2)

    # close_button = tkinter.Button(keyboard_window,text='Выйти',command=lambda: close_window(keyboard_window))
    # close_button.grid(row=10,column=1,pady=5,columnspan=2)

    keyboard_window.mainloop()

def mouse_add(window):
    global type_var_button
    global mouse_window
    type_var_button = tkinter.StringVar()
    mouse_window = tkinter.Toplevel(window, padx=5, pady=5)
    mouse_window.title('Добавление действия (мышь)')
    mouse_window['bg'] = 'lightgray'

    type_label = tkinter.Label(mouse_window,text='Тип действия', font=("Arial Bold", 13), bg='lightgray')
    type_label.grid(row=1,column=1)

    type_combo = ttk.Combobox(mouse_window,textvariable=type_var_button)
    type_combo['values'] = ('Клик', 'Сдвинуть')
    type_combo['state'] = 'readonly'
    type_combo.grid(row=1,column=2)

    

    # close_button = tkinter.Button(mouse_window,text='Выйти',command=lambda: close_window(mouse_window))
    # close_button.grid(row=10,column=1,pady=5,columnspan=2)

    type_combo.bind("<<ComboboxSelected>>", callbackFunc)

    mouse_window.mainloop()

def create_scenario(window):
    global global_list
    try:
        c = []
        with open('file_count.csv','r') as file_count:
            cur_count = file_count.read()
            a = set(cur_count)
            a.remove(';')
            b = all ^ a
            for i in b:
                c.append(int(i))
            count = min(c)
            file_name = 'scenario_' + str(count) + '.csv'
        with open('file_count.csv','a') as file_count:
            file_count.write((str(count) + ';'))
    except:
        with open('file_count.csv','w') as file_count:
            file_count.write('0;')
            file_name = 'scenario_' + '0' + '.csv'
    
    close_window(window)
    with open(file_name,'w') as file:
        for j in global_list:
            for k in j:
                file.write(k)
                file.write(';')
            file.write('\n')
    
    message = 'Клик-сценарий "' + file_name + '" успешно создан'
    mb = messagebox.showinfo(title='Успешно',message=message)


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

    pause_button = tkinter.Button(create_window, text="Пауза",command=lambda: pause_add(create_window))
    pause_button.grid(row=4,column=1,columnspan=2)

    # created_label = tkinter.Label(create_window,text='', font=("Arial Bold", 10), bg='lightgray')
    # created_label.grid(row=5,column=1,columnspan=2)

    create_button = tkinter.Button(create_window,text='Создать клик-сценарий',command=lambda: create_scenario(create_window))
    create_button.grid(row=5,column=1,columnspan=2,pady=5)

    create_window.mainloop()

def delete(window):
    delete_window = tkinter.Toplevel(window)
    delete_window.title('Удаление сценариев')
    delete_window['bg'] = 'lightgray'

    button_quit = tkinter.Button(delete_window, text="Выйти", command=lambda: close_window(delete_window))
    button_quit.grid(row=5, column=1)


    delete_window.mainloop()

if __name__ == "__main__":
    main()