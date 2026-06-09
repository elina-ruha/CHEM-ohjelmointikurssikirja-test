---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# *while*-silmukka
Silmukkarakenteilla voidaan toistaa tietty koodinpätkä useita kertoja. **while**-silmukassa toistojen määrä riippuu totuusehdosta:
```{code-cell} ipython3
:tags: ["auto-execute-page"]
luku = 1
while luku <= 5:
    # Huomaa sisennys: silmukka toistaa sisennettyä osaa!
    print(luku)
    luku += 1
    # luku += 1 tarkoitti samaa kuin luku = luku + 1
    # (ks. luku matemaattiset perusoperaattorit)
```
Toinen esimerkki, jossa ohjelman suoritus jatkuu silmukan jälkeen ensimmäisestä sisentämättömästä lauseesta:
```ipython3
# Alustetaan silmukassa tarvittavat muuttujat
luku = 1.0
lukuja = 0    
while luku > 0.0:
    luku = float(input("Anna luku (negatiivinen luku lopettaa):\n"))
    if luku > 0.0:
        lukuja += 1
# Silmukan päätyttyä suoritus jatkuu tästä
print("Annoit yhteensä", lukuja, "positiivista lukua")
```
Esimerkkisuoritus:
```
Anna luku (negatiivinen luku lopettaa):
> 324235
Anna luku (negatiivinen luku lopettaa):
> 12
Anna luku (negatiivinen luku lopettaa):
> 1
Anna luku (negatiivinen luku lopettaa):
> -1
Annoit yhteensä 3 positiivista lukua
```
:::{admonition} Huom!
:class: note
Jos totuusehto ei täyty 1. kierroksella, *while*-silmukkaa ei suoriteta yhtään kertaa!
:::
## Ikuinen silmukka
*while*-silmukkaa käytettäessä ohjelmointivirhe voi johtaa tilanteeseen, jossa totuusehto ei koskaan muutukaan epätodeksi.
Tyypillisin virhe on unohtaa silmukkalaskurin päivitys:
``` 
luku = 1
while luku <= 5:
    print(luku)
    # Tästä on unohtunut laskurin päivitys
    # luku += 1
    # Seurauksena olisi ikuinen silmukka
```
:::{admonition} Vinkki
:class: tip
Ikuisesta silmukasta pääsee pois painamalla Ctrl+C (ohjelman keskeytys)
:::
## break-käsky ja *while True:* -rakenne
*while*-silmukasta voi poistua milloin tahansa **break**-käskyllä:
``` ipython3
# Luodaan näennäisesti "ikuinen" silmukkaehto (True on aina totta)
while True:
    luku = int(input("Anna kokonaisluku ja tulostan sen. Luvulla 0 lopetan: "))
    if luku == 0:
        print("Loppu")
        # Poistutaan silmukasta break-käskyllä
        break
    else:
        print("Annoit luvun", luku)
```
Esimerkkitulostus:
```
Anna kokonaisluku ja tulostan sen. Luvulla 0 lopetan: > 6
> Annoit luvun 6
Anna kokonaisluku ja tulostan sen. Luvulla 0 lopetan: > 3
> Annoit luvun 3
Anna kokonaisluku ja tulostan sen. Luvulla 0 lopetan: > 0
Loppu
```
## Käyttäjän syötteen testaaminen *while True:* -rakenteella
*while True:* -rakenne on hyvin hyödyllinen esimerkiksi kun ohjelman pitää lukea käyttäjän syötteitä kunnes käyttäjä
antaa kelvollisen syötteen:
``` ipython3
# Pyydetään käyttäjältä ympyrän säde ja lasketaan pinta-ala
while True:
    r = float(input("Anna ympyrän säde:\n"))
    if r > 0:
        # Käyttäjän antama säde on OK, voidaan poistua silmukasta
        break
    else:
        # Käyttäjä antoi virheellisen säteen, tulostetaan ilmoitus ja palataan silmukan alkuun
        print("Virheellinen säde")
        
pinta_ala = 3.14159 * r**2
print("Pinta-ala on", round(pinta_ala, 2))
```
Esimerkkitulostus:
```
Anna ympyrän säde:
> 0
Virheellinen säde
Anna ympyrän säde:
> -1
Virheellinen säde
Anna ympyrän säde:
> 5.8
Pinta-ala on 105.68
```
Toinen esimerkki, jossa pyydetään käyttäjältä kokonaislukuja, kunnes käyttäjä antaa "*" ja sitten ohjelma laskee 
kokonaislukujen tulon:
``` ipython3
# Alustetaan ensin tulo-muuttuja ykköseksi
tulo = 1
while True:
    # Luetaan ensin käyttäjän syöte merkkijonona
    teksti = input("Anna kokonaisluku. * lopettaa.\n")
    if teksti == "*":
        # Käyttäjä antoi tähden, poistutaan silmukasta
        break
    else:
        # Käyttäjä antoi luvun. Muunnetaan merkkijono kokonaisluvuksi
        luku = int(teksti)
        # Kerrotaan tulo uudella luvulla
        tulo = tulo * luku
        # Tästä ohjelma palaa silmukan alkuun
        
print("Lukujen tulo:", tulo)
```
Esimerkkitulostus:
```
Anna kokonaisluku. * lopettaa.
> 3
Anna kokonaisluku. * lopettaa.
> 4
Anna kokonaisluku. * lopettaa.
> 5
Anna kokonaisluku. * lopettaa.
> *
Lukujen tulo: 60
```
### continue- ja else-käskyt
*while*-silmukoissa voi lisäksi hyödyntää **continue**-komentoa (hyppää silmukan alkuun) ja **else-lausetta** (suoritetaan
silmukan päätyttyä). Näitä emme hyödynnä vielä tässä vaiheessa kurssia.
### Tehtävä 1.10.1
Täydennä alla oleva ohjelma niin, että se tekee enintään kymmenen mittausta ja lopettaa arvojen kysymisen, jos mittauksien
summa ylittää 100 g. Tehtävässä käyttäjä antaa jokaisella kerralla massaksi 3.6583 g (joka on tallennettu jo etukäteen 
muuttujaan *massa* input-funktion tilalle).
``` ipython3
mittaukset = 0
summa = 0
TÄYDENNÄ mittaukset < TÄYDENNÄ and summa < TÄYDENNÄ:
    massa = float(input("Anna mitattu massa (g):\n"))
    if massa > 0:
        summa = TÄYDENNÄ + TÄYDENNÄ
        mittaukset += TÄYDENNÄ
    else:
        print("Virheellinen mittaus")
print(summa)
```
```{code-cell} ipython3
mittaukset = 0
summa = 0
TÄYDENNÄ mittaukset < TÄYDENNÄ and summa < TÄYDENNÄ:
    massa = float("3.6583")
    if massa > 0:
        summa = TÄYDENNÄ + TÄYDENNÄ
        mittaukset += TÄYDENNÄ
    else:
        print("Virheellinen mittaus")
print(summa)
```
