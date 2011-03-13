import Tkinter,Image,ImageDraw,ImageTk
class App(Tkinter.Frame):
    myCan = None
    im = None
    draw = None
    pm = None
    tk_img = None
    i = 0
    def say_hi(self):
        print "hi!!!"
    def frame_say_hi(self,event):
        print "hi" + str(event.x) + "," + str(event.y)
        self.im = Image.new("RGB",(200,200),0xffff00)
        self.draw = ImageDraw.Draw(self.im)
        self.draw.line([0,0,40,self.i],fill=127)
        self.pm = ImageTk.PhotoImage(self.im)
        ##print dir(can)
        #can.delete(tk_img)
        self.tk_img = self.myCan.create_image(100,100,image=self.pm)
        self.i = self.i + 10
    def __init__(self,master):
        Tkinter.Frame.__init__(self,master)
        self.pack()

        frame = Tkinter.Frame(self,width=200,height=200)
        frame.pack();
        self.myCan = Tkinter.Canvas(frame,highlightthickness=0,width=200,height=200,bg="black")
        self.myCan.bind("<Button-1>",self.frame_say_hi)
        self.myCan.pack()

root = Tkinter.Tk()
myapp=App(master=root)
root.title("test")
myapp.mainloop()
