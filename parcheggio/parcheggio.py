# Aurora Mingo
# 4BS
# PARCHEGGIO

from veicolo import*
from moto import*
from auto import*
from postomezzo import*
import datetime
import csv

#definisco la classe parcheggio
class Parcheggio:
    def __init__(self):
        """
        inizializza il parcheggio e definisce i posti disponibili
        """
        self.__listaParcheggiAuto = []
        self.__listaParcheggiMoto = []
        
        for x in range(1000):
            parcheggio = PostoMezzo("Auto")
            self.__listaParcheggiAuto.append(parcheggio)
        
        for y in range(200):
            parcheggio = PostoMezzo("Moto")
            self.__listaParcheggiMoto.append(parcheggio)
            
        self.__guadagnoTotale = 0
        
    
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
    #definizione delle property; so in ogni istante se richiamo la property quanti parcheggi rimangono
    @property
    def parcheggiAutoLiberi(self):
        contaPosti = 0
        for posto in self.__listaParcheggiAuto:
            if posto.occupato() == False:
                contaPosti += 1
                
        return contaPosti
    
    @property
    def parcheggiMotoLiberi(self):
        contaPosti = 0
        for posto in self.__listaParcheggiMoto:
            if posto.occupato() == False:
                contaPosti += 1
                
        return contaPosti
    
    @property
    def guadagnoTotale(self):
        return self.__guadagnoTotale
    
    #-----------------------------------------------------------------------------
    #creo la funzione per parcheggiare il veicolo
    def parcheggiaVeicolo(self, tipoVeicolo: str, targa:str):
        """
        permette di parcheggiare un veicolo
        """
        #scorro i posti mezzo e ne prendo 1
        if tipoVeicolo == "Auto":
            listaConsiderata = self.__listaParcheggiAuto
        else:
            listaConsiderata = self.__listaParcheggiMoto
            
        for posto in listaConsiderata:
            if posto.occupato() == False:
                #prendo un parcheggio
                postoConsiderato = posto
                break
        
        postoConsiderato.occupaPosto(targa)
        return
    #---------------------------------------------------------------------------
    def liberaPosto(self, tipoVeicolo: str, targa:str):
        """
        permette di liberare il parcheggio
        """
        #prendo la lista considerata
        if tipoVeicolo == "Auto":
            listaConsiderata = self.__listaParcheggiAuto
        else:
            listaConsiderata = self.__listaParcheggiMoto
        
        for posto in listaConsiderata:
            if posto.targa == targa:
                posto.liberaPosto(targa)
                break
        
        #crea il saldo dell''utente
        diff = posto.dataFineParcheggio - posto.dataInizioParcheggio
        secondiTotali = int(diff.total_seconds())  # questo me lo da in secondi
        
        #differenzio tra auto e moto
        if posto.tipo == "Auto":
            tariffa = 1.5
        else:
            tariffa = 1.2
        
        #calcolo i soldi totali
        contoLungo = (tariffa/3600)*secondiTotali
        contoApprossimato = int(contoLungo * 100)
        conto = contoApprossimato / 100
        
        #aggiungo il conto al saldo totale
        self.__guadagnoTotale += conto
        return conto
    
    #salvo lo stato corrente del parcheggio in un file di testo
    def salvaStatoParcheggio(self):
        """
        permette di salvare lo stato attuale del parcheggio, ovvero i veicoli parcheggiati
        e il totale raggiunto.
        """
        #creo la lista dei dati
        dati = []
        for posto in self.__listaParcheggiAuto:
            if posto.occupato() == True:
                dati.append({"tipo":posto.tipo,"targa":posto.targa,"dataInizioParcheggio":posto.dataInizioParcheggio, "dataFineParcheggio":posto.dataFineParcheggio})
                
        #la lista che utilizzo è quella creata all'inizio dei parcheggi
        campi = ["tipo","targa", "dataInizioParcheggio","dataFineParcheggio"]

        #creo il file di testo
        file = open("park.data", "w", newline="") 
        scrittore = csv.DictWriter(file, campi)
        
        #scrivo le righe da inserire
        for riga in dati:
            scrittore.writerow(riga)
        
        #inserisco il guagano totale
        file.write(f"Guadagno totale: {str(self.__guadagnoTotale)}")
        file.close()
#-----------------------------------------------------------------------------------
#TEST
if __name__ == "__main__":
    #creo un parcheggio
    parcheggio1 = Parcheggio()
    print(parcheggio1)
    print()
    
    #macchina 1
    parcheggio1.parcheggiaVeicolo("Auto", "AB 123 CD")
    print("Parcheggi auto:", parcheggio1.parcheggiAutoLiberi)
    print("Parcheggi moto:", parcheggio1.parcheggiMotoLiberi)
    sosta1 = parcheggio1.liberaPosto("Auto", "AB 123 CD")
    print("Il saldo è pari a:", sosta1)
    print(parcheggio1)
    print("Saldo totale:", parcheggio1.guadagnoTotale)
    print()
    
    #macchina 2
    parcheggio1.parcheggiaVeicolo("Auto", "EF 456 GH")
    print("Parcheggi auto:", parcheggio1.parcheggiAutoLiberi)
    print("Parcheggi moto:", parcheggio1.parcheggiMotoLiberi)
    sosta2 = parcheggio1.liberaPosto("Auto", "EF 456 GH")
    print("Il saldo è pari a:", sosta2)
    print(parcheggio1)
    print("Saldo totale:", parcheggio1.guadagnoTotale)
    print()
    
    #moto 1
    parcheggio1.parcheggiaVeicolo("Moto", "LM 789 PQ")
    print("Parcheggi auto:", parcheggio1.parcheggiAutoLiberi)
    print("Parcheggi moto:", parcheggio1.parcheggiMotoLiberi)
    sosta3 = parcheggio1.liberaPosto("Moto", "LM 789 PQ")
    print("Il saldo è pari a:", sosta3)
    print(parcheggio1)
    print("Saldo totale:", parcheggio1.guadagnoTotale)

    #provo la scrittura
    parcheggio1.salvaStatoParcheggio()
    
        
    
    
    