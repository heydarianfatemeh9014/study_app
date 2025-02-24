import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
import os
import pygame  # برای پخش صدا
import sys

def handle_exception(exc_type, exc_value, exc_traceback):
    # جلوگیری از نمایش ارور در کنسول
    pass

sys.excepthook = handle_exception

# فایل ذخیره‌سازی
SAVE_FILE = "other\\planner_data.txt"

# مقداردهی اولیه pygame
pygame.mixer.init()

# تابع برای پخش صدای کلیک
def play_click_sound(button_sound=True):
    sound_file = "other\\bib3.mp3" if button_sound else "other\\bib2.mp3"
    if os.path.exists(sound_file):
        pygame.mixer.Sound(sound_file).play()  # پخش صدای کلیک در صورت وجود فایل

# تابع برای بارگذاری داده‌ها از فایل
def load_data():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]  # خواندن داده‌ها و بازگشت به صورت لیست
    return []  # اگر فایل وجود نداشته باشد، لیست خالی بازگرداند

# تابع برای ذخیره داده‌ها در فایل
def save_data():
    with open(SAVE_FILE, "w") as file:
        file.write("\n".join(tasks))  # ذخیره داده‌ها به صورت خط به خط در فایل

# اضافه کردن کار جدید
def add_task():
    play_click_sound()  # پخش صدای کلیک
    task = task_entry.get()  # دریافت متن از ورودی
    if task:
        tasks.append(task)  # افزودن کار به لیست
        task_list.insert(tk.END, task)  # نمایش کار در لیست
        task_entry.delete(0, tk.END)  # پاک کردن ورودی متن
        save_data()  # ذخیره داده‌ها

# حذف کار انتخابی
def delete_task():
    play_click_sound()  # پخش صدای کلیک
    selected = task_list.curselection()  # دریافت آیتم انتخاب شده از لیست
    if selected:
        task = task_list.get(selected)  # دریافت متن کار
        tasks.remove(task)  # حذف کار از لیست داده‌ها
        task_list.delete(selected)  # حذف کار از لیست گرافیکی
        save_data()  # ذخیره تغییرات

# تیک زدن یا انجام کار
def mark_done():
    play_click_sound()  # پخش صدای کلیک
    selected = task_list.curselection()  # دریافت آیتم انتخاب شده
    if selected:
        task = task_list.get(selected)  # دریافت متن کار
        tasks[selected[0]] = f"✔️ {task}" if not task.startswith("✔️") else task.replace("✔️ ", "")  # اضافه یا حذف تیک
        task_list.delete(selected)  # حذف آیتم قدیمی
        task_list.insert(selected, tasks[selected[0]])  # افزودن آیتم به‌روزشده
        save_data()  # ذخیره تغییرات

# برگشتن به صفحه اصلی
def backdef():
    root.destroy()  # بستن پنجره اصلی
    import subprocess
    subprocess.run(['python',"all_codes\\start_proj.py"])  # اجرای صفحه اصلی

# رابط گرافیکی اصلی
root = tk.Tk()
root.title("Cute Planner")  # عنوان برنامه
root.geometry("800x600")  # تنظیم اندازه پنجره

# بک‌گراند
bg_image = Image.open("photos\\999.jpg")  # بارگذاری تصویر پس‌زمینه
bg_image = bg_image.resize((800, 600))  # تغییر اندازه تصویر به اندازه پنجره
bg_photo = ImageTk.PhotoImage(bg_image)  # تبدیل تصویر برای استفاده در Tkinter

bg_label = tk.Label(root, image=bg_photo)  # افزودن تصویر به لیبل
bg_label.place(relwidth=1, relheight=1)  # قرار دادن لیبل به صورت تمام صفحه

# لیست کارها
tasks = load_data()  # بارگذاری داده‌ها

task_frame = tk.Frame(root, bg="#d0f0c0", bd=2)  # فریم برای نمایش لیست کارها
task_frame.place(relx=0.05, rely=0.1, relwidth=0.6, relheight=0.7)

task_list = tk.Listbox(task_frame, font=("Segoe Print", 14), bg="#f0fff0", fg="#004d00", selectbackground="dark green")  # ایجاد لیست کارها
task_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

for task in tasks:
    task_list.insert(tk.END, task)  # افزودن هر کار به لیست گرافیکی

# ورودی متن
task_entry = tk.Entry(root, font=("Segoe Print", 14, "bold"), bg="#ffffff", bd=2)  # فیلد ورودی برای افزودن کار
task_entry.place(relx=0.05, rely=0.82, relwidth=0.6, height=40)

# دکمه‌ها
button_frame = tk.Frame(root, bg="dark green", bd=2)  # فریم برای دکمه‌ها
button_frame.place(relx=0.7, rely=0.1, relwidth=0.25, relheight=0.7)

button_style = ttk.Style()
button_style.configure("TButton", font=("Segoe Print", 10, "bold"), padding=10)  # تنظیمات استایل دکمه‌ها

add_button = ttk.Button(button_frame, text="➕", command=add_task, style="TButton")  # دکمه افزودن
add_button.pack(pady=20)

delete_button = ttk.Button(button_frame, text="🗑️", command=delete_task, style="TButton")  # دکمه حذف
delete_button.pack(pady=20)

done_button = ttk.Button(button_frame, text="✔️", command=mark_done, style="TButton")  # دکمه تیک زدن
done_button.pack(pady=20)

back_btn = tk.Button(root,text='Back',bg='red',fg='white',activebackground='dark red',activeforeground='white',font=('Segoe Print',17,'bold'),command=backdef).pack()  # دکمه بازگشت

# افزودن رویداد کلیک برای سایر بخش‌ها
def on_any_click(event):
    play_click_sound(button_sound=False)  # پخش صدای کلیک برای هر کلیک

root.bind_all("<Button-1>", on_any_click)  # اتصال رویداد کلیک به تابع
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

# راه‌اندازی برنامه
root.mainloop()
