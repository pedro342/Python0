### Varibales ###
from ast import Str


my_string_variable = 'My String variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print 
print(my_string_variable,str( my_int_variable ), my_bool_variable)

# Funciones del sistema
print(len(my_int_to_str_variable)) #len() = length()

# Variables en una sola linea
name, surname, alias, age = "Ped", "Rue", "S", 19
print("Name", name, "Surname", surname,"Alias", alias, "Age", age)

# Input
first_name = input('What is your name')
age = input("how old are you")

# Cambiando su tipo
#Python no tiene un tipado fuerte
name = 123
age = 'Pe'
print(name)
print(age)

# Forzamos el tipo?
address: str = "mi direccion"
address = 32 
print(address)