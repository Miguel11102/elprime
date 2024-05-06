class estudiante:
    """----------------------------------------
    # atributos
    -----------------------------------------"""
    def __init__(self, nombre, apellido, codigoEstudiante, codigoCurso):

        self.__nombre : nombre
        self.__apellido : apellido
        self.__codigoEstudiante : codigoEstudiante
        self.__codigoCurso : codigoCurso


    """------------------------------------------
    #metodos
    -------------------------------------------"""

    def darNombre(self):
        return self.__nombre + "" + self.__apellido
    
    def pertenecenMismoDepartamento(self):
        return
     
    def buscarCurso (self, pCodigoCurso):
        if pCodigoCurso == self.__codigoEstudiante:
            print("curso encontrado"+ self.__nombre)

    def buscarCurso(self, pCodigoCurso):
        if pCodigoCurso == self.__codigoCurso:
            print ("curso encontrado"+ self.__nombre)
        else: return None
