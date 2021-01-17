import os

from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import StringProperty, BooleanProperty
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.behaviors import FocusBehavior
from kivy.app import App

from app_module import imp_func
from app_module import encrypt
from app_module import custom_widget, contant
from app_module.custom_widget import Custom_Btn


LOGIN_DB_PATH = os.path.join("data", "login.db")


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    first_focus = BooleanProperty(True)

    def on_parent(self, widget, parent):
        # if first_focus is set, this Button takes the focus first
        if self.first_focus:
            self.focus = True

    password =b""
    user_name = StringProperty()
    caps = StringProperty()
    visible = BooleanProperty()

    def set_size(self):
        Window.size = (contant.WIDTH, contant.HEIGHT)
        self.ids.txt_user.text = f"Welcome {contant.getuser()}"

    def on_ok(self):
        self.ids.txt_pass.text = ""
        self.ids.txt_pass.focus = True
        self.visible = False

    def get_user_name(self):
        with open(LOGIN_DB_PATH, "r") as login_file:
            user_name = login_file.readline()
            self.user_name = user_name.replace("\n", "")
        login_file.close()
        return user_name

    def enable_pass(self):
        self.ids.txt_pass.password = True
        self.ids.txt_pass.focus = True

    def btn_login_click(self):

        password_ = self.ids.txt_pass.text

        if os.path.exists(LOGIN_DB_PATH):
            with open(LOGIN_DB_PATH, "r") as login_file:
                user_name = login_file.readline()
                self.user_name = user_name
                has = login_file.readline()
                if encrypt.validate_paswd(password_, has):
                    App.get_running_app().root.ids.scr.current = "scradd"
                    self.password = encrypt.key_from_paswd(password_)

                else:
                    self.ids.txt_pass.error()
                    imp_func.show_popup(head='Access Denied', body="Incorrect Password", color=(
                        1, 0, 0, 1), b1="OK", b2="Cancel", bo=self.on_ok, bc=self.on_ok, size=(240, 150))
                    self.ids.txt_pass.focus = False
            login_file.close()
