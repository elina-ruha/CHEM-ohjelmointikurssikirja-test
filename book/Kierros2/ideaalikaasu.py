# Moduuli ideaalikaasu:
# Apufunktioita ideaalikaasulle
# pV = nRT

# Moduuli määrittelee myös kaasuvakion R
# Lähde NIST CODATA2018: https://physics.nist.gov/cgi-bin/cuu/Value?r
R = 8.314462618 # J K^-1 mol^-1 

# Moduuli määrittelee neljä funktiota
def ratkaise_paine(V, n, T):
    return n * R * T / V
    
def ratkaise_tilavuus(p, n, T):
    return n * R * T / p

def ratkaise_ainemaara(p, V, T):
    return p * V / (R * T)

def ratkaise_lampotila(p, V, n):
    return p * V / (n * R)
