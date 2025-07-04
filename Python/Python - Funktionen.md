

# Funktionen schreiben

  

**def Begruessung(Name):

  

    return f'Guten Tag {Name}'

  

**print(Begruessung("Julia"))

**print(Begruessung("Juan"))

**print(Begruessung("Johannes"))

Ausgabe:

Guten Tag Julia 
Guten Tag Juan 
Guten Tag Johannes

**def quadratzahl(x):

   **return x * x

**print(quadratzahl(5))

Ausgabe: 25

**def quadratzahl(x):

   **return x + x

  **print(quadratzahl(5))

Ausgabe: 10

**def ist_negativ(x):

   **return x < 0

  **print(ist_negativ(-1))  # Ausgabe: True

**print(ist_negativ(5))   # Ausgabe: False

Ausgabe: 
True
False

**def ist_laenger(x,y):

   **if len(x) >= len(y):

   **return x

   **else:

   **return y

**print(ist_laenger("Joahnnes", "Julia"))

**print(ist_laenger("Raeuber Hotzenklotz", "Johannes"))


Ausgabe:
Joahnnes
Raeuber Hotzenklotz


**def absoluter_unterschied(x, y):

   **z = x - y

   **return abs(z)

**print(absoluter_unterschied(-5,-1))

Ausgabe:  4

**def anfangsbuchstabe(x):

   **if  x.startswith("A"):

   **return True

   **else:

   **return False

  
**print(anfangsbuchstabe("Johannes"))

**print(anfangsbuchstabe("Anna"))

print(anfangsbuchstabe("Annabelle"))

Ausgabe: 
False 
True
True

**def seitenlaengen(a, b, c):

   **return all(x > 0 for x in [a, b, c]) and a + b > c and a + c > b and b + c > a

  **print(seitenlaengen(5, 3, 10))

Ausgabe: False