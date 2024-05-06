class curso: 
    """-----------------------
    #atributos
    ------------------------"""

    def __init__(self, codigoCurso, nombreCurso, departamento, cantidadCreditos, notaMinima, notaMaxima):
        self.__codigoCurso : codigoCurso
        self.__nombreCurso : nombreCurso
        self.__departamento : departamento
        self.__cantidadCreditos : cantidadCreditos
        self.__notaMinima : notaMinima
        self.__notaMaxima : notaMaxima

    """-----------------------------------
    #metodos
    -----------------------------------"""

    def darCodigoCurso(self):
        return self.__codigoCurso
    
    def pertenecenMismoDepartamento (self):
        if self.__curso1.departamento == self.__curso2.departamento == self.__curso3.departamento == self.__curso4.departamento:
            print("los cursos son del mismo departamento")
        else: return None
    
    def estaCalificado(self):
        if self.__nota != 0:
            print ("curso calificado")

    def calcularPromedioEstudiante(self, promedio1, promedio2, promedio3, promedio4, promedioTotal):
        if (self.__curso1.getNota()*self.__curso2.getNota()*self.__curso3.getNota()*self.__curso4.getNota()) !=0:
            promedio1 = (self.__curso1.getnota()* self.__curso1.getcreditos()/ self.curso1.getcredito()) 
            promedio2 = (self.__curso2.getnota()* self.__curso2.getcreditos()/ self.curso2.getcredito()) 
            promedio3 = (self.__curso3.getnota()* self.__curso3.getcreditos()/ self.curso3.getcredito()) 
            promedio4 = (self.__curso4.getnota()* self.__curso4.getcreditos()/ self.curso4.getcredito()) 

            promedioTotal = (promedio1 + promedio2+ promedio3 + promedio4)/4
            return promedioTotal
        else: return None