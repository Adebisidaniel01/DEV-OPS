from flet import *
from Materials import SearchList, CategoryCircle

class SearchScreen(Container):
    def __init__(self, on_back_click=None):
        super().__init__()
        self.padding=padding.only(top=25)
        self.click = on_back_click
        self.category_tabs = Tabs(
            selected_index=0,
            on_change=self.on_tabs_change,
            tabs=[
                Tab(text='Fashion'),
                Tab(text='Home & Kitchen'),
                Tab(text='Gadgets'),
                Tab(text='Others'),
            ]
        )
        self.search_bar=SearchBar(
            on_tap=self.on_search,
            bar_leading=Text('CoreCart'),
            controls=[
                SearchList(search_text='Cloth'),
                SearchList(search_text='Food')
            ],
            width=280
        )
        self.home_kitchen_container = Container(
            visible=False,
            padding=padding.all(30),
            content=Column(
                controls=[
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            CategoryCircle(
                                img_pth='coremart/assets/furniture.jpg',
                                text='Furniture'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/appliances.jpg',
                                text='Appliances'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/kitchen_dining.jpg',
                                text='Kitchen & Dining'
                            ),
                        ]
                    ),
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            CategoryCircle(
                                img_pth='coremart/assets/home_decor.jpg',
                                text='Home Decor'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/bedding.jpg',
                                text='Bedding'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/bath.jpg',
                                text='Bath'
                            ),
                        ]
                    ),
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            CategoryCircle(
                                img_pth='coremart/assets/tools.jpg',
                                text='Tools & Hardware'
                            ),
                        ]
                    )
                ]                  
            )
        )
        self.others_container = Container(
            visible=False,
            padding=padding.all(30),
            content=Column(
                controls=[
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            CategoryCircle(
                                img_pth='coremart/assets/sports.jpg',
                                text='Sports'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/toys.jpg',
                                text='Toys & Games'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/books.jpg',
                                text='Books'
                            ),
                        ]
                    ),
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            CategoryCircle(
                                img_pth='coremart/assets/music.jpg',
                                text='Music'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/grocery.jpg',
                                text='Grocery'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/baby.jpg',
                                text='Baby'
                            ),
                        ]
                    ),
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            CategoryCircle(
                                img_pth='coremart/assets/automotive.jpg',
                                text='Automotive'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/pet.jpg',
                                text='Pet Supplies'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/health_beauty.jpg',
                                text='Health & Beauty'
                            ),
                        ]
                    ),
                ]
            )
        )
        self.gadgets_container = Container(
            visible=False,
            padding=padding.all(30),
            content=Column(
                controls=[
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            CategoryCircle(
                                img_pth='coremart/assets/monitors.jpg',
                                text='Monitors'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/laptops.jpg',
                                text='Laptops'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/desktops.jpg',
                                text='Desktops'
                            ),
                        ]
                    ),
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            CategoryCircle(
                                img_pth='coremart/assets/gadgets.jpg',
                                text='All-in-ones'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/tablets.jpg',
                                text='Tablets'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/phones.jpg',
                                text='Phones'
                            ),
                        ]
                    ),
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            CategoryCircle(
                                img_pth='coremart/assets/smartwatch.jpg',
                                text='Smartwatches'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/gaming.jpg',
                                text='Gaming'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/tvs.jpg',
                                text='TVS'
                            ),
                        ]
                    ),
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            CategoryCircle(
                                img_pth='coremart/assets/cameras.jpg',
                                text='Cameras'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/audio.jpg',
                                text='Audio'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/car_accessories.jpg',
                                text='Car Accessories'
                            ),
                        ]
                    ),
                ]
            )
        )
        self.fashon_container = Container(
            padding=padding.all(30),
            content=Column(
                controls=[
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            CategoryCircle(
                                img_pth='coremart/assets/women2.jpg',
                                text='Women'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/men.jpg',
                                text='Men'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/kids.jpg',
                                text='Kids'
                            ),
                        ]
                    ),
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            CategoryCircle(
                                img_pth='coremart/assets/shoes.jpg',
                                text='Shoes'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/accessories.jpg',
                                text='Accessories'
                            ),
                            CategoryCircle(
                                img_pth='coremart/assets/beauty.jpg',
                                text='Beauty'
                            ),
                        ]
                    ),
                ]
            )
        )
        self.content = Column(
            controls=[
                Row(
                    controls=[
                        IconButton(icon='arrow_back', on_click=self.click),
                        self.search_bar,
                    ]
                ),
                Container(
                    padding=padding.only(bottom=15)
                ),
                Column(
                    controls=[
                        self.category_tabs 
                    ]
                ),
                self.fashon_container,
                self.gadgets_container,
                self.others_container,
                self.home_kitchen_container
            ]
        )
    def on_tabs_change(self, e):
        index = self.category_tabs.selected_index
        self.fashon_container.visible = True if index == 0 else False
        self.home_kitchen_container.visible = True if index == 1 else False
        self.gadgets_container.visible = True if index == 2 else False
        self.others_container.visible = True if index == 3 else False
        self.update()


    def on_search(self, e):
        self.search_bar.open_view()

