### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.78, "hola", "q tal"] # Se puede guardar cualquier tipo de datos en una misma lista

print(type(my_other_list))


print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count("hola"))

age, height, name, surname = my_other_list
print(name)

my_other_list.append("Cirscunstancia") # Append agrega elementos al final
print(my_other_list)

my_other_list.insert(1, "cualq cosa") # Insert inserta en una posicion y no borra el contenido

my_other_list[1] = 'Cualq cosa'

my_other_list.remove("cualq cosa") # Remove borra lo que le pasemos en el parametro y borra solo el primer elemento igual, si hay copias, no las borra a todas

my_list.pop() # Quita el ultimo elemento de la lista por defecto, pero no lo borra, si le pasamos un parametro borra el elemento del indice que le pasamos

my_pop_element = my_list.pop() # Una forma de guardar el elemento quitado en una variable

del my_list[2] # Del borra un elemento de la lista que le pasemos por indice

my_list.clear() # Borra toda la lista

my_new_list = my_list.copy() # copy sirve para copiar las listas

my_new_list.reverse() # reverse da la vuelta la lista entera

my_new_list.sort() # sort ordena la lista indicando criterios, si no se los indica, las ordena por defecto de menor a mayor
