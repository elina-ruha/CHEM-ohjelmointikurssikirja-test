# Kertaus
Kerrataan virhetilanteiden käsittelyä ennen siirtymistä lukuun *SciPy*.
:::::{card}
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Minkä virheen seuraava komento antaisi? 
``` ipython3
luku = int("kaksi")
```
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

::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Missä tilanteessa seuraava koodi tulostaa 
``` ipython3
try:
    tiedosto = open(tiedoston_nimi, "r")
    for rivi in tiedosto
      try:
        luku = int(rivi)
        print("a")
      except ValueError:
        print("b")
    tiedosto.close()
except OSError:
    print("c")
```
---
[ ] Tiedosto avataan onnistuneesti
> Yritä uudelleen!
[ ] Tiedosto avataan onnistuneesti ja rivi muunnetaan kokonaisluvuksi onnistuneesti.
> Yritä uudelleen!
[ ] Tiedostoa ei pystytä avaamaan.
> Yritä uudelleen!
[x] Tiedosto avataan onnistuneesti, mutta riviä ei pystytä muuntamaan kokonaisluvuksi.
> Oikein!
---
::::

::::{question}
:type: multiple-choice
:variant: multiple-select
:nocaption:
:columns: 1

Mitä hyötyjä `with open`-funktion käyttämisessä on?
---
[x] Se sulkee tiedoston automaattisesti.
> Oikein!
[ ] Se lukee tiedoston automaattisesti.
> Ei valitettavasti, yritä uudelleen!
[ ] Se tarkistaa tiedoston automaattisesti, jolloin ei tarvita try-except-rakennetta.
> Ei valitettavasti, yritä uudelleen!
[x] Sitä käyttämällä voidaan korvata eräänlainen try-finally rakenne.
> Oikein! finally: tiedosto.close()
---
::::
:::::
