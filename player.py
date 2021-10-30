import tkinter
from tkinter import ttk
from tkinter import messagebox
import pyautogui
import csv
from glob import glob
import os
btn_var = ''
values = (' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
          'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright')


def close_window(window):
    window.destroy()


def execute(file_name):
    print(file_name)


def select(window):
    cur_row = 2
    select_window = tkinter.Toplevel(window, padx=5, pady=5)
    select_window.title('Выбор сценария')
    select_window['bg'] = 'lightgray'
    choose_label = tkinter.Label(
        select_window, text="Выберите сценарий", font=("Arial Bold", 20), bg='lightgray')
    choose_label.grid(row=1, column=1, columnspan=2)
    path = os.getcwd()
    path += "/*.csv"
    files_user = []
    files = glob(path)
    # print(files)
    for i in files:
        if "file_count" in i:
            files.pop(files.index(i))

    for i in files:
        a = i[-14:]
        files_user.append(a)
    for i in files_user:
        tkinter.Button(select_window, text=i, command=lambda: execute(i)).grid(
            row=cur_row, column=1, columnspan=2, pady=5)
        cur_row += 1

    select_window.mainloop()


def settings(window):
    global btn_var, delay_spin
    global cur_combo

    btn_var = tkinter.StringVar()
    cur_combo = btn_var.get()

    settings_window = tkinter.Toplevel(window, padx=5, pady=5)
    settings_window.title('Добавление паузы')
    settings_window['bg'] = 'lightgray'

    text_header = tkinter.Label(
        settings_window, text="Настройки", font=("Arial Bold", 20), bg='lightgray')
    text_header.grid(row=1, column=1, columnspan=2)

    delay_label = tkinter.Label(settings_window, text="Задержка перед стартом", font=(
        "Arial Bold", 16), bg='lightgray')
    delay_label.grid(row=2, column=1)

    delay_spin = tkinter.Spinbox(
        settings_window, from_=0, to=100, bg='lightgray')
    delay_spin.grid(row=2, column=2)

    ender_label = tkinter.Label(settings_window, text="Клавиша завершения", font=(
        "Arial Bold", 16), bg='lightgray')
    ender_label.grid(row=3, column=1)

    btn_combo = ttk.Combobox(settings_window, textvariable=btn_var)
    btn_combo['values'] = values
    btn_combo['state'] = 'readonly'
    # btn_combo.current(cur_combo)
    btn_combo.grid(row=3, column=2)

    button_quit = tkinter.Button(
        settings_window, text="Сохранить", command=lambda: close_window(settings_window))
    button_quit.grid(row=5, column=1, pady=5, columnspan=2)

    settings_window.mainloop()


def main():

    global root
    root = tkinter.Tk()
    root.title("Генератор сценариев")
    root['bg'] = 'lightgray'

    text_header_up = tkinter.Label(
        root, text="Кликер", font=("Arial Bold", 20), bg='lightgray')
    text_header_up.grid(row=1, column=1)
    text_header_down = tkinter.Label(
        root, text="Редактор сценариев", font=("Arial Bold", 16), bg='lightgray')
    text_header_down.grid(row=2, column=1)

    button_play = tkinter.Button(
        root, text="Выбрать", command=lambda: select(root))
    button_play.grid(row=3, column=1, pady=5)

    button_settings = tkinter.Button(
        root, text="Настройки", command=lambda: settings(root))
    button_settings.grid(row=4, column=1)

    button_quit = tkinter.Button(
        root, text="Выйти", command=lambda: close_window(root))
    button_quit.grid(row=5, column=1, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
