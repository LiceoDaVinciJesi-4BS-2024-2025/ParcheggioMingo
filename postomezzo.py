# Aurora Mingo
# 4BS
# Parcheggio OOP: livello 2

import veicolo
import moto
import auto
import datetime

tipoLista = ["Auto", "Moto"]

#definisco la classe
class PostoMezzo:
    def __init__(self, tipo: str):
        """
        inizializza la funzione, permette di parcheggiare un mezzo a seconda del se è libero o no
        """
        if tipo not in tipoLista:
            raise ValueError("Tipo non valido")
        self.__tipo = tipo
        
        #imposto una targa, se la targa è vuota il parcheggio è occupato
        self.__targa = ""
        
        #segno quando finisce il termine di occupazione
        self.__dataFineParcheggio = datetime.datetime(2000, 12, 12, 5, 2)
        
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
    @property
    def tipo (self):
        return self.__tipo
    
    @property
    def targa (self):
        return self.__targa
    
    @targa.setter
    def targa (self, targa):
        self.__targa = targa
        return
    
    @property
    def dataFineParcheggio(self):
        return self.__dataFineParcheggio
    
    @dataFineParcheggio.setter
    def dataFineParcheggio(self, data:datetime.datetime):
        """
        imposto la data del parcheggio
        """
        self.__dataFineParcheggio = data
        return 
        
        
        
        
        
        