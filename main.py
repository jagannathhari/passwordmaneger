import os


os.environ["KIVY_NO_FILELOG"] = "1"
#os.environ["KIVY_NO_CONSOLELOG"] = "0"
os.environ['KIVY_HOME'] = os.getcwd()
from kivy.core.window import Window
Window.clearcolor = (28 / 255, 36 / 255, 49 / 255, 1)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.uix.behaviors import FocusBehavior

from app_module.login_s import LoginScreen
from app_module.scrs import Scr_Add
from app_module.custom_widget import Custom_Btn, Custom_Txt, Show_Pass
from app_module.scr_register import RegisterScreen
from app_module.contant import LOGIN_DB_PATH
from app_module.scr_quey import Screen_Query
from app_module import contant
from kivy.clock import Clock
from kivy.config import Config
Config.set('kivy', 'window_icon', contant.ICON)
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('graphics', 'width', 490)
Config.set('graphics', 'height', 275)
Config.set('graphics', 'resizable', False)
Config.write()


class ScrnManager(ScreenManager):
    pass


class MainScreen(Screen):
    pass


Builder.load_file(os.path.join("ui", "scr_login.kv"))
Builder.load_file(os.path.join("ui", "scr_add.kv"))
Builder.load_file(os.path.join("ui", "custom_widget.kv"))
Builder.load_file(os.path.join("ui", "scr_regster.kv"))
Builder.load_file(os.path.join("ui", "scr_quesr.kv"))


class paswd_maneger(App):
    def build(self):
        self.icon = contant.ICON
        print(self.icon)
        home = Builder.load_file(os.path.join("ui", "main_ui.kv"))
        self.title = "Password Manager"
        return home

    def on_start(self):
        if contant.IS_LOGIN == "login":
            App.get_running_app().root.ids.scr.current = 'login'
            App.get_running_app().root.ids.scr.get_screen('login').ids.txt_pass.focus = True
            App.get_running_app().root.ids.scr.transition = SlideTransition()


paswd_maneger().run()
