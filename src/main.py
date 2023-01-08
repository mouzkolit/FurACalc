import flet as ft
from flet import (
    Page,
    colors
)
from welcome_page import WelcomePage
 


def main(page: Page):
    """_summary_

    Args:
        page (ft.Page): _description_
    """    
    page.title = "FurACalc"
    app = WelcomePage(page)
    page.update()
    

ft.app(target = main)