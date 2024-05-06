class LineaTelefonica:
    '''----------------------------------------------------------------
    # atributos
    ----------------------------------------------------------------'''
    #cantidad minutos  celular
    cantidadMinutos = ""
   
    # Costo de minutos de llamadas a celular
    costoMinutosCelular = ''
    
    # Numero de llamadas realizadas
    numeroLlamadas = ""
    
    # Numero de minutos consumidos
    numeroMinutos = ""
    
    # Costo total de las llamadas
    costoLlamadas = ""

    #estrato linea telefonica
    estrato = 0

    #descuento aplicable a las llamadas(valor entre 0.0 y 25.5)
    descuento = 0.0

    #cantidad de dinero disponible para gastar (prepago)
    prepago = 0.0

    #almacenar el total de segundos
    totalSegundos = 0

    #almacenar el costo de la llamada en dolares
    CostoLLamadaDolares= 0
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    # Inicializar el número de llamadas, número de minutos y costo de llamadas en 0.
    def __init__(self):
        self.numeroLlamadas= 0
        self.numeroMinutos = 0
        self.costoLlamadas= 0
        self.totalSegundos= 0
        self.CostoLLamadaDolares=0
        
        # TODO Parte2 PuntoA: Completar el método según la documentación dada.

    def reiniciar(self):
        self.numeroLlamadas= 0
        self.numeroMinutos = 0
        self.costoLlamadas= 0
        self.totalSegundos= 0
        self.CostoLLamadaDolares=0

    def convertirPesosADolares(self):
        convertido = float(self.costoLlamadas/ 3100)
        self.CostoLLamadaDolares = convertido
        return convertido
        

    #Retorna el costo total de las llamadas realizadas.
    def darCostoLlamadas(self):
        return self.costoLlamadas
        # TODO Parte2 PuntoB: Completar el método según la documentación dada.
        
    # Retorna el número de llamadas realizadas por esta línea.
    def darNumeroLlamadas(self):
        return self.numeroLlamadas
        # TODO Parte2 PuntoC: Completar el método según la documentación dada.
        
    # Retorna el número de minutos consumidos.
    def darNumeroMinutos(self):
        return self.numeroMinutos
        # TODO Parte2 PuntoD: Completar el método según la documentación dada.

    # Reinicia la línea telefónica, dejando todos sus valores en cero.
    # post: El número de llamadas, número de minutos y costo de llamadas son 0.
    def reiniciar(self):
        self.numeroMinutos = 0
        self.numeroLlamadas = 0
        self.costoLlamadas = 0

        # TODO Parte2 PuntoE: Completar el método según la documentación dada.

    # Agrega una llamada local a la línea telefónica
    # post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 35 ).
    # :param pMinutos Número de minutos de la llamada. pMinutos >0.
    def agregarLlamadaLocal(self, pMinutos, ):
        
        # Una llamada más
        self.numeroLlamadas += 1
        # Suma los minutos consumidos
        self.numeroMinutos += pMinutos
        # Suma el costo (costo por minuto: 35 pesos)
        self.costoLlamadas += pMinutos * 35
        #aumenta el saldo disponible
        dinerodisponible=self.darSaldoDisponible+self.agregarDineroSaldo
        return dinerodisponible

    """
        Agrega una llamada de larga distancia a la línea telefónica.
        
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 380 )
        
        :param pMinutos: Número de minutos de la llamada. pMinutos >0.
        """
    def agregarLlamadaLargaDistancia(self, pMinutos):
        # TODO Parte2 PuntoF: Completar el método según la documentación dada.

        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos
        self.costoLlamadas += pMinutos * 380
    '''
        Agrega una llamada a celular a la lÍnea telefónica
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 999 )
        :param pMinutos Número de minutos de la llamada. pMinutos >0.
    '''
    def agregarLlamadaCelular(self, pMinutos):
        # TODO Parte2 PuntoG: Completar el método según la documentación dada.
       
        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos
        self.costoLlamadas += pMinutos * 999
    
    def darDescuento(self):
        return self.descuento

    def aplicarDescuento(self):
        return (self.costoLlamadas * self.descuento)/100

    def darSaldoDisponible(self):
        return self.prepago

    def agregarDineroSaldo(self, valor):
        self.prepago += valor    
    

    def motivarCliente(self):
        if(self.darNumeroMinutos>30):
            self.aumentarSaldo + 1000
    
    def __init__(Self):
        Self.costoDolares = 0
        Self.numeroLlamadas = 0 
        Self.numeroMinutos = 0 
        Self.costoLlamadas = 0 
        Self.costoMinutosCelular = 0
        Self.cantidadMinutosCelular = 0

    def ConsultarCantidadMinutosCelular(self):

        return self.cantidadMinutosCelular

    def ConsultarCostoMinutosCelular(self):

        return self.costoMinutosCelular
    
    def reiniciar(self):
        self.numeroSegundos = 0
        self.costoDolares = 0
        self.numeroLlamadas = 0 
        self.numeroMinutos = 0 
        self.costoLlamadas = 0 
        self.costoMinutosCelular = 0
        self.cantidadMinutosCelular = 0
    
    def darEstrato(self):
        return self.estrato
    
    def definirEstrato(self, pEstrato):
        self.estrato - pEstrato

    def darMinutosPorEstrato(self):
        return self.numeroMinutos * self.estrato
    
    




    


