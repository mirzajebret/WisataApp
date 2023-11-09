from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
Window.size = (950, 550)
Builder.load_file("wisata.kv")


class WelcomeScrn(Screen):
    pass
class LoggedIn(Screen):
    pass
class LoggedIn2(Screen):
    pass
class selengkapnya(Screen):
    pass

class MainApp(MDApp):
    dialog = None
    dialog2 = None
    def build(self):
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.theme_style ='Dark'
        self.sm = ScreenManager()
        self.sm.add_widget(WelcomeScrn(name="welcome screen"))
        self.sm.add_widget(LoggedIn(name="logged in"))
        self.sm.add_widget(LoggedIn2(name="logged in2"))
        self.sm.add_widget(selengkapnya(name="selengkapnya"))
        return self.sm

    def change_screen(self, obj):
        self.sm.current = obj

    def show_alert_dialog(self):
        close_button = MDFlatButton(text='OK', on_release=self.close_dialog)
        if not self.dialog:
            self.dialog = MDDialog(title="Login Berhasil",type="simple",buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def samsak_alert(self):
        x_button = MDFlatButton(text='okai', on_release=self.close_dialog)
        if not self.dialog2:
            self.dialog2 = MDDialog(title="aduh", text="clicked", type="simple",buttons=[x_button])
        self.dialog2.open()
    
if __name__ == "__main__":
    MainApp().run()