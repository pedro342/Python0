### Funciones ###

def my_function ():
    print("Esto es una funcion")

my_function()
my_function()
my_function()

def sum_two_values(first_value, second_Value):
    print(first_value + second_Value)

sum_two_values(first_value=2, second_Value=3)    
sum_two_values(1, 6)
sum_two_values("1", "6")
sum_two_values(1.3, 6.5)

def sum_two_values_with_return(first_value, second_Value):
    my_sum = first_value + second_Value
    return my_sum

my_result = sum_two_values_with_return(5,7)

print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "rueda", name = "pedro")