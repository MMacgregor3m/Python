from pynput import keyboard 

if_name_==_"main_":
    listener = keyboard.Listener(on_press=keyPresssed)
    listener.start()
    input()
