# Aurora Mingo
# 4BS
# Esercizio parcheggio

# Livello 0
# Definire la classe Veicolo, contenente le seguenti informazioni: marca, modello, colore, cilindrata
# (int), alimentazione, targa. L’unica informazione obbligatoria è la targa, che deve essere della forma
# AB 123 CD (dove al posto delle ABCD ci va una qualunque lettera maiuscola dell’alfabeto e al
# posto di 123 ci va una qualunque sequenza numerica di 3 cifre).

listaAuto = ["Ferrari", "McLaren", "Mercedes", "Porsche", "Bugatti", "Fiat", "Opel"]

class Veicolo:
    
    def __init__(self, targa: str):
        """
        inizializza la classe; l'unica funzione è la targa
        """
        #controllo la targa
        alfabetoM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeri = "0123456789"
        
        #creo una lista con i tre elementi della targa
        listaTarga = targa.split(sep= " ")
        #controllo la prima parte
        if len(listaTarga[0]) == 2:
            for lettera in listaTarga[0]:
                if lettera not in alfabetoM:
                    raise ValueError ("Targa non valida")
        
        #controllo la seconda parte
        if len(listaTarga[1]) == 3:
            for numero in listaTarga[1]:
                if str(numero) not in numeri:
                    raise ValueError ("Targa non valida")
        
        #controllo la terza parte
        if len(listaTarga[0]) == 2:
            for lettera in listaTarga[2]:
                if lettera not in alfabetoM:
                    raise ValueError ("Targa non valida")
        
        self.__targa = targa
        #-------------------------------------------------------------
        self.__marca = "Ferrari"
        self.__modello = "Purosangue"
        self.__colore = "rosso"
        self.__cilindrata = 250
        self.__alimentazione = "benzina"
        
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
    #oggetto targa
    @property
    def targa(self):
        return self.__targa
    
    @targa.setter
    def targa(self, targa:str):
        """
        permette di rideterminare la targa
        """
        #creo una lista con i tre elementi della targa
        listaTarga = targa.split(sep= " ")
        #controllo la prima parte
        for lettera in listaTarga[0]:
            if lettera not in alfabetoM:
                raise ValueError ("Targa non valida")
        
        #controllo la seconda parte
        for numero in listaTarga[1]:
            if str(numero) not in numeri:
                raise ValueError ("Targa non valida")
        
        #controllo la terza parte    
        for lettera in listaTarga[2]:
            if lettera not in alfabetoM:
                raise ValueError ("Targa non valida")
        
        self.__targa = targa
        return
    
    #oggetto marca
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca:str):
        self.__marca = marca
        return
    
    @property
    def modello(self):
        return self.__modello
    
    @modello.setter
    def modello(self, modello:str):
        self.__modello = modello
        return
    
    @property
    def colore(self):
        return self.__colore
    
    @colore.setter
    def colore(self, colore:str):
        self.__colore = colore
        return
    
    @property
    def cilindrata(self):
        return self.__cilindrata
    
    @cilindrata.setter
    def cilindrata(self, cilindrata:str):
        self.__cilindrata = cilindrata
        return
    
    @property
    def alimentazione(self):
        return self.__alimentazione
    
    @alimentazione.setter
    def alimentazione(self, alimentazione:str):
        self.__alimentazione = alimentazione
        return
    
    
        
# Definire una serie di liste per marca, colore e alimentazione per indicare i valori accettabili.
# Cilindrata deve essere un intero positivo multiplo di 100. 
# Aggiungere un ordinamento implicito fra gli oggetti di tipo Veicolo in modo da renderli ordinabili
# alfabeticamente per marca, modello e numericamente (dal più piccolo al più grande) per cilindrata.