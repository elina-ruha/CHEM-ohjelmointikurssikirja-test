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
# Muotoiltu tulostaminen f-merkkijonoilla tai *str.format*-funktiolla
Tähän asti olemme käyttäneet *print*-funktiota tulostamiseen varsin suoraviivaisesti:
```{code-cell} ipython3
:tags: ["auto-execute-page"]
alkuaine = "C"
atomipaino = 12.011
print("Alkuaineen", alkuaine, "atomipaino on", atomipaino)
```
## f-merkkijonot
Pythonissa on myös edistyneempiä tapoja tulostaa muotoiltuja merkkijonoja. Pythonin versiosta 3.6 lähtien on ollut
mahdollista hyödyntää ns. [f-merkkijonoja](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) 
(engl. *f-strings*), joilla muuttujien arvojen sijoittaminen merkkijonoihin on erittäin helppoa:
```{code-cell} ipython3
alkuaine = "C"
atomipaino = 12.011
# Huomaa, miten print-lausekkeen sisällä oleva merkkijono alkaa f-kirjaimella ennen lainausmerkkiä
print(f"Alkuaineen {alkuaine} atomipaino on {atomipaino}")
```
f-merkkijonoja käytettäessä muuttujat voidaan siis upottaa merkkijonon sisään {muuttuja}-merkinnällä. 
## *str.format*-funktio
Ennen f-merkkijonoja muotoiltuun tulostamiseen käytettiin *str.format*-funktiota:
```{code-cell} ipython3
alkuaine = "C"
atomipaino = 12.011
print("Alkuaineen {} atomipaino on {}".format(alkuaine, atomipaino))
```
Merkkijonon "Alkuaineen {} atomipaino on {}" kaarisulut korvautuivat siis *format*-funktion parametreilla *alkuaine* ja
*atomipaino*. On makuasia, käyttääkö f-merkkijonoja vai *str.format*-funktiota. f-merkkijonoilla koodista tulee yleensä
selkeämpää ja tämän kurssin oppimateriaaleissa käytetään pääasiassa f-merkkijonoja.
## {}-kentän muotoilu
f-merkkijonojen {muuttuja}-kenttää voi muotoilla lukuisilla eri tavoilla. Sen tyypillisin käyttötapa on 
{**muuttuja:<leveys>.<tarkkuus><tyyppi>**}. 

Kentän tyyppiä merkitään kirjaimella. Tällä kurssilla tärkeimpiä kentän tyyppejä ovat
- liukuluku **f**
- kokonaisluku **d**
- merkkijono **s**

Esimerkkejä:
- liukuluku pyöristettynä kolmen desimaalin tarkkuuteen, automaattinen kentän leveys: **{muuttuja:.3f}**
- liukuluku, 6 merkkiä leveä kenttä, pyöristettynä nollan desimaalin tarkkuuteen: **{muuttuja:6.0f}**
- kokonaisluku, automaattinen kentän leveys: **{muuttuja:d}**
- kokonaisluku, 5 merkkiä leveä kenttä: **{muuttuja:5d}**
- merkkijono, automaattinen kentän leveys **{muuttuja:s}**

### Esimerkki 1
```{code-cell} ipython3
T = 300 # K
p = 1.12345 # atm
print(f"Olosuhteet ovat: {T:d} K, {p:.3f} atm")
```
### Esimerkki 2
```{code-cell} ipython3
n = 0.25          # mol
V = 0.00456       # m^3
T = 298.15        # K
R = 8.314462618   # J/(mol K)
p = n * R * T / V # Pa
# Tulostaa seitsemän merkkiä leveitä kenttiä
print(f"Kun n = {n:7.3f} mol, V = {V:7.5f} m^3, T = {T:7.2f} K, on paine p = {p:7.0f} Pa")
```
Vaikka f-merkkijonojen muotoilukenttien kokoaminen voi ensi alkuun vaikuttaa työläältä, on se todella paljon kätevämpää
kuin monimutkaisten tulostusten hoitaminen *print*- ja *round*-funktioiden avulla.

**Käytä lukuarvojen tulostamiseen tästä lähtien f-merkkijonoja.**

f-merkkijonojen laajempi dokumentaatio löytyy osoitteista 
<https://docs.python.org/3/reference/lexical_analysis.html#f-strings> ja 
<https://docs.python.org/3/library/string.html#format-specification-mini-language>.

:::::{card} Tehtävä 2.3.1
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mitä ohjelma tulostaa?
``` ipython3
luku = 15.2355
print(f"{luku:.1f}")
```
---
[ ] 15
> Yritä uudelleen!
[ ] 15.0
> Yritä uudelleen!
[x] 15.2
> Oikein!
[ ] 15.2355
> Yritä uudelleen!
---
::::
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mitä ohjelma tulostaa?
``` ipython3
luku = 32
print(f"{luku:d}")
```
---
[ ] {:32}
> Yritä uudelleen!
[x] 32
> Oikein!
[ ] 32.0
> Yritä uudelleen!
[ ] :32
> Yritä uudelleen!
---
::::
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mitä ohjelma tulostaa?
``` ipython3
p = 99765.1
T = 300
print(f"{p:.0f} Pa, {T:.2f} K")
```
---
[ ] 99765 Pa, 300 K
> Yritä uudelleen!
[ ] 99765.0 Pa, 300.00 K
> Yritä uudelleen!
[ ] 99765.0 Pa, 300.0 K
> Yritä uudelleen!
[x] 99765 Pa, 300.00 K
> Oikein!
---
::::
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mitä ohjelma tulostaa?
``` ipython3
V = 1 / 3
print(f"{V:4.5f}")
```
---
[ ] 0.33
> Yritä uudelleen!
[ ] 0
> Yritä uudelleen!
[x] 0.33333
> Oikein!
[ ] 1/3
> Yritä uudelleen!
---
::::
:::::
