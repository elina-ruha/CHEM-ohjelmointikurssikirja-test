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
# CodeRunnerin testien hyödyntäminen Spyderissä
CodeRunner-ohjelmointitehtävät sisältävät erilaisia testejä, joilla kirjoittamasi ohjelma tarkastetaan. Voit myös käyttää
näitä testejä Spyderissä (tai muussa kehitysympäristössä). Tämä nopeuttaa monesti virheiden etsimistä. Näin voit myös
välttää miinuspisteet, joita kertyy liian monesta palautusyrityksestä.
## Esimerkki
Kuvitellaan, että tehtävänä on kirjoittaa seuraavanlainen funktio:

*Kirjoita funktio tiheys, joka saa parametreinä yhdisteen massan (g) ja tilavuuden (cm^3). Funktio palauttaa yhdisteen
tiheyden (g/cm^3). Jos funktiota kutsutaan epäfysikaalisella parametrilla, sen pitää palauttaa arvo -1.*

Kirjoitetaan määritelmän täyttävä funktio:
``` ipython3
def tiheys(massa, tilavuus):
    if massa > 0 and tilavuus > 0:
        return massa/tilavuus
    else:
        return -1
```
Seuraavaksi katsotaan CodeRunnerin esimerkkitestit (**Test**) ja niitä vastaavat tulokset (**Result**):

| Test | Result |
| :---: | :---: |
| print(round(tiheys(5.0, 24.0), 2)) | 0.21 |
| print(tiheys(-1.0, 10))	| -1 |
| print(tiheys(2, 0))	| -1 |

Nyt voit käytännössä ajaa nämä testit Spyderissä omalle koodillesi kopioimalla yllä olevat testit *tiheys*-funktion
toteutuksen alle ja ajamalla koodin:
```{code-cell} ipython3
:tags: ["auto-execute-page"]
def tiheys(massa, tilavuus):
    if massa > 0 and tilavuus > 0:
        return massa/tilavuus
    else:
        return -1

# CodeRunner-testit:
print(round(tiheys(5.0, 24.0), 2))
print(tiheys(-1.0, 10))
print(tiheys(2, 0))
```
Tulostuvat arvot vastaavat Result-sarakkeen tuloksia, joten funktio on toteutettu oikein. Funktion voi nyt kopioida
CodeRunneriin ja tarkistaa.

## Yhteenveto
Varsinkin monimutkaisemmissa tehtävissä, joissa virheellisistä palautuksista tulee miinuspisteitä, on suositeltavaa ajaa
CodeRunnerin esimerkkitestit ensin Spyderissä ja vasta sitten palauttaa koodi CodeRunneriin. Palautuksen yhteydessä esiin
tulee tavallisesti lisää CodeRunner-testejä, joista osa voi epäonnistua, mutta sitten voit kopioida epäonnistuneet testit
Spyderiin ja alkaa testata koodiasi näitä testejä vasten.
