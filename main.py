from ast import Break, Pass
from importlib.resources import path
from re import search
from select import select
from turtle import Screen
from kivy.app import App
from kivy.lang import Builder
from kivymd.uix.widget import MDWidget
from kivymd.app import MDApp
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import Screen
from kivymd.uix.screen import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDFillRoundFlatIconButton
from kivy.properties import ObjectProperty
from kivymd.uix import MDAdaptiveWidget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.filemanager import MDFileManager
from File_Manager import FileModuleApp
from kivymd.toast import toast
from kivy.uix.widget import Widget
import ML
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time

KV = '''
<SwiperContent@MDBoxLayout>
    size_hint_y: None
    height: "175dp"
    
#:import get_color_from_hex kivy.utils.get_color_from_hex


ScreenManager:
    id:screen_manager
    primary_color: '#01538a'
    black: "000000"
    white: "fffffe"

    primary_font_regular: 'font_style/Poppins/Poppins-Regular.ttf'
    primary_font_medium: 'font_style/Poppins/Poppins-Medium.ttf'
    primary_font_bold: 'font_style/Poppins/Poppins-Bold.ttf'
    primary_font_black: 'font_style/Poppins/Poppins-Black.ttf'

    secondary_font_regular: 'font_style/Roboto/Roboto-Regular.ttf'
    secondary_font_medium: 'font_style/Roboto/Roboto-Medium.ttf'
    secondary_font_bold: 'font_style/Roboto/Roboto-Bold.ttf'
    secondary_font_black: 'font_style/Roboto/Roboto-Black.ttf'
    
    Screen1:
        name:'scr_1'
        MDBottomNavigation:
            panel_color: get_color_from_hex(root.primary_color)
            selected_color_background: get_color_from_hex(root.primary_color)
            text_color_normal: get_color_from_hex(root.black)
            text_color_active: get_color_from_hex(root.white)
            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Home'
                icon: 'home'
                id: screen_1
              
                Image:
                    source:'images/logo.jpg'
                    size_hint_y: None
                    height: "50dp"
                    pos_hint: {"x":dp (0.4), "y": dp(0.85)}
                    keep_ratio : True

                MDLabel:
                    id: menu
                    text: 'Amchart Overview'
                    font_name: root.primary_font_bold
                    font_size: '12dp'
                    pos_hint: {"x":dp (0.05), "y": dp(0.8)}
                    adaptive_height: True
                    adaptive_width: True
                    adaptive_size: True
                    
                MDSwiper:
                    id: swiper
                    y: menu.y - dp(200)
                    width_mult: 5
                    items_spacing: dp(20)
                    on_swipe_right: print("on_swipe_right")

                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                id: Normal
                                source: "images/Normal.jpg"
                                keep_ratio: True

                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                source: "images/Gassy.jpg"
                                keep_ratio: True

                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                source: "images/Gas_Locking.jpg"
                                keep_ratio: True

                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                source: "images/Controls.jpg"
                                keep_ratio: True

                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                source: "images/Current_Under.jpg"
                                keep_ratio: True

                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                source: "images/Cycling.jpg"
                                keep_ratio: True

                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                source: "images/Debris.jpg"
                                keep_ratio: True

                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                source: "images/Excess_Restart.jpg"
                                keep_ratio: True

                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                source: "images/False.jpg"
                                keep_ratio: True

                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                source: "images/No_Load.jpg"
                                keep_ratio: True
                        
                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                source: "images/Overload.jpg"
                                keep_ratio: True
                                
                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                source: "images/Power_Fluctuation.jpg"
                                keep_ratio: True

                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                source: "images/Pump_Off.jpg"
                                keep_ratio: True
                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                source: "images/Erratic.jpg"
                                keep_ratio: True

                    MDSwiperItem:
                        SwiperContent:
                            Image:
                                source: "images/Stuck_Close.png"
                                keep_ratio: True

                MDFillRoundFlatIconButton:
                    md_bg_color: get_color_from_hex(root.primary_color)
                    icon:''
                    x: 0.5*root.width - dp(70)
                    y : 0.05*root.height
                    padding: ['20dp', '15dp']
                    text: 'DIAGNOSTIC'
                    text_color: 1,1,1,1
                    font_name: root.primary_font_medium
                    font_size: '15dp'
                    adaptive_height: True
                    adaptive_width: True
                    adaptive_size: True
                    on_release:
                        screen_manager.current = 'scr_2'

            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'Guideline'
                icon: 'lifebuoy'

                ScrollView:
                    bar_color: get_color_from_hex(root.black)
                    MDList:
                        bg_color: get_color_from_hex ('#d9f5ff')
                        OneLineAvatarIconListItem:
                            on_release: 
                                screen_manager.current = 'control'
                            text: 'Control'

                            IconLeftWidget:
                                icon: "images/Controls.jpg"

                        OneLineAvatarIconListItem:
                            text: 'Undercurrent Load'
                            on_release: 
                                screen_manager.current = 'Undercurrent Load'
                            IconLeftWidget:
                                icon: "images/Current_Under.jpg"

                        OneLineAvatarIconListItem:
                            text: 'Excessive Cycling'
                            on_release: 
                                screen_manager.current = 'Excessive Cysling'
                            IconLeftWidget:
                                icon: "images/Cycling.jpg"

                        OneLineAvatarIconListItem:
                            text: 'Debris'
                            on_release: 
                                screen_manager.current = 'Debris'
                            IconLeftWidget:
                                icon: "images/Debris.jpg"
        
                        OneLineAvatarIconListItem:
                            text: 'Erratic'
                            on_release: 
                                screen_manager.current = 'Erratic'
                            IconLeftWidget:
                                icon: "images/Erratic.jpg"

                        OneLineAvatarIconListItem:
                            text: 'Excess Restart'
                            on_release: 
                                screen_manager.current = 'Excess Restart'                           

                            IconLeftWidget:
                                icon: "images/Excess_Restart.jpg"

                        OneLineAvatarIconListItem:
                            text: 'False Start'
                            on_release: 
                                screen_manager.current = 'False Start'
                            IconLeftWidget:
                                icon: "images/False.jpg"

                        OneLineAvatarIconListItem:
                            text: 'Gas Locking'
                            on_release: 
                                screen_manager.current = 'Gas Locking'
                            IconLeftWidget:
                                icon: "images/Gas_Locking.jpg"

                        OneLineAvatarIconListItem:
                            text: 'Gassy'
                            on_release: 
                                screen_manager.current = 'Gassy'
                            IconLeftWidget:
                                icon: "images/Gassy.jpg"

                        OneLineAvatarIconListItem:
                            text: 'Undercurrent Below No Load'
                            on_release: 
                                screen_manager.current = 'Undercurrent Below No Load'
                            IconLeftWidget:
                                icon: "images/No_Load.jpg"

                        OneLineAvatarIconListItem:
                            text: 'Normal'
                            on_release: 
                                screen_manager.current = 'Normal'
                            IconLeftWidget:
                                icon: "images/Normal.jpg"

                        OneLineAvatarIconListItem:
                            text: 'Overload'
                            on_release: 
                                screen_manager.current = 'Overload'
                            IconLeftWidget:
                                icon: "images/Overload.jpg"

                        OneLineAvatarIconListItem:
                            text: 'Power Fluctuation'
                            on_release: 
                                screen_manager.current = 'Power Fluctuation'
                            IconLeftWidget:
                                icon: "images/Power_Fluctuation.jpg"

                        OneLineAvatarIconListItem:
                            text: 'Pump Off'
                            on_release: 
                                screen_manager.current = 'Pump Off'
                            IconLeftWidget:
                                icon: "images/Pump_Off.jpg"

                        OneLineAvatarIconListItem:
                            text: 'Stuck Close'
                            on_release: 
                                screen_manager.current = 'Stuck Close'
                            IconLeftWidget:
                                icon: "images/Stuck_Close.png"

            MDBottomNavigationItem:
                name: 'screen 4'
                text: 'About'
                icon: 'account'

                MDLabel:
                    text: 'Created by: Al Rizki Dwi Lanang'
                    pos_hint: {"x":dp (0.05), "y": dp(0.3)}
                MDLabel:
                    text: 'Version 1.0'
                    pos_hint: {"x":dp (0.05), "y": dp(0.2)}

    Screen2:
        id: scr_2
        name:'scr_2'

        MDToolbar:
            id: Toolbar
            y:0.91*scr_2.height
            font_name: root.secondary_font_bold
            md_bg_color: get_color_from_hex(root.primary_color)
                
            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex(root.white)
                on_release:
                    screen_manager.current = 'scr_1'

        MDTextFieldRect:
            id: Name
            hint_text: "Name"
            multiline: False
            helper_text: "This will disappear when you click off"
            helper_text_mode: "on_focus"
            size_hint: 0.8, None
            height: "30dp"
            x: 0.1*scr_2.width
            y:0.8*scr_2.height
        
        MDTextFieldRect:
            hint_text: "Role"
            multiline: False
            helper_text: "This will disappear when you click off"
            helper_text_mode: "on_focus"
            size_hint: 0.8, None
            height: "30dp"
            x: 0.1*scr_2.width
            y:0.7*scr_2.height

        MDTextFieldRect:
            hint_text: "Company"
            multiline: False
            helper_text: "This will disappear when you click off"
            helper_text_mode: "on_focus"
            size_hint: 0.8, None
            height: "30dp"
            x: 0.1*scr_2.width
            y:0.6*scr_2.height

        MDRectangleFlatIconButton:
            md_bg_color: get_color_from_hex(root.primary_color)
            icon:'line-scan'
            icon_color : get_color_from_hex(root.black)
            x: 0.5*root.width - dp(60)
            y : 0.3*root.height 
            padding: ['27dp', '17dp']
            text: 'Scan'
            text_color: 1,1,1,1
            font_name: root.primary_font_medium
            font_size: '17dp'
            adaptive_height: True
            adaptive_width: True
            adaptive_size: True
            on_release:
                screen_manager.current = 'scr_5'

        MDFloatingActionButton:
            icon: "file-upload"
            icon_color: get_color_from_hex(root.white)
            md_bg_color: get_color_from_hex(root.primary_color)
            x: 0.02*root.width
            y : 0.01*root.height
            on_release:
                app.open_file_manager()

    Screen3:
        id: scr_3
        name:'scr_3'

        MDToolbar:
            id: Toolbar
            y:0.91*scr_3.height
            font_name: root.secondary_font_bold
            md_bg_color: get_color_from_hex(root.primary_color)

            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex(root.white)
                on_release:
                    screen_manager.current = 'scr_2'
        Image:
            id: predict_image
            source:''
            size_hint_y: None
            height: "220dp"
            y:predict.height+1.2*predict.y
            keep_ratio : True

        MDFillRoundFlatButton:
            id:predict
            md_bg_color: get_color_from_hex(root.primary_color)
            x: 0.5*root.width - dp(60)
            y : 0.3*root.height 
            padding: ['27dp', '17dp']
            text: 'Predict'
            text_color: 1,1,1,1
            font_name: root.primary_font_medium
            font_size: '17dp'
            adaptive_height: True
            adaptive_width: True
            adaptive_size: True
            on_release:
                app.predict()

    Screen4:
        id: scr_4
        name:'scr_4'

        MDToolbar:
            id: Toolbar
            y:0.91*scr_4.height
            font_name: root.secondary_font_bold
            md_bg_color: get_color_from_hex(root.primary_color)

            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex(root.white)
                on_release:
                    screen_manager.current = 'scr_3'
        Image:
            id: image_predict
            source:''
            size_hint_y: None
            height: "220dp"
            y:predict.height+1.2*predict.y
            keep_ratio : True

        MDFlatButton:
            id:predict
            md_bg_color: get_color_from_hex(root.primary_color)
            x: 0.5*root.width - dp(60)
            y : 0.3*root.height 
            padding: ['27dp', '17dp']
            text: 'Result'
            text_color: 1,1,1,1
            font_name: root.primary_font_medium
            font_size: '17dp'
            adaptive_height: True
            adaptive_width: True
            adaptive_size: True

        MDLabel:
            id: name_label
            text: ""
            font_size: dp(18)
            halign: 'center'
            y:predict.height-1.2*predict.y

    Screen5:
        id: scr_5
        name:'scr_5'
        Camera:
            id: camera
            resolution: (640, 480)
            play: True
        MDToolbar:
            id: Toolbar
            y:0.91*scr_5.height
            font_name: root.secondary_font_bold
            md_bg_color: get_color_from_hex(root.primary_color)

            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex(root.white)
                on_release:
                    screen_manager.current = 'scr_2'
        Button:
            text: 'Capture'
            size_hint_y: None
            height: '48dp'
            on_press: 
                app.capture()

    Screen6:
        id: scr_6
        name:'scr_6'

        MDToolbar:
            id: Toolbar
            y:0.91*scr_6.height
            font_name: root.secondary_font_bold
            md_bg_color: get_color_from_hex(root.primary_color)

            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: get_color_from_hex(root.white)
                on_release:
                    screen_manager.current = 'scr_5'
        FitImage:
            id: image_predict_scanner
            source:''
            size_hint_y: None
            height: "220dp"
            y:predict.height+1.2*predict.y
            keep_ratio : True

        MDFlatButton:
            id:predict
            md_bg_color: get_color_from_hex(root.primary_color)
            x: 0.5*root.width - dp(60)
            y : 0.3*root.height 
            padding: ['27dp', '17dp']
            text: 'Result'
            text_color: 1,1,1,1
            font_name: root.primary_font_medium
            font_size: '17dp'
            adaptive_height: True
            adaptive_width: True
            adaptive_size: True

        MDLabel:
            id: name_label_scanner
            text: ""
            font_size: dp(18)
            halign: 'center'
            y:predict.height-1.2*predict.y

    Screen:
        id: control
        name:'control'

        MDLabel:
            id: lbl_1
            text:'Control'
            y:control.y+0.45*root.height

        Image:
            source:'images/Stuck_Close.png'
            size_hint_y: None
            height: "300dp"
            y:0.45*lbl_1.height
            keep_ratio : True
        
        ScrollView:
            y:-0.6*lbl_1.height
            bar_color: get_color_from_hex(root.black)
            MDLabel:
                id:'control'
                text:'Normal '*1000
                size_hint_y:None
                font_size: 12
                text_size: self.width, None
                height: self.texture_size[1]

    Screen:
        name:'Undercurrent Load'
        MDLabel:
            text: "Undercurrent Load"
    Screen:
        name:'Excessive Cycling'
        MDLabel:
            text: "Excessive Cycling"
    Screen:
        name:'Debris'
        MDLabel:
            text: "Debris"
    Screen:
        name:'Erratic'
        MDLabel:
            text: "Erratic"
    Screen:
        name:'Excess Restart'
        MDLabel:
            text: "Excess Restart"
    Screen:
        name:'False Start'
        MDLabel:
            text: "False Start"
    Screen:
        name:'Gas Locking'
        MDLabel:
            text: "Gas Locking"
    Screen:
        name:'Gassy'
        MDLabel:
            text: "Gassy"
    Screen:
        name:'Undercurrent Below No Load'
        MDLabel:
            text: "Undercurrent Below No Load"
    Screen:
        name:'Normal'
        MDLabel:
            text: "Normal"
    Screen:
        name:'Overload'
        MDLabel:
            text: "Overload"
    Screen:
        name:'Power Fluctuation'
        MDLabel:
            text: "Power Fluctuation"
    Screen:
        name:'Pump Off'
        MDLabel:
            text: "Pump Off"
    Screen:
        name:'Overload'
        MDLabel:
            text: "Stuck Close"
'''

class Screen1(Screen):
    pass

class Screen2(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = 'scr_1'

class Screen3(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = 'scr_2'

class Screen4(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = 'scr_3'

class Screen5(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = 'scr_3'

class Screen6(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = 'scr_5'


class Diagnostic(MDApp):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.file_manager_obj=MDFileManager(
            select_path=self.select_path,
            exit_manager=self.exit_file_manager,
        )
        self.image_path = None

    def select_path(self, path):
        a = path
        print (a)
        self.exit_file_manager()
        self.image_path = a
        # b = ML.Machine_Learning(self.image_path)
        # MDApp.get_running_app().root.ids.name_label.text = b
        MDApp.get_running_app().root.ids.predict_image.source = a
        MDApp.get_running_app().root.current = 'scr_3'
        toast(a)
        return a

    def predict(self):
        if (self.image_path):
            b = ML.Machine_Learning(self.image_path)
            MDApp.get_running_app().root.ids.image_predict.source = self.image_path
            MDApp.get_running_app().root.ids.name_label.text = b
            MDApp.get_running_app().root.current = 'scr_4'
        else:
            print('image path unavailable')
            MDApp.get_running_app().root.current = 'scr_4'
        return b

    def open_file_manager(self):
        self.file_manager_obj.show_disks()
        self.open_file_manager = True

    def exit_file_manager(self, *args):
        self.file_manager_obj.close()
        self.open_file_manager = False

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.open_file_manager:
                self.file_manager_obj.back()
        return True

    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = MDApp.get_running_app().root.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        a = "IMG_{}.png".format(timestr)
        camera.export_to_png(a)
        ML.Machine_Learning(a)
        MDApp.get_running_app().root.ids.image_predict_scanner.source = a
        MDApp.get_running_app().root.ids.name_label_scanner.text = ML.Machine_Learning(a)
        MDApp.get_running_app().root.current = 'scr_6'
        print(a,type(a))
        print("Captured")
        return(a)


class AmchartApp(MDApp):
    Diagnostic()
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

# class MDAdaptiveWidget(MDWidget):
#     def press(self):
            # Create variables for our widget
            # name = self.ids.name_input.text
            
            # Update the label
            # self.ids.output.text = AmchartApp.predict(self)

#             # Clear input box
#             # self.ids.name_input.text = ''    


if __name__ == '__main__':  
    AmchartApp().run()