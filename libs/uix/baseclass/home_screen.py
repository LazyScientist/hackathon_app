from kivymd.uix.screen import MDScreen
from numpy import spacing
from libs.uix.components.kivy_garden.mapview import MapView
from kivy.factory import Factory
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from plyer import notification
from kivy.uix.videoplayer import VideoPlayer
import os

class HomeScreen(MDScreen):

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mapview = MapView(zoom=11, lat=50.6394, lon=3.057)

        self.home_layout1 = Factory.home_element1()
        self.home_layout1.ids.btn.bind(on_press=self.button_layout1)
        self.home_layout2 = Factory.home_element2()
        self.home_layout2.ids.btn.bind(on_press=self.button_layout2)
        self.home_layout3 = Factory.home_element3()
        self.home_layout3.ids.btn.bind(on_press=self.button_layout3)

        self.info_layout = Factory.info()


        self.ids.scroll_box.add_widget(self.home_layout1)
        self.ids.scroll_box.add_widget(self.home_layout2)
        self.ids.scroll_box.add_widget(self.home_layout3)


        self.list_box = Factory.list_box_container()
        def ddd(b):
            self.ids.scroll_box.remove_widget(self.list_box)
            self.ids.scroll_box.add_widget(self.info_layout)
        for i in range(0,10):
            listss= Factory.listitemss()
            listss.ids.txt.text = str(i)+"/12/2022"
            listss.ids.btn.bind(on_press=ddd)
            self.list_box.add_widget(listss)


        self.info_layout.ids.map_card.add_widget(self.mapview)

        # self.player = VideoPlayer(source='myvideo.avi', state='play',options={'allow_stretch': True})
        # self.info_layout.ids.video_box.add_widget(self.player)

    def button_layout1(self,btn):
        if btn.icon == 'arrow-right':
            btn.icon = 'arrow-left'
            self.ids.scroll_box.remove_widget(self.home_layout2)
            self.ids.scroll_box.remove_widget(self.home_layout3)
            self.info_layout.ids.Video.source = os.path.join('assets','images','demo2.mp4')
            self.ids.scroll_box.add_widget(self.info_layout)
            self.md_bg_color = self.home_layout1.ids.btn.md_bg_color


        else:
            btn.icon = 'arrow-right'
            self.ids.scroll_box.add_widget(self.home_layout2)
            self.ids.scroll_box.add_widget(self.home_layout3)
            self.ids.scroll_box.remove_widget(self.info_layout)
            self.md_bg_color = self.home_layout2.md_bg_color



    def button_layout2(self,btn):
        if btn.icon == 'arrow-right':
            btn.icon = 'arrow-left'
            self.ids.scroll_box.remove_widget(self.home_layout1)
            self.ids.scroll_box.remove_widget(self.home_layout3)
            self.ids.scroll_box.add_widget(self.list_box)
            self.md_bg_color =  self.home_layout1.ids.btn.md_bg_color

        else:
            btn.icon = 'arrow-right'
            self.ids.scroll_box.add_widget(self.home_layout1)
            self.ids.scroll_box.add_widget(self.home_layout3)
            self.ids.scroll_box.remove_widget(self.list_box)
            self.ids.scroll_box.remove_widget(self.info_layout)
            self.md_bg_color = self.home_layout2.md_bg_color











    def button_layout3(self,btn):
        if btn.icon == 'arrow-right':
            btn.icon = 'arrow-left'
            self.ids.scroll_box.remove_widget(self.home_layout2)
            self.ids.scroll_box.remove_widget(self.home_layout1)
            self.ids.scroll_box.add_widget(self.info_layout)
            self.md_bg_color =  self.home_layout1.ids.btn.md_bg_color
            notification.notify(title = 'monarch drone', message = 'unwanted object detacted')


        else:
            btn.icon = 'arrow-right'
            self.ids.scroll_box.add_widget(self.home_layout2)
            self.ids.scroll_box.add_widget(self.home_layout1)
            self.ids.scroll_box.remove_widget(self.info_layout)
            self.md_bg_color = self.home_layout2.md_bg_color
