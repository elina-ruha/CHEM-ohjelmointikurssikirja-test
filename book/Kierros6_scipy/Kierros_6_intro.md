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

# Kierros 6
Kuudes ja viimeinen kierros sisältää uutena asiana **Scipy**-kirjaston, jossa on valtava määrä työkaluja
tieteellistä laskentaa varten.

Kierroksen oppimateriaalissa käsitellään myös **olio-ohjelmointia**, jota harjoitellaan B-tehtävissä. Olio-ohjelmointi on
hyvin tärkeä lähestymistapa modernissa ohjelmistotuotannossa, mutta lyhyellä peruskurssilla ehdimme tutustua siihen vain kevyesti.

:::::{card} Tehtävä 6.0.1
Tästä alkaa kierros 6. Sitä ennen kierroksen 5 pikakertaus.
::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

Mitä haluat tehdä tiedostolle komennolla: tiedosto = open("tulokset.txt", "r")?
---
[x] lukea
> Oikein!
[ ] kirjoittaa
> Yritä uudelleen!
[ ] täydentää
> Yritä uudelleen!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

Funktio, jolla saat poistettua ylimääräiset välilyönnit?
---
[ ] split
> Yritä uudelleen!
[ ] rstrip
> Yritä uudelleen!
[x] strip
> Oikein!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

Millä funktiolla suljet tiedoston?
---
[x] close
> Oikein!
[ ] readline
> Yritä uudelleen!
[ ] finally
> Yritä uudelleen!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

Tekstitiedoston voi helposti muuttaa NumPy-taulukoksi funktiolla...
---
[x] loadtxt
> Oikein!
[ ] savetxt
> Yritä uudelleen!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

NumPy-taulukon voi muuttaa tekstitiedostoksi funktiolla...
---
[ ] loadtxt
> Yritä uudelleen!
[x] savetxt
> Oikein!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

Minkä virheen seuraava komento antaisi: luku = int("kaksi")?
---
[ ] IndentationError
> Yritä uudelleen!
[x] ValueError
> Oikein!
[ ] OSError
> Yritä uudelleen!
[ ] SyntaxError
> Yritä uudelleen!
---
::::

::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:
:columns: 1

Mikä virhetilanne pitää käsitellä, jos tiedostoa ei voi avata?
---
[ ] IndentationError
> Yritä uudelleen!
[ ] ValueError
> Yritä uudelleen!
[x] OSError
> Oikein!
[ ] SyntaxError
> Yritä uudelleen!
---
::::
:::::
