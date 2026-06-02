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
``` ipython3
print(x)
```
Traceback on:
``` ipython3
Traceback (most recent call last):
File "C:/Users/Omistaja/Desktop/ErrorExample1.py", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
```
<p> Tracebackin ensimmäinen rivi ilmoittaa meille virheen sijainnin. Tässä tapauksessa virhe tapahtui tiedostossa
ErrorExample1.py rivillä 1. Huomaa miten virheviestissä lukee polku, jossa tiedosto sijaitsee, pelkän nimen sijaan. </p>

Seuraava rivi kertoo meille, mitä kyseisellä rivillä lukee. Tässä tapauksessa koodin pätkä, mikä aiheuttaa virheen
on *print(x)*.

Viimeinen rivi tracebackissä kertoo meille mikä virhe on kyseessä. Kyseinen virhe on siis *NameError*, joka johtuu siitä,
että muuttujaa x ei ole määritelty.
## Esimerkki 2
Seuraava esimerkki on hieman monimutkaisempi traceback, joka on syntynyt seuraavasta koodista:
``` ipython3
def palautaAlkio(lista, alkio):
    return lista[alkio]
lista = [1, 2, 3]
print(palautaAlkio(lista,3))
```
Selkeyden vuoksi jaotellaan traceback osiin:
``` ipython3
Traceback (most recent call last):
File "<ipython-input-38-055a27710ada>", line 1, in <module><
    runfile('C:/Users/User/Desktop/ErrorExample.py', wdir='C:/Users/Sammako/Desktop')
File "C:\Users\User\Anaconda3\lib\site-packages\spyder\utils\site\sitecustomize.py", line 705, in runfile
    execfile(filename, namespace)
File "C:\Users\User\Anaconda3\lib\site-packages\spyder\utils\site\sitecustomize.py", line 102, in execfile
    exec(compile(f.read(), filename, 'exec'), namespace)
```
Yllä olevat viestit käsittelevät ohjelman kääntämistä, eikä niihin syvennytä tällä kurssilla.
``` ipython3
File "C:/Users/User/Desktop/ErrorExample.py", line 5, in <module>
    print(palautaAlkio(lista, 3))
```
Jälleen kerran tracebackistä selviää ohjelman polku, rivi, sekä rivin sisältö
``` ipython3
File "C:/Users/User/Desktop/ErrorExample.py", line 2, in palautaAlkio
    return lista[alkio]
```
Koska rivi, joka aiheuttaa virheen on funktiokutsu, ilmoittaa traceback vielä erikseen virheen sijaitsevan funktiossa
nimeltä *palautaAlkio*, sekä rivin, jossa virhe sijaitsee sekä, sisällön.

Tässä esimerkissä funktio, jossa virhe on, sijaitsee samassa tiedostossa kuin sen kutsu. Tapauksissa, jossa ohjelma kutsuu
useita eri funktiota, useista eri tiedostoista, tämän kaltainen viesti on erittäin hyödyllinen.
``` ipython3
IndexError: list index out of range
```
Virhe on *IndexError* eli ohjelma yrittää kutsua listan alkiota, jota ei ole olemassa.
:::{admonition} Huom!
:class: note
On mahdollista, että virhe aiheutuu kirjastossa kuten *numpy*. Tällöin traceback saattaa ilmoittaa virheen sijaitsevan 
esim. rivillä 1000, jossain satunnaisessa tiedostossa. Tällöin täytyy etsiä viimeisin rivi tracback:ssä, joka sijaitsee
itse luomassasi tiedostossa.
:::
## Esimerkki 3
Tracebackistä ei kuitenkaan aina ole apua. Otetaan esimerkiksi koodi
``` ipython3
def kerro_kymmenella(numero):
    return numero * 0
numero = 5
jako = 1 / kerro_kymmenella(numero)
print(jako)
```
Käyttäjä on luonut funktion, jonka pitäisi kertoa numero kymmenellä, mutta teki kirjoitusvirheen, minkä seurauksesta 
funktio palauttaa aina nollan. Kun tarkastelemme saatua tracebackiä, huomaamme ongelman olevan rivillä 6, sekä ongelman 
johtuvan nollalla jakamisesta.

Koska tehty virhe ei suoranaisesti aiheuta virhettä, vaan antaa väärän tuloksen, joka myöhemmin aiheuttaa virheen, ei
traceback ole yhtä hyödyllinen tässä tilanteessa. On myös tilanteita, kuten graafiset käyttöliittymät, jotka eivät aina 
kaatuessaan luo tracebackiä. Miten siis löytää virhe, kun sen sijaintia ei tiedetä?
## Virheen löytäminen
*print*-funktiot ovat yksinkertainen tapa löytää mahdollisia virheitä koodista. Alla oleva koodi kaatuu, mutta koska virhe 
on ikuinen silmukka ei traceback-viestiä synny.
```{code-cell} ipython3
numero = 5
kertoma = 1
print("testi")
while numero > 1:
    kertoma *= numero
print("testi")
```
Kun koodi ajetaan *print*-funktioiden kanssa, huomataan ensimmäisen tulostuvan, mutta toisen ei. Tästä on helppo päätellä, 
että virhe on *while*-silmukassa. Kun virheen sijainti tiedetään, on helppo huomata virheen johtuvan siitä, että muuttujan 
numero arvoa ei vähennetä silmukassa.
:::{admonition} Vinkki
:class: tip
Virheiden käsittelystä kerrotaan lisää muualla [oppimateriaalissa](../Kierros5/s5_4.md).
:::
