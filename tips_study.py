from tkinter import *
from PIL import Image, ImageTk
import subprocess
import sys

def handle_exception(exc_type, exc_value, exc_traceback):
    # جلوگیری از نمایش ارور در کنسول
    pass

sys.excepthook = handle_exception

def pomstart():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib3.mp3")
    pygame.mixer.music.play()
    tstaroot.destroy()
    import subprocess
    subprocess.run(["python", "all_codes\\pomo.py"])
# Function for showing tips
def show_tip(event, text):
    global u
    import pygame
    pygame.mixer.init()
    
    if u is None:  # If the label is not created yet
        u = Label(tstaroot, background='#d4c78c', fg='white',
                  text=text, font=('Lucida Console', 15, 'bold'))
        u.place(x=283, y=60)

# Function for hiding the tip
def hide_tip(event):
    global u
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib2.mp3")
    pygame.mixer.music.play()
    if u is not None:
        u.place_forget()  # Hide the label
        u = None  # Reset label to None

# Function to close the current window and open tips_study
def tips():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib3.mp3")
    pygame.mixer.music.play()
    tstaroot.destroy()
    subprocess.run(["python", "all_codes\\tips_study.py"])

# Placeholder function for Pomodoro button


# Placeholder function for Feynman button
def feinbtn():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib3.mp3")
    pygame.mixer.music.play()
    fenroot = Toplevel(tstaroot)
    fenroot.title('Feinman Technique')
    fenroot.config(bg='#94C973')
    fenroot.resizable(False, False)
    fenroot.geometry('800x500+300+40')

    feini = Image.open("photos\\brown.jpg")
    feini = ImageTk.PhotoImage(feini)
    feini_label = Label(fenroot, image=feini)
    feini_label.image = feini  # نگه داشتن تصویر پس‌زمینه
    feini_label.place(relwidth=1, relheight=1)

    
    canvas = Canvas(fenroot, width=500, height=300)
    canvas.create_image(0, 0, anchor=NW, image=feini)  # اضافه کردن تصویر پس‌زمینه
    canvas.place(relwidth=1, relheight=1)  # پر کردن پنجره با canvas

    # اضافه کردن متن به canvas
    canvas.create_text(230, 190, 
                    text=("The Feynman Technique is a learning strategy that involves four key steps: choose a concept to learn, teach it to someone else or explain it in simple terms, identify knowledge gaps, and simplify your explanations.​ This method promotes deep understanding by forcing learners to engage actively with the material, clarify their thoughts, and confront what they don't know."), 
                    font=('Dubai', 15, 'bold'), fill='white', width=450)

    fenroot.mainloop()

# Placeholder function for SQ3R button
from tkinter import *

from PIL import Image, ImageTk

def sqrbtn():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib3.mp3")
    pygame.mixer.music.play()

    sroot = Toplevel()

    sroot.title('SQR3 Technique')

    sroot.config(bg='#94C973')

    sroot.resizable(False, False)

    sroot.geometry('800x500+300+40')

    sri = Image.open("photos\\gr2.jpg")
    sri = sri.resize((800, 500))


    sri = ImageTk.PhotoImage(sri)

    sri_label = Label(sroot, image=sri)

    sri_label.image = sri

    sri_label.place(relwidth=1, relheight=1)

    canvas3 = Canvas(sroot, width=500, height=300)

    canvas3.create_image(0, 0, anchor=NW, image=sri)

    canvas3.place(relwidth=1, relheight=1)

    canvas3.create_text(260, 230,text=("​SQ3R is a reading comprehension method designed to improve understanding and retention of written information.​ It consists of five steps: Survey: Preview the material to get an overview. Question: Formulate questions based on headings to engage with the content. Read: Read actively to find answers to the generated questions. Recite: Summarize and paraphrase the information in your own words. Review: Go over the material to reinforce learning and enhance memory retention. ​This systematic approach helps learners to focus and structure their reading effectively."),font=('Dubai', 15, 'bold'), fill='dark green', width=450)

    sroot.mainloop()

# Placeholder function for Active Recall button

def arbtn():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib3.mp3")
    pygame.mixer.music.play()

    aroot = Toplevel()

    aroot.title('Active Recall Technique')

    aroot.config(bg='#94C973')

    aroot.resizable(False, False)

    aroot.geometry('800x500+300+40')

    ai = Image.open("photos\\gr3.jpg")
    ai = ai.resize((800, 500))


    ai = ImageTk.PhotoImage(ai)

    ai_label = Label(aroot, image=ai)

    ai_label.image = ai

    ai_label.place(relwidth=1, relheight=1)

    canvas4 = Canvas(aroot, width=500, height=300)

    canvas4.create_image(0, 0, anchor=NW, image=ai)

    canvas4.place(relwidth=1, relheight=1)

    canvas4.create_text(230, 270,text=("Active Recall is a learning technique that enhances memory by actively retrieving information instead of just reviewing it. Key Points:Self-Testing: Use flashcards and practice questions.Memory Strengthening: Actively recalling information boosts retention.Identifying Gaps: Helps identify areas needing focus.​Employing Active Recall can significantly improve learning and academic performance."),font=('Dubai', 16, 'bold'), fill='dark green', width=450)

    aroot.mainloop()

# Placeholder function for Spaced Repetition button
def srbtn():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib3.mp3")
    pygame.mixer.music.play()
    
    
    aroot = Toplevel()

    aroot.title('Spaced Repetition')

    aroot.config(bg='#94C973')

    aroot.resizable(False, False)

    aroot.geometry('800x500+300+40')

    ai = Image.open("photos\\grgr.jpg")

    ai = ImageTk.PhotoImage(ai)

    ai_label = Label(aroot, image=ai)

    ai_label.image = ai

    ai_label.place(relwidth=1, relheight=1)

    canvas4 = Canvas(aroot, width=500, height=300)

    canvas4.create_image(0, 0, anchor=NW, image=ai)

    canvas4.place(relwidth=1, relheight=1)

    canvas4.create_text(270, 290,text=("Spaced repetition is a scientifically proven method that involves\nreviewing information at closer intervals, boosting your memory,\nand making it less likely you'll forget everything. Studies\nshow it can significantly improve learning and reduce the time\nspent studying."),font=('Dubai', 18, 'bold'), fill='dark green', width=450)

    aroot.mainloop()

# Placeholder function for Mind Mapping button
def mmbtn():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib3.mp3")
    pygame.mixer.music.play()
    
    aroot = Toplevel()

    aroot.title('Mind Mapping')

    aroot.config(bg='#94C973')

    aroot.resizable(False, False)

    aroot.geometry('800x500+300+40')

    ai = Image.open("photos\\book.jpg")

    ai = ImageTk.PhotoImage(ai)

    ai_label = Label(aroot, image=ai)

    ai_label.image = ai

    ai_label.place(relwidth=1, relheight=1)

    canvas4 = Canvas(aroot, width=500, height=300)

    canvas4.create_image(0, 0, anchor=NW, image=ai)

    canvas4.place(relwidth=1, relheight=1)

    canvas4.create_text(230, 290,text=("A mind map involves writing down a central theme and thinking\nof new and related ideas which radiate out from the centre. By focusing\n on key ideas written down in your \nown words and looking for \nconnections between them, you can map knowledge in\n a way that will help you to better\n understand and retain information."),font=('Dubai', 18, 'bold'), fill='dark red', width=450)

    aroot.mainloop()

# Placeholder function for Leitner button
def lsbtn():
    
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib3.mp3")
    pygame.mixer.music.play()
    aroot = Toplevel()

    aroot.title('Leitner')

    aroot.config(bg='#94C973')

    aroot.resizable(False, False)

    aroot.geometry('800x500+300+40')

    ai = Image.open("photos\\girl.jpg")

    ai = ImageTk.PhotoImage(ai)

    ai_label = Label(aroot, image=ai)

    ai_label.image = ai

    ai_label.place(relwidth=1, relheight=1)

    canvas4 = Canvas(aroot, width=500, height=300)

    canvas4.create_image(0, 0, anchor=NW, image=ai)

    canvas4.place(relwidth=1, relheight=1)

    canvas4.create_text(230, 290,text=("The Leitner System is a spaced repetition technique for learning with flashcards. Cards are sorted into boxes based on how well the material is known. Correctly answered cards progress to boxes that you don't need to review as often, while incorrect ones are moved back to the first box for more frequent review."),font=('Dubai', 18, 'bold'), fill='dark green', width=450)

    aroot.mainloop()

# Setting up the main window
tstaroot = Tk()
tstaroot.title('Study App')
tstaroot.config(bg='#94C973')
tstaroot.resizable(False, False)
tstaroot.geometry('500x500+300+40')

# Setting background image
bg_image = Image.open("photos\\tecab.jpg")
bg_image = bg_image.resize((500, 600))
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = Label(tstaroot, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Initialize global variable for tooltip label
u = None

# Tooltips for different techniques
tips_dict = {
    'Pomodoro': 'Work 25\nmins then\nbreak 5 mins\nafter 4x\ntake a\nlonger break',
    'Feynman': 'Explain it\nsimply Teach\nsomeone else\nIdentify gaps',
    'SQ3R': 'Survey the\nmaterial\nQuestion\nthe content\nRead and\nRecite\nReview',
    'Active Recall': 'Test yourself\non the material\nRetrieve\ninformation',
    'Spaced Repetition': 'Review over\nincreasing\nintervals.\nUse\nflashcards',
    'Mind Mapping': 'Create visual\nmaps to\norganize ideas\nand concepts',
    'Leitner': 'Use flashcards\nReview\ndifficult\ncards more\noften'
}


def pomocom():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib3.mp3")
    pygame.mixer.music.play()
    pomoroot = Toplevel(tstaroot)
    pomoroot.title('Pomodoro Technique')
    pomoroot.config(bg='#94C973')
    pomoroot.resizable(False, False)
    pomoroot.geometry('800x500+300+40')

    pomi = Image.open("photos\\gr1.jpg")
    pomi = pomi.resize((800, 500))

    pomi = ImageTk.PhotoImage(pomi)
    pomi_label = Label(pomoroot, image=pomi)
    pomi_label.image = pomi  # نگه داشتن تصویر پس‌زمینه
    pomi_label.place(relwidth=1, relheight=1)

    
    canvas = Canvas(pomoroot, width=500, height=300)
    canvas.create_image(0, 0, anchor=NW, image=pomi)  # اضافه کردن تصویر پس‌زمینه
    canvas.place(relwidth=1, relheight=1)  # پر کردن پنجره با canvas

    # اضافه کردن متن به canvas
    canvas.create_text(330, 220, 
                    text=("The Pomodoro Technique is a time\n management method where\n work is divided into 25-minute\n intervals (Pomodoros) followed by \n5-minute breaks.\n After four Pomodoros, a longer break of \n15-30 minutes is taken. ​This approach\n enhances focus and productivity by\n structuring work sessions and encouraging regular rest."), 
                    font=('Dubai', 17, 'bold'), fill='dark green', width=450)
    
    sr = Button(pomoroot, command=pomstart, activebackground='green', background='#C4F29E', fg='green',
            activeforeground='#C4F29E', text='Do you want to try this technique?', font=('Lucida Console', 15, 'bold'),
            relief='flat', bd=0).pack()

    pomoroot.mainloop()

    

# Pomodoro button
pomo = Button(tstaroot, command=pomocom, activebackground='#d4c78c', background='#d4c78c', fg='#213B13',
              activeforeground='#213B13', text='Pomodoro\nTechnique', font=('Lucida Console', 15, 'bold'),
              relief='flat', bd=0,
              )
pomo.place(x=80, y=17)
pomo.bind("<Enter>", lambda event: show_tip(event, tips_dict['Pomodoro']))
pomo.bind("<Leave>", hide_tip)

# Feynman button
fein = Button(tstaroot, command=feinbtn, activebackground='#d4c78c', background='#d4c78c', fg='#213B13',
              activeforeground='#213B13', text='Feynman\nTechnique', font=('Lucida Console', 15, 'bold'),
              relief='flat', bd=0)
fein.place(x=80, y=85)
fein.bind("<Enter>", lambda event: show_tip(event, tips_dict['Feynman']))
fein.bind("<Leave>", hide_tip)

# SQ3R button
sqr = Button(tstaroot, command=sqrbtn, activebackground='#d4c78c', background='#d4c78c', fg='#213B13',
             activeforeground='#213B13', text='SQ3R\nMethod', font=('Lucida Console', 15, 'bold'),
             relief='flat', bd=0)
sqr.place(x=90, y=153)
sqr.bind("<Enter>", lambda event: show_tip(event, tips_dict['SQ3R']))
sqr.bind("<Leave>", hide_tip)

# Active Recall button
ar = Button(tstaroot, command=arbtn, activebackground='#d4c78c', background='#d4c78c', fg='#213B13',
            activeforeground='#213B13', text='Active\nRecall', font=('Lucida Console', 15, 'bold'),
            relief='flat', bd=0)
ar.place(x=90, y=221)
ar.bind("<Enter>", lambda event: show_tip(event, tips_dict['Active Recall']))
ar.bind("<Leave>", hide_tip)

# Spaced Repetition button
sr = Button(tstaroot, command=srbtn, activebackground='#d4c78c', background='#d4c78c', fg='#213B13',
            activeforeground='#213B13', text='Spaced\nRepetition', font=('Lucida Console', 15, 'bold'),
            relief='flat', bd=0)
sr.place(x=90, y=289)
sr.bind("<Enter>", lambda event: show_tip(event, tips_dict['Spaced Repetition']))
sr.bind("<Leave>", hide_tip)

# Mind Mapping button
mm = Button(tstaroot, command=mmbtn, activebackground='#d4c78c', background='#d4c78c', fg='#213B13',
            activeforeground='#213B13', text='Mind\nMapping', font=('Lucida Console', 15, 'bold'),
            relief='flat', bd=0)
mm.place(x=90, y=357)
mm.bind("<Enter>", lambda event: show_tip(event, tips_dict['Mind Mapping']))
mm.bind("<Leave>", hide_tip)

# Leitner button
ls = Button(tstaroot, command=lsbtn, activebackground='#d4c78c', background='#d4c78c', fg='#213B13',
            activeforeground='#213B13', text='The Leitner\nSystem', font=('Lucida Console', 15, 'bold'),
            relief='flat', bd=0)
ls.place(x=80, y=425)
ls.bind("<Enter>", lambda event: show_tip(event, tips_dict['Leitner']))
ls.bind("<Leave>", hide_tip)
import sys
import os

# اگر برنامه در حالت EXE است
if getattr(sys, 'frozen', False):
    # مسیر مناسب برای آیکون در هنگام اجرای EXE
    icon_path = os.path.join(sys._MEIPASS, '22.ico')
else:
    # مسیر آیکون در هنگام اجرای اسکریپت
    icon_path = '22.ico'

tstaroot.iconbitmap(icon_path)


def back():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("other\\bib2.mp3")
    pygame.mixer.music.play()
    tstaroot.destroy()
    subprocess.run(["python", "all_codes\\start_proj.py"])
back_bt = Button(tstaroot, activeforeground='pink', activebackground='red', fg='red', bg='pink', text='Back', font=('Segoe Print', 14, 'bold'), command=back).place(x=290, y=300)
# Start main loop to show the window
tstaroot.mainloop()
