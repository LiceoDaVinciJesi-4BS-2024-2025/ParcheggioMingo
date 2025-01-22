# Aurora Mingo
# 4BS
# PARCHEGGIO

from veicolo import*
from moto import*
from auto import*
from postomezzo import*
import datetime
import csv

listaMezziParcheggiati = []

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
        return __class__.__name__ + str(listaMezziParcheggiati)
    def __repr__(self):
        return __class__.__name__ + str(listaMezziParcheggiati)
    
    #definizione delle property; so in ogni istante se richiamo la property quanti parcheggi rimangono
    @property
    def parcheggiAuto(self):
        return self.__parcheggiAuto
    
    @property
    def parcheggiMoto(self):
        return self.__parcheggiMoto
    
    @property
    def guadagnoTotale(self):
        return self.__guadagnoTotale
    
    #-----------------------------------------------------------------------------
    #creo la funzione per parcheggiare il veicolo
    def parcheggiaVeicolo(self, tipoVeicolo: str, targa:str, oreSosta: datetime.time):
        """
        permette di parcheggiare un veicolo
        """
        #l'utente si riserva un posto nel parcheggio
        parcheggio = PostoMezzo(tipoVeicolo, targa, oreSosta)
        
        #aggiorno il numero di parcheggi disponibili
        if parcheggio.tipo == "Auto":
            self.__parcheggiAuto -= 1
        else:
            self.__parcheggiMoto -= 1
        
        #creo una lista di mezzi parcheggiati
        listaMezziParcheggiati.append({"tipo":parcheggio.tipo, "targa": parcheggio.targa, "oreSosta": parcheggio.oreSosta})
        
        #calcolo quanti soldi deve l'utente
        oreIntere = parcheggio.oreSosta.hour
        #differenzio tra auto e moto
        if parcheggio.tipo == "Auto":
            tariffa = 1.5
        else:
            tariffa = 1.2
        
        conto = oreIntere * tariffa
        
        #aggiungo i minuti
        minuti = parcheggio.oreSosta.minute
        conto += (tariffa/60)*minuti
        
        #aggiungo il conto al saldo totale
        self.__guadagnoTotale += conto
        
        return conto
    
    #salvo lo stato corrente del parcheggio in un file di testo
    def salvaStatoParcheggio(self):
        """
        permette di salvare lo stato attuale del parcheggio, ovvero i veicoli parcheggiati
        e il totale raggiunto.
        """
        #la lista che utilizzo è quella creata all'inizio dei parcheggi
        campi = ["tipo","targa", "oreSosta"]

        #creo il file di testo
        file = open("park_data.txt", "w", newline="") 
        scrittore = csv.DictWriter(file, campi)
        
        #scrivo le righe da inserire
        for riga in listaMezziParcheggiati:
            scrittore.writerow(riga)
        
        #inserisco il guagano totale
        file.write("Guadagno totale:", str(self.__guadagnoTotale))
        file.close()
#-----------------------------------------------------------------------------------
#TEST
if __name__ == "__main__":
    #creo un parcheggio
    parcheggio1 = Parcheggio()
    print(parcheggio1)
    print()
    
    #macchina 1
    sosta1 = parcheggio1.parcheggiaVeicolo("Auto", "AB 123 CD", datetime.time(1,0,0))
    print("Il saldo è pari a:", sosta1)
    print(parcheggio1)
    print("Saldo totale:", parcheggio1.guadagnoTotale)
    print("Parcheggi auto:", parcheggio1.parcheggiAuto)
    print("Parcheggi moto:", parcheggio1.parcheggiMoto)
    print()
    
    #macchina 2
    sosta2 = parcheggio1.parcheggiaVeicolo("Auto", "EF 456 GH", datetime.time(3,0,0))
    print("Il saldo è pari a:", sosta2)
    print(parcheggio1)
    print("Saldo totale:", parcheggio1.guadagnoTotale)
    print("Parcheggi auto:", parcheggio1.parcheggiAuto)
    print("Parcheggi moto:", parcheggio1.parcheggiMoto)
    print()
    
    #moto 1
    sosta3 = parcheggio1.parcheggiaVeicolo("Moto", "LM 789 PQ", datetime.time(2,0,0))
    print("Il saldo è pari a:", sosta3)
    print(parcheggio1)
    print("Saldo totale:", parcheggio1.guadagnoTotale)
    print("Parcheggi auto:", parcheggio1.parcheggiAuto)
    print("Parcheggi moto:", parcheggio1.parcheggiMoto)

    #provo la scrittura
    parcheggio1.salvaStatoParcheggio()
    
        
    
    
    