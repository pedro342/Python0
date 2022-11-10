### Clases ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson())
print(MyEmptyPerson)

class Person:
    def __init__(self, name, surname, alias = 'sin alias'):
        self.full_name = f"{name} {surname} {(alias)}"
        self.__name = name #__PRIVATE
        self.__surname = surname

    def get_name(self):
        return self.__name

    def set_username(self, username):
        self.__username = username     

    def walk (self):
        print(f"{self.full_name} Esta caminando")

my_person = Person("pedro", "rueda")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("pedro", "rueda", "nose")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "hector de leon (no se)"
print(my_other_person.full_name)