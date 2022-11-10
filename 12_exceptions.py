### Exceptions Handling ###

numberOne, numberTwo = 5, 1

numberTwo = "1"

try:
    print(numberOne + numberTwo)
    print("no hay error")
except:
    #se ejecuta si se produce una excepcion
    print("hay error")

try:
    print(numberOne + numberTwo)
    print("no hay error")
except:
    print("hay error")
else:
    #se ejecuta si no se produce una excepcion
    print("la ejecucion continua correctamente")
finally:
    #se ejecuta siempre
    print("la ejecucion continua")

#excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("no hay error")
except TypeError: #solo ejecuta si se produce este error
    #se ejecuta si se produce una excepcion
    print("hay error")
    
try:
    print(numberOne + numberTwo)
    print("no hay error")
except TypeError as error: #error es una variable 
    print(error) #muestra el error mas detallado

try:
    print(numberOne + numberTwo)
    print("no hay error")
except Exception as error: #formas de que el error se controle
    print(error)
