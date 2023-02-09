import pynput.keyboard


def imprimir():
    teclas = ' '.join(key_list)
    print(teclas)

key_list = []

def convert(key):
    if isinstance(key,pynput.keyboard.KeyCode):     
        return key.char
    else:
        return str(key) 

def push(key):
    key1=convert(key) 
    if key1 == "Key.esc":
        print("saliendo.....")
        imprimir()
        return False
    elif key1 == "Key.space":
        key_list.append(" ")
    else:
        key_list.append(key1)

with pynput.keyboard.Listener(on_press=push) as listen:
    listen.join()

    "Notes: u can print letters and numbers with curly brackets and more signs  "
         
    