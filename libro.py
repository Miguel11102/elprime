class libro:
    """----------------------
    #atributos
    ------------------------"""

    def __init__(self, pIsbn, pTitulo, pPrecioVenta, pPrecioCompra, pCantidadActual,pImagen):
        self.__isbn = pIsbn
        self.__titulo = pTitulo
        self.__precioVenta = pPrecioVenta
        self.__precioCompra = pPrecioCompra
        self.__cantidadActual = pCantidadActual
        self.__imagen = pImagen

    def getISBN(self):
        return self.__isbn
    
    def getTitulo (self):
        return self.__titulo
    
    def getPrecioVenta (self):
        return self.__precioVenta
    
    def getPrecioCompra (self):
        return self.__precioCompra
    
    def getcantidadActual (self):
        return self.__cantidadActual
    
    def getImagen (self):
        return self.__imagen
    
