# ایمپورت کردن تمام کتابخانه های مورد نیاز برنامه
from tkinter import *
from PIL import Image, ImageTk
import subprocess
import sys

def handle_exception(exc_type, exc_value, exc_traceback):
    # جلوگیری از نمایش ارور در کنسول
    pass

sys.excepthook = handle_exception

#توابع برای دکمه ها 
def start():#برای دکمه شروع
    import pygame#موزیک کلیک روی دکمه
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib4.mp3")
    pygame.mixer.music.play()
    root.destroy()#خراب کردن پنجره و بستن آن
    subprocess.run(["python", "all_codes\\start_proj.py"])

 #باز کردن برنامه بعدی

def about():#تابع درباره برنامه
    import pygame#موزیک کلیک روی دکمه
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib4.mp3")
    pygame.mixer.music.play()
    root.destroy()#خراب کردن پنجره و بستن آن
    subprocess.run(["python", "all_codes\\about.py"])  #باز کردن برنامه بعدی 
# ساختن پنجره و تنظیمات مربوط به آن
root = Tk()  
root.title('Study App')  #نام پنجره

root.config(bg='#94C973')  #تنظیمات رنگ پنجره
root.iconbitmap('photos\\22.ico')

import sys
import os

# اگر برنامه در حالت EXE است
if getattr(sys, 'frozen', False):
    # مسیر مناسب برای آیکون در هنگام اجرای EXE
    icon_path = os.path.join(sys._MEIPASS, '22.ico')
else:
    # مسیر آیکون در هنگام اجرای اسکریپت
    icon_path = '22.ico'

root.iconbitmap(icon_path)


root.resizable(False, False) #اندازه گذاری اش توسط کاربر تغییر نکند 

root.geometry('800x400+300+40')  #اندازه پنجره

# لیبل برای تصویر پس زمینه
bg_image = Image.open("photos\\grbg2.png")#باز کردن عکس از پوشه فوتوز

bg_image = bg_image.resize((800, 400)) #اندازه عکس به اندازه خود پنجره 

bg_image = ImageTk.PhotoImage(bg_image)  #قرار دادن عکس

bg_label = Label(root, image=bg_image)#تنظیمات لیبل عکس

bg_label.place(relwidth=1, relheight=1) #مکان لیبل

# دکمه های برنامه
btn_start = Button(root, activebackground='#7E8C69', activeforeground='#D3D9A7', bg='#F4E891', fg='#F5AE59', text='Start Now !', font=('Segoe Print', 14, 'bold'), command=start).place(x=580, y=100)#دکمه برای شروع

btn_about = Button(root, activebackground='#69648A', activeforeground='#C3B8FF', bg='#C3B8FF', fg='#69648A', text='How to Use?', font=('Segoe Print', 14, 'bold'), command=about).place(x=580, y=160)#دکمه برای دیدن کارکرد و درباره برنامه

root.mainloop() #حلقه پنجره
