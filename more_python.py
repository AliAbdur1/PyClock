from turtle import *
from tkinter import *
from time import strftime

my_list = [564564565456546456465456757657456745765756746]
n = 565464564654
if (n := len(my_list)) > 10:
    print(f"list is too long ({n} elements)")
else:
    print("this is fine")
# for steps in range(500):
#     for c in ('blue', 'red', 'green'):
#         color(c)
#         forward(steps)
#         right(30)
txt = ["3", "5", "7", "9"]
print(*txt) # for clean output without the list structure

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"hello from {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name) # example of super to pass attributes from parent class to child class
        self.age = age

    def greet(self):
        super().greet() # example of super to pass methods from parent class to child class
        print(f"and i am {self.age}")

child = Child("Atlas", 4)
child.greet()

x = [4,5,3,6,2,7,5,3,5,6,2,3,7,8,4,2,3,3,3,5,4,6,7,8,5,3,2,1]
most = max(set(x), key=x.count) # finds item in list with maximum amount of occurances
print(most)

# clock v
timeWindow = Tk()
timeWindow.title("python clock")
def time():
    mytime = strftime('%H:%M:%S %p')
    clock.config(text = mytime)
    clock.after(1000, time)

clock = Label(timeWindow, font = ('arial', 40, 'bold'),
                                  background = 'dark green',
                                  foreground = 'white')
clock.pack(anchor = 'center')
time()

mainloop()
# clock ^
