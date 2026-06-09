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
# Pythonin tietorakenteita
Tähän mennessä olemme tutustuneet yksinkertaisiin tietotyyppeihin kuten *int*, *float*, *str* ja *bool*. Nämä tietotyypit
ovat yksinkertaisia, koska niihin tallennetaan käytännössä vain yksi arvo, kuten yksi kokonaisluku. Mutta entä jos
haluaisimme säilöä vaikka 1000 kokonaislukua? Emme varmaankaan haluaisi määritellä tuhatta muuttujaa?

Otetaan nyt käyttöön monimutkaisempia tietorakenteita, joiden avulla voi hallita suuria tietomääriä. Pythonissa on useita erilaisia
tietorakenteita eri käyttötarkoituksiin. Tietorakenteet esitellään lyhyesti alla ja niistä kerrotaan enemmän seuraavissa kappaleissa.
## Lista
Lista (engl. *list*) on erittäin joustava tietorakenne. Listat määritellään hakasulkeiden avulla:
``` ipython3
tilavuudet = [10.2, 2.6, 3.55]
```
Listan yksittäistä arvoa kutsutaan listan **alkioksi**. Yllä olevassa listassa on siis kolme alkiota.
## Monikko
Monikko (engl. *tuple*) on kuten lista, mutta sitä ei voi muokata. Monikot määritellään tavallisten sulkeiden avulla:
``` ipython3
jalokaasut = ('He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn')
```
Kuten listojen kohdalla, myös monikon yksittäinen arvo on monikon **alkio**. Yllä olevassa listassa on siis kuusi alkiota.
## Sanakirja
Sanakirja (engl. *dictionary*) koostuu *avain:arvo* -pareista. Avainten tulee olla uniikkeja. Sanakirjat määritellään
kaarisulkeiden avulla:
``` ipython3
atomipainot = {'H':  1.008, 'C': 12.011, 'O': 15.999}
```
Yllä olevassa sanakirjassa on siis kolme *avain:arvo* -paria.
## Joukko
Joukko (engl. *set*) on tietorakenne, jossa kukin arvo voi esiintyä vain kerran. Emme hyödynnä joukkoja tällä kurssilla. 
Joukot määritellään kaarisulkeilla, mutta toisin kuin sanakirjat, joukot koostuvat yksittäisistä arvoista ilman avaimia: 
``` ipython3
metallit = {'Cu', 'Ag', 'Cu', 'Ag'}
```
Yllä olevan määrittelyn jälkeen metallit-joukon sisältö on {'Cu', 'Ag'}, eli vain uniikit arvot on tallennettu joukkoon.
:::::{card} Tehtävä 3.1.1
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mikä tietorakenne on kyseessä?
``` ipython3
suureet = ("paine", "tilavuus", "ainemäärä", "lämpötila")
```
---
[ ] lista
> Yritä uudelleen!
[x] monikko
> Oikein!
[ ] sanakirja
> Yritä uudelleen!
[ ] joukko
> Yritä uudelleen!
---
::::
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mikä tietorakenne on kyseessä?
``` ipython3
tiheydet = {"Cu": 8.96, "Ag": 10.49, "Au": 19.3}
```
---
[ ] lista
> Yritä uudelleen!
[ ] monikko
> Yritä uudelleen!
[x] sanakirja
> Oikein!
[ ] joukko
> Yritä uudelleen!
---
::::
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mikä tietorakenne on kyseessä?
``` ipython3
pH_mittaukset = [1.2, 2.4, 5.7, 11.9, 13.0]
```
---
[x] lista
> Oikein!
[ ] monikko
> Yritä uudelleen!
[ ] sanakirja
> Yritä uudelleen!
[ ] joukko
> Yritä uudelleen!
---
::::
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mikä tietorakenne on kyseessä?
``` ipython3
halogeenit = {"F", "Cl", "Br", "I"}
```
---
[ ] lista
> Yritä uudelleen!
[ ] monikko
> Yritä uudelleen!
[ ] sanakirja
> Yritä uudelleen!
[x] joukko
> Oikein!
---
::::
:::::
