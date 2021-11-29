import PyPDF2
import pyttsx3
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
# path of the PDF file
# path = open('file.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(file_path)

# the page with which you want to start
# this will read the page of 25th page.
from_page = pdfReader.getPage(25)

# extracting the text from the PDF
text = from_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()