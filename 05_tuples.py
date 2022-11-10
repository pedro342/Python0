### TUPLES ###

my_tuple = tuple()
my_other_tuple = (35, 60, 30)

my_tuple = (19, 1.78, "hola", "q tal")

my_tuple.count("hola")
my_tuple.index("q tal") # index nos dicta el indice de donde se encuentra la palabra

### LAS TUPLAS NO PUEDEN CAMBIAR VALORES, SON VALORES CERRADOS INMUTABLES ###

print(my_tuple+my_other_tuple) # Pueden concatenarse