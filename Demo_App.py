import os
import platform

from kivy.core.window import Window
from kivymd.app import MDApp

from libs.uix.baseclass.root import Root

try:
    from android.permissions import request_permission, Permission, check_permission

except :
    print('not android')

Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"  


# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"
else:
    if not check_permission(Permission.RECORD_AUDIO):
        request_permission(Permission.RECORD_AUDIO)
    if not check_permission(Permission.CAMERA):
        request_permission(Permission.CAMERA)
    else:
        print('Permission OK')
    Window.clear()
    Window.borderless = True
    Window.fullscreen = True
    Window.maximize() 


class Demo_App(MDApp):  # NOQA: N801
    def __init__(self, **kwargs):
        super(Demo_App, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.icon= os.path.join('assets','icons','my_icon.png')
        self.title = "Monarch drone"

        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue = "500"

        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style = "Light"

    def build(self):
        return Root()



#Note
# use os.path.join('folder','sub_folder','file.extension')   instead of using 'folder/sub_folder/file.extension'

