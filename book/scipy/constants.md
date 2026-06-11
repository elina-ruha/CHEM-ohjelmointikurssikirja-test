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
# scipy.constants
Moduuli *scipy.constants* sisältää [luonnonvakioita](https://docs.scipy.org/doc/scipy/reference/constants.html), joista 
yleisimmät voi ottaa käyttöön suoraan tuomalla pelkän *scipy.constants*-moduulin ohjelmaan:
```{code-cell} ipython3
:tags: ["auto-execute-page"]
import scipy.constants
print(f"Kaasuvakion R arvo on {scipy.constants.R:.7f} J K^-1 mol^-1")
```
## physical_constants-sanakirja
*scipy.constants* sisältää myös sanakirjan [*scipy.constants.physical_constants*](https://docs.scipy.org/doc/scipy/reference/constants.html#constants-database)
, jonka muoto on:
``` ipython3
physical_constants[name] = (arvo_liukulukuna, yksikkö_merkkijonona, epävarmuus_liukulukuna)
```
Sanakirjan avain on siis luonnonvakio ja arvo on kolmen alkion monikko (voit ajatella sitä listana).
Sanakirja sisältää laajan valikoiman luonnonvakioita, joiden arvot tulevat 
[CODATA-tietokannasta](https://physics.nist.gov/cuu/Constants/). Esimerkki sanakirjan käytöstä:
```{code-cell} ipython3
from scipy.constants import physical_constants as pc
m_e = pc["electron mass"][0]
m_e_yksikko = pc["electron mass"][1]
m_e_epavarmuus = pc["electron mass"][2]
print(f"Elektronin massa m_e on {m_e:.10e} {m_e_yksikko:s}")
print(f"Arvon epävarmuus on {m_e_epavarmuus:.2e} {m_e_yksikko:s}")
```
## Yksikkömuunnokset 
Moduuli sisältää myös arvoja [yksikkömuunnoksia](https://docs.scipy.org/doc/scipy/reference/constants.html#units) varten:
```{code-cell} ipython3
import scipy.constants
kcal_mol = 104.5 #kcal/mol
kJ_mol = kcal_mol * scipy.constants.calorie
print(f"{kcal_mol:.2f} kcal/mol on SI-yksiköissä {kJ_mol:.3f} kJ/mol")
```
### Tehtävä
Täytä puuttuvat kohdat niin, että
1) ohjelmaan tuodaan moduuli scipy.constants ja käytetään siitä physical_constants sanakirjaa
2) physical_constants sanakirjasta haetaan Avogadron vakion arvo ja yksikkö

Ohjelman pitäisi tulostaa:
```
Avogadron vakion arvo on 6.0221409 x 10^23 mol^-1
```
```{code-cell} ipython3
from TÄYDENNÄ import TÄYDENNÄ as pc
N_A = pc[TÄYDENNÄ][0]
N_A_yksikkö = pc[TÄYDENNÄ][1]
print(f"Avogadron vakion arvo on {(N_A / 10**23):.7f} x 10^23 { N_A_yksikko:s}")
```
