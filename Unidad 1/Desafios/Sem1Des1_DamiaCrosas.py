#Grupo de estudio Python #Semana 1 - Desafio 1

#Descripci�n:
#Calcular la edad de tres personas bas�ndose en el a�o actual entrado por teclado.

#Autor:
#Dami� Crosas

#Funciones
def checkYear(in_Year):
     if in_Year.isdigit() and len(in_Year) == 4:
          return True
     else:
          return False
     
def getActYear():
     year = 0
     okYear = False     
     while okYear == False:
          year = raw_input("Ingrese el a�o actual: ")
          okYear = checkYear(str(year))
          if okYear == False:
            print("Atenci�n: Ingrese el a�o en formato 'aaaa'.")
          print("")
     return int(year)
                  
def printPersonInfo(in_arrNames,in_arrYears,in_arrAges,in_nPersons):
        print( "" )
        for counter in range(in_nPersons):                
                print(in_arrNames[counter] + " naci� al a�o " + in_arrYears[counter] + " y ahora tiene " + in_arrAges[counter] + " a�os.")
               
def getPersonInfo(in_actYear,out_arrNames,out_arrYears,out_arrAges,in_nPersons):
         for counter in range(in_nPersons):
                name = raw_input("Ingrese el nombre: ")                
                okYear = False     
                while okYear == False:
                     year = raw_input("Ingrese el a�o de nacimiento: ")
                     okYear = checkYear(str(year))                     
                     if okYear == False:
                          print("Atenci�n: Ingrese un a�o en formato 'aaaa'.")
                     elif int(year) > in_actYear:
                        okYear = False
                        print("Atenci�n: Ingrese un a�o inferior al actual") 
                out_arrNames.append(name)
                out_arrYears.append(str(year))
                out_arrAges.append(str(in_actYear - int(year)))
                print("")
                      
def calcAges(in_actYear,in_nPersons):
                      
        #Definiciones de las matrizes
        arrNames  = []
        arrYears  = []
        arrAges   = []

        #Se obtiene la informaci�n de la persona
        getPersonInfo(in_actYear,arrNames,arrYears,arrAges,in_nPersons)
       
        #Impresi�n de los c�lculos
        printPersonInfo(arrNames,arrYears,arrAges,in_nPersons) 

#Main      
#C�lculo de la edad de 3 personas bas�ndose en el a�o entrado
calcAges(getActYear(),3)

