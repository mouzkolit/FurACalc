import flet as ft 
from DataLoader import CalciumData
import matplotlib
import seaborn 
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
import cv2
import numpy as np
from matplotlib.figure import Figure
from BackendMatplot import InteractiveBackend
#matplotlib.use("svg")

class DashBoard():
    
    def __init__(self, page):
        
        self.page = page
        self.file_picker = ft.FilePicker(on_result=self.on_dialog_result)
        self.page.overlay.append(self.file_picker)   
        self.current_path = ft.TextField(value = "Current Path:", text_align= ft.TextAlign.LEFT, width = 500)
        self.picker_button = ft.ElevatedButton("Choose Directory...", on_click=lambda _: self.file_picker.get_directory_path())
        self._route = "Welcome"
        self.data_loader = None
        
    def add_page(self, page, appbar) -> None:
        """_summary_: Should add the Dashboard Page to the screen 
        args:
        
            page: ft.Page
            appbar: ft.NavigationBar
        """
        print("added page")
        page.views.clear()
        print("yeah")
        page.views.append(
            self.view_page(appbar)
        )
        page.update()
        
    def view_page(self,appbar):
        self.view = ft.View(
            "/dashboard",
            [appbar,
                self.current_path,
                self.picker_button,
                
            ]
        )
        return self.view
        
    def on_dialog_result(self,e: ft.FilePickerResultEvent):
        """_summary_

        Args:
            e (ft.FilePickerResultEvent): Opens the filepicker
        """
        self.current_path.value = e.path
        path = "/"+"/".join(e.path.split("/")[3:])
        self.Calcium = CalciumData(path)
        self.image_iterator = iter(self.Calcium)
        self.draw_image()
        self.page.update()
        
        
    def draw_image(self, e = None):
        """_summary_: this should retrieve the image from the iterator
        Draw the image into a canvas and should finally connect to the
        interactive backend-->currently this is not supported

        Args:
            e ():. If not only one image is rendered then we have to remove the old
            canvas and data
        """
        self.fig = Figure()
        
        backend = InteractiveBackend(self.fig) # Loads all the figures and provide an iterator
        image = next(self.image_iterator)# next image
        
        _,thresh = cv2.threshold(image, np.mean(image), 255, cv2.THRESH_BINARY_INV)
        print(thresh.shape)
        
        # retrieves the contours
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #plt.imshow(thresh)
        backend.draw()
        self.fig.canvas.mpl_connect('button_press_event', backend.button_press_event)

        
        # check
        if e:
            self.view.controls.pop() 
        self.view.controls.append(
            ft.Card(
                content = ft.Container(
                    content = ft.Column(
                        [
                            MatplotlibChart(self.fig),
                    ft.Row(
                        [ft.TextButton("Next Image:", on_click = self.draw_image)]
                            )
                        ]
                        
                        ),
                    width = 400,
                    padding = 10,
                    )
                )
            )
        self.page.update()
        plt.close()
        
    def get_segmentations(self, image):
        """_summary_

        Args:
            image (backend.image): Is a single image that will be used for segmentation
        """
        print("Needs to be implemented")   
        pass     
        
       
    