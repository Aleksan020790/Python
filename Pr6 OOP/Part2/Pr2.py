# Создайте класс Passport (паспорт), который будет
# содержать паспортную информацию о гражданине заданной страны.
# С помощью механизма наследования, реализуйте
# класс ForeignPassport (загран.паспорт) производный от
# Passport.
# Напомним, что заграничный паспорт содержит помимо паспортных данных, также данные о визах, номер
# заграничного паспорта.
class Passport:
    def __init__(self,name, surname,age,city,address,number_passport):
        self.name=name
        self.surname=surname
        self.age=age
        self.city=city
        self.address=address
        self.number_passport=number_passport
    def show_info (self):
        print(self.name,self.surname, self.age,self.city, self.address,self.number_passport, end=" ")
class ForeignPassport(Passport):
    def __init__(self, name, surname, age, city, address, number_passport,viza, Foreign_number):
        super().__init__(name, surname, age, city, address, number_passport)
        self. viza= viza
        self. Foreign_number=Foreign_number
    def show_info(self):
        super().show_info()
        print(self.viza)
        print(self.Foreign_number)

Passport1=Passport("Oleksandra","Zhadan","32","Kriviy Rig", "Hayphonska22", "AO2345276")
Passport1.show_info()
ForeignPassport1=ForeignPassport("Oleksandra","Zhadan","32","Kriviy Rig", "Hayphonska22", "AO2345276","C","FF124521")
ForeignPassport1.show_info()

