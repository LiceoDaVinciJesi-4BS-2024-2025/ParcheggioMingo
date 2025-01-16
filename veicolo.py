# Aurora Mingo
# 4BS
# Esercizio parcheggio

# Livello 0
# Definire la classe Veicolo, contenente le seguenti informazioni: marca, modello, colore, cilindrata
# (int), alimentazione, targa. L’unica informazione obbligatoria è la targa, che deve essere della forma
# AB 123 CD (dove al posto delle ABCD ci va una qualunque lettera maiuscola dell’alfabeto e al
# posto di 123 ci va una qualunque sequenza numerica di 3 cifre).

# Definire una serie di liste per marca, colore e alimentazione per indicare i valori accettabili.
# Cilindrata deve essere un intero positivo multiplo di 100. 
listaMarche = ["ferrari", "mclaren", "mercedes", "porsche", "bugatti", "fiat", "opel","kawasaki", "aprilia", "ktm", "yamaha", "betamotor", "bmw", "ducati", "honda"]
listaColori = ["nero", "bianco", "grigio", "rosso", "blu", "verde", "giallo", "viola"]
listaAlimentazione = ["benzina", "diesel", "metano", "elettrico", "gpl"]

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
        #--------------------------------------------
        #controllo la prima parte
        if len(listaTarga[0]) != 2:
            raise ValueError ("Targa non valida")
        
        for lettera in listaTarga[0]:
            if lettera not in alfabetoM:
                raise ValueError ("Targa non valida")
        #--------------------------------------------
        #controllo la seconda parte
        if len(listaTarga[1]) != 3:
            raise ValueError ("Targa non valida")
        
        for numero in listaTarga[1]:
            if str(numero) not in numeri:
                raise ValueError ("Targa non valida")
        #-------------------------------------------
        #controllo la terza parte    
        if len(listaTarga[2]) != 2:
            raise ValueError ("Targa non valida")
            
        for lettera in listaTarga[2]:
            if lettera not in alfabetoM:
                raise ValueError ("Targa non valida")
        #----------------------------------------------
        self.__targa = targa
        return
    
    #oggetto marca
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca:str):
        if marca.lower() not in listaMarche:
            raise ValueError ("Valore non accettabile")
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
        if colore.lower() not in listaColori:
            raise ValueError("Valore non accettabile")
        self.__colore = colore
        return
    
    @property
    def cilindrata(self):
        return self.__cilindrata
    
    @cilindrata.setter
    def cilindrata(self, cilindrata:int):
        if cilindrata < 0 or cilindrata % 100 != 0:
            raise ValueError("Cilindrata non valida")
        
        self.__cilindrata = cilindrata
        return
    
    @property
    def alimentazione(self):
        return self.__alimentazione
    
    @alimentazione.setter
    def alimentazione(self, alimentazione:str):
        if alimentazione.lower() not in listaAlimentazione:
            raise ValueError("Valore non accettabile")
        
        self.__alimentazione = alimentazione
        return
    
    # Aggiungere un ordinamento implicito fra gli oggetti di tipo Veicolo in modo da renderli ordinabili
    # alfabeticamente per marca, modello e numericamente (dal più piccolo al più grande) per cilindrata.
    def __lt__(self, other):
        """
        determino come ordinare due fattori in base alla marca
        """
        #creo una lista per ordinarli alfabeticamente
        if self.__marca < other.marca:
            return True
        
        #controllo se la marca è uguale
        if self.__marca == other.__marca:
            if self.__modello < other.__modello:
                return True
        
        #controllo la cilindrata a livello numerico
        if self.__modello == other.__modello:
            if self.__cilindrata < other.__cilindrata:
                return True
        
        return False


#------------------------------------------------------------------------------
# TEST
if __name__ == "__main__":
    #veicolo1
    veicolo1 = Veicolo("AB 123 CD")
    print(veicolo1)
    print("Targa:", veicolo1.targa)
    print("Marca:", veicolo1.marca)
    print("Modello:", veicolo1.modello)
    print("Cilindrata:", veicolo1.cilindrata)
    print("Colore:", veicolo1.colore)
    print("Alimentazione:", veicolo1.alimentazione)

    #veicolo2
    veicolo2 = Veicolo("EF 456 GH")
    print(veicolo2)
    print("Targa:", veicolo2.targa)
    veicolo2.marca = "Fiat"
    print("Marca:", veicolo2.marca)
    veicolo2.modello = "Panda"
    print("Modello:", veicolo2.modello)
    veicolo2.cilindrata = 300
    print("Cilindrata:", veicolo2.cilindrata)
    veicolo2.colore = "verde"
    print("Colore:", veicolo2.colore)
    veicolo2.alimentazione = "diesel"
    print("Alimentazione:", veicolo2.alimentazione)

    #provo l'ordinamento
    print(veicolo1 < veicolo2)
    #provo l'ordinamento con marche diverse
    veicolo1.marca = "Fiat"
    print(veicolo1 < veicolo2)


