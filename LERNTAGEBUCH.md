# Praktikum_Daten-_und_Prozessanalyse -> Ziel: Quantencomputing

# Grober Fahrplan:
  - Englisch aufbessern (Lesen)
  - Literatur querlesen
  - Fortschritte/Arbeit Dokumentieren
## Themen:
  - Data Science
  - Doppelspalt
  - Bra-Ket-Notation
  - Superposition
  - Fairer Zufall
  - Verschränkung und wofür
  - Matritzen
  - Problem des Handelsreisenden (Grover-Algorithmus)
## Algorithmen
  - SQD
  - Deutsch-Jozsa-Algorithmus
  - Shor-Algorithmus
## Programmierung
  - Qiskit (IBM)
  - Q#
  - Anaconda (jupyter, PostgreSQL)


# Beginn Lerntagebuch (19.06.2025), Praktikumsbeginn (04.06.2025):

    In diesem Tagebuch werden meine Lernfortschritte, Misserfolge, Erkenntnisse, Ergebnisse sowie offenen Fragen festgehalten. Das Tagebuch beginnt mit dem 19.06.2025. Vermittelte Inhalte vor dem 19.06.2025 sind in DOCUMENTATION.md notiert und werden täglich festgehalten. 
    Das Lerntagebuch dient zum einem, das gelernte systematisch zu dokumentieren, zu verarbeiten und zu reflektieren, um so den Lernprozess nachhaltig zu gestalten. Weiter dient es auch als Nachweiß über erbrachte Leistungen (Proof Of Work). Zu Guter Letzt soll das Lerntagebuch einem digitalen Agenten übergeben werden, der mit dem Wissen Auszubildenden, Studierenden oder Lernenden unterstützen kann. 


# Woche 1+2 (04.06.2025 - 19.06.2025):
    Die ersten 2 Wochen waren zunächst recht unstrukturiert. Seit Tag eins habe ich einen groben Fahrplan an die Hand bekommen und einfach drauf losgelegt und die Themen oberflächlich und oder teilweise angegangen. Ich musste feststellen, dass ich zunächst erstmal mir Grundlagen aneignen muss um die Materie überhaupt angehen zu können. Des Weiteren gibt es sehr viele kleinere Unterthemen die es täglich nach und nach anzugehen gilt. 
    Dabei musste ich feststellen, dass einige Tools zunächst lernen musste zu bedienen. Angefangen der Umgang mit Gitkraken i.V.m. Github. 
    Zusammengfasst waren die ersten beiden Wochen keine fortschrittlichen Wochen.  Diese dienten zum Ankommen im Praktikumsbetrieb, zum Einrichten, zum Kennenlernen der Kollegen und zum Orientieren. Jetzt weiß ich grob, was ich alles an Skills benötige, um im Bereich Quanteninformatik mit Fokus auf Quantenalgorithmen foran zu kommen. 

# Tag 11 (19.06.2025):
  - Programmieren in Python lernen an: 
    * Matrixoperationen
    * Beispiele für O-Notationen (O[1], O[log n], O[n], O[n²], O[n!])
        Erklärung in Youtube angeschaut

Das Programmieren ist mit schwer gefallen - KI hat ausgeholfen - und Bedarf dringend Nachholbedarf. Beim Verstehen von Codezeilen hat mir ein Arbeitskollege das Debuggen in Visual Studio Code gezeigt und es half mir sehr, eine Funktion zu verstehen (Aha-Effekt).

def lineare_Suche(data, Zielwert):
    """Durchsucht eine Liste nach einem Zielwert (lineare Suche)."""
    for Index, Element in enumerate(data):  # Ein Durchlauf über alle Elemente
        if Element == Zielwert:
            return Index  # Gefundener Index
    return "nicht gefunden"  # Nicht gefunden

"Beispielaufruf"
numbers = [4, 2, 7, 1, 9, 5]
numbers2 = [3, 8, 6, 0, 2]
target_value = 2

Ergebnis = lineare_Suche(numbers2, target_value)
print(f"Der Wert {target_value} wurde im Index {Ergebnis} gefunden.")
print(numbers)

Ich verstand nicht, wo das Array numbers oder numbers2 von der Funktion lineare_Suche() verwendet wird. Mir wurde es sehr gut vom Kollegen erklärt und die Debuggingfunktion half, mir den Prozess zu durchlaufen Schritt für Schritt. 
Der oben angegebene Algorithmus stellt eine O(n) Laufzeitkomplexität dar, da die for-Schleife n-Schritte durchläuft bis zu einem Ergebnis. Wären 2 for-Schleifen gekoppelt dann gilt: O(n*n) = O(n²). Der Aufwand erhöht somit und für jede Mengeneingabe steigt der Aufwand nun quadratisch an anstatt linear wie bei O(n). 
Die O-Notationen oder auch Landaunotationen geben die Laufzeitkomplexität in Abhängigkeit zur Eingabemenge an. 

Gefühlt habe ich heute nicht viel geschafft, allerdings ist der Lerneffekt dafür nachhaltig und wird nicht so schnell wieder vergessen.

# Tag 12 (20.06.2025):
  - Python: Pandas -> Scatterplotts und Korrelationen
            Numpy Arrays
            Training -> Funktionen schreiben