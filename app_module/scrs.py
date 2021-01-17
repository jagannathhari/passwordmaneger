import os

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard as clp

from app_module import custom_widget
from app_module import contant, imp_func
try:
    from app_module import database

except:
    import database
LOGIN_DB_PATH = os.path.join("data", "login.db")


db_path = os.path.join(os.getcwd(), "data", "info" + database.DB_EXTENSION)


class Scr_Add(Screen):
    def __init__(self, **kwargs):
        super(Scr_Add, self).__init__(**kwargs)
        # Window.bind(on_key_down=self._on_keyboard_down)

    password_ = b""
    user_name_ = StringProperty()
    password_d = StringProperty()
    server_name = StringProperty()
    db_ = None

    def db(self):
        Window.size = (contant.A_WIDTH, contant.A_HEIGHT)
        self.password_ = App.get_running_app().root.ids.scr.get_screen('login').password
        self.user_name_ = App.get_running_app().root.ids.scr.get_screen('login').user_name
        self.db_ = database.open_database(db_path, self.password_)
        self.ids.txt_server1.focus = True

    def on_ok(self):
        pass

    def on_copy(self):
        clp.copy(self.password_d)

    def add(self):
        server_ = self.ids.txt_server1.text
        _password = self.ids.txt_paswd.text
        if _password == "":
            imp_func.show_popup(
                "Error", "Password can't be Empty", (1, 0, 0, 1))
            return 0
        print("finish")
        self.ids.txt_server1.text = ""
        self.ids.txt_paswd.text = ""
        res = database.insert_data(
            _password, server_, self.db_, self.password_)
        if res == "found":
            imp_func.show_popup("Error", "Data Already Exists", (1, 0, 0, 1))
            return 1

    def export_db(self):
        fname = imp_func.save_dlg()
        if fname:
            res = database.export_data(self.db_, self.password_, fname)
        if res == True:
            imp_func.show_popup("password Maneger",
                                "Successfully Exported", contant.ACTIVE_COLOR)
            return 1
        imp_func.show_popup("Error", "Unable To Export ", (1, 0, 0, 1))
        return 0

    def show(self):

        server_ = self.ids.txt_server1.text
        paswd = self.password_
        _password = database.fetch_data(self.db_, paswd, server_)
        if _password:
            self.password_d = _password
            imp_func.show_popup(server_, _password,
                                contant.ACTIVE_COLOR, b1="Copy", bo=self.on_copy)
        else:
            imp_func.show_popup("Error", "Server not found", (1, 0, 0, 1))

    def remove(self):
        server2remove = self.ids.txt_server1.text
        res = database.remove_server(self.db, server2remove)
        if not res:
            imp_func.show_popup("Error", "Data Not Found", (1, 0, 0, 1))

    def update(self):

        server_ = self.ids.txt_server1.text
        _password = self.ids.txt_paswd.text
        res = database.update_data(self.db, server_, _password, self.password_)
        if not res:
            imp_func.show_popup(
                "Error", "Data is not in database", (1, 0, 0, 1))

    def query(self):
        self.server_name = self.ids.txt_server1.text
        Window.set_system_cursor("arrow")
        App.get_running_app().root.ids.scr.current = "scrquery"
