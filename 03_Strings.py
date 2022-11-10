### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)
my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\tEste es un string\nescapado"
print(my_scape_string)

# Formateo

name, surname, age = 'Pedro', 'Rueda', '19'

print("Mi nombre es {} {} {}".format(name,surname,age))
print("Mi nombre es %s %s %s" %(name,surname,age))

# Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language # a = language[0] 
print(a)
print(b)

# Divison

lenguage_slice = language[1:3]
print(lenguage_slice)

lenguage_slice = language[1:]
print(lenguage_slice)

lenguage_slice = language[-2]
print(lenguage_slice)

lenguage_slice = language[0:6:2]
print(lenguage_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper()) #isupper comprueba si es mayuscula
print(language.startwith("py")) #como inicia?