---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.3
kernelspec:
  display_name: base
  language: python
  name: python3
---

# Kierros 1
Kurssin ensimmäisellä kierroksella tutustutaan ohjelmoinnin peruskäsitteisiin ja Python-ohjelmointikielen perusteisiin.
## 1. Spyder-ohjelmointiympäristön asentaminen
<p> Ohjelmointitehtävien tekemiseksi tarvitset esimerkiksi Spyder-ohjelmointiympäristön,
joka sisältää myös Python-kehitysympäristön. Oppimateriaalin Lisämateriaalia-luku
  sisältää Spyderin asennusohjeen ja Spyderin käyttöohjeita. </p>

## 2. Oppimateriaalin lukuohje
Kun oppimateriaalissa esitetään Python-koodia, se näyttää tältä:
```ipython3
print("Nyt lasketaan!")
print("11*11 on", 11*11)
```
Kun oppimateriaalissa näytetään, mitä Python-koodi tulostaa, sen voi kokeilla itse valitsemalla oppimateriaalin oikeasta yläkulmasta raketti-symbolija painamalla `Live Code` . Tällöin koodin voi "ajaa" painamalla koodilaatikon alareunasta `run` .Koodia voi myös editoida suoraan koodilaatikkossa tai lisätä uuden tyhjän koodilaatikon alle `add cell` -painikkeesta.
  
```{code-cell} ipython3
print("Nyt lasketaan!")
print("11*11 on", 11*11)
```

## 3. Oppimateriaalin esimerkkiohjelmien kokeileminen itse
- Kopioi esimerkkiohjelman koodi Spyder-editoriin.
- Aja koodi painamalla Spyderissä vihreää "Run"-painiketta tai F5-nappia.

````{admonition} Vinkki
:class: tip
Esimerkkiohjelmien **kokeileminen ja muokkaaminen on erittäin suositeltavaa**, koska se helpottaa merkittävästi esimerkkien ymmärtämistä.
````

## 4. Ohjelmakoodin kommentointi
Ohjelmien huolellinen kommentointi on ensiarvoisen tärkeää, jotta:
- Muut ymmärtävät, mitä kirjoittamasi koodi tekee
- Muistat itse, mitä kirjoittamasi koodi tekee!

Ohjelmakoodiin voi lisätä kommentteja #-merkin jälkeen:
```{code-cell} ipython3
#Aloitetaan!
print("Eka ohjelmani")
#Jatketaan!
print("Moi!") #Rivin loppuun voi myös lisätä kommentteja
```
Kokeile tulostaa ylläoleva koodi. Huomaa, että kommentit eivät tulostuneet.

Monirivisiä kommentteja voi kirjoittaa """"*kommentti*"""" -merkinnällä:
```{code-cell} ipython3
print("Eka ohjelmani")
"""
Olipa hieno kokemus!
Tämä on kolmerivinen välikommentti.
Sitten jatketaan!
"""
print("Moi!")
```
## 5. Muita Python-oppimateriaaleja
<p> Lisämateriaalin Python-verkkomateriaaleja -kappaleessa (linkki) on listattu 
  hyviä verkosta löytyviä oppimateriaaleja, joita voi myös hyödyntää Python-ohjelmoinnin opettelussa.
  Jos pidät opiskelusta videomateriaalien avulla, sivulta löytyy linkkejä videomuotoisiin oppimateriaaleihin. </p>

## 6. Jos olet aiemmin osallistunut kurssille *Ohjelmoinnin peruskurssi Y1*
<p> Jos olet aiemmin osallistunut Aallon yleiselle Python-kurssille, 
  tutustuthan lisämateriaalin kappaleeseen main-funktio (hyperlink) ennen kuin 
  aloitat tämän kurssin tehtävien tekemisen. </p>

## 7. Oppimateriaalin sisältämät tehtävät
Oppimateriaali sisältää myös erilaisia tehtäviä, joilla voit tarkistaa, kuinka hyvin olet sisäistänyt oppimateriaalissa käsitellyt asiat.

Oppaassa olevien tehtävien tarkoitus on tukea oppimista, ne eivät vaikuta kurssin arvosteluun!

Alla on kaksi esimerkkiä oppimateriaalin tehtävätyypeistä.

:::::{card} Tehtävä 1.0.1

::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

Mitä ohjelmointikieltä tällä kurssilla opetellaan?
---
[ ] Perl
[x] Python
> Oikein!
[ ] INTERCAL
[ ] Cobra
---

::::

::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

Minkä perusteella kurssin arvosana määräytyy?
---
[ ] Läsnäolon
[ ] Kysymysten esittämisen
[x] MyCourses-tehtävien pisteiden
> Oikein!
---

::::

:::::

:::::{card} Tehtävä 1.0.2

::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

Täydennä koodi niin, että ohjelma tulostaa:\
*Yksi*\
*Kaksi*\
*Kolme*\
print("Yksi")\
_____("Kaksi")\
pint("Kolme")
---
[ ] input
[x] print
> Oikein!
[ ] float
---

::::

:::::
