import matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


###################
# Function to create an Interactive Backend on its own for the Flet app, since this not 
# provided yet. Currently not working
###########################################
class InteractiveBackend(FigureCanvas):
    # Inherits from FigureCanvas from a qt backend
    def __init__(self, figure):
        """_summary_: This should initalize the new Figure Canvas

        Args:
            figure (matplotlib.figure.Figure): Figure holding the drawing
        """
        FigureCanvas.__init__(self, figure)
        self.figure = figure
        self.updated = False
        self.call_count = 0

    def draw(self):
        """_summary_: this should draws the image
        """
        if self.updated:
            return
        print("got into this function")
        self.call_count += 1
        if self.call_count > 100: # Limit the number of calls to 100
            return
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3], 'ro')
        self.figure.canvas.draw()
        self.updated = True

    def button_press_event(self, event):
        """_summary_: Evokes thes button press event and 
        identifies the location were someting is pressed

        Args:
            event (_type_): _description_
        """
        print("detected button")
        if event.inaxes:
            print("Clicked at x=%f, y=%f" % (event.xdata, event.ydata))
            self.updated = False
            self.call_count = 0
            self.draw()



