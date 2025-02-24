from tkinter import *
from tkinter import font
from calendar import monthrange, month_name
from datetime import date
from PIL import Image, ImageTk
from random import choice
import subprocess
import sys

def handle_exception(exc_type, exc_value, exc_traceback):
    # جلوگیری از نمایش ارور در کنسول
    pass

sys.excepthook = handle_exception


# تنظیمات اصلی برنامه و رابط کاربری
calr = Tk()
calr.title('Calendar Window')  # عنوان پنجره برنامه
calr.config(bg='#FCE4EC')  # تنظیم رنگ پس‌زمینه
calr.resizable(False, False)  # غیر قابل تغییر کردن اندازه پنجره
calr.geometry('500x500+300+40')  # تنظیم ابعاد و مکان نمایش پنجره
import sys
import os

# اگر برنامه در حالت EXE است
if getattr(sys, 'frozen', False):
    # مسیر مناسب برای آیکون در هنگام اجرای EXE
    icon_path = os.path.join(sys._MEIPASS, '22.ico')
else:
    # مسیر آیکون در هنگام اجرای اسکریپت
    icon_path = '22.ico'

calr.iconbitmap(icon_path)

# دریافت تاریخ فعلی
current_date = date.today()  # دریافت تاریخ امروز
current_month = current_date.month  # ماه فعلی
current_year = current_date.year  # سال فعلی

# تنظیمات فونت و رنگ‌ها
font_title = ('CommercialScript Bt', 28, 'bold')  # فونت عنوان
font_days = ('CommercialScript Bt', 15, 'bold')  # فونت روزها

# تعریف رنگ‌ها و پس‌زمینه‌های ممکن
color_palettes = [
    ['#66BB6A', '#FFB74D', '#FFEB3B', '#FFD54F'],  # سبز و زرد 
    ['#9C27B0', '#F06292', '#FF7043', '#DCE775'],
    ['#2196F3', '#4CAF50', '#FFC107', '#FF5722'],
    ['#E91E63', '#FF9800', '#8BC34A', '#00BCD4']
]

backgrounds = ['photos\\cute_yellow.png', 'photos\\cute_blue.png', 'photos\\cute_green.png', 'photos\\cute_brown.png']  # لیست تصاویر پس‌زمینه

# انتخاب تصادفی رنگ‌ها و پس‌زمینه
current_palette = choice(color_palettes)  # انتخاب تصادفی پالت رنگی
current_background = choice(backgrounds)  # انتخاب تصادفی تصویر پس‌زمینه

# بارگذاری تصویر پس‌زمینه
bg_image = Image.open(current_background)  # باز کردن تصویر پس‌زمینه
bg_image = bg_image.resize((500, 500))  # تغییر اندازه تصویر به اندازه پنجره
bg_image = ImageTk.PhotoImage(bg_image)  # تبدیل تصویر به فرمت مناسب برای Tkinter
bg_label = Label(calr, image=bg_image)  # تنظیم تصویر پس‌زمینه روی لیبل
bg_label.place(relwidth=1, relheight=1)  # تنظیم اندازه تصویر به اندازه کل پنجره

# تابع تغییر تم تقویم
def change_theme():
    global current_palette, bg_image, current_background
    current_palette = choice(color_palettes)  # تغییر پالت رنگی
    current_background = choice(backgrounds)  # تغییر پس‌زمینه
    bg_image = Image.open(current_background)
    bg_image = bg_image.resize((500, 500))
    bg_image = ImageTk.PhotoImage(bg_image)
    bg_label.config(image=bg_image)  # اعمال تصویر جدید به پس‌زمینه

# تابع به‌روزرسانی تقویم
def update_calendar(month, year):
    change_theme()  # تغییر تم تقویم
    for widget in frame_days.winfo_children():
        widget.destroy()  # پاک کردن محتوای قدیمی از فریم روزها

    title_label.config(text=f"{month_name[month]} {year}", fg=current_palette[0])  # تنظیم عنوان تقویم

    days_in_month = monthrange(year, month)[1]  # تعداد روزهای ماه فعلی
    first_day_of_month = monthrange(year, month)[0]  # روز اول ماه

    for i, day in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']):
        Label(frame_days, text=day, font=font_days, fg=current_palette[1]).grid(row=0, column=i, pady=5)  # نمایش نام روزهای هفته

    row = 1
    col = first_day_of_month

    for day in range(1, days_in_month + 1):
        color = current_palette[2] if col in [5, 6] else current_palette[0]  # تنظیم رنگ روزهای تعطیل و عادی
        if day == current_date.day and month == current_month and year == current_year:
            lbl = Label(frame_days, text=day, font=font_days, fg='white', bg=current_palette[3], width=4, height=2)  # نمایش روز فعلی با رنگ متفاوت
        else:
            lbl = Label(frame_days, text=day, font=font_days, fg=color, width=4, height=2)  # نمایش بقیه روزها

        lbl.grid(row=row, column=col, padx=2, pady=2)  # تنظیم مکان هر روز در جدول

        col += 1
        if col > 6:
            col = 0
            row += 1

# توابع تغییر ماه

def previous_month():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib2.mp3")
    pygame.mixer.music.play()
    global current_month, current_year
    current_month -= 1
    if current_month == 0:
        current_month = 12
        current_year -= 1
    update_calendar(current_month, current_year)  # به‌روزرسانی تقویم برای ماه قبلی

def next_month():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib2.mp3")
    pygame.mixer.music.play()
    global current_month, current_year
    current_month += 1
    if current_month == 13:
        current_month = 1
        current_year += 1
    update_calendar(current_month, current_year)  # به‌روزرسانی تقویم برای ماه بعدی

# ساخت عناصر تقویم

title_label = Label(calr, text="", font=font_title)  # عنوان تقویم
title_label.pack(pady=10)

frame_days = Frame(calr)  # فریم برای نمایش روزهای ماه
frame_days.pack(pady=10)

btn_prev = Button(calr, text="\u25C0", command=previous_month, bg=current_palette[1], fg='white', font=font_days, width=5)  # دکمه ماه قبلی
btn_prev.place(x=50, y=450)

btn_next = Button(calr, text="\u25B6", command=next_month, bg=current_palette[1], fg='white', font=font_days, width=5)  # دکمه ماه بعدی
btn_next.place(x=400, y=450)

# دکمه بازگشت به صفحه قبلی

def back():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib2.mp3")
    pygame.mixer.music.play()
    calr.destroy()
    subprocess.run(['python', "all_codes\\start_proj.py"])

back_bt = Button(calr, activeforeground='pink', activebackground='red', fg='red', bg='pink', text='Back', font=('Segoe Print', 14, 'bold'), command=back).place(x=0, y=0)

# نمایش تقویم برای ماه فعلی
update_calendar(current_month, current_year)

calr.mainloop()
