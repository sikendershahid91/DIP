#!/usr/bin/env python3 

#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import cip_controller
import numpy as np
from color_transformations_navya import rgb2cmyk
from color_transformations_navya import rgb2hsi
from sharpening_jay import sharpen_filter 
import filters
import cip
from PIL import Image, ImageTk
import cv2
import copy
from smoothing_wahab import smoothing_filter

class cip_ui:
    def __init__(self):
        self.imageController = cip_controller.image_selector
        self.window = tk.Tk()
        self.currentTab = 0
        self.tempImage = copy.deepcopy(self.imageController.cv2Image) #if the tab is changed then the temp image will be set to the current cv2 image stored
        self.originalImage = copy.deepcopy(self.tempImage)
        self.previousTab = copy.deepcopy(self.tempImage)
        self.note = ttk.Notebook(self.window)
        self.create_widgets()
        self.grey = False

    def get_current_tab(self): #This function returns the current tab which is usefule when apllying algos
        return(self.note.index(self.note.select()))

    def tabChange(self, thing=0):#If there is a temp change, tempImage is reset(Im not sure why the second arg is needed but it wont work without it)
        if self.currentTab == 0 and self.currentTab != self.get_current_tab():
            self.currentTab = self.get_current_tab()
            self.reset()
            self.create_image_display()
        

        elif self.currentTab != self.get_current_tab():
            self.currentTab = self.get_current_tab()
            self.tempImage = copy.deepcopy(self.imageController.cv2Image)
            self.previousTab = copy.deepcopy(self.imageController.cv2Image)
        if(self.currentTab == 2) or (self.currentTab == 1):
            self.tempImage = cv2.cvtColor(self.tempImage, cv2.COLOR_BGR2GRAY)
            self.grey=True
            temp = np.zeros((self.tempImage.shape[0], self.tempImage.shape[1], 3), dtype=np.uint8)
            for i in range(self.tempImage.shape[0]):
                for j in range(self.tempImage.shape[1]):
                    temp[i, j, 0] = self.tempImage[i, j]
                    temp[i, j, 1] = self.tempImage[i, j]
                    temp[i, j, 2] = self.tempImage[i, j]
            self.tempImage = temp
            self.imageController.cv2Image=self.tempImage
            self.create_image_display()

        elif self.grey :
            self.reset()
        print("tab index: ", self.currentTab)

    def reset(self):
        self.tempImage = copy.deepcopy(self.originalImage)
        self.previousTab = copy.deepcopy(self.originalImage)
        self.imageController.setImage(self.originalImage)
        self.create_image_display()
    
    def revert(self):
        self.tempImage = copy.deepcopy(self.previousTab)
        self.imageController.setImage(self.previousTab)
        self.create_image_display()

    def apply(self):
        Type = "RGB"
        if self.currentTab == 0:
            Type = self.color_transformation()
        elif self.currentTab == 1:
            self.density_slicing()
            self.grey = False
        elif self.currentTab == 2:
            self.greyscale_to_monocolor()
            self.grey = False
        elif self.currentTab == 3:
            self.intensity_slicing()
        elif self.currentTab == 4:
            self.smoothing()
        else:
            self.sharpening()
            

        self.imageController.setImage(self.tempImage)
        self.create_image_display(Type)

    def color_transformation(self):
        if(self.cit.get() == 1):
            self.tempImage = rgb2hsi.rgb2hsi(self.tempImage)
            return"HSL"
        else:
            self.tempImage = rgb2cmyk.rgb2cmyk(self.tempImage)
            return "CMYK"
        return "RGB"

    def greyscale_to_monocolor(self):
        temp = copy.deepcopy(self.tempImage)
        self.tempImage = filters.Slice().gray_to_color_transformation(temp, (float(self.blue_spinbox.get()), float(self.green_spinbox.get()), float(self.red_spinbox.get())))
    def density_slicing(self):
        temp = copy.deepcopy(self.tempImage)
        self.tempImage = filters.Slice().density_slicing(temp, (int(self.s_min_spinbox.get()),int(self.s_max_spinbox.get())),(float(self.d_blue_spinbox.get()), float(self.d_green_spinbox.get()), float(self.d_red_spinbox.get())))
    def intensity_slicing(self):
        col = 3-self.color_channel.get()
        print(col)
        temp = copy.deepcopy(self.tempImage[:,:,col])

        #if self.type_channel==2:#HSI
        #    temp = rgb2hsi.rgb2hsi(temp)
       # if self.type_channel==3:#CMYK
       #     temp = rgb2cmyk.rgb2cmyk(temp)
        options = [
        "Linear Slice",
        "Constant Slice",
        "Inverted Linear Slice",
        "Inverted Constant Slice"
        ]
        
        if self.slice_types.get()==options[0]:
            self.tempImage[:,:,col] = filters.Slice().linear_slice(temp, (float(self.s_min_spinbox.get()), float(self.s_max_spinbox.get())), float(self.gain_spinbox.get()))
        elif self.slice_types.get()==options[1]:
            self.tempImage[:,:,col] = filters.Slice().constant_slice(temp, (float(self.s_min_spinbox.get()), float(self.s_max_spinbox.get())), float(self.gain_spinbox.get()))
        elif self.slice_types.get()==options[2]:
            self.tempImage[:,:,col] = filters.Slice().inverted_linear_slice(temp, (float(self.s_min_spinbox.get()), float(self.s_max_spinbox.get())), float(self.gain_spinbox.get()))
        elif self.slice_types.get()==options[3]:
            self.tempImage[:,:,col] = filters.Slice().inverted_constant_slice(temp, (float(self.s_min_spinbox.get()), float(self.s_max_spinbox.get())), float(self.gain_spinbox.get())) 
            
    def smoothing(self):
        self.tempImage = smoothing_filter.smoothing(copy.deepcopy(self.tempImage))
    
    def sharpening(self):
        #cv2.imshow("sharp", self.tempImage)
        self.tempImage = sharpen_filter.sharpen(self.tempImage)
        
    def create_widgets(self):

        self.window.geometry("1000x520")  # You want the size of the app to be 500x500
        self.window.resizable(0, 0)
        self.window.title("Color Image Processing by Team 9")

        loadimg_button = tk.Button(text="Load image", command=self.imageController.selectImage)
        loadimg_button.place(x=20, y=20)
        apply_button = tk.Button(text="Apply", command=self.apply)
        apply_button.place(x=100, y=20)
        reset_button = tk.Button(text="Reset", command=self.reset)
        reset_button.place(x=150, y=20)
        revert_button = tk.Button(text="Revert", command=self.revert)
        revert_button.place(x=200, y=20)
        # Create main frame with tabs ("self.notebook")
        tab1 = tk.Frame(self.note, height=400, width=950)
        tab2 = tk.Frame(self.note, height=400, width=950)
        tab3 = tk.Frame(self.note, height=400, width=950)
        tab4 = tk.Frame(self.note, height=400, width=950)
        tab5 = tk.Frame(self.note, height=400, width=950)
        tab6 = tk.Frame(self.note, height=400, width=950)

        self.note.add(tab1, text="Color Image Transformation")
        self.note.add(tab6, text="Density Slicing")
        self.note.add(tab5, text="Monocolor")
        self.note.add(tab2, text="Intensity Slicing")
        self.note.add(tab3, text="Smoothing")
        self.note.add(tab4, text="Sharpening")

        self.note.place(x=20, y=70)
        self.note.bind("<<NotebookTabChanged>>",self.tabChange)
    
        self.create_CIT_tab(tab1)
        self.create_intensityslicing_tab(tab2)
        self.create_smoothing_tab(tab3)
        self.create_sharpening_tab(tab4)
        self.create_greyscale_to_monocolor(tab5)
        self.create_densityslicing_tab(tab6)
        print(tab1.event_info)

    def create_image_display(self, Type="RGB"):
        #.resize((350, 750), Image.ANTIALIAS)
        img = self.imageController.prepForDisplay(Type)
        panel = tk.Label(self.window, text ="image",image=img, height = 385, width = 660)
        panel.image=img
        panel.place(x = 300, y = 100)

    def create_CIT_tab(self, tab):
        # Tab 1 contents - Color Image Transformation
        
        lf = ttk.Labelframe(tab, text='Select methods', height=350, width=200)
        lf.place(x=20, y=20)

        self.cit = tk.IntVar()
        tk.Radiobutton(lf, text="RGB to HSI", variable=self.cit, value=1).place(x=10, y=10)
        tk.Radiobutton(lf, text="RGB to CMYK", variable=self.cit, value=2).place(x=10, y=40)

        tk.Frame(lf, height=2, width=170, bd=1, relief="sunken").place(x=10, y=80)

    def create_greyscale_to_monocolor (self, tab):
        lf = ttk.Labelframe(tab, text='Select methods', height=350, width=200)
        lf.place(x=20, y=20)
         # Red Channel value
        red_text = tk.Text(lf, height=2, width=10, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        red_text.place(x=10, y=10)
        red_text.insert("end", "Red:")

        self.red_spinbox = tk.Spinbox(lf, width=5, from_=0, to=255, increment=1)
        self.red_spinbox.place(x=100, y=10)
         # Green Channel Value
        green_text = tk.Text(lf, height=2, width=10, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        green_text.place(x=10, y=40)
        green_text.insert("end", "Green:")

        self.green_spinbox = tk.Spinbox(lf, width=5, from_=0, to=255, increment=1)
        self.green_spinbox.place(x=100, y=40)
         # Blue Channel Value
        blue_text = tk.Text(lf, height=2, width=10, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        blue_text.place(x=10, y=70)
        blue_text.insert("end", "Blue:")

        self.blue_spinbox = tk.Spinbox(lf, width=5, from_=0, to=255, increment=1)
        self.blue_spinbox.place(x=100, y=70)
    def create_intensityslicing_tab(self, tab):
        # Tab 2 contents - Intensity slicing
        lf = ttk.Labelframe(tab, text='Select methods', height=350, width=200)
        lf.place(x=20, y=20)

        self.slice_types = tk.StringVar()
        self.slice_types.set("Linear Slice")
        
        tk.OptionMenu(lf, self.slice_types, "Linear Slice","Constant Slice","Inverted Linear Slice", "Inverted Constant Slice").place(x=10, y=10)
        """
        # Channels
        self.type_channel = tk.IntVar()
        tk.Radiobutton(lf, text="RGB", variable=self.type_channel, value=1).place(x=10, y=50)
        tk.Radiobutton(lf, text="HSI", variable=self.type_channel, value=2).place(x=60, y=50)
        tk.Radiobutton(lf, text="CMYK", variable=self.type_channel, value=3).place(x=110, y=50)
        tk.Frame(lf, height=2, width=170, bd=1, relief="sunken").place(x=10, y=90)
"""
        # Color
        self.color_channel = tk.IntVar()
        tk.Radiobutton(lf, text="Red", variable=self.color_channel, value=1).place(x=10, y=100)
        tk.Radiobutton(lf, text="Green", variable=self.color_channel, value=2).place(x=10, y=120)
        tk.Radiobutton(lf, text="Blue", variable=self.color_channel, value=3).place(x=10, y=140)
        tk.Frame(lf, height=2, width=180, bd=1, relief="sunken").place(x=10, y=160)

        """
        # Minimun intensity found in image
        imin_text = tk.Text(lf, height=2, width=5, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        imin_text.place(x=10, y=180)
        imin_text.insert("end", "Min I:")

        self.i_min = tk.StringVar()
        imin_entry = tk.Entry(lf, width=5, relief="flat", bg="gray94", textvariable=self.i_min)
        imin_entry.place(x=60, y=180)
        self.i_min.set(str(.158))

        # Max intensity found in image
        imax_text = tk.Text(lf, height=2, width=5, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        imax_text.place(x=10, y=200)
        imax_text.insert("end", "Max I:")

        self.i_max = tk.StringVar()
        imax_entry = tk.Entry(lf, width=5, relief="flat", bg="gray94", textvariable=self.i_max)
        imax_entry.place(x=60, y=200)
        self.i_max.set(str(.858))
"""
        # Minimum intensity value for slicing
        smin_text = tk.Text(lf, height=2, width=10, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        smin_text.place(x=10, y=220)
        smin_text.insert("end", "Min Slicing:")

        self.s_min_spinbox = tk.Spinbox(lf, width=5, from_=0, to=255, increment=.001)
        self.s_min_spinbox.place(x=100, y=220)

        # Max intensity value for slicing
        smax_text = tk.Text(lf, height=2, width=10, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        smax_text.place(x=10, y=240)
        smax_text.insert("end", "Max Slicing:")

        self.s_max_spinbox = tk.Spinbox(lf, width=5, from_=0, to=255, increment=.001)
        self.s_max_spinbox.place(x=100, y=240)

        # TODO: prevent max to go below min and viceversa
        
        # Gain value for slicing
        gain_text = tk.Text(lf, height=2, width=10, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        gain_text.place(x=10, y=260)
        gain_text.insert("end", "Gain:")

        self.gain_spinbox = tk.Spinbox(lf, width=5, from_=0, to=2, increment=.001)
        self.gain_spinbox.place(x=100, y=260)

    def create_densityslicing_tab(self, tab):
        # Tab 5 contents - Density slicing
        lf = ttk.Labelframe(tab, text='Select methods', height=350, width=200)
        lf.place(x=20, y=20)
        # Minimum intensity value for slicing
        smin_text = tk.Text(lf, height=2, width=10, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        smin_text.place(x=10, y=40)
        smin_text.insert("end", "Min Slicing:")

        self.s_min_spinbox = tk.Spinbox(lf, width=5, from_=0, to=255, increment=1)
        self.s_min_spinbox.place(x=100, y=40)

        # Max intensity value for slicing
        smax_text = tk.Text(lf, height=2, width=10, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        smax_text.place(x=10, y=70)
        smax_text.insert("end", "Max Slicing:")

        self.s_max_spinbox = tk.Spinbox(lf, width=5, from_=0, to=255, increment=1)
        self.s_max_spinbox.place(x=100, y=70)

         # Red Channel value
        red_text = tk.Text(lf, height=2, width=10, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        red_text.place(x=10, y=100)
        red_text.insert("end", "Red:")

        self.d_red_spinbox = tk.Spinbox(lf, width=5, from_=0, to=255, increment=1)
        self.d_red_spinbox.place(x=100, y=100)
         # Green Channel Value
        green_text = tk.Text(lf, height=2, width=10, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        green_text.place(x=10, y=130)
        green_text.insert("end", "Green:")

        self.d_green_spinbox = tk.Spinbox(lf, width=5, from_=0, to=255, increment=1)
        self.d_green_spinbox.place(x=100, y=130)
         # Blue Channel Value
        blue_text = tk.Text(lf, height=2, width=10, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        blue_text.place(x=10, y=160)
        blue_text.insert("end", "Blue:")

        self.d_blue_spinbox = tk.Spinbox(lf, width=5, from_=0, to=255, increment=1)
        self.d_blue_spinbox.place(x=100, y=160)


    def create_sharpening_tab(self, tab):
        # Tab 3 contents - Sharpening
        lf = ttk.Labelframe(tab, height=350, width=200)
        lf.place(x=20, y=20)

        txt = tk.Text(lf, wrap="word", height=5, width=25, font=("TkDefaultFont", 8, "normal"), relief="flat",
                      bg="gray94")
        txt.place(x=10, y=30)
        txt.insert("end", "Load an image and click on \"Apply\" to perform sharpening")

    def create_smoothing_tab(self, tab):
        # Tab 3 contents - Smoothing
        lf = ttk.Labelframe(tab, height=370, width=200)
        lf.place(x=20, y=20)

        txt = tk.Text(lf, wrap="word", height=5, width=25, font=("TkDefaultFont", 8, "normal"), relief="flat",
                      bg="gray94")
        txt.place(x=10, y=30)
        txt.insert("end", "Load an image and click on \"Apply\" to perform smoothing")


app = cip_ui()

