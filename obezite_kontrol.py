import tkinter



my_window = tkinter.Tk()
my_window.title("BMI Calculator")
my_window.minsize(width=300, height=300)


label_1 = tkinter.Label(my_window, text="enter your weight (kg) : ", font=('bold', 10))
label_1.pack()

entry1 = tkinter.Entry(my_window,width=10)
entry1.pack()

label_2 = tkinter.Label(my_window, text="enter your height (cm) : ", font=('bold', 10))
label_2.pack()

entry1 = tkinter.Entry(my_window,width=10)
entry1.pack()






my_window.mainloop()