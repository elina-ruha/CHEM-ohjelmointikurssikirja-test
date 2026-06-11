# SciPy-kirjasto
[SciPy](https://www.scipy.org/) on Pythonilla luotu tieteellisen laskennan infrastruktuuri, joka on vapaasti kaikken 
Python-ohjelmoijien käytettävissä. SciPy on laaja kokonaisuus ja olemmekin jo käyttäneet osia siitä: 
- NumPy-kirjasto on osa SciPyä ja SciPyn eri toiminnot hyödyntävät hyvin paljon NumPy-taulukoita
- Matplotlib-kirjasto on osa SciPyä
- Jopa Spyderin interaktiivinen IPython-konsoli on osa Scipyä

SciPyn dokumentaatio löytyy osoitteesta <https://docs.scipy.org/doc/scipy/reference/> ja samasta paikasta löytyy myös
[tutoriaali](https://docs.scipy.org/doc/scipy/reference/tutorial/index.html) SciPyn erilaisista alamoduuleista. 
Alamoduuleja on toistakymmentä ja tällä kurssilla tutustumme niistä vain neljään:
- [scipy.constants](https://docs.scipy.org/doc/scipy/reference/constants.html): Luonnonvakiot. Sanakirjan
  [scipy.constants.physical_constants](https://docs.scipy.org/doc/scipy/reference/constants.html#scipy.constants.physical_constants)
   tietolähde on CODATA-tietokanta, jota tälläkin kurssilla olemme hyödyntäneet. Helppo tapa ottaa luonnonvakioiden tarkimmat tunnetut arvot käyttöön!
- [scipy.stats](https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html): Tilastolliset työkalut, esimerkiksi
   lineaarinen regressio ([scipy.stats.linregress](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html))
- [scipy.linalg](https://docs.scipy.org/doc/scipy/reference/tutorial/linalg.html): Lineaarialgebra, esimerkiksi matriisien
   käsittely ja yhtälönryhmän ratkaiseminen ([scipy.linalg.solve](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve.html))
- [scipy.integrate](https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html): Integrointi, erityisesti differentiaaliyhtälöiden
   numeerinen integrointi ([scipy.integrate.solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html))
:::{admonition} Vinkki
:class: tip
Oppimateriaalin seuraavissa kappaleissa annetaan käytännön esimerkkejä näiden alamoduulien hyödyntämisestä.
:::
