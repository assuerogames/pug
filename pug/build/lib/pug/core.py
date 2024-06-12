import pyautogui
import time

def greet():
    return "Hello from Pug!"

def auto_click(x, y):
    pyautogui.click(x, y)

def auto_write(text):
    pyautogui.write(text, interval=0.1)  # Adicione um pequeno intervalo entre os caracteres

def press_enter():
    pyautogui.press('enter')

def wait(seconds):
    time.sleep(seconds)

def show_mouse_position(countdown):
    print("A contagem regressiva começou:")
    for i in range(countdown, 0, -1):
        print(i)
        time.sleep(1)
    x, y = pyautogui.position()
    print(f"A posição atual do mouse é: ({x}, {y})")

def pug_cat():
    return "Criado por: Assuero"

def move_mouse(x, y):
    pyautogui.moveTo(x, y)

def right_click():
    pyautogui.rightClick()

def press_key(key):
    pyautogui.press(key)

def screenshot():
    return pyautogui.screenshot()

def get_screen_resolution():
    return pyautogui.size()

def wait_for_image(image_path, timeout=10):
    return pyautogui.locateCenterOnScreen(image_path, timeout=timeout)
