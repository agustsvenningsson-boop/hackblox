import webbrowser
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
mail_path = os.path.join(script_dir, "download_done.html")
webbrowser.open("file:///" + mail_path.replace("\\", "/"))
