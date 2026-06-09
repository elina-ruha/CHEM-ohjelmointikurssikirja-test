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
# Tyyppimuunnokset
Monesti on tarpeen muuntaa muuttujia yhdestä tyypistä toiseen.
## Merkkijonon muuntaminen lukuarvoiksi
Merkkijonon (str) voi muuntaa kokonaisluvuksi *int*-funktiolla ja liukuluvuksi *float*-funktiolla:
```{code-cell} ipython3
:tags: ["auto-execute-page"]
luku_str = "2"
print("luku_str * 2 on:", luku_str * 2)
luku_int = int(luku_str)
print("luku_int * 2 on:", luku_int * 2)
luku_float = float(luku_str)
print("luku_float * 2 on:", luku_float * 2)
```
:::{admonition} Huom!
:class: tip
Eli ensimmäinen "laskutoimitus" merkkijonoilla vain kaksinkertaistaa merkkijonon pituuden, mutta kaksi jälkimmäistä
laskutoimitusta laskevat oikeasti kokonais- ja liukuluvuilla. Merkkijonon muuntamista lukuarvoksi hyödynnämme varsinkin
*input*-funktion käytön yhteydessä.
:::
## Kokonaislukujen kysyminen käyttäjältä *input*-funktiolla
*input*-funktio lukee käyttäjältä merkkijonon. Muunnetaan luettu merkkijono kokonaisluvuksi *int*-funktiolla:
``` ipython3
luku = int(input("Anna luku niin kerron sen kahdella\n"))
print("Antamasi luku", luku, "kerrottuna kahdella on", 2 * luku)
```
Lopputulos (Muista, että ">"-merkki tarkoittaa käyttäjän *input*-funktiolle antamaa syötettä):
```
Anna luku niin kerron sen kahdella
> 3
Antamasi luku 3 kerrottuna kahdella on 6
```
## Liukulukujen kysyminen käyttäjältä *input*-funktiolla
Muunnetaan *input*-funktiolla luettu merkkijono suoraan liukuluvuksi *float*-funktiolla:
``` ipython3
luku = float(input("Anna luku niin kerron sen luvulla 2.6\n"))
print("Antamasi luku", luku, "kerrottuna luvulla 2.6 on", 2.6 * luku)
```
Lopputulos:
```
Anna luku niin kerron sen luvulla 2.6
> 5
Antamasi luku 5.0 kerrottuna luvulla 2.6 on 13.0
```
## Lukuarvojen muuntaminen merkkijonoksi
Liukuluvun tai kokonaisluvun voi muuntaa merkkijonoksi *str*-funktiolla:
```{code-cell} ipython3
mjono1 = str(5)
mjono2 = str(6.5)
print("Merkkijonojen mjono1 ja mjono2 yhdistelmä:", mjono1 + mjono2)
```
### Tehtävä 1.4.1
Täytä aukkopaikat niin, että tyyppimuunnokset ovat oikein.
```{code-cell} ipython3
# Merkkijono kokonaisluvuksi
kokonaisluku = TÄYDENNÄ("2017")
print(kokonaisluku)
# Merkkijono liukuluvuksi
liukuluku = TÄYDENNÄ("3.14")
print(liukuluku)
# Kokonaisluku merkkijonoksi
merkkijono = TÄYDENNÄ(82347827)
print(merkkijono)
```
