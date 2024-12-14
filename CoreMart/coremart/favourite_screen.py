from flet import *
from Materials import FavouriteCard


class FavouriteScreen(Container):
    def __init__(self):
        super().__init__()
        self.padding = padding.all(20)
        self.fav_list=[
            FavouriteCard(
                product_title='Agege Bread',
                image_path=f'https://picsum.photos/200/200?1'
            ),
            FavouriteCard(
                product_title='Agege Bread',
                image_path=f'https://picsum.photos/200/200?2'
            ),
            FavouriteCard(
                product_title='Agege Bread',
                image_path=f'https://picsum.photos/200/200?3'
            ),
            FavouriteCard(
                product_title='Agege Bread',
                image_path=f'https://picsum.photos/200/200?4'
            ),
            FavouriteCard(
                product_title='Agege Bread',
                image_path=f'https://picsum.photos/200/200?5'
            ),
            FavouriteCard(
                product_title='Agege Bread',
                image_path=f'https://picsum.photos/200/200?6'
            ),
            FavouriteCard(
                product_title='Agege Bread',
                image_path=f'https://picsum.photos/200/200?7'
            ),
            FavouriteCard(
                product_title='Agege Bread',
                image_path=f'https://picsum.photos/200/200?8'
            ),
        ]
        self.content=Column(
            controls=[
                Row(
                    scroll='hidden',
                    wrap=True,
                    controls=self.fav_list
                )
            ]
        )

    def delete_tile(self, e):
        if e.control:
            self.fav_list.pop(self.fav_list.index())
        self.update()

    