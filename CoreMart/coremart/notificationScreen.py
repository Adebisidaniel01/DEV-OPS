from flet import *
from Materials import NotificationList

class NotificationScreen(Container):
    def __init__(self, on_back_click=None):
        super().__init__()
        self.on_back_click = on_back_click
        self.content=Column(
            scroll = 'hidden',
            controls=[
                Row(
                    alignment='spaceBetween',
                    controls=[
                        Row(
                            controls=[
                                IconButton(icon='arrow_back', on_click=self.on_back_click),
                                Text('Notifications'),
                            ]
                        ),
                        IconButton(icon='delete', tooltip='Clear all')
                    ]
                ),
                NotificationList(),
                NotificationList()
            ]
        )