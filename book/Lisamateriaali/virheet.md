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
# Virheiden etsiminen ja korjaaminen
Virheiden löytäminen ja käsittely kuuluu jokaisen ohjelmoijan perustaitoihin ja on välttämätöntä suuria ohjelmia
kirjoittaessa. Tällä kurssilla ei luoda ohjelmia, jotka vaativat huomattavaa virheiden käsittelyä tai debuggaamista.
Edettäessä suurempiin ohjelmiin, erityisesti graafisen käyttöliittymän sisältäviin ohjelmiin ja sekä vaativampiin
(”pikkutarkkoihin”) kieliin (C, C++), on virheiden käsittely ja debuggaaminen erittäin oleellista.

Virheen löytäminen alkaa **traceback**-viestistä. Traceback on punainen virheilmoitus, joka kertoo syyn ohjelman kaatumiseen.
Aluksi viesti voi näyttää heprealta, mutta kun sitä oppii lukemaan, se on erittäin hyödyllinen apuväline virheiden löytämisessä.

## Esimerkki 1
Katsotaan ensin yksinkertaista tracebackiä, joka syntyy koodista
```{code-cell} ipython3
:tags: ["auto-execute-page"]
print(x)
```
Traceback on:
``` ipython3
Traceback (most recent call last):
File "C:/Users/Omistaja/Desktop/ErrorExample1.py", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
```
Tracebackin ensimmäinen rivi ilmoittaa meille virheen sijainnin. Tässä tapauksessa virhe tapahtui tiedostossa
*ErrorExample1.py* rivillä 1. Huomaa miten virheviestissä lukee polku, jossa tiedosto sijaitsee, pelkän nimen sijaan.

Seuraava rivi kertoo meille, mitä kyseisellä rivillä lukee. Tässä tapauksessa koodin pätkä, mikä aiheuttaa virheen
on *print(x)*.

Viimeinen rivi tracebackissä kertoo meille mikä virhe on kyseessä. Kyseinen virhe on siis *NameError*, joka johtuu siitä,
että muuttujaa x ei ole määritelty.
## Esimerkki 2
Seuraava esimerkki on hieman monimutkaisempi traceback, joka on syntynyt seuraavasta koodista:
```
def palautaAlkio(lista, alkio):
    return lista[alkio]
lista = [1, 2, 3]
print(palautaAlkio(lista,3))
Selkeyden vuoksi jaotellaan traceback osiin:

Traceback (most recent call last):
File "<ipython-input-38-055a27710ada>", line 1, in <module><
    runfile('C:/Users/User/Desktop/ErrorExample.py', wdir='C:/Users/Sammako/Desktop')
File "C:\Users\User\Anaconda3\lib\site-packages\spyder\utils\site\sitecustomize.py", line 705, in runfile
    execfile(filename, namespace)
File "C:\Users\User\Anaconda3\lib\site-packages\spyder\utils\site\sitecustomize.py", line 102, in execfile
    exec(compile(f.read(), filename, 'exec'), namespace)
Yllä olevat viestit käsittelevät ohjelman kääntämistä, eikä niihin syvennytä tällä kurssilla.

File "C:/Users/User/Desktop/ErrorExample.py", line 5, in <module>
    print(palautaAlkio(lista, 3))
Jälleen kerran tracebackistä selviää ohjelman polku, rivi, sekä rivin sisältö

File "C:/Users/User/Desktop/ErrorExample.py", line 2, in palautaAlkio

    return lista[alkio]
Koska rivi, joka aiheuttaa virheen on funktiokutsu, ilmoittaa traceback vielä erikseen virheen sijaitsevan funktiossa nimeltä palautaAlkio, sekä rivin, jossa virhe sijaitsee sekä, sisällön.

Tässä esimerkissä funktio, jossa virhe on, sijaitsee samassa tiedostossa kuin sen kutsu. Tapauksissa, jossa ohjelma kutsuu useita eri funktiota, useista eri tiedostoista, tämän kaltainen viesti on erittäin hyödyllinen.

IndexError: list index out of range
Virhe on IndexError eli ohjelma yrittää kutsua listan alkiota, jota ei ole olemassa.

On mahdollista, että virhe aiheutuu kirjastossa kuten numpy. Tällöin traceback saattaa ilmoittaa virheen sijaitsevan esim. rivillä 1000, jossain satunnaisessa tiedostossa. Tällöin täytyy etsiä viimeisin rivi tracback:ssä, joka sijaitsee itse luomassasi tiedostossa.
