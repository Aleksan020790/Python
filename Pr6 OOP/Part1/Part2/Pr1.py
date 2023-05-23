# Создайте класс Human, который будет содержать
# информацию о человеке.
# С помощью механизма наследования, реализуйте класс
# Builder (содержит информацию о строителе), класс Sailor
# (содержит информацию о моряке), класс Pilot (содержит
# информацию о летчике).
# Каждый из классов должен содержать необходимые
# для работы методы.
class Human:
    def __init__(self,name, surname,age,tel):
        self.name=name
        self.surname=surname
        self.__age=age
        self.tel=tel
    def show_info (self):
        print(self.name,self.surname, self.__age,self.tel, end=" ")

class Builder(Human):
    def __init__(self, name, surname,age, tel, firm) -> None:
        super().__init__(name,surname,age,tel)
        self.firm = firm
    def show_info(self):
        super().show_info()
        print(self.firm)

class Sailor(Human):
    def __init__(self, name, surname, age, tel,captain) -> None:
        super().__init__(name, surname, age, tel)
        self.captain=captain
    def show_info(self):
        super().show_info()
        print(self.captain)

class Pilot(Human):
    def __init__(self, name, surname, age, tel,ticket):
        super().__init__(name, surname, age, tel)
        self.ticket=ticket
    def show_info(self):
        super().show_info()
        print(self.ticket)
   

pilot1 = Pilot("Alex","Zhadan","32","+380975913130","Bisness Class")
pilot1.show_info()
sailor1 = Sailor("Alex","Zhadan","32","+380975913130","Captain")
sailor1.show_info()
builder1 = Builder("Alex","Zhadan","32","+380975913130","Start")
builder1.show_info()

human1 = Human("Alex","Zhadan","32","+380975913130")
human1.show_info()


        
            