import tkinter



my_window = tkinter.Tk()
my_window.title("BMI Calculator")
my_window.minsize(width=300, height=300)
my_window.config(pady=20)

label_1 = tkinter.Label(my_window, text=" enter your weight (kg) : ", font=('bold', 10))
label_1.pack()
label_1.config(pady=20)

entry1 = tkinter.Entry(my_window,width=22)
entry1.pack()



label_2 = tkinter.Label(my_window, text=" enter your height (cm) : ", font=('bold', 10))
label_2.config(pady=20)
label_2.pack()

entry2 = tkinter.Entry(my_window,width=22)
entry2.pack()


def calculate():
    try:
        weight = float(entry1.get())
        height = float(entry2.get())
        a = weight / ((height/100) * (height/100))
        print(a)
        return a
    except ValueError:
        print('you should enter a intiger')

my_button = tkinter.Button(text="Calculate", command=calculate)
my_button.pack()







'''if not label_2 == int(entry1.get()):
    print ('you should enter a intiger')'''




my_window.mainloop()