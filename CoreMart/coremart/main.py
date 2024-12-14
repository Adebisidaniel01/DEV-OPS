import flet as ft
from flet import *
from firebase_admin import initialize_app
import datetime
from Materials import AdsCart
from login_screen import LoginScreen
from main_screen import MainScreen
from search_screen import SearchScreen
from favourite_screen import FavouriteScreen
from notificationScreen import NotificationScreen



config = {
    "apiKey": "AIzaSyAIBGNY6z1-mLuQPtRtkAPWChLP987omSQ",
    "authDomain": "coremart-a63d5.firebaseapp.com",
    "projectId": "coremart-a63d5",
    "storageBucket": "coremart-a63d5.firebasestorage.app",
    "messagingSenderId": "782272261815",
    "appId": "1:782272261815:web:e08cca907494b398416732",
    "measurementId": "G-NKR9BJ2TVS", 
    "databaseURL": ""
  };



def main(pg: Page):
    def search_switch(e):
        main_screen.visible = False
        search_screen.visible = True
        favourite_screen.visible = False
        login_screen.visible = False
        notification_screen.visible=False
        pg.update()
    def on_notificaton(e):
        main_screen.visible = False
        search_screen.visible = False
        favourite_screen.visible = False
        login_screen.visible = False
        notification_screen.visible=True
        pg.update()
    def on_login(e):
        main_screen.visible = True
        login_screen.visible = False
        notification_screen.visible = False
        search_screen.visible = False
        pg.appbar.visible=True
        pg.drawer.selected_index = 0
        pg.update()
    main_screen = Container(
        content=MainScreen()  
    )

    search_screen = Container(
        visible=False,
        content=SearchScreen(on_back_click=on_login)
    )

    notification_screen = Container(
        visible=False,
        content=NotificationScreen(on_back_click=on_login)
    )

    favourite_screen = Container(
        visible=False,
        content=FavouriteScreen()
    )

    login_screen = Container(
        visible=False,
        content=LoginScreen(on_login=on_login)
    )

    def drawer_open(e):
        pg.drawer.open = True
        pg.update()

    def close_drawer(e):
        pg.drawer.open = False
        pg.update()

    def change_page(e):
        index = pg.drawer.selected_index
        main_screen.visible = True if index == 0 else False
        favourite_screen.visible = True if index == 2 else False
        login_screen.visible = True if index == 8 else False
        pg.appbar.visible = False if index == 8 else True
        notification_screen.visible = False
        search_screen.visible = False
        pg.drawer.open = False
        pg.update()

    pg.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Open Sans": "/fonts/openSans-Regular.ttf"
    }
    pg.scroll = 'hidden'
    pg.padding=0
    pg.drawer = NavigationDrawer(
        # bgcolor='green800',
        elevation=40,
        # indicator_color='#67b19f',
        indicator_shape=StadiumBorder(),
        shadow_color='red200',
        selected_index=0,
        on_change=change_page,
        controls=[
            Container(
                padding=padding.only(left=15, top=10, bottom=30),
                content=Column(
                    controls=[
                        Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                CircleAvatar(radius=30, foreground_image_src=f'https://picsum.photos/200/200?115'),
                                IconButton(icon=Icons.CANCEL, on_click=close_drawer)
                            ]
                        ),
                        Text('Olorunponle Timileyin\nCustomer'),
                        Row(
                            controls=[
                                Icon(name=Icons.STAR),
                                Text('91.8%')
                            ]
                        )
                    ]
                )
            ),
            Divider(),
            NavigationDrawerDestination(
                label='HOME',
                icon='home',
            ),
            NavigationDrawerDestination(
                label='ACCOUNT',
                icon='person_3',
            ),
            NavigationDrawerDestination(
                label='FAVOURITE',
                icon='favorite',
            ),
            NavigationDrawerDestination(
                label='PROMOTIONS',
                icon='discount',
            ),
            NavigationDrawerDestination(
                label='MY ORDERS',
                icon='shop',
            ),
            NavigationDrawerDestination(
                label='CONTACT US',
                icon='phone',
            ),
            NavigationDrawerDestination(
                label='SETTINGS',
                icon='settings',
            ),
            NavigationDrawerDestination(
                label='SIGN OUT',
                icon='logOut',
            ),
        ]
    )
    
    pg.add(
        main_screen,
        search_screen,
        favourite_screen,
        login_screen,
        notification_screen
    )
    pg.appbar = AppBar(
        elevation=1,
        surface_tint_color='blue800',
        # bgcolor='#67b19f',
        center_title=True,
        leading=IconButton(
            icon=Icons.MENU,
            on_click=drawer_open
        ),
        title=Container(
            height=40,
            width=180,
            padding=padding.only(left=7),
            shadow=BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color='#f1f1f1',
                offset=Offset(0, 0),
                blur_style=ShadowBlurStyle.OUTER
            ),
            border_radius=border_radius.all(20),
            # bgcolor='white',
            content=Text('CoreCart', size=30, weight='bold')
        ),
        actions=[
            IconButton(
                icon=Icons.SEARCH,
                tooltip='Notification',
                on_click=search_switch
            ),
            IconButton(
                icon=Icons.NOTIFICATIONS_SHARP,
                tooltip='Notification',
                on_click=on_notificaton
            )
        ]
    )
    # pg.theme_mode = ThemeMode.DARK
    pg.theme = Theme(font_family='sanfransisco')
    pg.update()
    

ft.app(target=main, assets_dir="assets")
