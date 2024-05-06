from enum import Enum
"""----------------------------------------------------
#enumeraciones
----------------------------------------------------"""
class tipo(Enum):
    PAPELERIA = 1
    SUPERMERCADO = 2
    FARMACIA = 3
class producto:
    __subsidio = False
    __calidad = "A"
    """---------------------------------------------------------------
    # constantes
    ------------------------------------------------------------------"""
    
    __IVA_PAPELERIA = 0.16
    __IVA_SUPERMECADO = 0.04
    __IVA_FARMACIA = 0.12

    PRECIO_MAXIMO = 500000

    """----------------------------------------------------------------
    # Atributos
    -------------------------------------------------------------------"""
    __nombre = None
    __tipo = Enum("tipo",["PAPELERIA", "SUPERMERCADO", "FARMACIA"])
    __valorUnitario = 0.0
    __cantidadBodega = 0
    __cantidadMinima = 0
    __cantidadUnidadesVendidas = 0

    """-------------------------------------------------------------------
    # Metodos
    --------------------------------------------------------------------"""
    def __init__ (self,tipo, pNombre, pValorUnitario, pCantidadBodega, pCantidadMinima, pCantidadUnidadesVendidas):
        self.__tipo
        self.__nombre
        self.__valorUnitario
        self.__cantidadBodega
        self.__cantidadMinima
        self.__cantidadUnidadesVendidas=0

    def getNombre(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo
    
    def getValorUnitario(self):
        return self.__valorUnitario
    
    def getCantidadBodegas(self):
        return self.__cantidadBodega
    
    def getCantidadMinima(self):
        return self.__cantidadMinima
    
    def getCantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas
    
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def setTipo (self,tipo):
        self.__tipo = tipo
    
    def setValorUnitario (self,valorUnitario):
        self.__valorUnitario = valorUnitario

    def setCantidadBodega (self,cantidadBodega):
        self.__cantidadBodega = cantidadBodega

    def setCantidadMinima (self,cantidadMinima):
        self.__cantidadMinima = cantidadMinima

    def setCantidadUnidadesVendidas (self,cantidadUnidadesVendidas):
        self.cantidadUnidadesVendidas = cantidadUnidadesVendidas

    def Vender(self, cantidad):
        if cantidad > self.__cantidadBodega:
            self.__cantidadUnidadesVendidas += cantidad
            self.__cantidadBodega += cantidad
        else:
            print("Cantidad no dispoible")

    def Hay_Suficiente(self, cantidad):
        #forma 1
        if cantidad <= self.__cantidadBodega:
            return True
        
    def DarIVA(self):
        if(self.__tipo=="PAPELERIA"):
            return self.__IVA_PAPELERIA
        elif(self.__tipo=="FARMACIA"):
            return self.__IVA_FARMACIA
        elif(self.__tipo=="SUPERMERCADO"):
            return self.__IVA_SUPERMECADO
        
        else:
            print("Categoria de producto no existe")

    def SubirValorUnitario(self):
        if self.__valorUnitario< 1000:
            self.__valorUnitario +=self.__valorUnitario*0.01
    
    def nombreTipoProducto(self):
        if self.__tipo == "SUPERMECADO":
            return "El producto es de supermecado"
        
    def aumentarValorUnitario (self):
        if self.__tipo == "DROGUERIA":
            aumento = self.__valorUnitario * 0.01
        
        elif self.__tipo == "SUPERMERCADO":
            aumento = self.__valorUnitario * 0.03

        elif self.__tipo == "PAPELERIA":
            aumento = self.__valorUnitario * 0.02





