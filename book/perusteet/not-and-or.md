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
# Loogiset operaattorit
Loogiset operaattorit toimivat yhdessä totuusmuuttujien kanssa.
## not-operaattori
**not**-operaattorilla voi kääntää totuusmuuttujan arvon tai ehtolauseen ehdon päinvastaiseksi:
``` ipython3
if not ylipaine:
    print("Ei vaaraa ylipaineesta")
```
Toinen esimerkki:
``` ipython3
alkuaine = input("Anna suosikkialkuaineesi symboli\n")
if not (alkuaine == "Au"):
    print("Et taida olla alkemisti")
```
Jos käyttäjä antaa suosikkialkuaineekseen raudan eli Fe, ohjelma tulostaa näin:
```{code-cell} ipython3
:tags: ["auto-execute-page"]
alkuaine = "Fe"
if not (alkuaine == "Au"):
    print("Et taida olla alkemisti")
```
## and-operaattori
**and**-operaattorilla voi yhdistää kaksi totuusmuuttujaa (tai ehtolauseen ehtoa). and-lauseen arvo on True, jos
molempien ehtojen arvo on True:
``` ipython3
if alkuaine1 == "Cu" and alkuaine2 == "O":
    print("Kuparioksidi")
```
``` ipython3
if ylipaine and T > 410.0:
    print("Kriittiset olosuhteet!")
```
## or-operaattori
**or**-operaattorilla voi myös yhdistää kaksi totuusmuuttujaa (tai ehtolauseen ehtoa). or-lauseen arvo on True, jos
jommankumman ehdon arvo on True:
``` ipython3
if kaasu == "He" or kaasu == "Ne":
    print("Jalokaasu")
```
``` ipython3
if T < 200.0 or T > 300.0:
    print("Lämpötila ei ole optimaalinen reaktion kannalta")
```
Ehtoja voi myös "ketjuttaa" useammalla or-lauseella:
``` ipython3
if kaasu == "He" or kaasu == "Ne" or kaasu == "Ar":
    print("Jalokaasu")
```
## Loogisten ehtojen ryhmittely
Monimutkaisemmat ehdot on parasta ryhmitellä sulkujen avulla:
``` ipython3
if massa > 200.0 or (tiheys > 22.59 and tilavuus > 10.0):
    print("Kappale on liian painava")
```
## Syventävää tietoa: Lyhennetty tapa kirjoittaa vertailuja:
Pythonissa voi myös yhdistää eri muuttujien vertailuja tavalla, joka on tuttu matematiikasta. Vertailulauseke
``` ipython3
if 10 < luku and luku < 1000:
```
on mahdollista kirjoittaa myös lyhennetyssä muodossa:
``` ipython3
if 10 < luku < 1000:
```
:::{admonition} Vinkki
:class: tip
Jälkimmäinen versio siis "piilottaa" **and**-operaattorin. Lisätietoja aiheesta 
[Pythonin virallisesta dokumentaatiossa](https://docs.python.org/3/reference/expressions.html#comparisons).
:::
:::::{card} Tehtävä 1.8.1
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mikä on muuttujan *prosessi* arvo, kun muuttujan *T* arvo on 50 ja muuttujan *p* arvo on 2.5?
``` ipython3
if T >= 200 and p < 3.0:
    prosessi = 1
elif T < 100 or p < 1.0:
    prosessi = 2
else:
    prosessi = 3
```
---
[ ] 1
> Yritä uudelleen!
[x] 2
> Oikein!
[ ] 3
> Yritä uudelleen!
---
::::
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mikä operaattori ehtolauseen AAA-kohtaan pitää laittaa, jotta ohjelma tulostaisi "Perovskiittirakenne"?
``` ipython3
alkuaine1 = "Ti"
alkuaine2 = "O"
alkuaine3 = "Sr"
if alkuaine1 == "Ti" and alkuaine2 == "O" and (alkuaine3 == "Sr" AAA alkuaine3 == "Ba"):
    print("Perovskiittirakenne")
```
---
[x] or
> Oikein!
[ ] not
> Yritä uudelleen!
[ ] and
> Yritä uudelleen!
---
::::
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mikä on muuttujan *varoitus* arvo koodin lopussa?
``` ipython3
paine = 6.0
if paine > 3.0:
    ylipaine = True
else:
    ylipaine = False

if not ylipaine:
    varoitus = False
else:
    varoitus = True
```
---
[x] True
> Oikein!
[ ] False
> Yritä uudelleen!
[ ] Ei True eikä False
> Yritä uudelleen!
---
::::
:::::
