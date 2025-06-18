class Sample:
    def add(self):
        print("addition")
class Demo:
    def sub(self):
        print("Subtraction")

class Practice(Demo,Sample):
    def mult(self):
        print("multiplication")

x = Practice()
x.add
x.sub
x.mult