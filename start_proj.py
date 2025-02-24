from tkinter import *  # ایمپورت کتابخانه tkinter برای ایجاد واسط کاربری گرافیکی
from PIL import Image, ImageTk  # ایمپورت ماژول‌های موردنیاز برای کار با تصاویر از کتابخانه PIL
import pygame  # ایمپورت کتابخانه pygame برای پخش موسیقی
import subprocess  # ایمپورت کتابخانه subprocess برای اجرای فایل‌های خارجی
import sys

def handle_exception(exc_type, exc_value, exc_traceback):
    # جلوگیری از نمایش ارور در کنسول
    pass

sys.excepthook = handle_exception

# ایجاد پنجره اصلی برنامه
staroot = Tk()  # ساخت یک پنجره جدید با استفاده از tkinter
staroot.title('Study App')  # تنظیم عنوان پنجره
staroot.config(bg='#94C973')  # تنظیم رنگ پس‌زمینه پنجره
staroot.resizable(False, False)  # غیر فعال کردن امکان تغییر اندازه پنجره
staroot.geometry('500x500+300+40')  # تنظیم اندازه و موقعیت اولیه پنجره

def tips():  # تعریف تابع برای نمایش تکنیک‌های مطالعه
    pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
    pygame.mixer.music.load("other\\bib3.mp3")  # بارگذاری فایل صوتی
    pygame.mixer.music.play()  # پخش موسیقی
    staroot.destroy()  # بستن پنجره اصلی
    subprocess.run(["python", "all_codes\\tips_study.py"])  # اجرای فایل خارجی tips_study.py

def cal():  # تعریف تابع برای باز کردن تقویم
    import pygame  # ایمپورت pygame برای اطمینان از دسترسی در این تابع
    pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
    pygame.mixer.music.load("other\\bib3.mp3")  # بارگذاری فایل صوتی
    pygame.mixer.music.play()  # پخش موسیقی
    staroot.destroy()  # بستن پنجره اصلی
    subprocess.run(["python", "all_codes\\calendar_proj.py"])  # اجرای فایل خارجی calendar_proj.py

def plan():  # تعریف تابع برای باز کردن پلنر
    import pygame  # ایمپورت pygame برای اطمینان از دسترسی در این تابع
    pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
    pygame.mixer.music.load("other\\bib3.mp3")  # بارگذاری فایل صوتی
    pygame.mixer.music.play()  # پخش موسیقی
    staroot.destroy()  # بستن پنجره اصلی
    subprocess.run(["python", "all_codes\\planner_proj.py"])  # اجرای فایل خارجی planner_proj.py

# بارگذاری و تنظیم تصویر پس‌زمینه
bg_image = Image.open("photos\\greeen.jpg")  # باز کردن تصویر پس‌زمینه
bg_image = bg_image.resize((500, 500))  # تغییر اندازه تصویر برای هماهنگی با پنجره
bg_image = ImageTk.PhotoImage(bg_image)  # تبدیل تصویر به فرمتی که tkinter پشتیبانی می‌کند

bg_label = Label(staroot, image=bg_image)  # ایجاد یک برچسب برای نمایش تصویر پس‌زمینه
bg_label.place(relwidth=1, relheight=1)  # گسترش برچسب به کل اندازه پنجره

import sys
import os

# اگر برنامه در حالت EXE است
if getattr(sys, 'frozen', False):
    # مسیر مناسب برای آیکون در هنگام اجرای EXE
    icon_path = os.path.join(sys._MEIPASS, '22.ico')
else:
    # مسیر آیکون در هنگام اجرای اسکریپت
    icon_path = '22.ico'

staroot.iconbitmap(icon_path)

def back():  # تعریف تابع برای بازگشت به صفحه اصلی
    import pygame  # ایمپورت pygame برای اطمینان از دسترسی در این تابع
    pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
    pygame.mixer.music.load("other\\bib2.mp3")  # بارگذاری فایل صوتی
    pygame.mixer.music.play()  # پخش موسیقی
    staroot.destroy()  # بستن پنجره اصلی
    subprocess.run(['python', 'main.py'])  # اجرای فایل خارجی main.py

# ایجاد دکمه‌ها با تنظیمات مختلف
back_bt = Button(staroot, activeforeground='pink', activebackground='red', fg='red', bg='pink', text='Back', font=('Segoe Print', 14, 'bold'), command=back).place(x=180, y=240)  # دکمه بازگشت
btn_tips = Button(staroot, activebackground='#528041', activeforeground='#D7F3AC', bg='#D7F3AC', fg='#528041', text='Study Techniques', font=('Segoe Print', 14, 'bold'), command=tips).place(x=0, y=0)  # دکمه تکنیک‌های مطالعه
btn_cal = Button(staroot, activebackground='#D7F3AC', activeforeground='#528041', bg='#528041', fg='#D7F3AC', text='Calendar', font=('Segoe Print', 14, 'bold'), command=cal).place(x=180, y=80)  # دکمه تقویم
btn_plan = Button(staroot, activebackground='#4F681A', activeforeground='#FAF795', bg='#FAF795', fg='#4F681A', text='Planner', font=('Segoe Print', 14, 'bold'), command=plan).place(x=0, y=160)  # دکمه پلنر

staroot.mainloop()  # اجرای حلقه اصلی برنامه برای نمایش پنجره
