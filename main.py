import pyautogui as pya
import pyperclip
import time
import json
import keyboard
import asyncio
from app import Application
from check import Check

check = Check()
pyperclip.copy(json.dumps([]))

def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.3)
    return pyperclip.paste()

def cut_clipboard():
    pya.hotkey('ctrl', 'x')
    time.sleep(.3)
    return pyperclip.paste()

def click_copy():
    pya.position() # позиция курсора
    clipboard = check.check_clipboard()
    new_txt = copy_clipboard()
    add = True
    for data in clipboard:
        if new_txt == data:
            add = False
            break
    if add:
        clipboard.append(new_txt)
    pyperclip.copy(json.dumps(clipboard))

def click_cut():
    pya.position() # позиция курсора
    clipboard = check.check_clipboard()
    new_txt = cut_clipboard()
    add = True
    for data in clipboard:
        if new_txt == data:
            add = False
            break
    if add:
        clipboard.append(new_txt)
    pyperclip.copy(json.dumps(clipboard))

def click_paste():
    clipboard = check.check_clipboard()
    empty = check.check_empty()
    Application(clipboard).make_app()
    if not empty:
        pya.position() # позиция курсора
        pya.hotkey('ctrl', 'v')
    pyperclip.copy(json.dumps(clipboard))
    time.sleep(.3)
    
async def main():
    keyboard.add_hotkey('ctrl+alt+a', click_copy)
    keyboard.add_hotkey('ctrl+alt+z', click_paste)
    keyboard.add_hotkey('ctrl+alt+x', click_cut)
    keyboard.wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    asyncio.run(main())
    loop.run_forever()
    loop.close()