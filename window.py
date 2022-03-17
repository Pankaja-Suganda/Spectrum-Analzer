"""
Created on Sat Mar 12 07:17:30 2022
@author: Pankaja Suganda
"""

# imported libraries (all required libraries included in requirement.txt file)
from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

# importint plotting libraries
from matplotlib.backends.backend_tkagg import *
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib

# importing suppotive libraries
from cursor import Cursor
from serial.tools import list_ports
import numpy as np
import pandas as pd
import serial
import time


# application title
# you can change aplication title 
APPLICATION_TITLE   = "Spectrum Analyzer"

# text style for
FONT_GENERAL        = 'Bebas Kai'
FONT_LABEL_FRAME    = 'Bebas Kai'

# font sizes
LABEL_FONT          = (FONT_GENERAL, 9, 'bold')
LABEL_FRAME_FONT    = (FONT_LABEL_FRAME, 9, 'bold')

# here you can change Background and button Colors
BACKGROUND_COLOR    = '#fff'
BUTTON_COLOR        = '#fff'

# graph animation interval
INTERVAL            = 10000

# label texts for top bar
REF_LABEL   = "Ref Level\t: {ref:.2f} dBm"
ATT_LABEL   = "Att\t: {att:.2f} dB"
RVB_LABEL   = "RBV\t: {rvb:.2f} MHz"
VBW_LABEL   = "VBW\t: {vbw:.2f} MHz"
SWT_LABEL   = "SWT : {swt:.2f} ms"
MODE_LABEL  = "Mode : {mode:} "

# label texts for bottom bar
CENTER_FREQ_LABEL   = "Center\t: {center_freq:.2f} MHz"
SPAN_LABEL          = "Span\t: {span:.2f} MHz"

""" this is main class for the Project"""
class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.show = []
        self.spec_freq = []
        self.spec_pow  = []
        self.create_widget()
        self.testArrFill()
        self.values_updater(10)

    def testArrFill(self):
        test = pd.read_csv('TraceFile.csv', delimiter=';', header=None) 
        self.spec_freq = test[0].tolist()
        self.spec_pow  = test[1].tolist()

    """drawing all widget on the  page"""
    def create_widget(self):

        # Create a Graph
        self.fig    = Figure(figsize=(5,5), dpi=100)
        
        self.graph  = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().place(x=0, y=30, height=385, width=725)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        cursor = Cursor(self.graph)
        self.canvas.mpl_connect('motion_notify_event', cursor.mouse_move)

        slider_update = Scale(self, from_=1, to=50, orient=HORIZONTAL, bg=BACKGROUND_COLOR, label="Frequency [Hz]")
        slider_update.place(x=665, y=80,  width=125)
        # self.toolbar.update()
        # self.canvas._tkcanvas.pack(side=tk.LEFT, expand=True)

        # adding the 'logo.jpg' image 
        r_image= Image.open('./images/logo.png').resize((150,40), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(r_image)
        
        self.logo_start = Label(self, width=150, height=50, bg=BACKGROUND_COLOR, fg='dark gray')
        self.logo_start.image = self.logo  
        self.logo_start.configure(image=self.logo)
        self.logo_start.place(x=5,y=5)

        # port selector combobox 
        self.port_selector = ttk.Combobox(self, textvariable="Select Port", width=17, values=list_ports.comports())
        self.port_selector.place(x=665, y=10)

        # port select
        self.btn_select = Button(self, text="Select", height=1, width=16, font =LABEL_FONT)
        self.btn_select.place(x=665, y=40)

        # creating paramters labels for top bar
        self.lblRefLevel = Label(self, text=REF_LABEL.format(ref = 0.00),  anchor="w", bg=BACKGROUND_COLOR, font =LABEL_FONT, width = 16)
        self.lblRefLevel.place(x=170, y=10)

        self.lblAtt = Label(self, text=ATT_LABEL.format(att = 0.00),   anchor="w", bg=BACKGROUND_COLOR, font =LABEL_FONT, width = 16)
        self.lblAtt.place(x=170, y=30)

        self.lblSWT = Label(self, text=SWT_LABEL.format(swt = 0.00),  anchor="w", bg=BACKGROUND_COLOR, font =LABEL_FONT, width = 12)
        self.lblSWT.place(x=300, y=30)

        self.lblRVB = Label(self, text=RVB_LABEL.format(rvb = 0.00),  anchor="w", bg=BACKGROUND_COLOR, font =LABEL_FONT, width = 16)
        self.lblRVB.place(x=400, y=10)

        self.lblVBW = Label(self, text=VBW_LABEL.format(vbw = 0.00),   anchor="w", bg=BACKGROUND_COLOR, font =LABEL_FONT, width = 16)
        self.lblVBW.place(x=400, y=30)

        self.lblMode = Label(self, text=MODE_LABEL.format(mode = "Auto Mode"),   anchor="w", bg=BACKGROUND_COLOR, font =LABEL_FONT, width = 16)
        self.lblMode.place(x=530, y=30)

        # creating paramters labels for bottom bar
        self.lblCenter_Freq = Label(self, text=CENTER_FREQ_LABEL.format(center_freq = 0.00),   anchor="w", font =LABEL_FONT, width = 16)
        self.lblCenter_Freq.place(x=300, y=450)

        self.lblSpan = Label(self, text=SPAN_LABEL.format(span = 0.00),   anchor="w", font =LABEL_FONT, width = 16)
        self.lblSpan.place(x=450, y=450)

        # #  25 mm button drawing
        # self.btn_25mm = Button(self, text=f'37 mm', width=25, height=5, font =LABEL_FONT, highlightthickness = 1, bd = 1, bg=BACKGROUND_COLOR, command=self.btn_37mm_command)
        # self.btn_25mm.place(x=576, y=210)

    def values_updater(self, time):

        self.port_selector['values'] = list_ports.comports()

        self.graph.clear()
        #self.graph.set_title("The Spectrum Analyzer")
        self.graph.set_xlabel("Frequency (Hz)")
        self.graph.set_ylabel("Power (dBm)")
        self.graph.grid()
        self.graph.plot(self.spec_freq,self.spec_pow,c='r')
        # self.graph.fill(self.spec_freq,self.spec_pow,c='r', alpha =0.3)
 
    """"function for 37 mm button"""
    def btn_37mm_command(self):
        print("Command for 37mm")

""""main functon"""
if __name__ == "__main__":

    window = Application()
    window.geometry("800x480")    # geometry settings for 7 inchs display
    window.attributes('-toolwindow', True)
    window.configure(bg = BACKGROUND_COLOR) # assigning background color
    update = animation.FuncAnimation(window.fig, window.values_updater, interval=INTERVAL) #value updating
    #window.wm_attributes('-fullscreen', 'True') # this is for enable the full screen view
    window.wm_title(APPLICATION_TITLE) # this is for enable the full screen view
    window.mainloop()