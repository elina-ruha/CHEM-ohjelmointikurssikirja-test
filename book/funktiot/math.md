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
# Matemaattiset funktiot (math)
Pythonin **math**-niminen *moduuli* sisältää suuren määrän erilaisia matemaattisia funktioita ja vakioita. Moduulien
luomisesta ja käyttämisestä kerrotaan lisää [seuraavassa luvussa](../Kierros2/s2_5.md), mutta ennen kuin sukellamme
syvemmälle moduulien maailmaan, otetaan math-moduulin sisältämät matemaattiset funktiot käyttöön.

math-moduuli tuodaan ensin oman ohjelman käyttöön lisäämällä ohjelman alkuun **import**-käsky:
``` ipython3
import math
```
Tämän jälkeen moduulin sisältämiä funktioita ja vakioita voi käyttää alla olevilla tavoilla. Voit kopioida esimerkit
Spyderiin ja ajaa ne, jos haluat nähdä tarkemmin, miten funktiot toimivat.
```{code-cell} ipython3
:tags: ["auto-execute-page"]
import math

# exp(x) -> Eksponenttifunktio e^x
print(math.exp(4))

# log(x) -> Luvun x luonnollinen logaritmi, ln(x)
print(math.log(54.598150033144236))

# log(x, y) -> Luvun x logaritmi, kantaluku y
print(math.log(8, 2))

# log10(x) -> Luvun x 10-kantainen logaritmi
print(math.log10(10000))

# pow(x, y) -> luku x potenssiin y. Sama kuin x**y, mutta muuntaa aina luvut (ja tuloksen) liukuluvuksi
print(math.pow(3, 2))

# sqrt(x) -> Luvun x neliöjuuri (kuten x**(1/2))
print(math.sqrt(9))

# pi -> pii (ei ole funktio vaan vakio)
print(math.pi)

# e -> Neperin luku (ei ole funktio vaan vakio)
print(math.e)

# sin(x), cos, tan, ... -> trigonometriset funktiot
print(math.sin(math.pi / 2))

# degrees(x) -> muuntaa radiaanit asteiksi
print(math.degrees(math.pi))

# radians(x) -> muuntaa asteet radiaaneiksi
print(math.radians(180))

# ceil(x) -> pyöristä kokonaislukuun ylöspäin
print(math.ceil(5.4))

# floor(x) -> pyöristä kokonaislukuun alaspäin 
print(math.floor(5.6))

# fabs(x) -> itseisarvo (muuten sama kuin Pythonin normaali abs()-funktio, mutta palauttaa aina liukuluvun)
print(math.fabs(-5.6))
```
:::{admonition} Vinkki
:class: tip
Math-moduulin dokumentaatio ja listaus kaikista sen sisältämistä funktioista löytyy osoitteesta 
<https://docs.python.org/3/library/math.html>.
:::
## Liukulukujen yhtäsuuruuden vertailu *math.isclose*-funktiolla
Liukulukujen yhtäsuuruuden vertailuun ei pidä käyttää `==` -operaattoria vaan 
[*math.isclose*](https://docs.python.org/3/library/math.html#math.isclose)-funktiota. Tällöin voit itse määritellä
tarkkuuden, jolla liukulukuja verrataan. Vertailu voi olla joko suhteellinen, jolloin käytetään parametria *rel_tol* tai
absoluuttinen, jolloin käytetään parametria *abs_tol*. 

Otetaan ensin esimerkki, jossa suhteellinen ja absoluuttinen vertailu johtavat samaan lopputulokseen:
```{code-cell} ipython3
import math
luku1 = 2.0
luku2 = 2.005
print(f"Luvut: {luku1:.3f} ja {luku2:.3f}")
if math.isclose(luku1, luku2, rel_tol = 0.01):
    print("Luvut ovat samat 1% suhteellisella tarkkuudella")
if math.isclose(luku1, luku2, abs_tol = 0.01):
    print("Luvut ovat samat 0.01 absoluuttisella tarkkuudella")
```
Toinen esimerkki, missä rel_tol ja abs_tol johtavat eri lopputulokseen:
```{code-cell} ipython3
import math
luku1 = 2000.0
luku2 = 2001.0
print(f"Luvut: {luku1:.3f} ja {luku2:.3f}")
if math.isclose(2000.0, 2001.0, rel_tol = 0.01):
    print("Luvut ovat samat 1% suhteellisella tarkkuudella")
if not math.isclose(luku1, luku2, abs_tol = 0.01):
    print("Luvut eivät ole samat 0.01 absoluuttisella tarkkuudella")
```
:::{admonition} Huom!
:class: note
Valinta *rel_tol* ja *abs_tol* -parametrien välillä riippuu vertailun luonteesta. Jos esimerkiksi vertaillaan
mittaustuloksia ja tiedetään vain mittausmenetelmän suhteellinen virhe, tulee käyttää suhteellista *rel_tol*-vertailua.
:::
### Tehtävä 2.4.1
Täydennä alla oleva koodi vaihtoehdoilla: `exp`, `import`, `cos`, `ceil`, `sin`, `pow`, `floor`, `math`, `pow`.
```{code-cell} ipython3
TÄYDENNÄ math
# Täydennä niin, että tulostuu 0
print(math.TÄYDENNÄ(11.1) - math.TÄYDENNÄ(12.9))

# Täydennä niin, että tulostuu 5
print(f"{math.TÄYDENNÄ(TÄYDENNÄ.log(5))}:.1f)

# Täydennä niin, että tulostaa 1
x = 0.15
print(f"{math.TÄYDENNÄ(math.TÄYDENNÄ(x), 2) + math.TÄYDENNÄ(math.TÄYDENNÄ(x), 2)}.1f")
```
