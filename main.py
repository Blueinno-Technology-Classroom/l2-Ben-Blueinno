import pyautogui as gui
import keyboard
import time
import multiprocessing

gui.PAUSE = 0

# gui.displayMousePosition()
btn_pos = (380, 380)

upgrade_btn_pos = [
    (860, 280),
    (860, 340),
    (860, 400),
    (860, 460),
    (860, 530),
]

def click_button():
    while True:
        gui.click(btn_pos)
        if keyboard.is_pressed("Esc"):
            break


def click_upgrade():
    while True:
        for x,y in upgrade_btn_pos:
            r, g, b = gui.pixel(x,y)
            print(g)
            if g > 200:
                time.sleep(0.2)
                gui.click(x,y)
        if keyboard.is_pressed("Esc"):
            break
        
if __name__ == '__main__':
    main_process = multiprocessing.Process(target=click_button)
    upgrade_process = multiprocessing.Process(target=click_upgrade)

    main_process.start()
    upgrade_process.start()