#requirements = python3,kivy,kivymd,psycopg2,functools,plyer,hashlib,datetime

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import psycopg2
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import AsyncImage
from functools import partial
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from plyer import camera
from kivy.uix.spinner import SpinnerOption
import hashlib
from datetime import datetime, timedelta
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex


kv = '''

ScreenManager:
    LoginScreen:
    RegisterScreen:
    UserScreen:
    MarketScreen:
    CatalogScreen:
    CollectionScreen:
    WishlistScreen:
    AddFunkoScreen:
    ShowFilters:
    FunkoScreen:

<LoginScreen>:
    name: "login"
    md_bg_color: 0,0,0,0
    BoxLayout:

        orientation: 'vertical'
        BoxLayout:
            orientation: 'vertical'
            AsyncImage:
                size_hint: 10,10
                source: "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/logo_peque.png"
                size_hint_x: 200
                keep_ratio: True
                pos_hint: {'center_x': 0.5}
        BoxLayout:
            size_hint: 1,0.3
            orientation: 'vertical'
            padding: 20
            BoxLayout:
                padding: 20
                TextInput:
                    id: inputMail
                    hint_text:'Email'
                    size_hint: 1, 3.5
                    font_size: 15
            BoxLayout:
                padding: 20
                TextInput:
                    id: inputPass
                    hint_text:'Password'
                    size_hint: 1, 3.5
                    font_size: 15
                    password: True

        BoxLayout:
            size_hint: .7,0.4
            orientation: 'vertical'
            Button:
                text:"Login"
                background_color: 0.1, 0.5, 0.6, 1
                pos_hint: {"x":.1, "y":0.3}
                size_hint: 1.22, 0.3
                on_press: root.loginFun()
            Button:
                text:"Crear cuenta"
                background_color: 0.1, 0.5, 0.6, 1
                pos_hint: {"x":.1, "y":0.3}
                size_hint: 1.22, 0.3
                on_press: root.manager.current = "register"
        BoxLayout:
            size_hint: .2,0.4



<RegisterScreen>:
    name: 'register'
    md_bg_color: 0,0,0,0
    BoxLayout:
        Button:
            color: (0,0,0,1)
            size_hint: (None, None)
            pos_hint:{"right":4,"top":1}
            background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/volver.png'
            on_press: root.manager.current = 'login'
    BoxLayout:
        padding: dp(4)
        size_hint: 1,1
        orientation: 'vertical'
        AsyncImage:
            size_hint: 10,10
            source: "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/logo_peque.png"
            size_hint_x: 200
            keep_ratio: True
            pos_hint: {'center_x': 0.5}
        BoxLayout:
            orientation: 'vertical'
            padding: dp(15)
            TextInput:
                id: inputUser
                hint_text:'User'
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                size_hint: 0.7, 0.1
                font_size: 15
        BoxLayout:
            orientation: 'vertical'
            padding: dp(15)
            TextInput:
                id: inputMail
                hint_text:'Mail'
                pos_hint: {'center_x': 0.5,  'center_y': 0.3}
                size_hint: 0.7, 0.1
        BoxLayout:
            orientation: 'vertical'
            padding: dp(15)
            TextInput:
                id: inputPass
                hint_text:'Password'
                pos_hint: {'center_x': 0.5,  'center_y': 0.3}
                size_hint: 0.7, 0.1
                password: True
        BoxLayout:
            orientation: 'vertical'
            padding: dp(15)
            TextInput:
                id: inputPassConf
                hint_text:'Password'
                pos_hint: {'center_x': 0.5,  'center_y': 0.3}
                size_hint: 0.7, 0.1
                password: True
        BoxLayout:
            padding: dp(15)
            padding_y:[50,5]
            orientation: 'vertical'
            Button:
                text:"Registrar"
                background_color: 0.1, 0.5, 0.6, 1
                pos_hint: {"x":0.15, "y":0.3}
                size_hint: 0.7, 0.2
                on_press: root.registr()


<UserScreen>:
    name: 'user'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            BoxLayout:
                id: user_layout
                padding: 20
                hight: 100
                BoxLayout:
                    orientation: 'vertical'
                    BoxLayout:
                        size: (1,0.32)
                        size_hint: (2, 0.03)
                        orientation: 'vertical'
                        AsyncImage:
                            source: "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/logo.png"
                            size_hint_y: 1
                            size_hint_x: 1
                            allow_stretch: True
                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint: (2, 0.03)
                        BoxLayout:
                            orientation: 'horizontal'
                            BoxLayout:
                                orientation: 'vertical'
                                md_bg_color: 0, 1, 1, .5
                                size_hint: 0.5, 1
                                pos_hint: {'bottom': 4}
                                AsyncImage:
                                    id: photoPerfil
                                    source: "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/logo.png"
                                    size_hint_y: None
                                    height: dp(130)
                                    allow_stretch: True
                                    pos_hint: {'center_x': 0.5}
                            BoxLayout:
                                orientation: 'vertical'
                                md_bg_color: 0, 1, 1, .5
                                Label:
                                    id: username_label
                                    text: root.getDatosUser()[0]
                                    color: (0,0,0,1)
                                    size_hint: (1.0, 1.20)
                                    pos_hint: {'left': 1}
                                    bold: True
                                Label:
                                    id: enVentalabel
                                    text: f'En venta: {root.getDatosUser()[4]}'
                                    color: (0,0,0,1)
                                    size_hint: (1.0, 1.15)
                                Label:
                                    id: vendidoslabel
                                    text: f'Vendidos: {root.getDatosUser()[5]}'
                                    color: (0,0,0,1)
                                    size_hint: (1.0, 1.10)
                                Label:
                                    id: valoracionLabel
                                    text: f'Valoración: {root.getDatosUser()[3]}/5'
                                    color: (0,0,0,1)
                                    size_hint: (1.0, 1.05)
                                    pos_hint: {'right': 1}
                                Label:
                                    id: premium
                                    text: f'Premium {root.getDatosUser()[6]}'
                                    color: (0,0,0,0.6)
                                    size_hint: (1.0, 1.05)
                                    pos_hint: {'right': 1}
                                    italic: True
                                Label:
                                    id: creation_date_label
                                    text: f'Miembro Desde: {root.getDatosUser()[1]}'
                                    color: (0,0,0,0.6)
                                    size_hint: (1.0, 1.05)
                                    pos_hint: {'right': 1}
                                    italic: True
                    BoxLayout:
                        id: listas
                        size: (1,1)
                        size_hint: (2, 0.1)
                        orientation: 'vertical'
                        Label:
                            text:'Listas:'
                            color: (0,0,0,1)
                            size_hint: (0, 1.05)
                            font_size: 20
                        BoxLayout:
                            orientation: 'vertical'
                            md_bg_color: 0, 1, 1, .5
                            canvas.before:
                                Color:
                                    rgba: 255, 0, 195, 0.1
                                RoundedRectangle:
                                    pos: self.pos
                                    size: self.size
                                    radius: [10, 10, 0, 0]
                            Button:
                                text: "Coleccion"
                                id: BotonCollist
                                color: (0,0,0,1)
                                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/Botton2.png'
                                on_press: root.manager.current = 'UserCollection'
                                on_release: app.cargarColeccion()
                        BoxLayout:
                            orientation: 'vertical'
                            md_bg_color: 0, 1, 1, .5
                            canvas.before:
                                Color:
                                    rgba: 255, 0, 195, 0.1
                                RoundedRectangle:
                                    pos: self.pos
                                    size: self.size
                                    radius: [0, 0, 0, 0]
                            Button:
                                text: "Lista De Deseos"
                                id: BotonWishlist
                                color: (0,0,0,1)
                                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/Botton2.png'
                                on_press: root.manager.current = 'UserWishlist'
                                on_release: app.cargarDeseos()
                        BoxLayout:
                            orientation: 'vertical'
                            md_bg_color: 0, 1, 1, .5
                            canvas.before:
                                Color:
                                    rgba: 255, 0, 195, 0.1
                                RoundedRectangle:
                                    pos: self.pos
                                    size: self.size
                                    radius: [0, 0, 10, 10]
                            Button:
                                text:'Productos en Venta(25)'
                                color: (0,0,0,1)
                                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/Botton2.png'
                    BoxLayout:
                        size: (1,1)
                        size_hint: (1.2, 0.05)
                        orientation: 'vertical'
                        BoxLayout:
                            padding: 10
                            orientation: 'horizontal'
                            md_bg_color: 0, 1, 1, .5
                            Button:
                                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/ajustes.png'
                                size_hint: None, None
                            Button:
                                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/add.png'
                                size_hint: None, None
                                on_press: root.manager.current = 'AddNewFunko'
                            Button:
                                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/chat.png'
                                size_hint: None, None
                            Button:
                                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/favoritos.png'
                                size_hint: None, None
                            Button:
                                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/signOut.png'
                                size_hint: None, None
                                on_press: root.manager.current = "login"
        BoxLayout:
            size_hint_y: None
            height: 100
            orientation: 'horizontal'
            Button:
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/userA.png'
                on_press: root.manager.current = 'user'
                canvas.before:
                    Color:
                        rgba: 255, 0, 195, 0.2
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [0, 10, 0, 0]
            Button:
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/MarketA.png'
                on_press: root.manager.current = 'market'
            Button:
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/catalogoA.png'
                on_press: root.manager.current = 'catalog'
<MarketScreen>:
    name: 'market'
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            GridLayout:
                id: Market_layout
                cols: 2
                spacing: 10
                size_hint_y: None
                height: self.minimum_height
        BoxLayout:
            size_hint_y: None
            height: 100
            orientation: 'horizontal'
            Button:
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/userA.png'
                on_press: root.manager.current = 'user'
            Button:
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/MarketA.png'
                on_press: root.manager.current = 'market'
                canvas.before:
                    Color:
                        rgba: 255, 0, 195, 0.2
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 0, 0]
            Button:
                on_press: root.manager.current = 'catalog'
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/catalogoA.png'

<CatalogScreen>:
    name: 'catalog'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            padding: [20, 20, 20, 0]
            size_hint_y: None
            height: 110
            orientation: 'horizontal'
            TextInput:
                id: barra_de_busqueda
                hint_text:'Busca por nombre'
                pos_hint: {'center_x': 0, 'center_y': 0.4}
                size_hint: .9, .34
                on_text:
                font_size: 14
            Button:
                size_hint_y: 0.8
                size_hint_x: 0.3
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/BottonBuscar.png'
                on_press: root.actualizar_texto(barra_de_busqueda.text)
            Button:
                size_hint_y: 0.8
                size_hint_x: 0.3
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/BottonOrdenar.png'
                on_press: root.OrdenarAZ()
            Button:
                size_hint_y: 0.8
                size_hint_x: 0.3
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/BottonQuitarFiltro.png'
                on_press: root.limpiar_Filtros()

        BoxLayout:
            size_hint_y: 0.07
            height: 5
            Label:
                text:'Atributos'
                color: (0,0,0,1)
            Label:
                text:'Categoria'
                color: (0,0,0,1)
            Label:
                text:'Tamaño'
                color: (0,0,0,1)
        BoxLayout:
            padding: [0, 0, 0, 20]
            size_hint_y: 0.07
            height: 5

########################## Desplegable de Type #####################################

            Spinner:
                id: type
                text: 'Sin Filtros'
                values: ['Sin Filtros', 'Glow In The Dark', 'Chase', 'Flocked', 'Scented', 'Diamond', 'Bloody', 'Metallic', 'Exclusivo de tiendas', 'Exclusivo de Convencion', 'Otros...']
                size_hint_x: None
                width: "180dp"
                background_color: 255, 0, 132, 1
                option_cls: 'CustomSpinnerOption'
                on_text: root.filtroType(self.text)

########################## Desplegable de Cat #####################################

            Spinner:
                id: cat
                text: 'Sin Filtros'
                values: ['Sin Filtros', 'Pop! Animation', 'Pop! Disney', 'Pop! Games', 'Pop! Game Of Thrones', 'Pop! Harry Potter', 'Pop! Heroes', 'Pop! Marvel', 'Pop! Star Wars', 'Otros...']
                size_hint_x: None
                width: "180dp"
                background_color: 255, 0, 132, 1
                option_cls: 'CustomSpinnerOption'
                on_text: root.filtroCat(self.text)

########################## Desplegable de Size #####################################

            Spinner:
                id: size
                text: 'Sin Filtros'
                values: ['Sin Filtros', '4"(Estandar)', '6"(Super Sized)', '10"(Jumbo)', '18"(Mega)']
                size_hint_x: None
                width: "180dp"
                background_color: 255, 0, 132, 1
                option_cls: 'CustomSpinnerOption'
                on_text: root.filtroSize(self.text)

########################## Fin de Desplegables #####################################

        ScrollView:
            id: catalog_scroll
            on_scroll_stop: root.check_scroll(self)
            GridLayout:
                id: catalog_layout
                cols: 3
                spacing: 10
                size_hint_y: None
                height: self.minimum_height
                canvas.before:
                    Color:
                        rgba: 255, 255, 255, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [10,]
        BoxLayout:
            size_hint_y: None
            height: 100
            orientation: 'horizontal'
            Button:
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/userA.png'
                on_press: root.manager.current = 'user'
            Button:
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/MarketA.png'
                on_press: root.manager.current = 'market'
            Button:
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/catalogoA.png'
                on_press: root.manager.current = 'catalog'
                canvas.before:
                    Color:
                        rgba: 255, 0, 195, 0.2
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 0, 0, 0]

<CollectionScreen>:
    name: 'UserCollection'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            size_hint_x: 3
            height: 100
            halign: "right"
            orientation: 'horizontal'
            padding: 10
            background_color: (0,0,0,3)
            Button:
                color: (0,0,0,1)
                size_hint: (None, 0.7)
                pos_hint:{"right":4,"top":1}
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/volver.png'
                on_press: root.manager.current = 'user'
            Label:
                text: 'Colección'
                color: (0,0,0,1)
                bold: True
                height: dp(60)
                size_hint: (None, None)
                font_size: sp(40)
                pos_hint:{"right":4,"top":0.5}
        BoxLayout:
            orientation: 'vertical'
            ScrollView:
                GridLayout:
                    id: Collection_layout
                    cols: 3
                    spacing: 10
                    size_hint_y: None
                    height: self.minimum_height
                    canvas.before:
                        Color:
                            rgba: 255, 255, 255, 1
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [10,]


<WishlistScreen>:
    name: 'UserWishlist'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            size_hint_x: 3
            height: 100
            halign: "right"
            orientation: 'horizontal'
            padding: 10
            background_color: (0,0,0,3)

            Button:
                color: (0,0,0,1)
                size_hint: (None, 0.7)
                pos_hint:{"right":4,"top":1}
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/volver.png'
                on_press: root.manager.current = 'user'


            Label:
                text: 'Lista de deseos'
                color: (0,0,0,1)
                bold: True
                height: dp(60)
                size_hint: (None, None)
                font_size: sp(40)
                pos_hint:{"right":4,"top":0.5}

        BoxLayout:
            orientation: 'vertical'
            ScrollView:
                GridLayout:
                    id: wishlist_layout
                    cols: 3
                    spacing: 10
                    size_hint_y: None
                    height: self.minimum_height
                    canvas.before:
                        Color:
                            rgba: 255, 255, 255, 1
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [10,]

<AddFunkoScreen>:
    name: 'AddNewFunko'
    MDBoxLayout:
        orientation: 'vertical'
        BoxLayout:
            #Button:
            #    text: "Tomar Foto"
            #    size_hint: (None, None)
            #    size: (150, 50)
            #    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            #    on_release: root.open_camera()
            AsyncImage:
                id: image_preview
                size_hint: (None, None)
                size: (180, 180)
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                source: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/Empty/left_empty.png'
                on_touch_down: root.check_touch(*args)
            AsyncImage:
                id: image_preview2
                size_hint: (None, None)
                size: (180, 180)
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                source: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/Empty/front_empty.png'
                on_touch_down: root.check_touch()
            AsyncImage:
                id: image_preview
                size_hint: (None, None)
                size: (180, 180)
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                source: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/Empty/right_empty.png'
        BoxLayout:
            AsyncImage:
                id: image_preview
                size_hint: (None, None)
                size: (180, 180)
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                source: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/Empty/top_empty.png'
            AsyncImage:
                id: image_preview
                size_hint: (None, None)
                size: (180, 180)
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                source: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/Empty/damage_empty.png'
            AsyncImage:
                id: image_preview
                size_hint: (None, None)
                size: (180, 180)
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                source: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/Empty/damage_empty2.png'
        MDBoxLayout:
            size_hint_y: None
            height: dp(56)
            padding: dp(10)
            spacing: dp(10)
            MDIconButton:
                icon: 'arrow-left'
                theme_text_color: 'Custom'
                text_color: (1, 1, 1, 1)
                on_release: root.manager.current = 'user'
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(10)
            MDBoxLayout:
                padding: dp(10)
                spacing: dp(10)
                MDTextField:
                    id: nombre_funko
                    hint_text: 'Nombre del funko'
                    size_hint_x: None
                    width: "300dp"
                    on_text_validate: app.process()
                MDTextField:
                    id: numero_funko
                    hint_text: '01'
                    size_hint_x: None
                    width: "100dp"
                    on_text_validate: app.process()
                MDTextField:
                    id: precio_funko
                    hint_text: '€'
                    size_hint_x: None
                    width: "100dp"
                    on_text_validate: app.process()
            MDTextField:
                id: descripcion_funko
                hint_text: 'Descripción'
                multiline: True
                size_hint_y: None
                height: "500dp"
                on_text_validate: app.process()
            MDBoxLayout:
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: dp(56)
                Spinner:
                    id: estado_caja
                    text: 'Estado de la caja'
                    values: ['Siempre con protector', 'como nueva', 'algo tocada', 'destrozada', 'no hay caja']
                    size_hint_x: None
                    width: "250dp"
                Spinner:
                    id: estado_funko
                    text: 'Estado del Funko'
                    values: ['Nunca Sacado de la caja', 'solo abierto para ver', 'expuesto sin caja', 'con algún desperfecto']
                    size_hint_x: None
                    width: "250dp"
            MDBoxLayout:
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: dp(56)
                Spinner:
                    id: tamano_funko
                    text: 'Tamaño'
                    values: ['4"(Estandar)', '6"(Super Sized)', '10"(Jumbo)', '18"(Mega)']
                    size_hint_x: None
                    width: "250dp"
                Spinner:
                    id: categoria_funko
                    text: 'Categoría'
                    values: ['Pop! Marvel', 'Pop! Disney', 'Pop! Rocks', 'Pop! Animation', 'Otros...']
                    size_hint_x: None
                    width: "250dp"
            MDBoxLayout:
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: dp(56)
                Spinner:
                    id: atributos_funko
                    text: 'Atributos'
                    values: ['Glow In The Dark', 'Chase', 'Bloody', 'Diamond']
                    size_hint_x: None
                    width: "250dp"
            BoxLayout:
                Button:
                    text: 'Subir Producto'
                    on_release: root.upload_product()

<FunkoScreen>:
    name: 'FunkoScreen'
    GridLayout:
        cols: 1
        padding: dp(20)
        spacing: dp(10)
        GridLayout:
            cols: 2
            size_hint_y: None
            height: dp(48)
            spacing: dp(10)
            Button:
                background_normal: 'https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/volver.png'
                size_hint_x: None
                width: dp(60)
                allow_stretch: True
                on_release: root.manager.current = 'catalog'
            Label:
                text: app.nombre
                color: (0, 0, 0, 1)
                font_size: '24sp'
                bold: True
                size_hint_x: 1
                valign: 'middle'
                halign: 'center'
        AsyncImage:
            source: app.imagen_source
            size_hint_y: None
            height: dp(360)
            allow_stretch: True
            pos_hint: {'center_x': 0.5}
            canvas.before:
                Color:
                    rgba: 255, 255, 255, 1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [10,]
        BoxLayout:
            AsyncImage:
                source: app.Sticker
            AsyncImage:
                source: app.Sticker2
            AsyncImage:
                source: app.Sticker3
            AsyncImage:
                source: app.Sticker4
        GridLayout:
            cols: 1
            size_hint_y: None
            height: dp(160)
            spacing: dp(10)
            padding: dp(10)
            Label:
                text: "Atributos: " + app.tipo
                color: (0, 0, 0, 1)
                font_size: '20sp'
                valign: 'middle'
            Label:
                text: "Categoría: " + app.category
                color: (0, 0, 0, 1)
                font_size: '20sp'
                valign: 'middle'
            Label:
                text: 'Tamaño: 4"'
                color: (0, 0, 0, 1)
                font_size: '20sp'
                valign: 'middle'
            Label:
                text: 'Precio: $20' # pendiente hacer que funcione el precio
                color: (0, 0, 0, 1)
                font_size: '20sp'
                valign: 'middle'
        BoxLayout:
        GridLayout:
            id: grid_layout
            cols: 2
            size_hint_y: None
            height: dp(80)
            padding: dp(10)
            spacing: dp(10)
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
            Button:
                text: "Añadir a Colección"
                id: addcol
                size_hint: None, None
                size: '240dp', '70dp'
                font_size: '18sp'
                background_color: (0.3, 0.6, 0.9, 1)
                on_release: app.insertarFunkoColeccion(self)
            Button:
                id: addwish
                text: "Ñista"
                size_hint: None, None
                size: '240dp', '70dp'
                font_size: '18sp'
                background_color: (0.9, 0.3, 0.6, 1)
                on_release: app.insertarFunkoDeseo(self)
'''

Window.softinput_mode = "below_target"
Window.size = (540, 960)
filtro = [""]


def hash_password(password):
    # Función para hashear la contraseña utilizando SHA-256
    return hashlib.sha256(password.encode()).hexdigest()[:20]
def generate_unique_id(cursor):
    puntero = ConexionPGAdmin()
    max_id = puntero.comandoSelect("SELECT MAX(user_code) FROM usuarios").fetchone()[0]
    puntero.cerrar()
    if max_id is None:
        return 'U0001'
    else:
        new_id = int(max_id[1:]) + 1
        return 'U{:04d}'.format(new_id)
class LoginScreen(Screen):
    emailglobal = None
    def mostrar_popup(self, mensaje, ruta_imagen=None):
        content = BoxLayout(orientation='vertical')
        label2 = Label(text="(Usuario o Contraseña invalido)")
        content.add_widget(label2)

        if ruta_imagen is not None:
            imagen = AsyncImage(source=ruta_imagen)
            content.add_widget(imagen)
            imagen.size_hint_y = 37
        label = Label(text=mensaje)
        content.add_widget(label)

        popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 400), background_color=get_color_from_hex("#FF5733"))
        popup.background = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/fondoGandalf.png"

        popup.open()
    def loginFun(self):
        self.Mail = self.ids.inputMail.text #Nota: ajustar a Mail en el login
        LoginScreen.emailglobal = self.Mail
        self.passwrd = self.ids.inputPass.text
        if self.Mail != "" and self.passwrd != "":
            try:
                puntero = ConexionPGAdmin()
                self.cont = puntero.comandoSelect(f"SELECT passd FROM usuarios WHERE email LIKE '{self.Mail}'").fetchone()[0]
                puntero.cerrar()
                if hash_password(self.passwrd) == self.cont:
                    self.manager.current = 'user'
            except:
                mensaje_error = "NO...PUEDES...PASAAAR!!!"
                ruta_imagen_error = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/NavMenu/gandalf2.png"
                self.mostrar_popup(mensaje_error, ruta_imagen_error)
class ConexionPGAdmin():
    def __init__(self):
        try:
            # Conexión a la base de datos
            self.connection = psycopg2.connect(
                host="demofm.postgres.database.azure.com",
                user="administrameesta",
                password="2J8g+A.Yx;G,Z5J",
                database="postgres"
            )
            self.cursor = self.connection.cursor()
        except psycopg2.Error as e:
            print("Error:", e)
    def comandoSelect(self, sql, valores = None):
        if self.cursor:
            self.cursor.execute(sql, valores)
            return self.cursor
    def comandoInsert(self, sql, valores = None):
        if self.cursor:
            self.cursor.execute(sql, valores)
            self.connection.commit()
    def cerrar(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
class RegisterScreen(Screen):

    def mostrar_popup(self, mensaje):
        popup = Popup(title='Error', content=Label(text=mensaje), size_hint=(None, None), size=(400, 200))
        popup.open()
    def registr(self):
        self.user = self.ids.inputUser.text
        self.Mail = self.ids.inputMail.text
        self.passwd = self.ids.inputPass.text
        self.passwdConf = self.ids.inputPassConf.text
        self.telefono = "601"  # Asumiendo un valor predeterminado por ahora

        if (self.passwd == self.passwdConf):
            self.passwd = hash_password(self.passwd)
            try:
                # Conexión a la base de datos
                self.puntero = ConexionPGAdmin()
                # Crear un cursor para ejecutar consultas
                self.id_usuario = generate_unique_id(self.puntero)
                self.fecha_registro = datetime.now().strftime('%Y-%m-%d')  # Obtener la fecha actual del sistema
                self.estado = '0'  # Estado por defecto
                self.fecha_estado = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

                data = (self.id_usuario, self.user,
                        self.Mail, self.passwd, self.telefono,
                        self.fecha_registro, self.estado, self.fecha_estado)

                self.sql = '''
                INSERT INTO usuarios (user_code, username, email, passd, phone, creation_date, premium, premium_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                '''
                self.puntero.comandoInsert(self.sql, data)

                print("Datos insertados correctamente.")

            except:
                print("Error registro")
                mensaje_error = "este usuario ya existe... NO...PUEDES...PASAAAR!!!"
                self.mostrar_popup(mensaje_error)

            finally:
                self.puntero.cerrar()
        else:
            mensaje_error = "La contraseña no coincide"
            self.mostrar_popup(mensaje_error)
class ImageButton(ButtonBehavior, AsyncImage):
    pass
class UserScreen(Screen):
    ListaDeseosID = None
    ColeccionID = None

    def on_enter(self):
        self.getDatosUser()
    def getDatosUser(self):
        EmailDeInicioDeSesion = LoginScreen.emailglobal
        sinImgnUser = "https://raw.githubusercontent.com/valskenway/funkomarktph/main/NoProfilePh.png"


        conexion = ConexionPGAdmin()
        QueryDatosUser = f"SELECT username, creation_date, photo, valoracion, en_venta, vendidos, premium, user_code FROM usuarios WHERE email LIKE '{EmailDeInicioDeSesion}'"
        RecopiladorDatos = conexion.comandoSelect(QueryDatosUser).fetchone()



        if RecopiladorDatos is not None:  # Verificar si hay resultados
            username = RecopiladorDatos[0]
            Creation_Date = RecopiladorDatos[1]
            Imgn_User = RecopiladorDatos[2]
            valoracion = RecopiladorDatos[3]
            en_venta = RecopiladorDatos[4]
            vendidos = RecopiladorDatos[5]
            premium = RecopiladorDatos[6]

            if Imgn_User is None:
                Imgn_User = sinImgnUser
            if premium != 0:
                premium = "SI"
            else:
                premium = "NO"

            UserCode = RecopiladorDatos[7]
            QueryListasUser= f"SELECT lista_id, nombre_lista FROM lista_nombres WHERE user_code LIKE '{UserCode}'"
            UserLists = conexion.comandoSelect(QueryListasUser).fetchall()
            ColeccionID = None

            for lista_id, nombre_lista in UserLists:
                if nombre_lista == 'Coleccion':
                    UserScreen.ColeccionID = lista_id
                elif nombre_lista == 'ListaDeseos':
                    UserScreen.ListaDeseosID = lista_id

            #print(f"El nombre de usrCode asociado al correo electrónico {EmailDeInicioDeSesion} es: {UserCode}")
            print(f"las lista de deseos de este usuario({UserCode}) es {UserScreen.ListaDeseosID} y la coleccion es: {UserScreen.ColeccionID}")
            # PARA LOS LABELS
            self.ids.username_label.text = username
            self.ids.creation_date_label.text = f"Miembro desde: {Creation_Date}"
            self.ids.photoPerfil.source = Imgn_User
            self.ids.valoracionLabel.text = f"Valoraciones: {valoracion}/5"
            self.ids.vendidoslabel.text = f"vendidos: {vendidos}"
            self.ids.enVentalabel.text = f"en venta: {en_venta}"
            self.ids.premium.text = f"premium: {premium}"

            conexion.cerrar()
            self.contadorList()
            return username, Creation_Date, Imgn_User, valoracion, vendidos, en_venta, premium, self.ListaDeseosID, self.ColeccionID
        else:
            # RESETEA VALORES
            conexion.cerrar()
            return '', '', None, '', '', '', '', None, None

    def contadorList(self, instance=None):
        conexion = ConexionPGAdmin()
        queryComprobacion = f"SELECT COUNT(*) FROM lista_funkos WHERE lista_id LIKE '{UserScreen.ListaDeseosID}'"
        ContadorListDeseos = conexion.comandoSelect(queryComprobacion).fetchone()
        queryComprobacion2 = f"SELECT COUNT(*) FROM lista_funkos WHERE lista_id LIKE '{UserScreen.ColeccionID}'"
        ContadorListColeccion = conexion.comandoSelect(queryComprobacion2).fetchone()
        conexion.cerrar()
        ListaCol = "Coleccion (" + str(ContadorListColeccion[0]) + ")"
        ListaDes = "Lista de deseos (" + str(ContadorListDeseos[0]) + ")"
        self.ids.BotonWishlist.text = ListaDes
        self.ids.BotonCollist.text = ListaCol
        return ListaDes, ListaCol
class MarketScreen(Screen):
    pass
class CatalogScreen(Screen):

    texto_de_busqueda = StringProperty('')
    offset = 0
    ABC = True
    Orden = "DESC"


    def OrdenarAZ(self):
        if self.ABC:
            self.ABC = False
            self.Orden = "ASC"

        else:
            self.ABC = True
            self.Orden = "DESC"
        print(self.ABC)
        layout = self.ids.catalog_layout
        layout.clear_widgets()
        print("Cambiando Orden...")
        MainApp.loaded_items = 0
        self.offset = 0
        self.cargar_elementos()
        return self.Orden


    def actualizar_texto(self, busqueda):
        self.texto_de_busqueda = busqueda.strip()
        if len(self.texto_de_busqueda) < 2:
            mensaje_error = "Se requieren al menos 2 caracteres para la búsqueda."
            self.mostrar_popup(mensaje_error)
            return None
        elif self.texto_de_busqueda:
            print("Se va a Buscar:", self.texto_de_busqueda)
        else:
            print("Mostrando todos los elementos.")
        self.cargar_elementos()
        return self.texto_de_busqueda

    def mostrar_popup(self, mensaje):
        popup = Popup(title='Error', content=Label(text=mensaje), size_hint=(None, None), size=(400, 200))
        popup.open()

    def filtroCat(self, Cat):
        print(Cat)
        if Cat is not None:
            self.conditions[1] = Cat
            layout = self.ids.catalog_layout
            layout.clear_widgets()
            print("Subiendo arriba...")
            MainApp.loaded_items = 0
            self.cargar_elementos()

    def filtroType(self, type):
        print(type)
        if type is not None:
            self.conditions[2] = type
            layout = self.ids.catalog_layout
            layout.clear_widgets()
            print("Subiendo arriba...")
            MainApp.loaded_items = 0
            self.cargar_elementos()

    def filtroSize(self, Size):
        print(Size)
        if Size is not None:
            self.conditions[3] = Size
            layout = self.ids.catalog_layout
            layout.clear_widgets()
            print("Subiendo arriba...")
            MainApp.loaded_items = 0
            self.cargar_elementos()

    def on_enter(self, *args):
        print("onEnter...")
        super().on_enter(*args)
        layout = self.ids.catalog_layout
        layout.clear_widgets()
        print("cargando catalogo...")
        self.conditions = [None, None, None, None]
        self.conditionsWords = ["funko_name", "funko_category", "funko_type", "funko_size"]
        MainApp.loaded_items = 0
        self.cargar_elementos(nuevos_elementos=False)

    def limpiar_Filtros(self):
        print("DentroDeLimpìarFiltros")
        self.texto_de_busqueda = ''
        self.filtroCat(None)
        spinnerCat = self.ids.cat
        spinnerCat.text = 'Sin Filtros'
        spinnerType = self.ids.type
        spinnerType.text = 'Sin Filtros'
        spinnerSize = self.ids.size
        spinnerSize.text = 'Sin Filtros'
        layout = self.ids.catalog_layout
        layout.clear_widgets()
        print("quitando filtros...")
        MainApp.loaded_items = 0
        self.conditions = [None, None, None, None]
        self.offset = 0

        self.cargar_elementos(nuevos_elementos=False)



    def cargar_elementos(self, nuevos_elementos=False):
        scroll_view = self.ids.catalog_scroll
        scroll_pos = scroll_view.scroll_y
        old_content_height = sum(w.height for w in self.ids.catalog_layout.children)
        layout = self.ids.catalog_layout
        TextoABuscar = self.texto_de_busqueda.lower().strip()
        self.conditions[0] = TextoABuscar


        base_query = "SELECT funko_name, photo FROM catalogo"
        parametros = []
        query_where_clauses = []

        reset_loaded_items = True

        if self.conditions:
            MainApp.loaded_items = 0


            base_query = "SELECT funko_name, photo FROM catalogo"
            for j in range(len(self.conditions)):

                condition_value = self.conditions[j]
                if condition_value and condition_value != "Sin Filtros":
                    if nuevos_elementos:
                        pass
                    else:
                        layout.clear_widgets()
                        self.offset = 0
                        print("limpiando")
                    condition_value = str(condition_value).lower()
                    query_where_clauses.append(f"LOWER({self.conditionsWords[j]}) ILIKE %s")
                    parametros.append(f"%{condition_value}%")

            if query_where_clauses:
                query = f"{base_query} WHERE " + " AND ".join(query_where_clauses)
            else:
                query = base_query
        else:
            query = base_query

        offset = self.offset
        orden = self.Orden

        query += f" ORDER BY funko_name {orden} LIMIT 200 OFFSET {offset}"
        print(query)

        conexion = ConexionPGAdmin()
        packNombrePhoto = conexion.comandoSelect(query, parametros).fetchall()

        if not packNombrePhoto:
            # Si no se encontraron resultados, mostrar mensaje de error
            mensaje_error = "No se existe ese funko!."
            self.mostrar_popup(mensaje_error)
        else:
            MainApp.loaded_items += len(packNombrePhoto)
        conexion.cerrar()



        for name, image_path in packNombrePhoto:
            aux = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=310, padding=10)

            ######### NOMBRE FUNKO #########

            max_chars = 22  # Maximo de caracteres por nombre, si no ...
            truncated_text = name[:max_chars] + ('...' if len(name) > max_chars else '')
            label = Label(text=truncated_text, halign="center", valign='bottom', size_hint=(None, None),
                          color=(0, 0, 0, 1), bold=True, size=(160, 40))

            ######### IMAGEN FUNKO #########
            aimg = ImageButton(source=image_path)
            aimg.bind(on_press=partial(self.on_button_press, label_text=name))



            ######### LLAMADA A LOS WIDGETS #########
            aux.add_widget(aimg)
            aux.add_widget(label)
            layout.add_widget(aux)

        new_content_height = sum(w.height for w in self.ids.catalog_layout.children)
        try:
            scroll_view.scroll_y = 1 - round((1/round((new_content_height / old_content_height),9)),5)
            if scroll_view.scroll_y < 0:
                scroll_view.scroll_y = 1
        except:
            scroll_view.scroll_y = 1
        print(scroll_view.scroll_y)

    def on_button_press(self, instance=None, label_text=None):
        app = MDApp.get_running_app()
        app.on_button_press(instance, label_text)

    def check_scroll(self, scroll_view, *args):
        if scroll_view.scroll_y <= 0.01:  # Ajuste según sea necesario para la sensibilidad
            print('Cargando Nuevos Funkos...')
            self.offset += 200  # Incrementar el offset para cargar nuevos elementos
            old_anchor = self.get_first_visible_element()  # Obtener el primer elemento visible en la pantalla antes de cargar nuevos elementos
            self.cargar_elementos(nuevos_elementos=True)  # Cargar nuevos elementos
            Clock.schedule_once(lambda dt: self.adjust_scroll_position(scroll_view, old_anchor), 0.1)  # Ajustar el desplazamiento después de cargar nuevos elementos

    def get_first_visible_element(self):
        layout = self.ids.catalog_layout
        scroll_view = self.ids.catalog_scroll
        scroll_height = scroll_view.height
        scroll_y = scroll_view.scroll_y

        for child in layout.children:
            if child.y + child.height > scroll_y * scroll_height:
                return child  # Retorna el primer elemento visible
        return None  # Retorna None si no se encuentra ningún elemento visible
    def find_element_in_new_elements(self, old_anchor):
        layout = self.ids.catalog_layout
        for child in layout.children:
            if isinstance(child, BoxLayout):
                label = None
                for widget in child.children:
                    if isinstance(widget, Label):
                        label = widget
                        break
                if label is not None and label.text == old_anchor:
                    return child  # Retorna el nuevo elemento correspondiente
        return None  # Retorna None si no se encuentra el elemento
    def adjust_scroll_position(self, scroll_view, old_anchor):
        new_anchor = self.find_element_in_new_elements(old_anchor)  # Buscar el mismo elemento en el nuevo conjunto de elementos
        if new_anchor:
            # Calcular el desplazamiento necesario para mantener el elemento en la misma posición relativa
            old_content_height = sum(w.height for w in self.ids.catalog_layout.children)
            new_content_height = sum(w.height for w in self.ids.catalog_layout.children)
            scroll_ratio = old_content_height / new_content_height
            new_scroll_pos = scroll_view.scroll_y * scroll_ratio
            scroll_view.scroll_y = max(0, min(1, new_scroll_pos))
def on_spinner_select(self, text):
    print("Seleccionado:", text)
class CustomSpinnerOption(SpinnerOption):
    def __init__(self, **kwargs):
        super(CustomSpinnerOption, self).__init__(**kwargs)
        self.background_color = (255, 0, 132, 0.8)
class CollectionScreen(Screen):
    pass
class WishlistScreen(Screen):
    pass
class AddFunkoScreen(Screen):
    def upload_product(self):
        nombreM = self.ids.nombre_funko.text.strip()
        numeroM = self.ids.numero_funko.text.strip()
        precioM = self.ids.precio_funko.text.strip()
        descripcionM = self.ids.descripcion_funko.text.strip()
        estado_cajaM = self.ids.estado_caja.text.strip()
        estado_funkoM = self.ids.estado_funko.text.strip()
        tamanoM = self.ids.tamano_funko.text.strip()
        categoriaM = self.ids.categoria_funko.text.strip()
        atributosM = self.ids.atributos_funko.text.strip()

        #SI TE FALTA ALGUN DATO TE LA POKEMAMASTE, UN POP UP
        if '' in [nombreM, numeroM, precioM, descripcionM, estado_cajaM, estado_funkoM, tamanoM, categoriaM, atributosM]:
            empty_fields = [field_name for field_name, value in zip(['Nombre', 'Número', 'Precio', 'Descripción', 'Estado Caja', 'Estado Funko', 'Tamaño', 'Categoría', 'Atributos'], [nombreM, numeroM, precioM, descripcionM, estado_cajaM, estado_funkoM, tamanoM, categoriaM, atributosM]) if not value]
            self.show_empty_fields_popup(empty_fields)
            return

        # POSTERIOMENTE UN INSERT
        print(f"Nombre: {nombreM}, Número: {numeroM}, Precio: {precioM}, Descripción: {descripcionM}, "
              f"Estado Caja: {estado_cajaM}, Estado Funko: {estado_funkoM}, Tamaño: {tamanoM}, "
              f"Categoría: {categoriaM}, Atributos: {atributosM}")


    def show_empty_fields_popup(self, empty_fields):
        content = Label(text=f'Los siguientes campos obligatorios* están vacíos:\n{", ".join(empty_fields)}')
        popup = Popup(title='Campos Vacíos:', content=content, size_hint=(None, None), size=(400, 200))
        popup.open()
    def check_touch(self, instance, touch):
        if instance.collide_point(*touch.pos):
            print("Abriendo Camara para hacer foto...")
            try:
                camera.take_picture(filename='temp_image.jpg', on_complete=self.photo_taken)
            except Exception as e:
                print("Error al abrir la cámara:", e)

    def photo_taken(self, filepath):
        try:
            if filepath:
                self.ids.image_preview.source = filepath
        except Exception as e:
            print("Error al mostrar la foto tomada:", e)
class ShowFilters(Screen):
    pass
class FunkoScreen(Screen):
    def go_back(self):
        self.manager.transition.direction = 'right'
        if self.pantalla_anterior == "WishlistScreen":
            self.manager.current = "wishlist"
        elif self.pantalla_anterior == "CatalogScreen":
            self.manager.current = "catalog"
        elif self.pantalla_anterior == "CollectionScreen":
            self.manager.current = "collection"
class MyScreenManager(ScreenManager):
    pass
class MainApp(MDApp, BoxLayout):
    def build(self):
        # Cargar la interfaz definida en el KV
        self.screen_manager = MyScreenManager()
        screen = Builder.load_string(kv)
        self.FunkoScreen = FunkoScreen()
        return screen



    ######### estas definiciones las he hecho para cuando pinches a un funko #########
    nombre = StringProperty('')
    category = StringProperty('')
    tipo = StringProperty('')
    #tamano = StringProperty('')
    Sticker = StringProperty('')
    Sticker2 = StringProperty('')
    Sticker3 = StringProperty('')
    Sticker4 = StringProperty('')
    imagen_source = StringProperty('https://images.hobbydb.com/processed_uploads/catalog_item_photo/catalog_item_photo/image/896890/Twinkie_the_Kid_%2528Metallic%2529_Vinyl_Art_Toys_28dc8669-5b9a-48ea-a056-e7240a8b3982.JPG')
    #################################################################################


    def on_button_press(self, instance=None, label_text=None):   ##### ESTA FUNCIONA ES CUANDO PINCHAS EN UN FUNKO DE CATALOGO
        print('Imagen presionada:', label_text)

        query = "SELECT funko_name,photo,funko_category,funko_type,funko_size FROM catalogo WHERE funko_name LIKE '" + label_text + "' LIMIT 1"
        conexion = ConexionPGAdmin()
        nombre, photo_url, category, tipo, tamano = conexion.comandoSelect(query).fetchone()

        conexion.cerrar()


        ## condicionales para stickers ##
        if tipo.strip().lower() == "other":
            tipo = "regular"
            self.Sticker = ""
            self.Sticker2 = ""
            self.Sticker3 = ""
        if "Diamond" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/diamond.png"
            self.Sticker2 = ""
            self.Sticker3 = ""
        if "Chase" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Chase.png"
            self.Sticker2 = ""
            self.Sticker3 = ""
        if "Flocked" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/flocked.png"
            self.Sticker2 = ""
            self.Sticker3 = ""
        if "Glow In The Dark" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/GITD.png"
            self.Sticker2 = ""
            self.Sticker3 = ""
        if "Scented" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/scented.png"
            self.Sticker2 = ""
            self.Sticker3 = ""
        if "Vendor Exlusive" in tipo.strip():
            #tipo = "Vendor Exclusive"
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Exclusive.png"
            self.Sticker2 = ""
            self.Sticker3 = ""

            ##### CONDICIONALES DOBLES #####
        if "Glow In The Dark" in tipo.strip() and "Chase" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/GITDChase.png"
            self.Sticker2 = ""
            self.Sticker3 = ""
        if "Flocked" in tipo.strip() and "Chase" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/flockedChase.png"
            self.Sticker2 = ""
            self.Sticker3 = ""

            ##### + de 1 Sticker ###
        if "Flocked" in tipo.strip() and "Scented" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/flocked.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/scented.png"
            self.Sticker3 = ""
        if "Scented" in tipo.strip() and "Vendor Exlusive" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/scented.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Exclusive.png"
            self.Sticker3 = ""
        if "Vendor Exlusive" in tipo.strip() and "Chase" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Chase.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Exclusive.png"
            self.Sticker3 = ""
        if "Glow In The Dark" in tipo.strip() and "Vendor Exlusive" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/GITD.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Exclusive.png"
            self.Sticker3 = ""
        if "diamond" in tipo.strip() and "Chase" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/diamond.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Chase.png"
            self.Sticker3 = ""
        if "Diamond" in tipo.strip() and "Vendor Exlusive" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/diamond.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Exclusive.png"
            self.Sticker3 = ""
        if "Flocked" in tipo.strip() and "Vendor Exlusive" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/flocked.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Exclusive.png"
            self.Sticker3 = ""
        if "Glow In The Dark" in tipo.strip() and "Vendor Exlusive" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/GITD.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Exclusive.png"
            self.Sticker3 = ""
            ##### CONDICIONALES TRIPLES #####
        if "Diamond" in tipo.strip() and "Vendor Exlusive" in tipo.strip() and "Chase" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/diamond.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Exclusive.png"
            self.Sticker3 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Chase.png"
        if "Flocked" in tipo.strip() and "Vendor Exlusive" in tipo.strip() and "Chase" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/flocked.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Exclusive.png"
            self.Sticker3 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Chase.png"
        if "Glow In The Dark" in tipo.strip() and "Vendor Exlusive" in tipo.strip() and "Chase" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/GITDChase.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Exclusive.png"
            #self.Sticker3 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Chase.png"
        if "Glow In The Dark" in tipo.strip() and "Vendor Exlusive" in tipo.strip() and "diamond" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/GITD.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Exclusive.png"
            self.Sticker3 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/diamond.png"
        if "Glow In The Dark" in tipo.strip() and "Vendor Exlusive" in tipo.strip() and "Flocked" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/GITD.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Exclusive.png"
            self.Sticker3 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/flocked.png"
        if "Glow In The Dark" in tipo.strip() and "Vendor Exlusive" in tipo.strip() and "Flocked" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/GITD.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Exclusive.png"
            self.Sticker3 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/flocked.png"
        if "Glow In The Dark" in tipo.strip() and "Vendor Exlusive" in tipo.strip() and "Flocked" in tipo.strip():
            self.Sticker = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/GITD.png"
            self.Sticker2 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/Exclusive.png"
            self.Sticker3 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/flocked.png"

            ##### CONDICIONALES CONVENCIONES #####
            if "ECCC" in nombre.strip() or "Spring Convention" in nombre.strip() or "Emerald" in nombre.strip():
                self.Sticker4 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/SprintCon.png"
            else:
                self.Sticker4 = ""
            if "Fall Convention" in nombre.strip() or "new york" in nombre.strip():
                self.Sticker4 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/FallCon.png"
            else:
                self.Sticker4 = ""
            if "SDCC" in nombre.strip() or "Summer Convention" in nombre.strip() or "San Diego Comic Con" in nombre.strip():
                self.Sticker4 = "https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/stickers/SummerCon.png"
            else:
                self.Sticker4 = ""


        self.nombre = nombre
        self.category = category
        self.tipo = tipo
        self.imagen_source = photo_url



        lista_deseos_id = UserScreen.ListaDeseosID
        lista_coleccion_id = UserScreen.ColeccionID
        conexion1 = ConexionPGAdmin()
        queryComprobacion = f"SELECT funko_name, lista_id FROM lista_funkos WHERE funko_name LIKE %s AND lista_id LIKE %s LIMIT 1;"
        nombreFunkoDeseos = conexion1.comandoSelect(queryComprobacion, (nombre, lista_deseos_id))
        Existe = nombreFunkoDeseos.fetchone()

        queryComprobacion2 = f"SELECT funko_name, lista_id FROM lista_funkos WHERE funko_name LIKE %s AND lista_id LIKE %s LIMIT 1;"
        nombreFunkoColeccion = conexion1.comandoSelect(queryComprobacion2, (nombre, lista_coleccion_id))
        Existe2 = nombreFunkoColeccion.fetchone()
        conexion1.cerrar()

        if Existe and Existe[1] == lista_deseos_id:
            print(f"El funko {nombre} ya existe en la lista de deseos")
            self.root.get_screen('FunkoScreen').ids.addwish.text = 'Borrar de lista de deseos'
        else:
            print("el Funko No existe en la lista de deseos")
            self.root.get_screen('FunkoScreen').ids.addwish.text = "Añadir a lista de deseos"

        if Existe2 and Existe2[1] == lista_coleccion_id:
            print(f"El funko {nombre} ya existe en la coleccion")
            self.root.get_screen('FunkoScreen').ids.addcol.text = 'Borrar de Coleccion'
        else:
            print("el Funko No existe en la coleccion")
            self.root.get_screen('FunkoScreen').ids.addcol.text = "Añadir de Coleccion"


        self.root.current = 'FunkoScreen'
        funko_screen = self.root.get_screen('FunkoScreen')

        print('Nombre:', nombre)
        print('Category:', category)
        print('Type:', tipo)
        print('Size:', tamano, 'pulgadas')
        print("__________________________")

    def insertarFunkoDeseo(self, button):
        nombreFunko = self.nombre
        lista_deseos_id = UserScreen.ListaDeseosID
        print(f"estamos en mainapp y la lista de deseos en uso es: {lista_deseos_id}")

        conexion = ConexionPGAdmin()
        queryComprobacion = f"SELECT funko_name, lista_id FROM lista_funkos WHERE funko_name LIKE %s AND lista_id LIKE %s LIMIT 1;"
        nombreFunkoColeccion = conexion.comandoSelect(queryComprobacion, (nombreFunko, lista_deseos_id))
        resultado = nombreFunkoColeccion.fetchone()
        print(resultado)

        if resultado and resultado[1] == lista_deseos_id:
            print(f"El funko {nombreFunko} ya existe en la lista de deseos, se va a proceder a borrar")
            conexion.comandoInsert(f"DELETE FROM lista_funkos WHERE lista_id LIKE '{lista_deseos_id}' AND funko_name LIKE '{nombreFunko}'")
            button.text = 'Añadir a lista de deseos'
        else:
            print("vamos a insertar el funko: ", nombreFunko, "en la lista de deseos:", lista_deseos_id)
            conexion.comandoInsert(f"INSERT INTO lista_funkos (lista_id, funko_name) VALUES ('{lista_deseos_id}', '{nombreFunko}')")
            button.text = 'Borrar de lista de deseos'
        conexion.cerrar()
        UserScreen().contadorList()
    def insertarFunkoColeccion(self, button):
        nombreFunko = self.nombre
        lista_Coleccion_id = UserScreen.ColeccionID
        conexion = ConexionPGAdmin()
        queryComprobacion = "SELECT funko_name, lista_id FROM lista_funkos WHERE funko_name LIKE %s AND lista_id LIKE %s LIMIT 1;"
        nombreFunkoColeccion = conexion.comandoSelect(queryComprobacion, (nombreFunko, lista_Coleccion_id))
        resultado = nombreFunkoColeccion.fetchone()

        if resultado and resultado[1] == lista_Coleccion_id:
            conexion.comandoInsert(f"DELETE FROM lista_funkos WHERE lista_id LIKE '{lista_Coleccion_id}' AND funko_name LIKE '{nombreFunko}'")
            #button.text = 'Añadir a colección'
        else:
            print("vamos a insertar el funko: ", nombreFunko, "en la coleccion:", lista_Coleccion_id)
            conexion.comandoInsert(f"INSERT INTO lista_funkos (lista_id, funko_name) VALUES ('{lista_Coleccion_id}', '{nombreFunko}')")
            #button.text = 'Borrar en colección'
        conexion.cerrar()
        UserScreen().contadorList()
    def on_checkbox_active(self, checkbox_instance, is_active=True):
        global filtro
        if is_active:
            print(f"Mostrando Funkos  {checkbox_instance}")
            #filtro += []

        else:
            print("sin filtros aplicados")
            filtro = ''

        return filtro, checkbox_instance, is_active

    def on_start(self):


        ############ USER ###############

        User_Layout = self.root.get_screen('user').ids.user_layout
        aux1 = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=310)
        User_Layout.add_widget(aux1)

        self.root.current = 'login'

    def cargarDeseos(self):
        ############ USER WISHLIST ###############
        listaDeseosID = UserScreen.ListaDeseosID
        queryFunkoLista = f"SELECT funko_name FROM lista_funkos WHERE lista_id LIKE '{listaDeseosID}'"
        conexion = ConexionPGAdmin()
        NombreFunkoLista = conexion.comandoSelect(queryFunkoLista).fetchall()
        print("se va a buscar: ", NombreFunkoLista)

        ##################################################################

        condiciones = " OR ".join([f"funko_name LIKE '%{tupla[0]}%'" for tupla in NombreFunkoLista])

        # Ahora usamos estas condiciones en la consulta SQL.
        query2 = f"SELECT funko_name, photo FROM catalogo WHERE {condiciones} LIMIT 200"
        packNombrePhoto1 = conexion.comandoSelect(query2).fetchall()
        print(packNombrePhoto1)
        conexion.cerrar()

        layout1 = self.root.get_screen('UserWishlist').ids.wishlist_layout
        layout1.clear_widgets()

        for i in packNombrePhoto1:
            listaDeseos = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=310, padding=10)

            ######### NOMBRE FUNKO #########
            max_chars = 22  #Maximo de caracteres por nombre, si no ...
            truncated_text1 = i[0][:max_chars] + ('...' if len(i[0]) > max_chars else '')
            label1 = Label(text=truncated_text1, halign="center", valign='bottom', size_hint=(None, None),
                           color=(0, 0, 0, 1), bold=True, size=(160, 40))

            ######### IMAGEN FUNKO #########
            aimg1 = ImageButton(source=i[1])
            aimg1.bind(on_press=partial(self.on_button_press, label_text=i[0]))

            ######### LLAMADA A LOS WIDGETS #########
            listaDeseos.add_widget(aimg1)
            listaDeseos.add_widget(label1)
            layout1.add_widget(listaDeseos)


        ############ MARKET ###############

        Marketlistlayout = self.root.get_screen('market').ids.Market_layout

        MarketImagelist = ['https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/FunkoEnVentaPrueba/front.png','https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/FunkoEnVentaPrueba/front.png','https://raw.githubusercontent.com/JorgeOrtiz2480/AuxImgFunkoMark/main/img/FunkoEnVentaPrueba/front.png']
        MarketFunkoList = ['SUPERMAN (EARTH 23) 84','SUPERMAN (EARTH 23) 84','SUPERMAN (EARTH 23) 84']
        MarketFunkoPrice = ['180€','140€','1800€']

        for i in range(0, len(MarketImagelist)):
            MarketBox = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=310, padding=10)

            MarketFunko = Button(size_hint_y=.5, background_normal=MarketImagelist[i], size_hint_x=.9)

            MarketName = Label(text=MarketFunkoList[i], halign="left", valign='bottom', size_hint=(None, None),
                               color=(0, 0, 0, 1), bold=True, size=(230, 20))

            MarketPrice = Label(text=MarketFunkoPrice[i], halign="center", valign='bottom', size_hint=(None, None),
                                color=(0, 0, 0, 1), bold=True, size=(280, 30))

            MarketBox.add_widget(MarketFunko)
            MarketBox.add_widget(MarketName)
            MarketBox.add_widget(MarketPrice)
            Marketlistlayout.add_widget(MarketBox)
    def cargarColeccion(self):
        ############ USER COLLECTION ###############
        listaColeccionID = UserScreen.ColeccionID
        queryFunkoLista = f"SELECT funko_name FROM lista_funkos WHERE lista_id LIKE '{listaColeccionID}'"
        conexion = ConexionPGAdmin()
        NombreFunkoLista = conexion.comandoSelect(queryFunkoLista).fetchall()
        print("se va a buscar: ", NombreFunkoLista)

        ##################################################################

        condiciones = " OR ".join([f"funko_name LIKE '%{tupla[0]}%'" for tupla in NombreFunkoLista])

        # Ahora usamos estas condiciones en la consulta SQL.
        query2 = f"SELECT funko_name, photo FROM catalogo WHERE {condiciones} LIMIT 200"
        packNombrePhoto2 = conexion.comandoSelect(query2).fetchall()
        print(packNombrePhoto2)
        conexion.cerrar()

        layoutCol = self.root.get_screen('UserCollection').ids.Collection_layout
        layoutCol.clear_widgets()
        for i in packNombrePhoto2:
            listaColeccion = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=310, padding=10)

            ######### NOMBRE FUNKO #########
            max_chars = 22  #Maximo de caracteres por nombre, si no ...
            truncated_text2 = i[0][:max_chars] + ('...' if len(i[0]) > max_chars else '')
            label2 = Label(text=truncated_text2, halign="center", valign='bottom', size_hint=(None, None),
                           color=(0, 0, 0, 1), bold=True, size=(160, 40))

            ######### IMAGEN FUNKO #########
            aimg2 = ImageButton(source=i[1])
            aimg2.bind(on_press=partial(self.on_button_press, label_text=i[0]))

            ######### LLAMADA A LOS WIDGETS #########
            listaColeccion.add_widget(aimg2)
            listaColeccion.add_widget(label2)
            layoutCol.add_widget(listaColeccion)

MainApp().run()
