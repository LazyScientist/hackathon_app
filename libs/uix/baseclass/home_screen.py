from kivymd.uix.screen import MDScreen


class HomeScreen(MDScreen):

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def btn_press_test(self):
        print("its working")
    pass
    """
    Example Screen.
    """
