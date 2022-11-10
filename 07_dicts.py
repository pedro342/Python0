### Dictionaries ###

my_dict = dict()
my_other_dict = {}

my_other_dict = {"nombre":"pedro","apellido":"rueda","edad":19, 1:"Python"}

my_dict = {
    "nombre":"pedro",
    "apellido":"rueda",
    "edad":19, 
    "lenguajes":{"Python", "java","c"}
    }

print(my_dict['nombre'])

del my_dict["nombre"]

my_dict.items()#Muestra todo
my_dict.keys()#Muestra las llaves
my_dict.values()#Muestra solo los valores