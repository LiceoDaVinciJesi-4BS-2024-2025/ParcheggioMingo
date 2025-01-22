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
    def __init__(self, tipo: str, targa:str = "", oreSosta:datetime.time = datetime.time(00, 00, 00)):
        """
        inizializza la funzione, permette di parcheggiare un mezzo a seconda del se è libero o no
        """
        if tipo not in tipoLista:
            raise ValueError("Tipo non valido")
        self.__tipo = tipo
        
        #imposto una targa, se la targa è vuota il parcheggio è occupato
        self.__targa = targa
        
        #segno quando finisce il termine di occupazione
        # self.__dataFineParcheggio = 0
        self.__oreSosta = oreSosta
        
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
    
#     @property
#     def dataFineParcheggio(self):
#         return self.__dataFineParcheggio
#     
#     @dataFineParcheggio.setter
#     def dataFineParcheggio(self, data:datetime.datetime):
#         """
#         imposto la data del parcheggio
#         """
#         self.__dataFineParcheggio = data
#         return

    @property
    def oreSosta(self):
        return self.__oreSosta
    
    @oreSosta.setter
    def oreSosta(self, ora:datetime.time):
        """
        imposto la durata del parcheggio
        """
        self.__oreSosta = ora
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
    parcheggio.targa = "AB 123 CD"
    print("Parcheggio occupato:", parcheggio.occupato())
    print("Targa auto parcheggiata:", parcheggio.targa)
        
        
        
        
        
        