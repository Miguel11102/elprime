from transaccion import transaccion

class libro:
    """----------------------
    #atributos
    ------------------------"""

    def __init__(self, pIsbn, pTitulo, pPrecioVenta, pPrecioCompra, pCantidadActual,pImagen):
        self.__transacciones = []
        self.__isbn = pIsbn
        self.__titulo = pTitulo
        self.__precioVenta = pPrecioVenta
        self.__precioCompra = pPrecioCompra
        self.__cantidadActual = pCantidadActual
        self.__imagen = pImagen

    def getISBN(self):
        return self.__isbn
    
    def setISBN (self, nIsbn):
        self.__isbn= nIsbn
    
    def getTitulo (self):
        return self.__titulo
    
    def setTitulo (self, nTitulo):
        self.__titulo= nTitulo
    
    def getPrecioVenta (self):
        return self.__precioVenta
    
    def setPrecioVenta (self, nPrecioVenta):
        self.__precioVenta = nPrecioVenta
    
    def getPrecioCompra (self):
        return self.__precioCompra
    
    def setPrecioVenta (self, nPrecioCompra):
        self.__precioCompra = nPrecioCompra
    
    def getcantidadActual (self):
        return self.__cantidadActual
    
    def setCantidadActual (self, nCantidadActual):
        self.__cantidadActual= nCantidadActual
    
    def getImagen (self):
        return self.__imagen
    
    def setImagen (self, nImagen):
        self.__imagen= nImagen

    def getTransacciones (self):
        return self.__transacciones
    
    def setTransacciones (self, nTransacciones):
        self.__transacciones = nTransacciones

    def vender (self, cantidad, fecha):

        vendido = False

        if cantidad <= self.getcantidadActual():

            self.__cantidadActual -= cantidad

            self.setCantidadActual(self.getcantidadActual() - cantidad)
            nueva = transaccion(1, cantidad, fecha)
            self.__transacciones.append(nueva)
            vendido =  True

        return vendido
    
    def abastecer (self, cantidad, fecha):
        
        self.setCantidadActual(self.getcantidadActual() + cantidad)
        nueva= transaccion(2, cantidad, fecha)
        self.__transacciones.append(nueva)


