import Tkinter,Image,ImageDraw,ImageTk
def say_hi():
    print "hi!!!"
def frame_say_hi(event):
    print "hi  " + str(event.x) + "," + str(event.y)

root = Tkinter.Tk()
frame = Tkinter.Frame(root,width=200,height=200)
frame.pack()

can = Tkinter.Canvas(frame,highlightthickness=0,width=200,height=200,bg="black")
can.bind("<Button-1>",frame_say_hi)
can.pack()

im = Image.new("RGB",(200,200),0xffff00)
draw = ImageDraw.Draw(im)
draw.line([0,0,40,30],fill=127)
#draw.rectangle([0, 0, 40, 40 ],  fill="green")
#del draw
draw.ellipse((10,10,50,50),fill=127)
pm = ImageTk.PhotoImage(im)
tk_img = can.create_image(100,100,image=pm)

root.mainloop()
