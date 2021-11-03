from psutil import process_iter
from player import close
from player import btn_var as btn
import threading
import keyboard
stopped = False
btn = 'pageup'


def func():
    while True:
        if keyboard.is_pressed(btn):
            stopped = True
            break
    # print("triggered")
    close()


thread = threading.Thread(target=func, daemon=True)
thread.start()

if __name__ == '__main__':
    func()
