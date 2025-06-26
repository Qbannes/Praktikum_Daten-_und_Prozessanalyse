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
		
<<<<<<< HEAD
	- $$ H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} $$
=======
		- $$ H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} $$
>>>>>>> origin/main

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
- Jetzt messen wir wieder unseren Münzwurf, aber dieses Mal mit **zwei** Münzen gleichzeitig und erhalten beim Öffnen der Hand (Messung) bei beiden Qubits immer |0〉 oder |1〉 aufgrund der Verschränkung. Beide Qubits stehen somit immer in Korrelation: $$ P(00) = \frac{1}{2}, \quad P(11) = \frac{1}{2} $$

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

