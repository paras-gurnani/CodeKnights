from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class MainPage:
    def __init__(self,window):
        self.window = window
        self.frame = Frame(window, height=640, width=740, bg="white")
        self.frame.pack()
        self.add_labels()
        self.add_buttons()
        self.add_loader()
        self.convert()



    def add_labels(self):
        self.brand = Label(self.frame, text="CodeKnights",padx=10, font=('Segoe UI Black bold', 25), bg='white')
        self.brand.place(x=30,y=30)

    def add_buttons(self):
        # upload_icon = PhotoImage(file = r'D:\coding\DevnagiriOCR\upload_icon.png')
        self.upload_pdf = Button(self.frame,command=self.browse,text='Upload the pdf file',padx=10,font=('Seoge UI Black bold',15),bg='white')
        self.upload_pdf.place(x=210,y=200)
        self.convert_button=Button(self.frame,command=self.load,text='Convert',padx=10,font=('Seoge UI Black',10),bg='white')
        self.convert_button.place(x=420,y=205)
        self.excel_sheet = Button(self.frame,text='Converted Excel Sheet',padx=10,font=('Seoge UI Black bold',15),bg='white')
        self.excel_sheet.place(x=235,y=340)

    def add_loader(self):
        self.progress = ttk.Progressbar(self.frame, orient=HORIZONTAL,length=250, mode='determinate')
        self.progress.place(x=225,y=275)

    def convert(self):
        pass

    def load(self):
        import time
        self.progress['value'] = 20
        self.window.update_idletasks()
        time.sleep(0.5)

        self.progress['value'] = 40
        self.window.update_idletasks()
        time.sleep(0.5)

        self.progress['value'] = 60
        self.window.update_idletasks()
        time.sleep(0.5)

        self.progress['value'] = 80
        self.window.update_idletasks()
        time.sleep(0.5)

        self.progress['value'] = 100
        self.window.update_idletasks()
        time.sleep(0.5)
        self.progress['value'] = 100

    def browse(self):
        self.filename = filedialog.askopenfilename(initialdir='/', title='Select PDF')
        print(type(self.filename), self.filename)


if __name__=='__main__':
    window = Tk()
    window.geometry('740x640')
    MainPage(window)
    window.mainloop()