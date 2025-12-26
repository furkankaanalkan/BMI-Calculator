import tkinter
from time import process_time

my_window = tkinter.Tk()
my_window.title("BMI Calculator")
my_window.minsize(width=300, height=300)
my_window.config(pady=20)

label_1 = tkinter.Label(my_window, text=" enter your weight (kg) : ", font=('bold', 10))
label_1.pack()
label_1.config(pady=20)

entry1 = tkinter.Entry(width=22)
entry1.pack()



label_2 = tkinter.Label(my_window, text=" enter your height (cm) : ", font=('bold', 10))
label_2.config(pady=20)
label_2.pack()

entry2 = tkinter.Entry(width=22)
entry2.pack()

label_3 = tkinter.Label(font=('bold', 10))
label_3.pack()


def calculate():
    try:
        global label_3

        weight = float(entry1.get())
        height = float(entry2.get())
        a = weight / ((height/100) * (height/100))
        label_3.config(text='--> ', pady=20)

        if  a < 18.5:
            label_3.config(text=f" {a:.2f} you are underweight")
        elif 18.5 < a < 24.9:
            label_3.config(text=f" {a:.2f} you are normal")
        elif 25 < a < 29.9:
            label_3.config(text=f" {a:.2f} you are overweight")
        elif 30 < a < 34.9:
            label_3.config(text=f" {a:.2f} you are obese")
        else:
            label_3.config(text=f" {a:.2f} you are extremly obese")

    except :
        label_3.config(text='enter a valid number')



my_button = tkinter.Button(text="Calculate", command=calculate )
my_button.pack()
label_3.config(text='enter a valid number')



'''if not label_2 == int(entry1.get()):
    print ('you should enter a intiger')'''




my_window.mainloop()

