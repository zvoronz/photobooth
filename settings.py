#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 11, 2017 01:50:04 AM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import settings_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    settings_support.set_Tk_var()
    top = photobooth_settings (root)
    settings_support.init(root, top)
    root.mainloop()

w = None
def create_photobooth_settings(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    settings_support.set_Tk_var()
    top = photobooth_settings (w)
    settings_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_photobooth_settings():
    global w
    w.destroy()
    w = None


class photobooth_settings:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 14 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("594x400+100+0")
        top.title("photobooth settings")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.btnSave = Button(top)
        self.btnSave.place(relx=0.74, rely=0.83, height=44, width=127)
        self.btnSave.configure(activebackground="#d9d9d9")
        self.btnSave.configure(activeforeground="#000000")
        self.btnSave.configure(background="#d9d9d9")
        self.btnSave.configure(command=settings_support.onBtnSaveConfig)
        self.btnSave.configure(disabledforeground="#a3a3a3")
        self.btnSave.configure(font=font9)
        self.btnSave.configure(foreground="#000000")
        self.btnSave.configure(highlightbackground="#d9d9d9")
        self.btnSave.configure(highlightcolor="black")
        self.btnSave.configure(pady="0")
        self.btnSave.configure(text='''Save''')

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.0, rely=0.29, height=19, width=131)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(justify=RIGHT)
        self.TLabel1.configure(text='''Print format:''')

        self.cbPrintFormat = ttk.Combobox(top)
        self.cbPrintFormat.place(relx=0.24, rely=0.28, relheight=0.05
                , relwidth=0.11)
        self.cbPrintFormat.configure(textvariable=settings_support.combobox)
        self.cbPrintFormat.configure(takefocus="")
        self.cbPrintFormat.configure(cursor="arrow")

        self.btnCameraUpdate = Button(top)
        self.btnCameraUpdate.place(relx=0.86, rely=0.02, height=24, width=67)
        self.btnCameraUpdate.configure(activebackground="#d9d9d9")
        self.btnCameraUpdate.configure(activeforeground="#000000")
        self.btnCameraUpdate.configure(background="#d9d9d9")
        self.btnCameraUpdate.configure(command=settings_support.onBtnCameraUpdate)
        self.btnCameraUpdate.configure(disabledforeground="#a3a3a3")
        self.btnCameraUpdate.configure(foreground="#000000")
        self.btnCameraUpdate.configure(highlightbackground="#d9d9d9")
        self.btnCameraUpdate.configure(highlightcolor="black")
        self.btnCameraUpdate.configure(pady="0")
        self.btnCameraUpdate.configure(text='''Update''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.0, rely=0.36, height=21, width=130)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Delay screens:''')

        self.cbDelayScreen = ttk.Combobox(top)
        self.cbDelayScreen.place(relx=0.24, rely=0.37, relheight=0.05
                , relwidth=0.11)
        self.cbDelayScreen.configure(textvariable=settings_support.combobox2)
        self.cbDelayScreen.configure(takefocus="")
        self.cbDelayScreen.configure(cursor="arrow")

        self.TLabel2 = ttk.Label(top)
        self.TLabel2.place(relx=0.0, rely=0.45, height=19, width=130)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(text=''''Strike a pose' delay:''')

        self.txtSAP = ttk.Entry(top)
        self.txtSAP.place(relx=0.24, rely=0.44, relheight=0.05, relwidth=0.11)
        self.txtSAP.configure(textvariable=settings_support.txtSAPVar)
        self.txtSAP.configure(takefocus="")
        self.txtSAP.configure(cursor="arrow")

        self.TLabel3 = ttk.Label(top)
        self.TLabel3.place(relx=0.35, rely=0.45, height=19, width=20)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(relief=FLAT)
        self.TLabel3.configure(text='''ms''')

        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.03, rely=0.53, relheight=0.38, relwidth=0.31)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=186)

        self.btnTakePhoto = Button(top)
        self.btnTakePhoto.place(relx=0.03, rely=0.93, height=24, width=187)
        self.btnTakePhoto.configure(activebackground="#d9d9d9")
        self.btnTakePhoto.configure(activeforeground="#000000")
        self.btnTakePhoto.configure(background="#d9d9d9")
        self.btnTakePhoto.configure(command=settings_support.onBtnTakePhoto)
        self.btnTakePhoto.configure(disabledforeground="#a3a3a3")
        self.btnTakePhoto.configure(foreground="#000000")
        self.btnTakePhoto.configure(highlightbackground="#d9d9d9")
        self.btnTakePhoto.configure(highlightcolor="black")
        self.btnTakePhoto.configure(pady="0")
        self.btnTakePhoto.configure(text='''Take photo''')

        self.Label6 = Label(top)
        self.Label6.place(relx=0.0, rely=0.03, height=21, width=64)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(justify=RIGHT)
        self.Label6.configure(text='''Camera:''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.0, rely=0.1, height=21, width=64)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(justify=RIGHT)
        self.Label2.configure(text='''Printer:''')
        self.Label2.configure(width=64)

        self.lblCamera = Label(top)
        self.lblCamera.place(relx=0.13, rely=0.03, height=21, width=424)
        self.lblCamera.configure(activebackground="#f9f9f9")
        self.lblCamera.configure(activeforeground="black")
        self.lblCamera.configure(background="#ffffff")
        self.lblCamera.configure(disabledforeground="#a3a3a3")
        self.lblCamera.configure(foreground="#000000")
        self.lblCamera.configure(highlightbackground="#d9d9d9")
        self.lblCamera.configure(highlightcolor="black")
        self.lblCamera.configure(textvariable=settings_support.lblCameraVar)

        self.lblPrinter = Label(top)
        self.lblPrinter.place(relx=0.13, rely=0.1, height=21, width=424)
        self.lblPrinter.configure(activebackground="#f9f9f9")
        self.lblPrinter.configure(activeforeground="black")
        self.lblPrinter.configure(background="#ffffff")
        self.lblPrinter.configure(disabledforeground="#a3a3a3")
        self.lblPrinter.configure(foreground="#000000")
        self.lblPrinter.configure(highlightbackground="#d9d9d9")
        self.lblPrinter.configure(highlightcolor="black")
        self.lblPrinter.configure(textvariable=settings_support.lblPrinterVar)

        self.btnUpdatePrinter = Button(top)
        self.btnUpdatePrinter.place(relx=0.86, rely=0.1, height=24, width=67)
        self.btnUpdatePrinter.configure(activebackground="#d9d9d9")
        self.btnUpdatePrinter.configure(activeforeground="#000000")
        self.btnUpdatePrinter.configure(background="#d9d9d9")
        self.btnUpdatePrinter.configure(command=settings_support.onBtnPrinterUpdate)
        self.btnUpdatePrinter.configure(disabledforeground="#a3a3a3")
        self.btnUpdatePrinter.configure(foreground="#000000")
        self.btnUpdatePrinter.configure(highlightbackground="#d9d9d9")
        self.btnUpdatePrinter.configure(highlightcolor="black")
        self.btnUpdatePrinter.configure(pady="0")
        self.btnUpdatePrinter.configure(text='''Update''')

        self.ckPreviewScreen = Checkbutton(top)
        self.ckPreviewScreen.place(relx=0.43, rely=0.28, relheight=0.06
                , relwidth=0.24)
        self.ckPreviewScreen.configure(activebackground="#d9d9d9")
        self.ckPreviewScreen.configure(activeforeground="#000000")
        self.ckPreviewScreen.configure(background="#d9d9d9")
        self.ckPreviewScreen.configure(disabledforeground="#a3a3a3")
        self.ckPreviewScreen.configure(foreground="#000000")
        self.ckPreviewScreen.configure(highlightbackground="#d9d9d9")
        self.ckPreviewScreen.configure(highlightcolor="black")
        self.ckPreviewScreen.configure(justify=LEFT)
        self.ckPreviewScreen.configure(text='''Preview screen''')
        self.ckPreviewScreen.configure(variable=settings_support.ckBoxVar)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.42, rely=0.35, height=21, width=147)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''End screen delay:''')

        self.Label7 = Label(top)
        self.Label7.place(relx=0.42, rely=0.43, height=21, width=148)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Preview screen delay:''')

        self.txtEndDelay = ttk.Entry(top)
        self.txtEndDelay.place(relx=0.67, rely=0.35, relheight=0.05
                , relwidth=0.11)
        self.txtEndDelay.configure(textvariable=settings_support.txtEndScreenDelayVar)
        self.txtEndDelay.configure(takefocus="")
        self.txtEndDelay.configure(cursor="arrow")

        self.txtPreviewDelay = ttk.Entry(top)
        self.txtPreviewDelay.place(relx=0.67, rely=0.43, relheight=0.05
                , relwidth=0.11)
        self.txtPreviewDelay.configure(textvariable=settings_support.txtPreviewScreenDelay)
        self.txtPreviewDelay.configure(takefocus="")
        self.txtPreviewDelay.configure(cursor="arrow")






if __name__ == '__main__':
    vp_start_gui()



