# Tuodaan koko ideaalikaasu-moduuli ohjelman testi.py käyttöön
import ideaalikaasu
# ideaalikaasu-moduulin funktioiden eteen pitää lisätä viittaus "ideaalikaasu."
p = ideaalikaasu.ratkaise_paine(0.002, 0.01, 300) # Parametrit V, n, T
print(f"Paine: {p:.3f} Pa")
