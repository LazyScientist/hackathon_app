from kivymd.uix.screen import MDScreen
from libs.uix.components.kivy_garden.mapview import MapView



class HomeScreen(MDScreen):

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mapview = MapView(zoom=11, lat=50.6394, lon=3.057)


        self.ids.map_card.add_widget(self.mapview)
        
    def btn_press_test(self):
        print("its working")
    pass
    """
    Example Screen.
    """
