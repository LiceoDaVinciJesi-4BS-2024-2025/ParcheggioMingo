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
    def __init__(self, tipo: str, targa: str = "", dataInizioParcheggio: datetime.datetime = None, dataFineParcheggio: datetime.datetime = None): # ci inserisco solo il tipo di parcheggio, targa:str = "", dataFineParcheggio:datetime.datetime = None):
        """
        inizializza la funzione, permette di parcheggiare un mezzo a seconda del se è libero o no
        """
        if tipo not in tipoLista:
            raise ValueError("Tipo non valido")
        self.__tipo = tipo
        
        # la targa è vuota, il parcheggio è occupato
        self.__targa = targa
        
        #segno quando finisce il termine di occupazione
        self.__dataInizioParcheggio = dataInizioParcheggio
        self.__dataFineParcheggio = dataFineParcheggio
        
        
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
    
    @property
    def dataInizioParcheggio(self):
        return self.__dataInizioParcheggio
    
    @property
    def dataFineParcheggio(self):
        return self.__dataFineParcheggio

    
    #creo una funzione per occupare il parcheggio
    def occupaPosto (self, targa:str):
        """
        creo una funzione per occupare un parcheggio
        """
        self.__targa = targa
        self.__dataInizioParcheggio = datetime.datetime.now()
        return
        
    #creo una funzione per liberare il parcheggio
    def liberaPosto (self, targa:str):
        """
        creo una funzione per liberare il parcheggio
        """
        self.__targa = ""
        self.__dataFineParcheggio = datetime.datetime.now()
        return
    
    #creo una funzione per vedere se è occupato
    def occupato(self):
        if self.__targa == "":
            return False
        return True
    
#------------------------------------------------------------------------
#TEST
if __name__ == "__main__":
    parcheggio = PostoMezzo("Auto")
    print(parcheggio)
    print("Parcheggio occupato:", parcheggio.occupato())
    parcheggio.occupaPosto("AB 123 CD")
    print("Parcheggio occupato:", parcheggio.occupato())
    print("Targa auto parcheggiata:", parcheggio.targa)
    parcheggio.liberaPosto("AB 123 CD")
    print("Parcheggio occupato:", parcheggio.occupato())