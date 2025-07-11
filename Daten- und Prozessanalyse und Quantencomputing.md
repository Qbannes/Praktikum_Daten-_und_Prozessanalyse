
# Inhaltsverzeichnis

## Lineare Algebra [[Daten- und Prozessanalyse und Quantencomputing#Lineare Algebra]] 

## Python

### - Funktionen [[Daten- und Prozessanalyse und Quantencomputing#Python - Funktionen]] 


## Qubits

### 01 - Quantenbit

### 02 - Verschränkung

### 03 - Blochkugel


## Quantenalgorithmen
### 01 Deutsch-Josza-Algorithmus [[Daten- und Prozessanalyse und Quantencomputing#01 - Deutsch-Josza-Algorithmus]] 
### 02 Grover-Algorithmus [[Daten- und Prozessanalyse und Quantencomputing#02 - Grover-Algorithmus]]  
### 03 Shor-Algorithmus [[Daten- und Prozessanalyse und Quantencomputing#03 - Shor-Algorithmus]]  

## Q# 
### - Quantencomputing mit Q# [[Daten- und Prozessanalyse und Quantencomputing#Quantencomputing mit Q]] 








































## Lineare Algebra
### Mengennotation

### Set-Builder-Notation
He (Helium) und weitere sind Mitglied der Menge N
$$N=\{ He, Ne,{\dots},Rn, Og \}$$

mit Bedingungen :
In der Menge können Bedingungen und oder Beschreibungen enthalten sein
$$N=\{x\, |\,x<10\}$$
$$N=\{x\,\,\text{ist eine Primzahl} \,|\,x<8\}$$
ist gleichbedeutend mit 
$$N=\{2, 3, 5, 7\}$$

## Andere Mengennotation

Helium ist eine Menge von N
$$He\in N$$
Oxygen ist keine Menge von N
$$O\not\in N$$
X ist eine Teilmenge von Y
$$X \subseteq Y$$
Y ist Obermenge von x
$$Y \supseteq X$$
Leere Menge
$$\emptyset \quad \text{oder} \quad \varnothing\,\,\,\,\,\,\text{oder}\,\,\,\,\,\{\}$$
Die Leere Menge ist Teilmenge aller Elemente

## Wichtige Mengen der Zahlen
Menge der natürlichen Zahlen
$$\mathbb{N}\{0,1,2,3\\{\dots}\}$$
Menge der ganzen Zahlen
$$\mathbb{Z}=\{\dots-3,-2,-1,0,1,2,3\dots\}$$
Menge der rationalen Zahlen umfasst alle Brüche
$$
\mathbb{Q} = \left\{ \frac{p}{q} \;\Big|\; p \in \mathbb{Z}, \, q \in \mathbb{Z} \setminus \{0\} \right\}
$$
Menge der reellen Zahlen 
$$\mathbb{R}= \{\frac{1}{3},4,0.33,3.14159,\dots\}$$





## Python - Funktionen

  

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


### 01 - Quantenbit
**sehr spezielles physikalisches System**

wird mathematisch durch eine Wellenfunktion beschrieben -> Zustandsvektor -> Zustand
Nur zwei Zustände haben eine besondere Bedeutung.
-> *Dirac-Notation*:
$$
|0 \rangle \text{ und } |1 \rangle
$$
Ket-Null und Ket-Eins.
$$
|0 \rangle = \left[\begin{array}{c}1  \\ 0 \end{array}\right]
$$
$$
|1 \rangle = \left[\begin{array}{c}0  \\ 1 \end{array}\right]
$$

$$
|\varphi \rangle = \alpha \cdot |0 \rangle + \beta \cdot |1 \rangle
$$
$$
\text{Zustandsvektor: } \left(\begin{array}{c} \alpha \\ \beta \end{array}\right)
$$
Alpha und Beta sind komplexe Zahlen.
Sobald man misst kollabiert das Quantenbit zufällig.

$$
|\alpha|^2 = \text{Wahrscheinlichkeit, dass das Qubit zu } |0\rangle \text{ kollabiert.}
$$

Alle anderen Zustände (Superpositionen) sind bei und nach der Messung irrelevant.

[[03 - Bloch-Kugel]]
[[02 - Verschränkung]]
[[02 - Quantengatter]]


### 02 - Verschränkung
Mathematischer Beweis, dass, wenn gemessen wird, also der Zustand kollabiert wird, das verschränkte Quantenobjekt ebenfalls EINEN bestimmten Wert einnehmen muss, bei deren Messung.

Beispiel:
$$
|\psi\rangle = \frac {1}{\sqrt{2}} \left( |00\rangle + |11\rangle \right)
$$
Wenn das erste Qubit mit einer Chance von 50% zu $|0\rangle$ kollabiert muss das zweite ebenfalls zu $|0\rangle$ kollabieren.
![[{A74AE3D1-BEFE-45CA-B0A8-DDC40214492A}.png]]
Bell-State

### 03 - Blochkugel
![[{1742FD17-5D03-493D-990A-A011FFA5150D}.png]]
Superposition ist alles, außer genau im Nord- oder Südpol. Am Äquator herrscht eine 50/50 Chance, zu einem der beiden Zustände zu kollabieren


## 01 - Deutsch-Josza-Algorithmus

Erster Quantenalgorithmus, der ein Problem schneller lösen kann als ein klassischer Algorithmus.
NICHT dazu da, um Rechenprobleme zu lösen
f ist ein Orakel / eine BlackBox, also unbekannt

Problem:
$$
f: \{0,1\}^n \to \{0,1\}
$$
Eingabe von x mit 
$$
0 \le x \le 2^n-1
$$

Klassischer Algoritmus:
Mindestens 
$$
2^{n-1} +1
$$
Überprüfungen, um sicher festzustellen, dass
1. f ist konstant, also jedes $f(x) = 1$ oder jedes $f(x) = 0$ oder
2. f ist balanciert, also die Hälfte aller $f(x) = 1$ und die andere Hälfte $f(x) = 0$.

Quantenalgorithmus:
![[{9F60E4C4-FB1B-41BE-84A5-178AEA694044}.png]]
...

[https://de.wikipedia.org/wiki/Deutsch-Jozsa-Algorithmus]()

## 02 - Grover-Algorithmus
Findet ein Element in einer unsortierten Folge.
[https://www.youtube.com/watch?v=RQWpF2Gb-gU]() Teil 1
https://www.youtube.com/watch?v=Dlsa9EBKDGI Teil 2
Funktioniert, indem die Wahrscheinlichkeit, dass das Ergebnis bei der Messung richtig ist, auf 100% erhöht wird. 
erster Suchalgorithmus mit
$$
O(\sqrt{N})
$$
bei einer unsortierten Folge.
## 03 - Shor-Algorithmus

Zerlegt jegliche Zahl sehr schnell in ihre Primfaktoren.
Wächst polynomiell.
Risiko für Verschlüsselungsverfahren, die auf der Schwierigkeit, große Primzahlen in ihre Primfaktoren zu zerlegen, basieren.
## Quantencomputing mit Q# 
In diesem Kapitel werden die Quantenalgorithmen in Q# gezeigt und anschließend der Code erläutert. Weiter wird liegen mathematische Ausdrücke sowie das jeweilige Quantengatter bei.

Zu den Codes:

**open Microsoft.Quantum.Intrinsic;** macht alle Funnktionen, die in Microsoft.Quantum.Intrinsic bereitgestellt werden für die Verwendung in einem Q#-Notebook oder einer Quelldatei verfügbar, ohne dass ihre vollständigen Namen angegeben werden müssen.

# Quanten-Zufallszahl (0 oder 1)


namespace QuantumRandom {
    open Microsoft.Quantum.Intrinsic;

    @EntryPoint()
    operation RandomBit() : Result {
        use qubit = Qubit();
        H(qubit);           // Hadamard-Gate anwenden
        let result = M(qubit); // Messen
        Reset(qubit);       // Qubit zurücksetzen
        return result;      // Ergebnis: Zero (0) oder One (1)
    }
}

- Quibit initialisieren:
	- use qubit = Qubit();` erstellt **ein** Qubit im Zustand |0〉
- Dann bringen wir das Qubit mittels Hadamard-Gate in Superposition (0 und1)
	- H(qubit) wendet das **Hadamard-Gate (H)** an:
	- $$ H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}} $$
	- Das Qubit ist jetzt in einer 50/50-Superposition von |0〉 und |1〉
	- Mit M(qubit) leiten wir den Messvorgang, was die Superposition unverzüglich kollabieren lässt und dich das Qubit für 0 oder 1 entscheidet. Man stelle sich dazu einen Münzwurf vor, die nach dem Wurf in der Hand gefangen wird und beim Öffnen (Messen) ihren Zustand 0 oder 1 preisgibt.
	- Mit Reset(qubit) setzen wir das Qubit auf 0, da es für die Quantenhardware nötig ist.

	- Quantengatter:
		Hadamard-Gate (H): Es erzeugt die Superposition aus |0〉
		
	- $$ H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} $$

# Bell-Zustand (Verschränkung)

namespace BellState {
    open Microsoft.Quantum.Intrinsic;

    @EntryPoint()
    operation CreateBellPair() : (Result, Result) {
        use (q1, q2) = (Qubit(), Qubit());
        H(q1);          // H auf q1
        CNOT(q1, q2);   // CNOT zwischen q1 (Control) und q2 (Target)
        let r1 = M(q1); // Messen von q1
        let r2 = M(q2); // Messen von q2
        ResetAll([q1, q2]);
        return (r1, r2); // Ergebnisse sind immer gleich!
    }
}

- Für die Verschränkung benötigen wir **zwei** Qubits |00〉
	- Wir wenden das Hadamard-Gate auf Qubit 1 an **H(q1);**
		 $$ H_1|00\rangle = \frac{|00\rangle + |10\rangle}{\sqrt{2}} $$
- Hier lassen wir als nächstes beide Qubits das CNOT-Gate passieren mit **CNOT(q1, q2);**
	- $$ \text{CNOT}\left(\frac{|00\rangle + |10\rangle}{\sqrt{2}}\right) =$$
	- und die beiden Qubits befinden sich nun im Bell-Zustand: $$= \frac{|00\rangle + |11\rangle}{\sqrt{2}} $$
- Jetzt messen wir wieder unseren Münzwurf, aber dieses Mal mit **zwei** Münzen gleichzeitig und erhalten beim Öffnen der Hand (Messung) bei beiden Qubits immer |0〉 oder |1〉 aufgrund der Verschränkung (Ergebnisse sind immer gleich!). Beide Qubits stehen somit immer in Korrelation: $$ P(00) = \frac{1}{2}, \quad P(11) = \frac{1}{2} $$

- Quantengatter (CNOT):   
-  *Wenn das Kontrollqubit (q1) |1〉 ist, dann flippt das Zielqubit (q2) immer*
  $$ \text{CNOT} = \begin{pmatrix} 
  1 & 0 & 0 & 0 \\ 
  0 & 1 & 0 & 0 \\ 
  0 & 0 & 0 & 1 \\ 
  0 & 0 & 1 & 0 
  \end{pmatrix} $$

# Deutsch-Jozsa-Algorithmus


namespace Deutsch {
    open Microsoft.Quantum.Intrinsic;

    operation BalancedOracle(q : Qubit) : Unit {
        X(q); // Flippt |0〉 ↔ |1〉 (balancierte Funktion)
    }

    @EntryPoint()
    operation CheckIfConstant() : Bool {
        use (q1, q2) = (Qubit(), Qubit());
        X(q2);       // q2 auf |1〉 setzen
        H(q1); H(q2); // Superposition beider Qubits
        BalancedOracle(q1); // Orakel anwenden
        H(q1);       // Interferenz erzeugen
        let result = M(q1) == Zero; // Messen
        ResetAll([q1, q2]);
        return result; // True = konstant, False = balanciert
    }
}



$$H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}$$