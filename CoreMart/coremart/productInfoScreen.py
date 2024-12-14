from flet import *


class ProductInfoScreen(Container):
    def __init__(self, on_back_click=None):
        super().__init__()
        self.on_back_click = on_back_click
        self.prouct_text = Text(
            value='Ques Designer',
            weight=FontWeight.W_500,
            size=30
        )
        self.product_desc_text=Text(
            value='We got you covered with the world most popular designer brand at a very affordable price, what are you waiting for, order now!'
        )
        self.product_price=Text(
            value='25000',
            weight=FontWeight.W_600,
            size=25
        )
        self.rating_text = Text(
            value='4.8'
        )

        self.item_remaining_text = Text(
            value=f'Item Remaining: 20',
            size=9
        )
        self.theme = Theme(hint_color='black')
        self.content = Column(
            controls=[
                Container(
                    
                    content=Stack(
                        
                        controls=[
                            Row(
                                scroll=ScrollMode.HIDDEN,
                                controls=[
                                    Image(
                                        width=360,
                                        height=240,
                                        src=f'https://picsum.photos/200/200?19',
                                        filter_quality=FilterQuality.HIGH,
                                        fit=ImageFit.COVER
                                    ),
                                    Image(
                                        width=360,
                                        height=240,
                                        src=f'https://picsum.photos/200/200?20',
                                        filter_quality=FilterQuality.HIGH,
                                        fit=ImageFit.COVER
                                    ),
                                    Image(
                                        width=360,
                                        height=240,
                                        src=f'https://picsum.photos/200/200?21',
                                        filter_quality=FilterQuality.HIGH,
                                        fit=ImageFit.COVER
                                    ),
                                ]
                            ),    
                            Row(
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    IconButton(icon=Icons.ARROW_BACK, icon_color='red', on_click=self.on_back_click),
                                    IconButton(icon=Icons.FAVORITE_OUTLINE_OUTLINED, icon_color='red'),
                                ]
                            )
                        ]
                    )
                ),
                Container(
                    padding=20,
                    height=280,
                    content=Column(
                        controls=[
                            Row(
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    self.prouct_text,
                                    Row(
                                        controls=[
                                            Icon(
                                                name=Icons.STAR,
                                                color='#67b19f'
                                            ),
                                            self.rating_text
                                        ]
                                    )
                                ]
                            ),
                            self.product_desc_text,
                            self.item_remaining_text,
                            
                        ]
                    )
                ),
                Container(
                    padding=padding.only(right=20, left=20, top=5),
                    
                    content=Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Column(
                                controls=[
                                    Text(value='Price:'),
                                    self.product_price
                                ]
                            ),
                            ElevatedButton(
                                icon=Icons.TROLLEY,
                                text='ADD TO CART',
                                height=70,
                                # bgcolor='#67b19f'
                            )  
                        ]
                    )
                ),
                Container(
                    padding=20,
                    content=ElevatedButton(
                        text='ORDER',
                        width=360,
                        height=60,
                        # style=ButtonStyle(bgcolor='#67b19f')
                    )
                )
            ]
        )
