import Tkinter

s = Tkinter.Scrollbar()
L = Tkinter.Listbox()

s.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
L.pack(side=Tkinter.LEFT, fill=Tkinter.Y)

s.config(command=L.yview)
L.config(yscrollcommand=s.set)

for i in range(30):
    L.insert(Tkinter.END, str(i)*3)

Tkinter.mainloop()