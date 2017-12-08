class Person:
    def __init__(self, name, adress, status, sex):
        self.name = name
        self.adress = adress
        self.status = status
        self.sex = sex
    
    def write(self):
        print(self.name, self.adress, self.status, self.sex)



class User(Person):
   def __init__(self, email, home_page):
       self.email = email
       self.home_page = home_page
       
   def write2(self):
        print(self.email, self.home_page)

var_name = Person('Volodumyr','Ivano-Frankivsk', 'Odrygenuy', 'man')
var_name2 = User('123@gmail', 'httml')
print(var_name.write())
print(var_name2.write2())
       