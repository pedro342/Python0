### SETS ###

my_set = set()
my_other_Set = {} #Diccionario

my_other_Set = {"q tal", "como", 0,} #Set

my_other_Set.add("hola") #Un set no es una estructura ordenada, por lo que no se pueden acceder a elementos mediante [0]
my_other_Set.add("hola") #Un set no admite repetidos

print("hola" in my_other_Set) #hola existe en my_other_Set??

my_other_Set.remove("hola")

my_other_Set.clear()

my_new_set = my_set.union(my_other_Set)

my_new_set.difference(my_set) #Busca la diferencia entre ambos sets