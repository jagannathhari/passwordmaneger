import random
import string
import bcrypt
#import win32ui
from app_module import custom_widget


def show_popup(head, body, color, b1="OK", b2="Cancle", bo=(lambda: 1), bc=(lambda: 1), size=(350, 200)):
    popup = custom_widget.Custom_Popup(
        title=head, size_hint=(None, None), size=size)
    popup.lbl_color = color
    popup.lbl_text = body
    popup.btn_bind = bo
    popup.btn_cancle = bc
    popup.btn1txt = b1
    popup.btn2txt = b2
    popup.show_me()


def save_dlg():
    dlg = win32ui.CreateFileDialog(
        0, ".txt", "", 2, "Excel Files (*.xlsx)|*.xlsx|All Files (*.*)|*.*|")
    dlg.DoModal()
    filename = dlg.GetPathName()
    return filename


def hash_paswd(paswd):
    password = paswd.encode("utf-8")
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed.decode("utf-8")


def validate_paswd(paswd, hashed):
    password = paswd.encode("utf-8")
    hash_ = hashed.encode("utf-8")
    if bcrypt.checkpw(password, hash_):
        return True
    else:
        False


def generate_pswd(lenth=8):
    strin = string.ascii_letters + string.digits + string.punctuation
    paswd = [random.choice(strin) for i in range(lenth)]
    return "".join(paswd)
