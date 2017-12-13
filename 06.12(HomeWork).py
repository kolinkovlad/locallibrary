class Person:
    def __init__(self, name, addres, status, sex):
        self.name = name
        self.addres = addres
        self.status = status
        self.sex = sex
    def vuvid(self):
        return self.name, self.addres, self.status, self.sex

class User(Person):
   def __init__(self, home_pge, email):
       self.home_pge = home_pge
       self.email = email
   def vuv(self):
        return self.email, self.home_pge

a = Person("Ростик", "Угорники..", "Студент", "Чол.")
b = User('daniliv.rostik@gmail.com', 'vk.com/anody')
print(a.vuvid())
print(b.vuv())
