
class NameGreeter:
    last_name = "Ivanov"

    def __init__(self, name, agggge):
        self.name = name
        self.age = agggge

    def greet(self):
        print("Hi! ", self.name, self.last_name, "With age ", self.age)


class NewGreeter(NameGreeter):
    name = "asfsf"
    def info(self):
        return self.name, self.last_name, self.age

# my_var = NameGreeter("Taras", 12)
# # print(type(my_var))
# my_var.greet()
#
# my_var2 = NameGreeter("Petro", 26)
# my_var2.name = "Zahar"
# my_var2.last_name = "Petrov"
# print(my_var2.name)
# print(my_var.name)
#
# my_var.city = "Ivano-Frankivsk"
#
# print(my_var.city)
new_var = NewGreeter("Mkola", 3)

new_var.additional_var = "bla-bla"

# print(new_var.last_name)
print(new_var.info())

