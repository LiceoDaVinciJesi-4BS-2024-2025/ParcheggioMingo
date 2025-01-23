# Aurora Mingo
# 4BS
# OOP: Parcheggio, livello 1
# classe Moto

#creo la classe auto derivante da veicolo
import veicolo

class Moto(veicolo.Veicolo):
    
    def __init__(self, targa: str, numeroMaxPass: int, persTrasportate: int):
        """
        inizializza la funzione
        """
        super().__init__(targa)
        if numeroMaxPass <= 0 or numeroMaxPass > 2:
            raise ValueError("Valore non accettabile")
        self.__numeroMaxPass = numeroMaxPass
        
        if persTrasportate > numeroMaxPass or persTrasportate <= 0:
            raise ValueError("Persone portate più dei posti disponibili")
        self.__persTrasportate = persTrasportate
        #guarda se devi trasportare anche le altre funzioni
    
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
    #creo le proprietà
    @property
    def numeroMaxPass (self):
        return self.__numeroMaxPass

    @property
    def persTrasportate (self):
        return self.__persTrasportate
    
    @persTrasportate.setter
    def persTrasportate(self, numero:int):
        """
        permette di reimpostare le persone trasportate
        """
        if numero <= 0 or numero > self.__numeroMaxPass:
            raise ValueError("Valore non accettabile")
        self.__persTrasportate = numero
        return
    
#-----------------------------------------------------------------------------------------------------
#TEST
if __name__ == "__main__":
    #creo una moto
    moto1 = Moto("AB 123 CD", 2, 1)
    print(moto1)
    moto1.marca = "kawasaki"
    moto1.numeroMaxPass = 1
    moto1.persTrasportate = 1
    print(moto1)