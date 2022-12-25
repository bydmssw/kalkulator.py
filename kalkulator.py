# import library tkinter
from tkinter import *

# layout jendela program
window = Tk()
window.title("Kalkulator GUI Dengan Python")
window.geometry('350x200')

# kolom data nilai pertama
lbl = Label(window, text="Masukan Nilai Pertama : ",anchor="e",width=28)
lbl.grid(column=0, row=0)
nilai1 = Entry(window,width=10)
nilai1.grid(column=1,row=0)
 
# kolom data nilai kedua
lbl2 = Label(window, text="Masukan Nilai Kedua : ",anchor="e",width=28)
lbl2.grid(column=0, row=1)
nilai2 = Entry(window,width=10)
nilai2.grid(column=1,row=1)

# kolom hasil kalkulasi data nilai pertama dan kedua
lbl3 = Label(window, text="Hasil : ",anchor="e",width=20)
lbl3.grid(column=0, row=2)
hasil = Label(window, text="0",anchor="w",width=10)
hasil.grid(column=1, row=2)

""" Berikut dibawah ini adalah fungsi operator aritmatika
Pertambahan, pengurangan, perkalian, dan pembagian """

def tambah():
    hasil.configure(text=(int(nilai1.get())+int(nilai2.get())))
 
def kurang():
    hasil.configure(text=(int(nilai1.get())-int(nilai2.get())))
 
def kali():
    hasil.configure(text=(int(nilai1.get())*int(nilai2.get())))
 
def bagi():
    hasil.configure(text=(int(nilai1.get())/int(nilai2.get())))

# tombol operasi pertambahan
btn = Button(window, text="Tambah", command=tambah)
btn.grid(column=0, row=3)

# tombol operasi pengurangan
btn = Button(window, text="Kurang", command=kurang)
btn.grid(column=1, row=3)

# tombol operasi perkalian
btn = Button(window, text="Kali", command=kali)
btn.grid(column=0, row=4)

# tombol operasi pembagian
btn = Button(window, text="Bagi", command=bagi)
btn.grid(column=1, row=4)
 
window.mainloop()