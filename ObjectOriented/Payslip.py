class Payslips:
    def __init__(self, name, payment, amount) -> None:
            self.name = name
            self.payment = payment
            self.amount =amount

    def pay(self):
        self.payment = "yes"
    
    def status(self):
        if self.payment == "yes":
            return self.name + " is paid "+str(self.amount)
        else:
            return self.name + " is not paid yet"


niyam =Payslips("Niyam", "no", 100000)
niyam.pay()
print(niyam.status())

class ChildPayslips(Payslips):
    def __init__(self, name, payment, amount, gender):
        super().__init__(name, payment, amount)
        self.gender = gender

    def genderWhat(self):
        return self.gender
        print(self.gender)

sichu = ChildPayslips("Sichu", "no", 100000,"female")
print(sichu.status())
print(sichu.genderWhat())
