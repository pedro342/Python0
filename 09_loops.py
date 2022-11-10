### Loops ###

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print("Mi condicion es >= 10")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("stop")
        break

    print(my_condition)

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (19, 1.78, "hola", "q tal")

for element in my_tuple:
    print(element)

my_other_Set = {"q tal", "como", 0,}

for element in my_other_Set:
    print(element)

my_other_dict = {"nombre":"pedro","apellido":"rueda","edad":19, 1:"Python"}

for element in my_other_dict.values(): #Forma para ver values de dict
    print(element)
    if element == "edad":
        break
    print("se ejecuta")
else:
    print("El bucle for para mi dict ha finalizado")