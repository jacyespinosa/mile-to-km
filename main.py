from tkinter import *

window = Tk()
window.title("Jacy's Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=100, pady=100)

#Function that converts mile to km
def mile_km_converter():
  new_number['text'] = round(int(input.get()) * 1.609344, 0)

#Create is_equal_to label
is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=1, row=2)

#Number input
input = Entry(width=10)
print(input.get())
input.grid(column=2, row=1)

#Miles label
miles_label = Label(text='Miles')
miles_label.grid(column=3, row=1)

#New number label
new_number = Label(text='0')
new_number.grid(column=2, row=2)

#Km label
km_label = Label(text='Km')
km_label.grid(column=3, row=2)

#Calculate Button
calculate = Button(text='Calculate', command=mile_km_converter)
calculate.grid(column=2, row=3)


window.mainloop()