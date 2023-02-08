import pynput.keyboard


def push(key):
    key1=convert(key)
    print("tecla presionada: {}".format(key1))

def out(key):
     key1=convert(key)
     print("tecla liberada: {}".format(key1))
     if str(key) == "key.esc":
        print("saliendo....")
        return False

def convert(key):
    if iinstance(key,pynput.keyboard.KeyCode):
        return str(key)
    else:
        return str(key)


with pynput.keyboard.Listener(on_press=push,on_release=out) as listen:
    listen.join()

    "Notes: i fixed the compilation problem, in the 16 line it was mispelled isinstance "