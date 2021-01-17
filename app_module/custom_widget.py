import os
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.properties import StringProperty, ListProperty
from kivy.uix.textinput import TextInput
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.behaviors import FocusBehavior


from app_module import contant


class HoverBehavior:
    """Hover behavior.
    :Events:
        `on_enter`
            Fired when mouse enter the bbox of the widget.
        `on_leave`
            Fired when the mouse exit the widget
    """

    hovered = BooleanProperty(False)
    border_point = ObjectProperty(None)
    '''Contains the last relevant point received by the Hoverable. This can
    be used in `on_enter` or `on_leave` in order to know where was dispatched the event.
    '''

    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return  # do proceed if I'm not displayed <=> If have no parent
        pos = args[1]
        # Next line to_widget allow to compensate for relative layout
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            # We have already done what was needed
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        pass

    def on_leave(self):
        pass


Factory.register('HoverBehavior', HoverBehavior)


class MYFocusbehaviour(FocusBehavior):
    next_ = ObjectProperty()
    previous_ = ObjectProperty()

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        self.previous_ = self.get_focus_previous()

        if keycode[1] == "tab" and ('shift' not in modifiers):
            self.next_ = self.get_focus_next()
            self.next_.focus = True
        if keycode[1] == "tab" and ('shift' in modifiers) and (self.previous_ != None):
            self.previous_.focus = True
            return True
        if (isinstance(self, Custom_Btn) or isinstance(self, Show_Pass)) and (keycode[1] == "enter" or keycode[1] == "numpadenter"):
            self.dispatch("on_press")
        return True

        # print(self.get_focus_previous(), self.get_focus_previous())

    def keyboard_on_key_up(self, window, keycode):

        if (isinstance(self, Custom_Btn) or isinstance(self, Show_Pass)) and (keycode[1] == "enter" or keycode[1] == "numpadenter"):
            self.dispatch("on_release")
        super(MYFocusbehaviour, self).keyboard_on_key_up(window, keycode)


class Custom_Btn(Button, HoverBehavior, MYFocusbehaviour):
    first_focus = BooleanProperty(False)

    def on_parent(self, widget, parent):
        # if first_focus is set, this Button takes the focus first
        if self.first_focus:
            self.focus = True

    def on_enter(self, *args):
        self.background_normal = f"atlas://{contant.ASSEST_PATH}/theme/btn_h"

    def on_leave(self, *args):
        self.background_normal = f"atlas://{contant.ASSEST_PATH}/theme/btn_n"


class Custom_Txt(TextInput, HoverBehavior, MYFocusbehaviour):
    iscps_on = StringProperty()

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        self.write_tab = False
        if keycode[1] == "backspace":
            self.do_backspace(from_undo=False, mode='bkspc')
        if keycode[1] == "right":
            self.do_cursor_movement("cursor_right")
        if keycode[1] == "left":
            self.do_cursor_movement("cursor_left")
        if "capslock" in modifiers:
            self.iscps_on = "[color=#ff3333]Capslock On[/color]"
        else:
            self.iscps_on = ""

        super(Custom_Txt, self).keyboard_on_key_down(
            window, keycode, text, modifiers)

    def on_enter(self, *args):
        if not self.focus:
            self.background_normal = f"atlas://{contant.ASSEST_PATH}/theme/txt_hover"
        Window.set_system_cursor("ibeam")

    def on_leave(self, *args):
        if not self.focus:
            self.background_normal = f"atlas://{contant.ASSEST_PATH}/theme/txt_normal"
        Window.set_system_cursor("arrow")

    def error(self):
        self.focus = True
        self.text = ""
        self.background_active = f"atlas://{contant.ASSEST_PATH}/theme/txt_error"

    def error1(self):
        self.background_active = f"atlas://{contant.ASSEST_PATH}/theme/txt_error"

    def success(self):
        self.background_active = f"atlas://{contant.ASSEST_PATH}/theme/txt_success"


class Custom_Popup(Popup):

    lbl_color = ListProperty(contant.TEXT_COLOR)
    lbl_text = StringProperty()
    can_dismiss = BooleanProperty(False)
    btn_bind = ObjectProperty()
    btn_cancle = ObjectProperty()
    btn1txt = StringProperty()
    btn2txt = StringProperty()

    def btn_bind_(self):
        try:
            self.btn_bind()
            self.close_me()
        except:
            self.close_me()

    def btn_cancle_(self):
        try:
            self.btn_cancle()
            self.dismiss()
        except:
            self.dismiss()

    def show_me(self):
        self.ids.btn1.text = self.btn1txt
        self.ids.btn2.text = self.btn2txt
        self.ids.btn1.focus = True
        self.open()

    def close_me(self):
        self.btn_cancle()
        self.dismiss()

    def btn_ok_press(self):

        self.close_me()


class Show_Pass(Button, HoverBehavior, MYFocusbehaviour):
    first_focus = BooleanProperty(False)

    def on_parent(self, widget, parent):
        # if first_focus is set, this Button takes the focus first
        if self.first_focus:
            self.focus = True

    def on_enter(self, *args):
        self.background_normal = f"atlas://{contant.ASSEST_PATH}/theme/Show_h"
        Window.set_system_cursor("hand")

    def on_leave(self, *args):
        self.background_normal = f"atlas://{contant.ASSEST_PATH}/theme/Show"
        Window.set_system_cursor("arrow")
