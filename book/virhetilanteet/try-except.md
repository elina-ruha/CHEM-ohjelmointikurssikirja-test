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
# Virhetilanteiden käsittely (try-except-finally)
## Poikkeukset
Hyvässä ohjelmakoodissa varaudutaan aina erilaisiin virhetilanteisiin, kuten
- käyttäjän antama virheellinen syöte
- tiedoston avaaminen epäonnistuu

Pythonissa virhetilanteet hoidetaan **poikkeusten** (engl. *exception*) avulla.

Oletkin varmasti jo kohdannut lukuisia poikkeuksia kurssin aikana. Esimerkiksi jos olet yrittänyt muuntaa vääränlaista
merkkijonoa lukuarvoksi komennolla
```{code-cell} ipython3
:tags: ["auto-execute-page"]
luku = int("kolme")
```
Python ilmoittaa *ValueError*-poikkeuksesta.
## Poikkeusten "nappaaminen" ohjelmakoodissa
Virhetilanteessa Python "nostaa" (engl. *raise*) poikkeuksen. Poikkeuksen voi "napata" (engl. *catch*) ja käsitellä, jolloin
se ei johda ohjelman suorituksen keskeytymiseen.

Poikkeusten nappaamiseen ja käsittelemiseen käytetään **try-except** -rakennetta. Napataan virheellisestä lukuarvosta
johtuva *ValueError*-poikkeus:
``` ipython3
while True:
    try:
        luku = float(input("Anna liukuluku:\n"))
        # Jos suoritus jatkui tänne, käyttäjä antoi kelvollisen liukuluvun      
        break
    except ValueError:
        # Napataan ValueError-poikkeus (virheellinen lukuarvo)
        print("Virheellinen lukuarvo!")
        # Virhe on nyt käsitelty ja ohjelman suoritus palaa while-silmukan alkuun
print("Annoit luvun", luku)
```
Esimerkkisuoritus:
```
Anna liukuluku:
> kolme piste kaksi
Virheellinen lukuarvo!
Anna liukuluku:
> 3.2
Annoit luvun 3.2
```
## Poikkeus tiedostoa avattaessa (*OSError*)
Tiedostoja käsitellessä voi tulla vastaan virhetilanteita (esimerkiksi yritetään avata tiedostoa, jota ei ole olemassa).
Tällöin pitää napata virhe *OSError*:
```{code-cell} ipython3
# Luetaan rivit tiedostosta
try:
    tiedosto = open("rivit.txt", "r")
    for rivi in tiedosto:
        print(rivi)  
except OSError:
    print("Virhe avattaessa tiedostoa rivit.txt")
```
## Sisäkkäiset try-lausekkeet
Monesti tarvitaan sisäkkäisiä *try*-lausekkeita, joilla hoidetaan erityyppiset virheet. Hyvä nyrkkisääntö on, että
*try*-avainsana tulisi olla mahdollisimman lähellä riviä, jossa odotat virheen tapahtuvan. Esimerkki:
``` ipython3
nimi = "luku.txt"
try:
    # Yritetään avata tiedosto, tämä voi johtaa virheeseen
    tiedosto = open(nimi, "r")
    # Tiedosto aukesi onnistuneesti, luetaan siitä
    for rivi in tiedosto:
        try:
            # Yritetään muuntaa teksti liukuluvuksi
            luku = float(rivi)
            # Onnistui, tulostetaan luku
            print("Tiedosto sisälsi luvun", luku)  
        except ValueError:
            # float()-funktio aiheutti ValueError-virheen
            print(f"Virheellinen lukuarvo {rivi.strip():s} tiedostossa {nimi:s}")
            
    # Suljetaan lopuksi tiedosto            
    tiedosto.close()
except OSError:
    # Tänne päädytään, jos open-funktio epäonnistui
    print("Virhe avattaessa tiedostoa", nimi)
```
Jos kaikki menee hyvin, ohjelma tulostaa:
```
Tiedosto sisälsi luvun 1.0
```
Jos tiedostoa ei ole olemassa, ohjelma tulostaa:
```
Virhe luettaessa tiedostoa luku.txt
```
Jos tiedostossa on virheellisiä lukuja, ohjelma tulostaa esimerkiksi:
```
Virheellinen lukuarvo 1.0a tiedostossa luku.txt
Tiedosto sisälsi luvun 2.0
```
## try-except-finally
**try-except-finally**-rakenteella voidaan varmistaa, että jokin asia tehdään varmasti, vaikka virheitä syntyisi.
Luetaan tekstiä tiedostosta ja napataan poikkeukset (tässä tapauksessa tiedosto sisältää ainoastaan tekstin "keukeu"):
```{code-cell} ipython3
nimi = "teksti.txt"
try:
    # Yritetään avata tiedosto, tämä voi johtaa virheeseen
    tiedosto = open(nimi, "r")
    try:
        # Tiedosto aukesi onnistuneesti, yritetään lukea tiedoston sisältö read()-funktiolla
        teksti = tiedosto.read()
        # Onnistui, tulostetaan sisältö
        print("Tiedosto sisälsi tekstin", teksti)  
    except OSError:
        # read()-funktio aiheutti OSError-virheen, tiedostoa ei voi lukea
        print(f"Tiedostoa {nimi:s} ei voitu lukea")
    finally: 
        # Suljetaan tiedosto riippumatta siitä, oliko virheitä vai ei
        print("Suljetaan tiedosto")        
        tiedosto.close()
except OSError:
    # Tänne päädytään, jos open-funktio epäonnistui.
    print("Virhe avattaessa tiedostoa", nimi)
    # Tiedostoa ei avattu, joten sitä ei tarvitse myöskään sulkea
```
Jos kaikki menee hyvin, ohjelmaa tulostaa saman kuin yllä olevan koodin ajaessa tulostuu.

Jos tiedostoa ei ole olemassa, ohjelma tulostaa:
```
Virhe avattaessa tiedostoa teksti.txt
```
Jos tiedostossa on virheellisiä lukuja, ohjelma tulostaa:
```
Tiedostoa teksti.txt ei voitu lukea
Suljetaan tiedosto
```
Ohjelma siis sulkee viimeisenä tekonaan tiedoston. Tämä on tärkeää ja tiedostojen kanssa tuleekin aina käyttää
**try-finally** -rakennetta. Helpoiten tämän vaatimuksen voi kuitata käyttämällä **with**-lausetta (ks. [seuraava luku](../Kierros5/s5_5.md)).
## try-except-else(-finally)
**try-except**-rakenteeseen voi yhdistää myös **else**-osan, joka suoritetaan siinä tapauksessa, että **try**-osio ei
aiheuttanut poikkeuksia:
``` ipython3
try:
    luku = float(input("Anna luku:\n"))
except ValueError:
    print("Virheellinen luku")
else:
    print("Annoit luvun", luku)
```
**try-except-else**-rakenteeseen voi yhdistää vielä **finally**-osan, jossa esimerkiksi suljetaan avatut tiedostot.
## Lista Pythonin poikkeuksista
Mistä tietää, mikä poikeus pitäisi napata? Tässä on lista [Pythonin sisäänrakennetuista poikkeuksista](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).
Tällä kurssilla tärkeimmät poikkeukset ovat *OSError* (virhe avattaessa tai käsitellessä tiedostoa) ja *ValueError* 
(virhe muunnettaessa tekstiä lukuarvoksi). 
:::{admonition} Huom!
:class: note
Monimutkaisemmissa ohjelmissa pitää ottaa huomioon myös erilaisten kirjastojen poikkeustilanteet. Oikeassa ohjelmistossa,
jonka tehtävä on esimerkiksi valvoa kriittistä tuotantoprosessia, voikin olla enemmän 
virheenkäsittelykoodia kuin varsinaista toiminnallista koodia!
:::
### Tehtävä 5.4.1
*tulokset.txt* on tiedosto, joka sisältää reaktiotuotteen konsentraatiot viiden minuutin välein. Tiedoston kolme 
ensimmäistä riviä voisivat näyttää esimerkiksi tältä:
``` ipython3
1.23
1.32
1.44
```
Täydennä koodi vaihtoehdoilla: `OSError`, `except`, `try`, `ValueError`
```{code-cell} ipython3
tulokset = "tulokset.txt"
ajanhetki = 0
TÄYDENNÄ:
    tiedosto = open(tulokset, "r")
    for rivi in tiedosto:
        try:
            luku = float(rivi)
            ajanhetki += 5
            print(f"Konsentraatio {luku}, aikaa kulunut {ajanhetki} minuuttia")
        TÄYDENNÄ TÄYDENNÄ:
            print(f"Virheellinen lukuarvo {rivi.strip():s} tiedostossa {tulokset:s}")
    tiedosto.close()
except TÄYDENNÄ:
    print("Virhe avattaessa tiedostoa", tulokset)
```
