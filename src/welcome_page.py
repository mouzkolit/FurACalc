from flet import (
    Container,
    Icon,
    Page,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin,
    OutlinedButton,
    UserControl
)
from navbar_left import NavBar

class WelcomePage():
    def __init__(self, page: Page):
        self.page = page
        self.navbar_control = NavBar(page)
        self.appbar = AppBar(
            leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=Text("FurCalc",size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                OutlinedButton(text = "Analysis", height= 50, on_click=self.navbar_control.change_navbar_state),
                OutlinedButton(text = "ImageLoader", height= 50,on_click=self.navbar_control.change_navbar_state),
                OutlinedButton(text = "Show Data", height= 50, on_click=self.navbar_control.change_navbar_state),
            ],
        )
        self.navbar_control.appbar = self.appbar
        self.page.appbar = self.appbar
        self.page.update()
        
                         
