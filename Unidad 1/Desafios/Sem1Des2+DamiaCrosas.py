#Grupo de estudio Python #Semana 1 - Desafio 2

#Descripci�n:
#

#Autor:
#Dami� Crosas

#Funciones
def getNumber():
     while True:
          number = raw_input("Introduce un n�mero:")
          if number.isdigit():
               return int(number)
               break
          else:
               print("No es un valor entero!!")
               continue
          
def printResults(inNumber):
     number = inNumber
     for i in range(number):
         print number
         number += i     

#Main      
#
printResults(getNumber())

