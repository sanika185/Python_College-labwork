class Reliance :
    def mukesh(self):
        print("I OWN Jio and MI team")
class Jio(Reliance):
    def Anant(self):
        print("I take Jio")

j= Jio()
j.Anant()
j.mukesh()

class MIteam(Jio):
    def Akash(self):
        print("I take MI")
x=MIteam()
x.Anant()
x.mukesh()