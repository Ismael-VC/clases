#Grupo de estudio Python #Semana 1 - Desafio 3

#Descripci�n:
#Dibujar un gr�fico de barras seg�n valores entrados

#Autor:
#Dami� Crosas

#Funciones
def getLine(inSize,inIndex):
      if inSize >= inIndex:
           return "____ "
      else:
           return "     "     
     
def printGraph():
     #Get sizes     
     sizeMax = input("Entre tama�o M�ximo:")
     sizeB1 =  input("Entre tama�o Barra 1:")
     sizeB2 =  input("Entre tama�o Barra 2:")
     sizeB3 =  input("Entre tama�o Barra 3:")
     sizeB4 =  input("Entre tama�o Barra 4:")
     
     #Gr�fico
     print "+++++++++++++++++++++++" 
     Output = "+ "
     for n in range(sizeMax,0,-1):
           Output = "+ "
           Output = Output + getLine(sizeB1,n)
           Output = Output + getLine(sizeB2,n)
           Output = Output + getLine(sizeB3,n)
           Output = Output + getLine(sizeB4,n)
           print Output + "+" 

     print "+  B1   B2   B3   B4  +"
     print "+++++++++++++++++++++++"
      
#Main      
#Impresi�n del gr�fico
printGraph()


    
        


