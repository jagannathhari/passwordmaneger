from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.app import App
from kivy.core.window import Window

import os

from app_module import imp_func
from app_module import encrypt
from app_module import custom_widget
from app_module import contant


class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)

    def on_ok(self):
        self.ids.txt_rcpass.focus = True

    def enable(self):
        self.ids.txt_rpass.password = True
        self.ids.txt_rpass.focus = True

    def btn_register_click(self):
        if len(self.ids.txt_user.text) == 0:
            print("asdf")
        if (self.ids.txt_rpass.text == self.ids.txt_rcpass.text) and len(self.ids.txt_rpass.text) > 0:
            with open(contant.LOGIN_DB_PATH, "w") as login_file:
                login_file.write(self.ids.txt_user.text + "\n")
                login_file.write(encrypt.hash_paswd(self.ids.txt_rpass.text))
                App.get_running_app().root.ids.scr.get_screen('login').ids.txt_pass.focus = True
                App.get_running_app().root.ids.scr.transition = SlideTransition()
                App.get_running_app().root.ids.scr.current = 'login'
                return 1

        else:
            popup = custom_widget.Custom_Popup(
                title='Error', size_hint=(None, None), size=(300, 225))
            popup.lbl_color = (1, 0, 0, 1)
            popup.lbl_text = "Confirm Password Not Matched"
            self.ids.txt_rcpass.text = ""
            self.ids.txt_rcpass.error()
            popup.btn_bind = self.on_ok
            popup.btn_cancle = self.on_ok
            popup.show_me()
            return 1
