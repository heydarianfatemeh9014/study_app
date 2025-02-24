from tkinter import *
from PIL import Image, ImageTk
import subprocess
import sys

def handle_exception(exc_type, exc_value, exc_traceback):
    # جلوگیری از نمایش ارور در کنسول
    pass

sys.excepthook = handle_exception

# لیست تصاویر پس‌زمینه
photo_list = [
    'photos\\hi_about.png',
    'photos\\greewin.png',
    'photos\\greewin (1).png',
    'photos\\greewin (2).png',
    'photos\\greewin (3).png',
    'photos\\greewin (4).png',
    'photos\\greewin (5).png',
    'photos\\greewin (6).png'
]

# تنظیمات اصلی
root = Tk()
root.title('About This Application')
root.config(bg='#FCE4EC')
root.resizable(False, False)
root.geometry('800x500')
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

# تصویر پس‌زمینه
bg_label = Label(root)
bg_label.place(relwidth=1, relheight=1)

# متغیر برای تغییر پس‌زمینه
backgr = 0  # مقدار اولیه

# تابع برای تغییر تصویر
def update_background():
    global backgr
    # بررسی محدوده مقدار `backgr`
    if backgr < 0:
        backgr = 0
    elif backgr >= len(photo_list):
        backgr = len(photo_list) - 1
    
    # بارگذاری تصویر جدید
    img = Image.open(photo_list[backgr])
    img = img.resize((800, 500))
    bg_image = ImageTk.PhotoImage(img)
    bg_label.config(image=bg_image)
    bg_label.image = bg_image

    # مدیریت دکمه‌ها
    if backgr == 0:
        pr_btn.place_forget()  # مخفی کردن دکمه قبلی
    else:
        pr_btn.place(x=15, y=230, height=30, width=40)

    if backgr == len(photo_list) - 1:
        next_btn.place_forget()  # مخفی کردن دکمه بعدی
    else:
        next_btn.place(x=750, y=230, height=30, width=40)

# توابع تغییر مقدار `backgr`
def next_def():
    global backgr
    backgr += 1
    update_background()

def pr_def():
    global backgr
    backgr -= 1
    update_background()

# دکمه‌ها
next_btn = Button(root, text=">>", font=('Segoe Print', 20, 'bold'), bg='pink', fg='red', command=next_def)
pr_btn = Button(root, text="<<", font=('Segoe Print', 20, 'bold'), bg='pink', fg='red', command=pr_def)

# دکمه بازگشت به صفحه قبلی

def back():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib2.mp3")
    pygame.mixer.music.play()
    root.destroy()
    subprocess.run(["python", "main.py"])

back_bt = Button(root, activeforeground='pink', activebackground='red', fg='red', bg='pink', text='Back', font=('Segoe Print', 14, 'bold'), command=back).place(x=0, y=0)

# مقداردهی اولیه تصویر
update_background()

# شروع برنامه
root.mainloop()
