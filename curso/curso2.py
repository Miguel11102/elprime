class curso:

   """----------------------------------------
    #atributos 
    ------------------------------------------"""

   __notas = [3, 5, 3, 2, 3.5, 1, 3.5, 4, 3.5, 5, 4.5, 4.2]

   """--------------------------------------------
    #metodos
    --------------------------------------------"""

   def elementos_Totales(self):
     curso_notas=len(self.__notas)
     return curso_notas
    
   def promedio_notas(self):
       suma = 0.0
       indice = 0

       while indice <= 12:
          suma= suma+self.__notas[indice]
          indice +=1
          
          return suma/indice

   def calcularCantidadAProbados(self):
       aprobados = 0
       indice = 0

       while indice <12:
          if (self.__notas[indice]>=3.0)and(self.__notas[indice]<=5):
             aprobados+=1
             indice+=1

             return aprobados 

   def calcularCantidadAprobados2(self):
      aprobados = 0

      for indice in range(12):
         if (self.__notas[indice]>=3.0)and(self.__notas[indice]<=5):
            aprobados+=1
   
      return aprobados
   
   def calcularCantidadAprobados3(self):
      aprobados= 0
      for nota in self.__notas:
         if nota >= 3.0 and nota <= 5.0:
            aprobados+=1
      
      return aprobados
   
   def calcularMayorNota(self):
      maxima=0
      for nota in self.__notas:
         if nota > maxima:
            maxima = nota
      return maxima
   
   def hacerCurva(self):
      indice = 0
      while indice<12:
         if self.nota[indice]<=4.75:
            self.__notas[indice]*=1.05
            indice*=1
            return self.__notas  

   
   def hayAlgunCinco_uno(self):
      i=0
      hayCinco = False
      while i<len(self.__notas) and not hayCinco:
         if self.__notas[i] == 5.0:
            hayCinco = True
         i+=1
      return hayCinco

   def hayAlgunCinco_dos(self):
      hayCinco = False

      for i in range(len(self.__notas)):
         if (self.__notas[i] == 5):
            hayCinco=True
            break

      return hayCinco
   
   def hayalgunCinco_tres(self):
      hayCinco = False
      for nota in self.__notas:
         if nota == 5:
            hayCinco=True
            break
      
      return hayCinco
   
   def asignarNotas(self):
      notasIguales = 0
      for i in range (len(self.__notas)):
         if self.__notas[i] == 1.5:
            self.__notas[i] = 2.5
         if notasIguales == 3:
            break
      return notasIguales
   
   def encontrarNotasCinco (self):
      contador = 0
      for i in range (len(self.__notas)):
         if self.__notas[i] == 5.0:
            contador += 1
            contador == 3
            return i
         else:
            return -1
         
   def reemplazarNotasHasta3(self):
      for i in range (len(self.__notas)):
         if self.__notas[i] > 3.0:
            break
         self.__notas[i]= 0.0

   def minNotasSumar(self):
      suma = 0
      numNotas = 0

      for nota in self.__notas:
         suma+= nota
         numNotas += 1
         if suma > 30:
            break
      return numNotas
   