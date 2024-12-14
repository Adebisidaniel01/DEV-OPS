from flet import *


class AdsCart(Container):
    def __init__(self, image_src, product_title, product_desc, product_price, on_info_click=None):
        super().__init__()
        self._image_src = image_src
        self.product_title = product_title
        self.product_desc = product_desc
        self.product_price = product_price
        self.on_info_click = on_info_click
        self.product_title_text = Text(value=self.product_title, size=16, weight='bold')
        self.product_desc_text = Text(value=self.product_desc, size=13)
        self.product_price_text = Text(value=self.product_price, size=23, weight='bold')
        # self.shadow=BoxShadow(
        #     spread_radius=2,
        #     blur_radius=5,
        #     color='#f3f3f3',
        #     offset=Offset(0,1),
        #     blur_style=ShadowBlurStyle.OUTER
        # )
        self.content=Container(
            width=200,
            content=Column(
                controls=[
                    Image(
                        src=self._image_src,
                        width=300,
                        height=200,
                        fit=ImageFit.FIT_WIDTH
                    ),
                    Container(
                        padding=padding.only(top=10, left=5),
                        content=Column(
                            controls=[
                                self.product_title_text,
                                self.product_desc_text,
                                Row(
                                    alignment='spaceBetween',
                                    controls=[
                                        self.product_price_text,
                                        IconButton(icon=Icons.ARROW_CIRCLE_RIGHT_OUTLINED, tooltip='More info', on_click=self.on_info_click)
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )


class SearchList(ListTile):
    def __init__(self, search_text):
        super().__init__()
        self.search_text = search_text
        self.leading = Icon(name='search')
        self.title = Text(value=self.search_text)
        self.trailing = IconButton(icon='cancel')

class FavouriteCard(Container):
    def __init__(self, product_title, image_path):
        super().__init__()
        self.image_path = image_path
        self.title = product_title
        self.height = 220
        self.width = 150
        # self.border_radius = border_radius.only(bottom_left=30, bottom_right=30)
        self.alignment = alignment.center
        self.content=Column(
            controls=[
                Image(
                    src=self.image_path,
                    width=150,
                    height=150,
                    fit=ImageFit.FIT_WIDTH
                ),
                Container(
                    padding=padding.only(left=5, right=5),
                    content=Column(
                        controls=[
                            Text(
                                value=self.title
                            ),
                            Text(
                                value='5000'
                            )
                        ]
                    )
                )
            ]
        )


class CustomButton(ElevatedButton):
    def __init__(self, name, _color, _image_src):
        super().__init__()
        self.name = name
        self._color = _color
        self._image_src = _image_src
        self.style=ButtonStyle(
            color=self._color,
            shape=RoundedRectangleBorder(radius=5)
        )
        self.width=280
        self.height=48
        self.content=Row(
            alignment='center',
            spacing=4,
            controls=[
                Image(
                    src=self._image_src,
                    width=30,
                    height=30
                ),
                Text(
                    value=self.name,
                    color='black',
                    size=14,
                    weight='bold'
                )
            ]
        )

class NotificationList(Container):
    def __init__(self):
        super().__init__()
        self.notification_title = ''
        self.notification_subtitle = ''
        self.profile_name = ''
        self.content=ListTile(
            title=Text('New update!'),
            subtitle=Text(f'{'Adeyemi'} who you follow just posted a new product'),
            bgcolor=Text('blue200')
        )

class CategoryCircle(Container):
    def __init__(self, img_pth, text, click_event=None):
        super().__init__()
        self.click_event = click_event
        self.img_pth = img_pth
        self.text = text
        self.on_click = self.click_event
        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                Container(
                    height=90,
                    width=90,
                    content=Image(
                        src=self.img_pth,
                        border_radius=180,
                        fit=ImageFit.FILL
                    )
                ),
                Text(value=self.text, size=12, weight='bold_100')
            ]
        )