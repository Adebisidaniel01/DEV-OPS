from flet import *
from Materials import CustomButton

class LoginScreen(Container):
    def __init__(self, on_login=None):
        super().__init__()
        self.theme_mode = ThemeMode.LIGHT
        self.on_login = on_login
        self.username_field=TextField(
            border_color='transparent',
            bgcolor='transparent',
            hint_text='username',
            hint_style=TextStyle(color='#154c79'),
            text_style=TextStyle(color='#154c79'),
            width=210,
            filled=True,
            on_focus=self.username_focus,
            on_blur=self.username_blur,
            cursor_color='#154c79',
            autofill_hints=AutofillHint.NAME
        )
        self.password_field=TextField(
            border_color='transparent',
            bgcolor='transparent',
            hint_text='password',
            hint_style=TextStyle(color='#154c79'),
            text_style=TextStyle(color='#154c79'),
            password=True,
            can_reveal_password=True,
            width=210,
            filled=True,
            on_focus=self.password_focus,
            on_blur=self.password_blur,
            cursor_color='#154c79',
            autofill_hints=AutofillHint.PASSWORD
        )
        self.username_cont=Container(
            shadow=BoxShadow(
                spread_radius=1,
                blur_radius=1,
                color="#808080",
                offset=Offset(0, 0),
                blur_style=ShadowBlurStyle.OUTER
            ),
            width=280,
            padding=padding.only(right=25, left=25),
            border_radius=border_radius.all(10),
            content=Row(
                controls=[
                    Icon(name=Icons.PERSON_3, color="#154c79"),
                    self.username_field
                ]
            ),
        )
        self.password_cont=Container(
            shadow=BoxShadow(
                spread_radius=1,
                blur_radius=1,
                color="#808080",
                offset=Offset(0, 0),
                blur_style=ShadowBlurStyle.OUTER
            ),
            width=280,
            padding=padding.only(right=25, left=25),
            border_radius=border_radius.all(10),
            content=Row(
                controls=[
                    Icon(name=Icons.PASSWORD, color='#154c79'),
                    self.password_field,
                ]
            ),
        )
        # self.gradient = LinearGradient(
        #     colors=['white', '#67b19f'],
        #     begin=alignment.top_left,
        #     end=alignment.bottom_right
        # )
        # self.height=820
        self.padding = padding.only(top=180)
        # self.alignment = Alignment(0.0, 1.0)
        self.content = Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                # Container(
                #     padding=padding.only(bottom=150),
                #     bgcolor=Colors.TRANSPARENT
                    # shadow=BoxShadow(
                    #     spread_radius=2,
                    #     blur_radius=10,
                    #     color='#154c79',
                    #     offset=Offset(0,0),
                    #     blur_style=ShadowBlurStyle.OUTER
                    # ),
                    # alignment=alignment.top_center,
                    # content=Column(
                    #     controls=[
                    #         Text("CoreMart", size=40, weight="bold", color='#154c79'),
                            
                    #     ]
                    # )
                # ),
                Container(
                    # height=350,
                    expand=True,
                    padding=padding.only(bottom=15, top=20),
                    shadow=BoxShadow(
                        color=Colors.BLUE_GREY_300,
                        spread_radius=1,
                        blur_radius=10,
                        offset=Offset(0,0),
                        blur_style=ShadowBlurStyle.OUTER
                    ),
                    # blur=Blur(10, 12, BlurTileMode.MIRROR),
                    border_radius=border_radius.only(top_left=30, top_right=30),
                    bgcolor=Colors.TRANSPARENT,
                    alignment=alignment.bottom_center,
                    content=Column(
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            # Text(value=self.invite_text),
                            Text(
                                value="CoreMart",
                                size=40,
                                weight="bold",
                                color='#154c79',
                            ),
                            self.username_cont,
                            Container(height=12),
                            self.password_cont,
                            
                            Container(
                                padding=padding.only(top=30),
                                content=Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        OutlinedButton(
                                            text='Sign In',
                                            style=ButtonStyle(
                                                color='#154c79',
                                                shape=RoundedRectangleBorder(radius=5)
                                            ),
                                            on_click=self.on_login
                                        ),
                                        ElevatedButton(
                                            text='Register',
                                            style=ButtonStyle(
                                                color='white',
                                                bgcolor='#154c79',
                                                shape=RoundedRectangleBorder(radius=5)
                                            ),
                                        )
                                    ]
                                )
                            ),
                            Text('Or continue with'),
                            Container(
                                content=Column(
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment='center',
                                    controls=[
                                        CustomButton(
                                            name='Facebook',
                                            _color='f0f3f6',
                                            _image_src='coremart/assets/facebook.jpg'
                                        ),
                                        CustomButton(
                                            name='Google',
                                            _color='f0f3f6',
                                            _image_src='coremart/assets/google.jpg'
                                        ),
                                    ]
                                )
                            ),
                            Container(
                                padding=20,
                                content=Text(
                                    value='By signing in you accept the Terms of Service and Privacy Policy',
                                    style=TextStyle(
                                        color='blue500',
                                        size=12,
                                        decoration=TextDecoration.UNDERLINE,
                                        decoration_color='blue500',
                                        italic=True,
                                    )
                                )
                            )
                        ]
                    )
                )
                
            ]
        )

    def username_focus(self, e):
        self.username_cont.shadow.blur_radius=10    
        self.update()

    def username_blur(self, e):
        self.username_cont.shadow.blur_radius=1
        self.update()

    def password_focus(self, e):
        self.password_cont.shadow.blur_radius=10
        self.update()

    def password_blur(self, e):
        self.password_cont.shadow.blur_radius=1
        self.update()
