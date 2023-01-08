import flet as ft 
from Dashboard import DashBoard

class NavBar():
    def __init__(self, page):
        """Create the Navigation Bar
        """
        self._route = "Welcome"
        self.page = page
        self.dashboard = DashBoard(page)
        self.appbar = None
    
    def change_navbar_state(self,e):
        """

        Args:
            e (_type_): _description_
        """
        selected_name = e.control.text
        if selected_name == "Analysis":
            self.route = "WelcomePage"
            self.dashboard.add_page(self.page, self.appbar)
        elif selected_name == "ImageLoader":
            self.route = "Dashboard"
        elif selected_name =="Show Data":
            self.route = "ImageLoader"
            
    @property 
    def route(self):
        """ Retrieve the selected index"""
        print(f"Retrieved: {self._route}")
        return self._route
    
    @route.setter
    def route(self, value):
        print(f"Set Route to the following value: {value}")
        self._route = value      
        
        
        
    
        
     
        
        