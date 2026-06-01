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
# 3.3 Listojen käsittely
Listoja voi muokata useilla erilaisilla funktioilla:
## Alkioiden lisääminen
```{code-cell} ipython3
:tags: ["auto-execute-page"]
# Tyhjä lista luodaan pelkillä hakasulkeilla
alkuaineet = []

# 1) append-funktio lisää listaan yhden alkion:
alkuaineet.append('Cu')
alkuaineet.append('Ag')
print(alkuaineet)

# 2) Listoja voi yhdistää "+"-operaattorilla: 
alkuaineet = alkuaineet + ['S', 'O']
print(alkuaineet)

# 3) extend-funktio lisää useita alkioita listan loppuun: 
alkuaineet.extend(['Hg', 'Au'])
print(alkuaineet)

# 4) insert-funktio lisää alkion haluttuun kohtaan:
alkuaineet.insert(0, 'Na')
print(alkuaineet)
```
## Alkioiden poistaminen
```{code-cell} ipython3
alkuaineet = ['Na', 'Cu', 'Ag', 'S', 'O', 'Hg', 'Au']

# remove(x) poistaa alkion, jonka arvo on x
alkuaineet.remove('Au')
print(alkuaineet)

# del-komento poistaa alkion, jonka indeksi on n 
del alkuaineet[0]
print(alkuaineet)
```
## Alkion olemassaolon testaaminen ja indeksin etsiminen
```{code-cell} ipython3
alkuaineet = ['Cu', 'Ag', 'S', 'O', 'Hg']

# in-avainsanalla voi testata, onko alkio listassa:
if 'O' in alkuaineet:
    print("Happi on vahvasti mukana")

# in-avainsanasta on myös käänteisversio "not in": 
if 'He' not in alkuaineet:
    print("Ei ole heliumia")

# index-funktio kertoo tietyn alkion indeksin
print(f"Kuparin indeksi listassa on: {alkuaineet.index('Cu')}")
```
## Listojen lajittelu
```{code-cell} ipython3
# Listan lajittelu (aakkosjärjestykseen) sort-funktiolla
alkuaineet = ['Cu', 'Ag', 'S', 'O', 'Hg']
alkuaineet.sort()
print(alkuaineet)
```
## Listan pienin ja suurin alkio
Listan pienimmän alkion voi etsiä *min*-funktiolla ja suurimman alkion *max*-funktiolla:
```{code-cell} ipython3
aallonpituudet = [532, 632, 588, 229, 1030, 601]
print(min(aallonpituudet))
print(max(aallonpituudet))
```
### Tehtävä 3.3.1
Täydennä alla oleva koodi ohjeiden mukaisesti.
```{code-cell} ipython3
yhdisteet = []
# Täydennä niin, että listan sisältö on ['CH4']
yhdisteet.TÄYDENNÄ("CH4")
# Täydennä niin, että lista tyhjenee
yhdisteet.TÄYDENNÄ("CH4")
# Täydennä niin, että listan sisältö on ['NaCl', 'RbCl', 'CsCl']
yhdisteet.TÄYDENNÄ(["NaCl", "RbCl", "CsCl"])
# Täydennä niin, että listan sisältö on ['NaCl', 'CsCl']
del yhdisteet[TÄYDENNÄ]
# Täydennä niin, että listan sisältö on ['NaCl', 'KCl', 'CsCl']
yhdisteet.TÄYDENNÄ(1, "KCl")
# Täydennä niin, että tulostaa "CsCl OK"
if "CsCl" in TÄYDENNÄ:
    TÄYDENNÄ("CsCl OK")
# Täydennä niin, että tulostaa 1
TÄYDENNÄ(yhdisteet.TÄYDENNÄ("KCl"))
```
