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

# Kierros 5
## Tiedostojen käsittely
Viidennellä kierroksella tutustumme tiedostojen käyttöön Pythonissa. Tietojen lukeminen tiedostosta ja kirjoittaminen
tiedostoon on aivan keskeinen tehtävä ohjelmoinnissa.
## Huomioitavaa tiedostojen hallinnasta
- Kierroksen 5 tehtäviä tehdessäsi sinulla olisi hyvä olla jonkinlainen kokonaiskuva tiedostojen hallinnasta
   käyttämässäsi käyttöjärjestelmässä (Windows, MacOS tai Linux).
- Kun kirjoitat ohjelmakoodin, joka luo uuden tiedoston, ohjelmasi luo tiedoston oletuksena samaan hakemistoon,
  missä ohjelman .py-tiedosto sijaitsee.
- Luomme kurssilla pääasiassa tekstitiedostoja. Voit tarkastella luomasi tiedoston sisältöä yksinkertaisesti avaamalla
 tekstitiedoston mihin tahansa tekstieditoriin (onnistuu yleensä kaksoisklikkaamalla tiedostoa). Voit avata tiedoston myös
 Spyderiin.
- Kun tehtävässä pitää luoda tekstitiedosto, kannattaa aina tarkistaa luomasi tiedoston sisältö tekstieditorilla!
- Kun tehtävässä pitää lukea olemassaolevan tekstitiedoston sisältö, kannattaa aina ensin tarkastella tiedostoa tekstieditorissa,
   jotta hahmotat paremmin, mitä tiedoston lukeminen vaatii ohjelmakoodiltasi.
## Virheenkäsittely
Kierroksen aiheisiin kuuluu myös virheenkäsittely. Ohjelmien suorituksessa tulee usein vastaan virhetilanteita, joista 
pitäisi selvitä kunnialla (käyttäjä antaa luvun sijasta merkkijonon, avattava datatiedosto onkin tyhjä, jne...).
Opettelemme käyttämään try-except-finally -rakenteita virheenkäsittelyyn.

:::::{card} Tehtävä 5.0.1
Tästä alkaa kierros 5. Sitä ennen kierroksen 4 pikakertaus.
::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

Funktio, jolla luodaan liukulukuja sisältävä NumPy-taulukko?
---
[x] linspace
> Oikein!
[ ] arange
> Yritä uudelleen!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

Millä funktiolla voit luoda nollilla alustetun NumPy-taulukon?
---
[ ] poly1d
> Yritä uudelleen!
[x] zeros
> Oikein!
[ ] arange
> Yritä uudelleen!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

Sinulla on kaksi yhtä pitkää NumPy-taulukkoa, haluat jakaa taulukon 1, taulukon 2 arvoilla. Voit suorittaa sen näin: taulukko1 / taulukko2?
---
[x] Totta
> Yritä uudelleen!
[ ] Tarua
> Oikein!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

Millä funktiolla voit luoda kuvaajan?
---
[ ] plt.show
> Yritä uudelleen!
[ ] plt.linspace
> Yritä uudelleen!
[x] plt.plot
> Oikein!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

Millä funktiolla voit luoda polynomin?
---
[ ] np.polyfit
> Yritä uudelleen!
[x] np.poly1d
> Oikein!
[ ] pol.deriv
> Yritä uudelleen!
---
::::
:::::
