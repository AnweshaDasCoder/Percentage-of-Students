from tkinter import *
root= Tk()
root.geometry("600x600")

BTN_3 = Button(root, text="Grade 3", command=three)
BTN_3.pack()
Label_3 = Label(root,text="")
Label_3.pack()
BTN_5 = Button(root, text="Grade 5", command=five)
BTN_5.pack()
Label_5 = Label(root,text="")
Label_10.pack()
BTN_10 = Button(root, text="Grade 10", command=ten)
BTN_10.pack()
Label_10 = Label(root,text="")
Label_10.pack()

class third_grade():  
    def __init__(self, Language_Arts, Math): 
        self.LA = Language_Arts
        self.MT = Math
        
    def percetage(self):
        
class fifth_grade():  
    def __init__(self, Language_Arts, Science, Math): 
        self.LA = Language_Arts
        self.MT = Math
        self.SC = Science
        
class tenth_grade():  
    def __init__(self, Language_Arts, Science, Math, Social_Studies): 
        self.LA = Language_Arts
        self.MT = Math
        self.SC = Science
        self.SS = Social_Studies
        

    