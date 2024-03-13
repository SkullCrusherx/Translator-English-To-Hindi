from googletrans import Translator
from tkinter import *

import tkinter.messagebox as messagebox
root = Tk()
root.geometry('500x500')
root.title('English To Hindi Tranlator')

def btn():
    translator = Translator()
    input_text = text.get("1.0", "end-1c")  # Retrieve the text from the text area
    out = translator.translate(input_text, dest='hi')
    # Display the translated text
    sublime = str(out.text)
    filed2.delete("1.0", "end")  # Clear the existing text in the Text widget
    filed2.insert("1.0", sublime)


def copy_text():
    label_text = filed2.get("1.0", END).strip()
    if label_text:
        # Copy the text to the clipboard
        root.clipboard_clear()
        root.clipboard_append(label_text)
        pop = Label(root,text="Copy Successful")
        pop.pack()
    else:
        messagebox.showwarning("No Text", "Please enter some text to copy.")

text = Text(root, height=10, width=50, background='#ebdcb5')
text.pack(pady=10, padx=20)

button = Button(root, text='Translate', command=btn)
button.pack(pady=20, anchor="center")

filed2 = Text(root, width=50,height=10, background='#97c9f0')
filed2.pack()

button2 = Button(root, text='Copy', command=copy_text)
button2.pack(pady=20, anchor="center")

root.mainloop()

