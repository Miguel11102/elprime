class transaccion:
    TIPO = {
        1:'Venta',
        2:'ABASTECIMIENTO'
    }

    def __init__(self, tipo, cantidad, fecha):

        self.__tipo = self.TIPO['1'] if tipo == 1 else self.TIPO['2']
        self.__cantidad = cantidad
        self.__fecha = fecha
    
    def getTipo(self):
        return self.__tipo
    
    def setTipo(self, tipo):
        self.__tipo = self.TIPO['1'] if tipo == 1 else self.TIPO['2']

    
    
