from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.app import App
from app_module import contant
from app_module import database
from app_module import imp_func
from kivy.core.window import Window
from app_module import database
from kivy.core.clipboard import Clipboard as clp
from kivy.core.text.markup import MarkupLabel


class Recycle_Button(Button):

    def show_password(self):
        _password = database.fetch_data(
            App.get_running_app().root.ids.scr.get_screen('scradd').db_, App.get_running_app().root.ids.scr.get_screen('scradd').password_, self.get_sname(self.text))
        imp_func.show_popup(self.get_sname(self.text), _password,
                            contant.ACTIVE_COLOR, b1="Copy", bc=(lambda: clp.copy(_password)))

    def get_sname(slef, text):
        text_ = text.replace("[color=#ff0000]", "")
        text_ = text_.replace("[/color]", "")
        return text_


class Screen_Query(Screen):
    server = StringProperty()
    db_ = None
    server = None

    def decorate_text(self, text, text1):
        text_ = text.replace(text1, f"[color=#ff0000]{text1}[/color]")
        return text_

    def entered(self):
        Window.size = (contant.A_WIDTH - 100, contant.A_HEIGHT + 150)
        self.db_ = App.get_running_app().root.ids.scr.get_screen('scradd').db_
        self.server = App.get_running_app().root.ids.scr.get_screen('scradd').server_name
        self.ids.review.data = ({'text': f"{self.decorate_text(x,self.server)}"}
                                for x in database.get_query(self.db_, self.server))

    def go_back(self):
        App.get_running_app().root.ids.scr.current = "scradd"
