from libro import libro
class tiendaLibros:

    def __init__(self,):
        self.__caja = 1000000
        self.__catalogo = []
        
    def getCatalogo(self):
        return self.__catalogo
    
    def getCaja(self):
        return self.__caja
    
    def buscarLibroPorTitulo(self,titulo):
        libroBuscado = None

        for libro in self.__catalogo:
            if libro.getTitulo() == titulo:
                libroBuscado= libro
                break
        
        return libroBuscado
    
    def buscarLibroPorIsbn(self,isbn):
        libroBuscado = None

        for libro in self.__catalogo:
            if libro.getIsbn() == isbn:
                libroBuscado= libro
                break
        
        return libroBuscado
    

        
    
    def registrarLibro(self, pIsbn, pTitulo, pPrecioVenta, pPrecioCompra, pCantidadActual,pImagen):
        buscar = self.buscarLibroPorIsbn(pIsbn)
        nuevo= None
        if buscar == None:
            nuevo = libro(pIsbn, pTitulo, pPrecioVenta, pPrecioCompra, pCantidadActual,pImagen)
            self.__catalogo.append(nuevo)
        return nuevo
    
    def EliminarLibro(self, isbn):
        buscar = self.buscarLibroPorIsbn(isbn)

        if buscar:
            if buscar.getCanidadActual() == 0:
                self.__catalogo.remove(buscar)
                eliminado = True
        return eliminado
    
    def darLibroMasEconomico (self,):
        menosCostoso = None
        if (len(self.__catalogo)>0):
            menosCostoso = self.__catalogo[0]
            for libro in self.__catalogo:
                if libro.getPrecioVenta() < menosCostoso.getPrecioVenta():
                    menosCostoso = libro

        return menosCostoso
    
    def darLibroMasCostoso (self,):
        masCostoso = None
        if (len(self.__catalogo)>0):
            masCostoso = self.__catalogo[0]
            for libro in self.__catalogo:
                if libro.getPrecioVenta() > masCostoso.getPrecioVenta():
                    masCostoso = libro

        return masCostoso
    
    def vender(self, cantidad, fecha, isbn, titulo=None):
        vendido = False
        buscado = self.buscarLibroPorIsbn(isbn)
       
        if titulo is not None and buscado is None:
            buscado = self.buscarLibroPorTitulo(titulo)

        if buscado:
            vendido = buscado.vender(cantidad, fecha)
            self.setCaja(self.getCaja()+(cantidad*buscado.getPrecioVenta()))

            return vendido
        
