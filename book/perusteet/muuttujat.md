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
# Muuttujat
Ohjelmoidessa tallennamme tietoa *muuttujiin* (engl. *variable*). Esimerkiksi *input*-funktio tallentaa tässä esimerkissä
käyttäjän syötteen merkkijonona muuttujaan, jonka nimi on etunimi:
``` ipython3
etunimi = input("Anna etunimesi\n")
```
Tavallisia muuttujatyyppejä Pythonissa ovat:

| Muuttujatyyppi | Nimi Pythonissa | Esimerkkejä | Kommentti |
| :---: | :---: | :---: | :---: |
| Merkkijono | **str** | "Hei!", 'OK' | Sekä "kaksinkertaiset" että 'yksinkertaiset' lainausmerkit toimivat |
| Kokonaisluku | **int** | 2, 0, -2, 1924	| Positiiviset ja negatiiviset kokonaisluvut ja nolla |
| Liukuluku | **float** | 1.04, -3.0004	| Desimaaliluku |
| Kompleksiluku | **complex** | 2.0 + 3.0j | Emme käytä tällä kurssilla |
| Totuusarvo | **bool** | True tai False | Englannin kielen sanasta Boolean |

Muuttujiin voidaan sijoittaa arvoja "="-merkin avulla. Muutama esimerkki muuttujien käytöstä:
```{code-cell} ipython3
:tags: ["auto-execute-page"]
iso_luku = 50000005
print("Iso lukumme on", iso_luku)
pieni_luku = 0.0009
print("Pieni lukumme on", pieni_luku) 
```
Muuttuja **iso_luku** on yllä olevassa kokonaisluku, kun taas muuttuja **pieni_luku** on liukuluku.
:::{admonition} Huom!
:class: note
Toisin kuin monissa muissa ohjelmointikielissä, Pythonissa muuttujan tyyppiä ei tarvitse määritellä ennen muuttujan
käyttämistä. Python päättelee muuttujan tyypin, kun muuttujan arvo asetetaan.
:::
## Merkkijonomuuttujien luominen
```{code-cell} ipython3
# Tyhjän merkkijonomuuttujan luominen:
teksti = ""
# Merkkijonomuuttujan alustaminen merkkijonolla:
tervehdys = "Hei!"
print(tervehdys)
```
## Muuttujien nimeäminen
:::{admonition} Huom!
:class: danger
Älä käytä muuttujien nimissä koskaan **ääkkösiä (ä, ö, å) tai erikoismerkkejä (*, /, jne.)!** Se johtaa ongelmiin.
:::
## Lukuarvojen yksikköjen huomioiminen
Tieteellisessä laskennassa meidän pitää aina olla selvillä käytössä olevista yksiköistä. Python ei pidä mitenkään kirjaa
muuttujan yksiköistä, vaan se on ohjelmoijan vastuulla. Onkin erittäin tärkeää kirjata yksiköt aina muistiin kommentteina. 
Esimerkiksi:
``` ipython3
# Tehtävän lähtöarvot
n = 0.334  # ainemäärä, mol
V = 0.014  # tilavuus, m^3
p = 101325 # paine, Pa
```
On erittäin suositeltavaa pitää kaikki lukuarvot **SI-yksiköissä** aina kun mahdollista.
## Lisätietoa: liukulukujen tieteellinen merkintätapa
Pythonissa voi käyttää myös tieteellistä merkintätapaa, missä **2e5** tarkoittaa **2 * 10{sup}`5`**. Esimerkki:
```{code-cell} ipython3
tosi_pieni = 0.0000002
print("Luku on:", tosi_pieni)
```
:::::{card} Tehtävä 1.2.1
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mikä on muuttujan *vastaus* tyyppi?
``` ipython3
vastaus = 42
```
---
[ ] liukuluku (float)
> Yritä uudelleen!
[ ] merkkijono (str)
> Yritä uudelleen!
[x] kokonaisluku (int)
> Oikein!
[ ] kompleksiluku (complex)
> Yritä uudelleen!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mikä on muuttujan *kuukausi* tyyppi?
``` ipython3
kuukausi = "mmaaarraskuuu"
```
---
[ ] liukuluku (float)
> Yritä uudelleen!
[ ] kokonaisluku (int)
> Yritä uudelleen!
[ ] totuusarvo (bool)
> Yritä uudelleen!
[x] merkkijono (str)
> Oikein!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mikä on muuttujan *moolimassa* tyyppi?
``` ipython3
moolimassa = 16.04
```
---
[x] liukuluku (float)
> Oikein!
[ ] merkkijono (str)
> Yritä uudelleen!
[ ] kokonaisluku (int)
> Yritä uudelleen!
[ ] kompleksiluku (complex)
> Yritä uudelleen!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mikä on muuttujan *maanantai* tyyppi?
``` ipython3
maanantai = False
```
---
[ ] merkkijono (str)
> Yritä uudelleen!
[ ] liukuluku (float)
> Yritä uudelleen!
[ ] kokonaisluku (int)
> Yritä uudelleen!
[x] totuusarvo (bool)
> Oikein!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mikä on muuttujan *kertolasku* tyyppi?
``` ipython3
kertolasku = 3 * 4 * 5
```
---
[ ] liukuluku (float)
> Yritä uudelleen!
[ ] merkkijono (str)
> Yritä uudelleen!
[x] kokonaisluku (int)
> Oikein!
[ ] kompleksiluku (complex)
> Yritä uudelleen!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mikä on muuttujan *jakolasku* tyyppi?
``` ipython3
jakolasku = 3 / 4 / 5
```
---
[x] liukuluku (float)
> Oikein!
[ ] merkkijono (str)
> Yritä uudelleen!
[ ] kokonaisluku (int)
> Yritä uudelleen!
[ ] kompleksiluku (complex)
> Yritä uudelleen!
---
::::
:::::
