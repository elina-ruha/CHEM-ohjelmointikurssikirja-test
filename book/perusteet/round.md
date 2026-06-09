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
# Lukuarvojen pyöristäminen (round)
Edellisessä luvussa opeteltiin lukemaan lukuarvoja *input*-funktiolla:
``` ipython3
luku = float(input("Anna luku niin kerron sen numerolla 2.6\n"))
print("Antamasi luku", luku, "kerrottuna numerolla 2.6 on", 2.6 * luku)
```
Tarkastellaan, mitä tämä koodi tulostaa, kun annamme syötteeksi liukuluvun 3.0:
```
Anna luku niin kerron sen numerolla 2.6
> 3.0
Antamasi luku 3.0 kerrottuna numerolla 2.6 on 7.800000000000001
```
:::{admonition} Miksi koodi tulostaa 7.800000000000001 eikä 7.8?
:class: note dropdown
Tämä johtuu tavasta, jolla tietokoneet käsittelevät liukulukuja (lisätietoa aiheesta kiinnostuneille
[Python-tutoriaalissa](https://docs.python.org/3/tutorial/floatingpoint.html)). Luonnollisesti meille riittäisi tässä
tapauksessa yhden desimaalin tarkkuus.
:::
Tutustutaan seuraavaksi pyöristysfunktioon *round*.
## *round*-funktio
Kokonaisluvun (int) muuntaminen liukuluvuksi (float) on yksinkertaista. Muunnetaan kokonaisluku 5 liukuluvuksi ja tulostetaan se:
```{code-cell} ipython3
:tags: ["auto-execute-page"]
print(float(5))
```
Mutta liukulukujen muuntamisessa kokonaisluvuiksi tulee olla tarkkana:
```{code-cell} ipython3
print(int(5.1))
print(int(5.9))
```
Liukuluvun suora muunnos *int*-funktiolla siis katkaisee liukuluvun desimaalipisteen kohdalta. Liukuluvun voi pyöristää
lähimpään kokonaislukuun [*round*](https://docs.python.org/3/library/functions.html#round)-funktiolla:
```{code-cell} ipython3
print(round(5.1))
print(round(5.9))
```
Liukulukuja voi myös pyöristää haluttuun tarkkuuteen. *round*-funktion toinen parametri kertoo käytettävien desimaalien määrän:
```{code-cell} ipython3
print(round(5.666, 1))
print(round(5.666, 2))
```
*round*-funktiota voi siis hyödyntää, kun ilmoitamme liukulukulaskujen tuloksia käyttäjälle. Kierroksen 2 materiaalissa
tutustumme muotoiltujen merkkijonojen tulostamiseen f-merkkijonoilla tai *str.format*-funktiolla. Niiden avulla
liukulukujen pyöristäminen tulostamista varten on hyvin helppoa.
:::{admonition} Huom!
:class: caution
Älä koskaan pyöristä liukulukuja laskutoimitusten aikana! Liukuluvuilla työskennellään aina mahdollisimman suurella
tarkkuudella ja ainoastaan käyttäjälle ilmoitettava luku pyöristetään johonkin ihmissilmälle sopivampaan tarkkuuteen. 
Ilmoitustarkkuuteen pätevät tässä samat säännöt kuin normaalistikin, eli tuloksen ilmoitustarkkuus riippuu esim. lähtöarvojen tarkkuudesta.
:::
## Lisätietoa: Kokonaislukujen pyöristäminen *round*-funktiolla
*round*-funktiolla on myös vähemmän tunnettu ominaisuus, jonka avulla voi helposti pyöristää lukuja haluttuun ilmoitustarkkuuteen
myös desimaalipisteen vasemmalta puolen. Tätä ominaisuutta tarvitaan usein luonnontieteissä, kun mittaustarkkuus rajoittaa
vastauksen tarkkuutta. Tällöin funktion toinen parametri annetaan negatiivisena:
```{code-cell} ipython3
print(round(5624, -3)) # tarkkuus: 10^3
print(round(5624, -2)) # tarkkuus: 10^2
print(round(5624, -1)) # tarkkuus: 10^1
```
:::{admonition} Vinkki
:class: tip
Tässä esimerkissä pyöristettiin siis kokonaislukuja haluttuun tarkkuuteen. Eli *round*-funktion toinen parametri *ndigits*
tarkoittaa sekä positiivisten että negatiivisten lukujen kohdalla "pyöristä tarkkuuteen 10{sup}`-ndigits`".
:::

:::::{card} Tehtävä 1.5.1
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mitä tämä ohjelma tulostaa?
``` ipython3
print(round(3.14159, 2))
```
---
[x] 3.14
> Oikein!
[ ] 3.14159
> Yritä uudelleen!
[ ] 3.1
> Yritä uudelleen!
[ ] pii
> Yritä uudelleen!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mitä tämä ohjelma tulostaa?
``` ipython3
paine = 0.9998 # bar
print("Paine on:", round(paine, 1), "bar")
```
---
[ ] Paine on: 0.9 bar
> Yritä uudelleen!
[ ] Paine on: 1.00 bar
> Yritä uudelleen!
[x] Paine on: 1.0 bar
> Oikein!
[ ] 1.0
> Yritä uudelleen!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mitä tämä ohjelma tulostaa?
``` ipython3
tilavuus = int(22.9)
print(round(tilavuus, 1))
```
---
[ ] 23.0
> Yritä uudelleen!
[x] 22
> Oikein!
[ ] 22.0
> Yritä uudelleen!
[ ] 23
> Yritä uudelleen!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mitä tämä ohjelma tulostaa?
``` ipython3
print(round(32564, -2))
```
---
[ ] 32564
> Yritä uudelleen!
[ ] 32560
> Yritä uudelleen!
[x] 32600
> Oikein!
[ ] 33000
> Yritä uudelleen!
---
::::
:::::
