__author__ = 'Babayev Ilyas'
#from sys import exit
#from Tkinter import *
#
#root = Tk()
#Button(root, text='Hello World!', command=exit).pack()
#Label(root, text='yo man').pack()
#last = Listbox(root, {'1':'hello', '2':'world', '3':'executable', '4':'list text and so on'}).pack()
#root.mainloop()

from Tkinter import *

class AllTkinterWidgets:
    def __init__(self, master):
        frame = Frame(master, width=500, height=400, bd=1)
        frame.pack()


        iframe3 = Frame(frame, bd=2, relief=GROOVE)
        listbox = Listbox(iframe3, height=4)
        for line in ['Listbox Entry One','Entry Two','Entry Three','Entry Four']:
            listbox.insert(END, line)
        listbox.pack(fill=X, padx=5)
        iframe3.pack(expand=1, fill=X, pady=10, padx=5)

        iframe4 = Frame(frame, bd=2, relief=SUNKEN)
        text=Text(iframe4, height=10, width =65)
#        fd = open('test.py')
        lines = "hello\nworld"
#        fd.close()
        text.insert(END, lines)
        text.pack(side=LEFT, fill=X, padx=5)
        sb = Scrollbar(iframe4, orient=VERTICAL, command=text.yview)
        sb.pack(side=RIGHT, fill=Y)
        text.configure(yscrollcommand=sb.set)

class My :
    def __init__(self, master):
        frame1 = Frame(master)
        Button(frame1, text="hello", fill=X, padx=2).pack()
        Button(frame1, text="hello1").pack()
        frame1.pack()


root = Tk()
all = AllTkinterWidgets(root)
#all = My(root)
root.title('Tkinter Widgets')
root.mainloop()
