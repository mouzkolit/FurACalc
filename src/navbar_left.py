import flet as ft 
from Dashboard import DashBoard
from DataShower import DataShower

class NavBar():
    def __init__(self, page):
        """This is the controller for the Navigation Part
        Which should detect on_click changes of the Buttons
        Added to the AppBar
        args:
            page (ft.Page) -> Main Page of the App 
        """
        self._route = "Welcome"
        self.page = page
        self.dashboard = DashBoard(page) 
        self.appbar = None
    
    def change_navbar_state(self,e):
        """
        This is the controller function that should detect changes when a button in the 
        AppBar is clicked
        Args:
            e (event): Button click event in the AppBar
        """
        selected_name = e.control.text # should return the Text of the Button
        if selected_name == "Analysis":
            self.route = "WelcomePage"
            self.dashboard.add_page(self.page, self.appbar)
            
        elif selected_name == "ImageLoader":
            self.route = "Dashboard"
            
        elif selected_name =="Show Data":
            self.route = "Data"
            self.table_shower = DataShower(self.page, self.appbar)
            self.table_shower.add_page(self.page, self.appbar)
            
    @property 
    def route(self):
        """ Retrieve the selected index"""
        print(f"Retrieved: {self._route}")
        return self._route
    
    @route.setter
    def route(self, value):
        print(f"Set Route to the following value: {value}")
        self._route = value      
        
        
        
    
        
     
        
        