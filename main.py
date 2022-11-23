# Ez a főprogram , a programunk mindenkori belépési pontja
# Innen hívhatjuk az általunk megírt függvényeket

import valtozok
import elagazasok
import ciklusok
import lista

# ------------------------ VÁLTOZÓK -----------------------------
# kiírás
valtozok.kiiras()

# változók használata, adattípusok
valtozok.kiiras_nev()

# műveletek szövegekkel
valtozok.muveletek_szovegekkel()
valtozok.muveletekszovegekkel2()

# műveletek számokkal
valtozok.muveletek_szamokkal()

# adatbekérés
valtozok.adatbekeres()

# -------------------------ELÁGAZÁSOK --------------------------------------

# elágazások
elagazasok.egyszeru_elagazas()
# többszörös elágazások
elagazasok.tobbszoros_elagazas_paritas()
elagazasok.tobbszoros_elagazas_osztalyzat()

# feltételek, OR, AND, Logikai műveletek
elagazasok.feltetelek_and()
elagazasok.feltetelek_or()

# egymásba ágyazott elágazások
elagazasok.egymasbaagyazott()

# KOMPLEX FELADAT
elagazasok.pizza()
elagazasok.pizza2()
"""Készíts Pizza rendelő alkalmazást:
A program kérje be, hogy sajtos, gombás, vagy sonkás pizzát kér-e? 
Kérje be a pizza méretét: 
    kicsi   - az ára az ár 90%-a  
    normál  - az ára az ár 100%-a
    nagy    – az ára az ár 110%-a 
    
Kérje be, hogy feltét kell-e? 

1.	Normál sajtos pizza alapára 1000 Ft
2.	Normál gombás pizza alapára 1100Ft
3.	Normál sonkás pizza alapára 1200 Ft

Az extra feltét plusz 50 Ft-ba kerül. """


# ------------------------------------ CIKLUSOK -----------------------------------

# ciklusok - while ciklus - számlálós ciklus
ciklusok.szamlalos()
# elöltesztelős ciklus - while - ellenőrzött adatbekérés
ciklusok.ellenorzott_adatbekeres()
ciklusok.adatbekeres()

# programozási tételek - számokon
ciklusok.megszamlalas()
ciklusok.osszegzes()
ciklusok.maximumkivalasztas()

ciklusok.eldontes()


# egymásba ágyazott ciklusok
ciklusok.szorzotabla()


# ------------------------------------ LISTÁK ---------------------------------
# listák

# listák bejárása
lista.listabejaras()
lista.lottoszamok()

# programozási tételek listákon
lista.megszamlalas()
lista.osszegzes()
lista.maximumkivalasztas()
lista.eldontes()
lista.nyert_e_lotto()
# egymásba ágyazott ciklussal két lista
lista.hanytalalat_lotto()

lista.megszamlalas_szoveg()
lista.abetuk_szama()
lista.osszegzes_szoveg()
lista.maximumkivalasztas_szoveg()


#################################################################################################
# egymásba ágyazott listák

#################################################################################################
# fájlbeolvasás

#################################################################################################
# osztályok használata
