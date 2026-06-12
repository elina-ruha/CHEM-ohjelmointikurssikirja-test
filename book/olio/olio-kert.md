# Kertaus
Kerrataan vielä lopuksi olio-ohjelmointia.
:::::{card}
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Mikä on käynnistysmetodi?
---
[x] `__init__`
> Oikein!
[ ] `__str__`
> Yritä uudelleen!
[ ] `self`
> Yritä uudelleen!
[ ] `self.__init__`
> Yritä uudelleen!
---
::::
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Miten viittaat *Molekyyli*-luokan olion *metaanin* kaavaan?
---
[ ] kaava
> Yritä uudelleen!
[ ] Molekyyli.kaava
> Yritä uudelleen!
[x] metaani.kaava
> Oikein!
[ ] self.kaava
> Yritä uudelleen!
---
::::
::::{question}
:type: multiple-choice
:variant: single-select
:nocaption:
:columns: 1

Miten voi luoda uuden *Molekyyli*-luokan olion?
``` ipython3
class Molekyyli:
  def __init__(self, kaava, moolimassa):
```
---
[ ] `metaani.__init__("CH4", 16.04)`
> Yritä uudelleen!
[ ] `metaani = Molekyyli.__init("CH4", 16.04)`
> Yritä uudelleen!
[ ] `metaani = Molekyyli(metaani, "CH4", 16.04)`
> Yritä uudelleen!
[x] `metaani = Molekyyli("CH4", 16.04)`
> Oikein!
---
::::

::::{question}
:type: multiple-choice
:variant: multiple-select
:nocaption:
:columns: 1

Valitse oikeat väittämät liittyen luokkamuuttujiin.
---
[ ] Luokkamuuttuja kannattaa määritellä käynnistysmetodissa.
> Luokkamuuttuja kannattaa määritellä metodien ulkopuolella. Yritä uudelleen!
[x] Luokkamuuttujien tiedot ovat yhteisiä kaikille luokan olioille.
> Oikein!
[x] Luokkamuuttujaan viitataan luokan nimen avulla luokan metodeissa ja luokan ulkopuolella.
> Oikein!
[ ] Luokkamuuttujan arvoa ei voi muuttaa metodeissa vaan sen muuttamiseen tulee olla oma metodi.
> Luokkamuuttujan arvo voi muuttaa eri metodeissa. Yritä uudelleen!
---
::::
:::::
