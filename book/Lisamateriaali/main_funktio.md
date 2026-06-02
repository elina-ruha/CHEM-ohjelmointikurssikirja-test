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
# *main*-funktio
Jos olet aiemmin osallistunut kurssille **CS-A1111 Ohjelmoinnin peruskurssi Y1**, olet todennäköisesti tutustunut
lähestymistapaan, jossa Python-ohjelmat kirjoitetaan aina *main*-funktion sisään. Esimerkiksi näin:
``` ipython3
def main():
    nimi = input("Anna nimesi:\n")
    print("Moi", nimi)
    
main()
```
Ohjelman suoritus voisi näyttää esimerkiksi tältä:
> Anna nimesi:\
> :Karl\
> Moi Karl

Tällä kurssilla vastaava ohjelmat kannattaa kuitenkin kirjoittaa **ilman *main*-funktiota**. Eli:
``` ipython3
nimi = input("Anna nimesi:\n")
print("Moi", nimi)
```
Syynä on se, että osa CodeRunner-testeistä **ei valitettavasti toimi**, jos vastaus on kirjoitettu *main*-funktiota käyttäen.
## Syventävää tietoa: Miksi *main*-funktiota käytetään?
Pythonissa ei siis ole pakko kirjoittaa ohjelmia *main*-funktiota käyttäen. Milloin *main*-funktiota sitten olisi
syytä käyttää?

*main*-funktion käyttäminen on erittäin tärkeää esimerkiksi silloin, kuin kirjoitetaan moduuleja, jotka sisältävät muissa
ohjelmissa käytettäviä funktioita, mutta moduuli voidaan ajaa myös omana ohjelmanaan. Tällöin on tärkeätä erottaa
tilanteet, joissa jokin toinen ohjelma kutsuu moduulin funktiota tai moduuli ajetaan sellaisenaan. 

<p> Otetaan esimerkki, jossa meillä on määritelty laskin-moduuli (tiedosto laskin.py):</p>
``` ipython3
# Moduuli laskin
# Funktio tuplaa: palauttaa parametrin "luku" kaksinkertaisena
def tuplaa(luku):
    return luku * 2

# main-funktio, jota ei kutsuta, jos joku tuo laskin-moduulin omaan ohjelmaansa
# import-käskyllä ja kutsuu tuplaa-funktiota   
def main():
    numero = int(input("Anna kokonaisluku:\n"))
    tupla = tuplaa(numero)
    print("Antamasi luku kaksinkertaisena on:", tupla)

# Kutsutaan main-funktiota vain, jos joku ajaa laskin-moduulin sellaisenaan
# Esimerkiksi avaa tiedoston Spyderiin ja ajaa koodin
if __name__ == "__main__":    
    main()
```
Luodaan nyt ohjelma, joka hyödyntää *laskin*-moduulia:
``` ipython3
import laskin
print("5 x 2 on:", tuplaa(5))
```
Ohjelma tulostaisi pelkästään
> 5 x 2 on: 10

<p> Toisaalta jos ajamme tiedoston laskin.py sellaisenaan (esimerkiksi Spyderissä), Python suorittaa laskin-moduulin
main-funktion ja suoritus näyttää tältä:</p>
> Anna kokonaisluku:\
> :9\
> Antamasi luku kaksinkertaisena on: 18

Ratkaisevan tärkeässä roolissa on siis `__name__` -erikoismuuttuja, joka saa arvon "`__main__`", kun moduuli on ajettu
omana ohjelmanaan (__ = kaksi alaviivaa peräkkäin).

Lisää yksityiskohtia aiheeseen liittyen esimerkiksi
[Pythonin dokumentaatiossa](https://docs.python.org/3/library/__main__.html).
