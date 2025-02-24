import tkinter as tk
from tkinter import PhotoImage
from  bidi.algorithm import get_display
import arabic_reshaper
import tkinter
from tkinter import *
from random import*
#persian typing setting
def convert(text):
    rt = arabic_reshaper.reshape(text)
    converted = get_display(rt)
    return converted
#file setting
