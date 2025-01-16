# Aurora Mingo
# 4BS
# PARCHEGGIO

import veicolo
import moto
import auto
import postomezzo
import datetime

#definisco la classe parcheggio
class Parcheggio:
    def __init__(self):
        """
        inizializza il parcheggio e definisce i posti disponibili
        """
        self.__parcheggiAuto = 1000
        self.__parcheggiMoto = 200
        self.__guadagnoTotale = 0
    
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
    #definizione delle property
    @property
    def parcheggiAuto(self):
        return self.__parcheggiAuto
    
    @property
    def parcheggiMoto(self):
        return self.__parcheggiMoto
    
    #creo la funzione per parcheggiare il veicolo
    def parcheggiaVeicolo(self, tipoVeicolo: str, targa:str, oreSosta: float):
        """
        permette di parcheggiare un veicolo
        """
        
    
    
    