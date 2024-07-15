import speedtest
import math
from tkinter import*

def bytes_to_Mg(size_of_bytes):
    i = int(math.floor(math.log(size_of_bytes,1024)))
    power = math.pow(1024,i)
    size = round(size_of_bytes / power , 2)
    return f'{size} Mpbs'

def show_speed():
    wifi = speedtest.Speedtest()
    download_speed = wifi.download()
    upload_speed = wifi.upload()
    downlodeEn.insert(0,bytes_to_Mg(download_speed))
    uploadeEn.insert(0,bytes_to_Mg(upload_speed))

def delete_speed():
    downlodeEn.delete(0,END)
    uploadeEn.delete(0,END)

toolSpeed = Tk()
toolSpeed.title('Speed test')

toolSpeed.config(bg='#5834eb')

downlodeValue = StringVar
uploadeValue = StringVar

l1 = Label(toolSpeed,text='Speed test tool',font=('arial',20,'bold'), bg='#5834eb', activebackground='#b81c91')
l1.pack()

l1 = Label(toolSpeed , text='Download speed:' , bg='#5834eb',font=('arial',15,'bold'))
l1.pack()

downlodeEn = Entry(toolSpeed,textvariable=downlodeValue,relief='flat',highlightcolor='#271196',highlightthickness=2)
downlodeEn.pack()

l2 = Label(toolSpeed , text='Upload speed:', bg='#5834eb',font=('arial',15,'bold'))
l2.pack()


uploadeEn = Entry(toolSpeed,textvariable=uploadeValue,relief='flat',highlightcolor='#271196',highlightthickness=2)
uploadeEn.pack()




showputton = Button(text='Start Test',command=show_speed , activebackground='#b81c91')
showputton.pack()

delputton = Button(text='Clear Test',command=delete_speed , activebackground='#b81c91')
delputton.pack()


toolSpeed.mainloop()