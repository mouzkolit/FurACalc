import flet as ft 
import pandas as pd
from DataLoaderLogs import DataLoaderLogs



class DataShower:
    """_summary_
    """
    def __init__(self, page: ft.Page, appbar: ft.AppBar):
        self.page = page
        self.appbar = appbar
        self.file_picker = ft.FilePicker(on_result=self.on_dialog_result)
        self.page.overlay.append(self.file_picker)   
        self.current_path = ft.TextField(value = "Current Path:", text_align= ft.TextAlign.LEFT, width = 500)
        self.picker_button = ft.ElevatedButton("Choose Directory...", on_click=lambda _: self.file_picker.get_directory_path())
        
    def add_page(self, page: ft.Page, appbar: ft.AppBar) -> None:
        """_summary_: Should add the Dashboard Page to the screen 
        """
        print("added page")
        page.views.clear()
        print("yeah")
        page.views.append(
            self.view_page(appbar)
        )
        page.update()
        
    def view_page(self,appbar: ft.AppBar) -> ft.View:
        self.view = ft.View(
            "/dashboard",
            [appbar,
                self.current_path,
                self.picker_button,
                
            ]
        )
        return self.view
     
    def on_dialog_result(self,e: ft.FilePickerResultEvent) -> None: 
        """Event Handler after Picking the 

        Args:
            e (ft.FilePickerResultEvent): _description_
        """
        self.current_path.value = e.path
        path = "/"+"/".join(e.path.split("/")[3:])
        self.load_logs = DataLoaderLogs(path) # is the dataframe load
        table_iterator = iter(self.load_logs)
        self.show_table(table_iterator)
        
    def show_table(self, table_iterator: list) -> None:
        """Function to Show the table in the App
        Component Should also be added to a Card for more Interactivty @toDo

        Args:
            table_iterator (iter): Iterator through the list of dataframes
        """
        trial_table = next(table_iterator)
        column_list = [ft.DataColumn(ft.Text(i)) for i in trial_table.columns]
        final_values = []
        for row in trial_table.values:
            row_list = []
            for values in row:
                row_list.append(ft.DataCell(ft.Text(str(values))))
                
            final_values.append(ft.DataRow(cells = row_list,))
        
        self.view.controls.append(
            ft.Row(
                [ft.DataTable(columns = column_list, rows = final_values)],
            scroll = "adaptive",
                     )
            )
                        
        self.view.scroll = "auto"
        self.page.scroll = "always"
        self.page.update()
                
            
                
        
        
        
        
    
        