class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def shownumber(self):
        print(self.real,"i +",self.img,"j")
        
    def __add__(self,num2):
        newnum_real=self.real+num2.real
        newnum_img=self.img+num2.img
        return complex(newnum_real,newnum_img)
        
num1 = complex(5,6)
num2 = complex(1,3)
num3 = num1 + num2
num1.shownumber()
num2.shownumber()
num3.shownumber()