from flet import *
from Materials import AdsCart
from productInfoScreen import ProductInfoScreen


class MainScreen(Container):
    def __init__(self):
        super().__init__()
        self.product_content = Container(
            visible=False,
            content=ProductInfoScreen(on_back_click=self.back_to_main_screen)
        )
        self.theme_mode = ThemeMode.DARK
        self.padding=20
        self.main_content = Column(
            controls=[
                Container(
                    content=Column(
                        controls=[
                            Text("Top Deals!"),
                            Container(
                                content=Row(
                                    scroll=ScrollMode.HIDDEN,
                                    spacing=10,
                                    controls=[
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?10',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?20',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?30',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                    ]
                                )
                            )
                        ]
                    )
                ),
                Container(
                    content=Column(
                        controls=[
                            Text('Tasty Foods'),
                            Container(
                                content=Row(
                                    scroll=ScrollMode.HIDDEN,
                                    controls=[
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?15',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?25',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?35',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                    ]
                                )
                            )

                        ]
                    )
                ),
                Container(
                    content=Column(
                        controls=[
                            Text('Classic Outfits'),
                            Container(
                                content=Row(
                                    scroll=ScrollMode.HIDDEN,
                                    controls=[
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?12',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?22',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?32',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                    ]
                                )
                            )

                        ]
                    )
                ),
                Container(
                    content=Column(
                        controls=[
                            Text('Quality Assesories'),
                            Container(
                                content=Row(
                                    scroll=ScrollMode.HIDDEN,
                                    controls=[
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?14',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?24',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?34',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                    ]
                                )
                            )

                        ]
                    )
                ),
                Container(
                    content=Column(
                        controls=[
                            Text('Others'),
                            Container(
                                content=Row(
                                    scroll=ScrollMode.HIDDEN,
                                    controls=[
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?16',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?26',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                        AdsCart(
                                            image_src=f'https://picsum.photos/200/200?36',
                                            product_title='Luxury Card',
                                            product_desc='Step up your class with Golden luxury card',
                                            product_price='10000',
                                            on_info_click=self.show_product_info
                                        ),
                                    ]
                                )
                            )

                        ]
                    )
                )
            ]
        )
        self.content = self.main_content

    def show_product_info(self, e):
        self.product_content.visible = True
        self.content = self.product_content
        self.update()

    def back_to_main_screen(self, e):
        self.product_content.visible = False
        self.content = self.main_content
        self.update()
