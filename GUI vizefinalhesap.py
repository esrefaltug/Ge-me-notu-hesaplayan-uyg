import tkinter
class vizefinalort:

    def __init__(self):

        self.pencerem=tkinter.Tk()

        self.vizeframe=tkinter.Frame()
        self.finalframe=tkinter.Frame()
        self.sonucframe=tkinter.Frame()
        self.buttonframe=tkinter.Frame()

        self.vizelabel=tkinter.Label(self.vizeframe,text="Vize notu: ")
        self.vizeentry=tkinter.Entry(self.vizeframe,width=12)

        self.vizelabel.pack(side='left')
        self.vizeentry.pack(side='left')

        self.finallabel=tkinter.Label(self.finalframe,text="Final notu: ")
        self.finalentry=tkinter.Entry(self.finalframe,width=12)

        self.finallabel.pack(side='left')
        self.finalentry.pack(side='left')

        self.sonuclabel=tkinter.Label(self.sonucframe,text='Sonuç: ')
        self.avg= tkinter.StringVar()
        self.snclabel=tkinter.Label(self.sonucframe,textvariable=self.avg)

        self.sonuclabel.pack(side='left')
        self.snclabel.pack(side='left')

        self.hspbutton=tkinter.Button(self.buttonframe,text='Hesapla',command=self.Hesapla)
        self.cksbutton=tkinter.Button(self.buttonframe,text='Çıkış',command=self.pencerem.destroy)

        self.hspbutton.pack(side='left')
        self.cksbutton.pack(side='left')

        self.vizeframe.pack()
        self.finalframe.pack()
        self.sonucframe.pack()
        
        self.buttonframe.pack()

        tkinter.mainloop()

    def Hesapla(self):
            self.vize=float(self.vizeentry.get())
            self.final=float(self.finalentry.get())
            self.sonuc=(self.vize*4/10+self.final*6/10)
            self.avg.set(self.sonuc)

vizefinalort()

