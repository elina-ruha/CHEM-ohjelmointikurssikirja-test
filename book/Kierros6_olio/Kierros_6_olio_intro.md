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
# Kierros 6: Olio-ohjelmointi
Aiemmin tällä kurssilla olemme tutustuneet erilaisiin **tietorakenteisiin** kuten listat, sanakirjat ja NumPy-taulukot.
Olemme myös tutustuneet **funktioihin**, joilla näitä tietorakenteita voi käsitellä. Esimerkkinä vaikkapa *max(lista)*,
joka palauttaa listan suurimman alkion.

Tutustutaan nyt lyhyesti **olioihin** (engl. *object*). Voimme ajatella olioita tietorakenteina, jotka sisältävät myös
tietojen käsittelyyn tarkoitettuja funktioita.
## Luokan määritteleminen ja olioiden luominen
Jotta voimme luoda uuden olion, meidän pitää ensin määritellä **luokka** (engl. *class*) joka kuvaa olion ominaisuudet.
Määritellään luokka *Molekyyli* (luokkien nimet kirjoitetaan isolla alkukirjaimella):
``` ipython3
class Molekyyli:
    def __init__(self, kaava, moolimassa):
        self.kaava = kaava
        self.moolimassa = moolimassa
       
    def laske_ainemaara(self, massa):
        return massa / self.moolimassa
```
*Molekyyli*-luokka sisältää kaksi funktiomäärittelyä. Näitä luokan sisältämiä funktioita kutsutaan **metodeiksi** 
(engl. *method*) erotuksena tavallisista funktioista, jotka eivät kuulu mihinkään luokkaan. *Molekyyli*-luokka sisältää
**käynnistysmetodin** *_init_* ja metodin *laske_ainemaara*. 
:::{admonition} Huom!
:class: tip
Molempien metodien ensimmäinen parametri on *self*. Tämä parametri viittaa aina olioon itseensä. Python hoitaa
*self*-parametrin automaattisesti, eli sitä ei anneta, kun metodia kutsutaan.
:::
Käynnistysmetodissa *_init_* luodaan oliolle kaksi **kenttää**: *kaava* ja *moolimassa*. Kenttiin pitää viitata
metodin *self*-parametrin avulla.

Katsotaan, mitä määrittelemällämme luokalla voidaan nyt tehdä. Luodaan *Molekyyli*-luokkaan pohjautuvat oliot *metaani* ja *etaani*:
``` ipython3
metaani = Molekyyli("CH4", 16.04) 
etaani = Molekyyli("C2H6", 30.07)
```
Käsky *Molekyyli("CH4", 16.04)* tarkoittaa, että *Molekyyli*-luokan *_init_*-metodia kutsutaan parametreilla "CH4" ja 
16.04 (*self*-parametria ei anneta, vaan Python antaa sen *_init_*-käynnistysmetodille automaattisesti). Käsky palauttaa
uuden olion, jonka kentät *kaava* ja *moolimassa* on täytetty arvoilla "CH4" ja 16.04. Tämä olio sijoitetaan muuttujaan *metaani*.
## Kokonainen olioesimerkki
Luokkamäärittelyn pohjalta voi luoda mielivaltaisen määrän uusia olioita. Katsotaan kokonaisen esimerkin avulla, miten
olioiden kenttiä voi lukea ja miten niiden metodeja käytetään:
```{code-cell} ipython3
:tags: ["auto-execute-page"]
class Molekyyli:
    def __init__(self, kaava, moolimassa):
        self.kaava = kaava
        self.moolimassa = moolimassa
       
    def laske_ainemaara(self, massa):
        return massa / self.moolimassa

metaani = Molekyyli("CH4", 16.04) 
etaani = Molekyyli("C2H6", 30.07)

# Käytetään olioiden kenttiä
print(f"Metaanin molekyylikaava on {metaani.kaava}")
print(f"Etaanin molekyylikaava on {etaani.kaava}")
print(f"Metaanin moolimassa on {metaani.moolimassa} g/mol")
print(f"Etaanin moolimassa on {etaani.moolimassa} g/mol")

# Käytetään laske_ainemaara-metodia. 
# Huomaa, että self-parametria ei anneta
n_metaani = metaani.laske_ainemaara(5.0) # 5 g metaania
n_etaani = etaani.laske_ainemaara(7.0)   # 7 g etaania
print(f"5 g metaania on {n_metaani:.3f} mol")
print(f"7 g etaania on {n_etaani:.3f} mol")
```
Kannattaa tutustua esimerkkiin huolella. Esimerkki on yksinkertainen, mutta sen tarkoituksena on havainnollistaa, miten olioiden
avulla voidaan yhdistää tietorakenteet ja funktiot samaan pakettiin. *self*-parametrin käyttö on yksi olio-ohjelmoinnin avainkäsitteistä.
:::{admonition} Huom!
:class: tip
*laske_ainemaara*-metodissa *self.moolimassa* viittaa kunkin olion omaan *moolimassa*-kenttään. Sillä on siis eri arvo
metaanille ja etaanille. Näin ainemäärä lasketaan oikein kullekin oliolle. Parametri *massa* taas määritetään aina 
metodia *laske_ainemaara* kutsuttaessa.
:::
## Yllättävä käänne
Olemme itse asiassa käyttäneet olioita aivan koko kurssin ajan! Pythonissa oikeastaan **kaikki** asiat ovat olioita.
Esimerkiksi *int* ja *float* -tyyppiset muuttujat tai *list* ja *dict* -tietorakenteet ovat kaikki olioita, jotka sisältävät
myös metodeja kyseisten olioiden käsittelemiseksi:
```{code-cell} ipython3
# float-olio sisältää esimerkiksi is_integer()-metodin
liukuluku = 3.14
print(liukuluku.is_integer())
liukuluku_int = 3.0
print(liukuluku_int.is_integer())
```
*list*-tietorakenne sisältää useita metodeja, joita olemmekin jo käyttäneet
```{code-cell} ipython3
lista = [1, 2, 3]
# Tulostetaan ykkösten määrä listassa
print(lista.count(1))
# Lisätään yksi ykkönen listaan
lista.append(1)
# Tulostetaan ykkösten määrä listassa
print(lista.count(1))
```
### Tehtävä 6.0.2
Alla on yksinkertainen luokka Atomi, joka sisältää *laske_varaus*-metodin alkuaineelle. Täydennä koodi niin, että luokka toimisi.
```{code-cell} ipython3
"""Täydennä""" Atomi:
    def __"""Täydennä"""__(self, merkki, protonit, elektronit):
        self.merkki = merkki
        self.protonit = protonit
        self.elektronit = elektronit
        
    def laske_varaus("""Täydennä"""):
        varaus = self.protonit - self.elektronit
        if varaus > 0:
            return "+" + str(varaus)
        return varaus
    
fluori = """Täydennä"""("F", 9, 10)   
varaus = fluori."""Täydennä"""()
print(varaus)
```
