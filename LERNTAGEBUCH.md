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

Das Programmieren ist mit schwer gefallen - KI hat ausgeholfen - und es bedarf dringend Nachholbedarf. Beim Verstehen von Codezeilen hat mir ein Arbeitskollege das Debuggen in Visual Studio Code gezeigt und es half mir sehr, eine Funktion zu verstehen (Aha-Effekt).

**def lineare_Suche(data, Zielwert):
    """Durchsucht eine Liste nach einem Zielwert (lineare Suche)."""
    for Index, Element in enumerate(data):  # Ein Durchlauf über alle Elemente
        if Element == Zielwert:
            return Index  # Gefundener Index
    return "nicht gefunden"  # Nicht gefunden

**"Beispielaufruf"
numbers = [4, 2, 7, 1, 9, 5]
numbers2 = [3, 8, 6, 0, 2]
target_value = 2

**Ergebnis = lineare_Suche(numbers2, target_value)
print(f"Der Wert {target_value} wurde im Index {Ergebnis} gefunden.")
print(numbers)

Ich verstand nicht, wo das Array numbers oder numbers2 von der Funktion lineare_Suche() verwendet wird. Mir wurde es sehr gut vom Kollegen erklärt und die Debuggingfunktion half, mir den Prozess zu durchlaufen Schritt für Schritt. 
Der oben angegebene Algorithmus stellt eine O(n) Laufzeitkomplexität dar, da die for-Schleife n-Schritte durchläuft bis zu einem Ergebnis. Wären 2 for-Schleifen gekoppelt dann gilt: O(n*n) = O(n²). Der Aufwand erhöht somit und für jede Mengeneingabe steigt der Aufwand nun quadratisch an anstatt linear wie bei O(n). 
Die O-Notationen oder auch Landaunotationen geben die Laufzeitkomplexität in Abhängigkeit zur Eingabemenge an. 

Gefühlt habe ich heute nicht viel geschafft, allerdings ist der Lerneffekt dafür nachhaltig und das Gelernte wird nicht so schnell wieder vergessen.

# Tag 12 (20.06.2025):
  - Python: Pandas -> Scatterplotts und Korrelationen
            Numpy Arrays
            Training -> Funktionen schreiben

Heute habe ich das Programmieren mit Python trainiert und einen Datensatz analysiert und visualisiert. Da das Programmieren noch nicht so leicht von der Hand geht, habe ich einige Funktionen geschrieben [[Python - Funktionen]] 

Der heutige Tag stimmt mich traurig, da mein Vorgesetzter nicht zufrieden mit mir ist und das Gefühl hat, so habe ich es zumindest verstanden, dass ich nicht genügend Interesse für Informatik mitbringe. Das ist für mich unverständlich. 

# Wochenende (22.06.2025):
  - Fahrplan nach " 1, 2, 3 Daily" angepasst

Fahrplan nochmals angepasst mit klarem Ziel: Quantenalgorithmen in der Logistik zum Einsatz bringen. Der Weg dorthin wird im Dreiklang (1,2,3 Daily) von Quanteninformatik, Daten und Prozesse begleitet und harmoniert perfekt mit 
dem Fach des Daten- und Prozessanalysten. Der Höhepunkt wird das Projekt sein, welches den Titel "Hybride Optimierung von Logistikrouten: Quantenalgorithmen (QAOA) vs. klassische Methoden am Beispiel Traveler-Salesman-Problem" tragen wird.

Ich schätze das Ziel als sehr ambitioniert ein und denke, dass die verbleibenden acht Monate nicht ausreichen werden, allerdings irre ich mich auch gerne. 

# Tag 13 (23.06.2025):
  - Quantenmechanik zum Anfassen [Youtube](https://www.youtube.com/watch?v=LaGPEWb1VFk)
    * Quantengatter
  - Daten: Distanzmatrix in Python, Daten beschaffen, in Python einlesen und Berechnungen durchgeführt
  - Prozesse: BPMN-Model eines Störungsfalls in der Logistikbranche

Quantenmechanik:
Der Vortrag von Prof. Dr. Steffen Glaser Quantenmechanik zum Anfassen veranschaulicht sehr gut, wie sich Qubits verhalten, wenn man Sie manipuliert. 
Hadamard-Gatter: bringt in Superposition, CNOT-Gatter in Abhängigkeit zu Qubit X: Verschränkung zweier Qubits, Messgatter: Messung
Die Schaltkreise sind ideal, um besondere Algorithmen zu entwerfen. 

Daten:
Die Entfernungen zueinander, von 48000 Städten zu berechnen, scheiterte an der Hardware meines Laptops. 2000 Städte täten es auch. Bei der Berechnung der Entfernung bediente
ich mich der Haversine-Formel in Python. 
Größte Hürde war es, die CSV auf 2001 Zeilen runter zu kürzen und diese in Python wieder einzulesen. Python fand die Spalten auf Mal nicht mehr. Die CSV hatte ich mit EXCEL 
bearbeitet. Zwei Stunden habe ich rumprobiert, bis mit Notepad ++ die Erlösung möglich war, die CSV zu bearbeiten und dann von Python einlesen zu lassen. Woran es lag 
weiß ich allerdings immer noch nicht. Aber ich hab das Problem zunächst erstmal selbst gelöst. 

Prozesse: 
Das BPMN-Modell stellt ein Szenario in der Logistikbranche eines Logistikunternehmens dar. Rund 15000 Frachten müssen innerhalb kürzester Zeit neu disponiert werden. Hier
soll verdeutlicht werden, dass darüber beschieden werden muss, ob und in welchem Maße Quantentechnologien zum Einsatz kommen soll, um die 15000 Frachten binnen kürzester zeit
umzudisponieren.


# Tag 14 (24.06.2025):
  - Buch: Learn Quanten Computing with Python and Q# (Seite 1-18)

Quanten:
Das Buch Learn Quantum Computing with Python and Q# hat einen für mich wesentliche Aspekt auf den ersten Seiten geliefert. Quantencomputer werden vorerst nur
spezielle Aufgaben lösen können und des Weiteren sind sie hinsichtlich der Eingabemenge sehr begrenzt. Lediglich Eingaben von höchstens ein paar dutzend Bits 
können Quantensysteme der heutigen Größe aufzeichnen. Und zu guter Letzt gibt es auch bisher keine festen Regeln, um zu entscheiden, welche Aufgaben am besten
auf klassischen Computern und welche Aufgaben die Vorteile von Quantencomputern nutzen können.

Daten:
Die Datenbank über die Städte und unter anderem ihre Koordinaten habe ich die Spalte Liefermenge in Paletten hinzugefügt. 
LKWs laden Paletten, die irgendwo hin müssen. Die Städte haben jetzt Liefermengen zugeteilt bekommen womit man jetzt Routen planen kann, wie und wo ein LKW hinbringt und oder auflädt. Die Komplexität für einen Algorithmus wird sich erhöhen. Um wie viel, das werde ich in Kürze herausfinden. 
"Quintessenz": Die Komplexität vor der die Logistik an sich steht ist immens und gar nicht mehr vorstellbar. 

Prozesse:
Digitaler Zwilling: Wie schon mit Klaus besprochen bietet der digitale Zwilling Möglichkeiten der Daten- und Prozessanalyse. Gerade beim Abbild von Maschinen, ganzen Produktionsanlagen oder sogar ganzer Unternehmen oder Konzerne kommen 
unermesslich viele Daten zusammen, die gerade dazu einladen analysiert und benutzt zu werden, um Prozesse zu optimieren im Machine Learning einzusetzen oder Statistiken für Verhalten, Abnutzung, Vorhersagen, Unternehmensentscheidungen und vieles mehr zu erstellen.

ActiveDB:
Laut Internet und Youtubeauftritten eines Partners der Firma bill-x kann ActiveBD als Schnittstelle mit der Fülle an Daten 
, die in Maschinen anfallen umgehen und damit zugleich Kunden- und Unternehmenspreferenzen gerecht werden. 


# Tag 15 (25.06.2025):
  - Q#: Versuch, Q# unter Visual Studio Code zum Laufen zu bringen
    * Versuch, Code zum Laufen zu bringen gescheitert
  - Qiskit: Versuch, in Qiskit Algorithmen zu starten und zu visualisieren gescheitert
  
Quanten: Q#-Code zum Laufen zu bekommen ist gescheitert. Zunächst habe ich versucht die Umgebung in Visual Studio Code für Q# herzustellen. Daran bin ich kläglich gescheitert. 
         Co-Pilot konnte mir weitestgehend helfen, bin aber auch damit bei einem Schritt gescheitert. für Q# war eine Installation von Nöten und .Net Version 6.0.42, die explizit nur mit Visual Studio Code kooperiert. Nachdem ich mehrere .NET Versionen probiert hatte, habe ich gemerkt, dass ich die Umgebungsvariabel ändern musste. Darüber hinaus musste
         ich auch feststellen, dass ich mehrere Python Versionen installiert hatte und musst die ältere Version deinstallieren. 
         Ab einem gewissen Punkt wollte ich auf Conda umschwenken und ab da an ging gar nichts mehr. 
         Zurück zu Visual Studio Code habe ich es nach Stunden endlich hinbekommen die Umgebung so einzurichten, dass ich im Prinzip beginnen konnte zu programmieren.
         Gleich habe ich zwei Codes in Q# aus dem Buch "Learn Quantum Computing with Python and Q#" ausprobiert, die nicht funktionierten. Das Buch verwies auf ein 
         Repository, dass alle Code-Zeilen aus dem Buch enthält (https://github.com/crazy4pi314/learn-qc-with-python-and-qsharp) Leider ohne Erfolg. 
         die beiden Beispiele aus dem Buch liefen lediglich nach Korrektur auf (https://quantum.microsoft.com/en-us/tools/quantum-coding)
         Die Code-Zeilen aus dem Repository sind drei Jahre alt. Wahrscheinlich hat sich seither einiges geändert, ist meine Vermutung. Ricarda konnte mir leider auch 
         nicht helfen. Kai hat es geschafft, dass die Fehlermeldung nach dem Ausführen eines Programms wegfiel indem wir die Namespaces im Code von Q# entfernten. 
         Nachdem über ein halber Tag draufgegangen ist, werde ich mich Qiskit und Python und Jupyter zuwenden, was bisher reibungslos funktionierte.

Qiskit, macht seit heute auch Probleme, denn es will nicht den Crover-Algorithmus starten weil es dann rummeckert, dass bestimmte Module nicht in den aus zu importierenden Modulen zu finden sind. Angeblich gibt es Versionsinkompatibilitäten zwischen Qiskit, Matplotlb und Numpy. Viel zu lange probiere ich mehrere Versionen aus durch deinstallieren und installieren. Ich kann zwar Quantenalgorithmen anwenden, allerdings nicht visualisieren. 


# Tag 16 (26.06.2025):

- Einführung durch Kai in Obsidian
- Verknüpfen der Markdowndateien
- Erstellung von To-Do-Liste (Quests.md)
	- Latex Plugin für Obsidian (Zeigt unter anderen Formeln in Obsidian an aus Plaintext)
		* [Youtube](https://www.youtube.com/watch?v=FA0z7oR7OWc) 
	- Quantenalgorithmen programmiert und in eigener Markdown verständlich erklärt
[[Quantenalgorithmen Q Sharp]]
	- Erlaubnis erhalten von www.nobocham.de für Download von Koordinaten

Heute habe ich Obsidian kennen- und gleich schätzen gelernt. Die Möglichkeiten der intelligenten Verknüpfungen meiner Dokumentationen sind extrem nützlich gerade im Hinblick auf das Wissen, welches sich in der kommenden Zeit ansammeln wird. Alle Berührungspunkte von Quanteninformatik, Daten- und Prozessanalyse, der Ausbildung oder wenn es auch nur der Alltag oder Nebenschauplätze sind, können als Netzwerk, durch das man sich schnell bewegen kann, überschaubar angezeigt werden.

Auf der Microsoft Quantum-Coding-Seite (https://quantum.microsoft.com/en-us/tools/quantum-coding) lassen sich die Quantenalgorithmen ausprobieren in Q# ausprobieren und werden gleich geplottet. Erste Algorithmen, wie den (echten) Zufallsalgorithmus, Bell-Zustand (Verschränkung) und Deutsch-Jozsa-Algorithmus habe ich getestet und in meiner Wissensseite [[Quantenalgorithmen Q Sharp]] diese näher erläutert. Ich hatte mich bisher sehr schwer getan, aber **allein anhand des Codes konnte man die Algorithmen auf Anhieb verstehen**. 

Allein der Zufallsalgorithmus könnte in wichtigen Bereichen, wie der Kryptografie eingesetzt werden. Es könnten Echte Zufallsschlüsselgeneriert werden. Eine Rückrechnung wäre dann nicht mehr möglich. 
Überall im Bereich KI, wo es Psyeudozufallsalgorithmen gibt oder z.B. in der Wirtschaft (Monte-Carlo-Simulationen).

Die Koordinaten von Hauptstädten weltweit
 darf ich nun offiziell runterladen nach einer Anfrage vom 23.06.2025 und für die Datenanalyse nutzen.
## Problem Github und Anzeigen von Plaintext: 
[[Quests#1. Es gibt Probleme mit der Vorschau in Github. Plaintext von mathematischen Formeln wird von Github Preview mal als Formel dargestellt und mal nicht. Ich finde bisher keine Lösung]]

# Tag 17 (27.06.2025):
- Quanten: Quantum IBM Composer (https://quantum.ibm.com/composer/files/4cccdbc18766adc14b8a6e4c77856e529ee24663b69dbccc3de528db3d4be757)
Allerdings benötigt man einen Account, den Schaltkreis zu testen. 
- Webscraping der Koordinaten von www.nobocham.de
- Berechnung der Entfernungsmatrix in Jupyter

Mit dem Quantum Composer von IBM kann man sich eigene Schaltkreise zusammenstellen. Darin gibt es reichlich Einstellungsmöglichkeiten und Gatter. Nur leider ist für das Ausführen 
ein Account nötig, der für eine gewisse Zeit kostenlos ist.
[[DOCUMENTATION#Tag 17 (27.06.2025)]]
## To-Do
- Hierzu befrage ich Klaus, ob ich einen Zugriff bekommen kann
[[Quests]]

# Tag 18 (30.06.2025):
- Einrichtung Arbeitsplatz des Praktikanten.
- Planung und Ziele mit ihm besprochen. Ziel ist ein Miniprojekt in dem
wir Zufallsalgorithmen der klassischen Computer mit den Quantencopmputern
vergleichen.
- Einrichtung eines gemeinsamen Repostory mit dem Prakitkanten.
- Rundgang und Begrüßung der Kollegen im Betrieb.

Jonas der Praktikant bringt Programmierkenntnisse in Java mit und sein Lieblingsfach nach Informatik ist Mathematik. Ideal für mein Vorhaben, in Ihn Quantencomputing zu involvieren.
Jonas bekommt von mir einige Grundlagen in Python und Aufgaben für seinen ersten Tag. Weiter durfte er sich am Vormittag schon mit Lektüre über Quantencomputing einlesen. 
Gemeinsam führen wir ein Repository, welches er später nach seinem Praktikum unter anderem als Referenz nutzen kann. Ich freue mich auf die Arbeit mit ihm. Das miteinander ist von gegenseitigem Respekt erfüllt. 

Derweil Jonas sich an den Aufgaben versucht, richte ich nebenher noch das gemeinsame Repository ein, erstelle bzw. stelle Aufgaben bereit für ihn, die uns später in gewissen Teilen ins gemeinsame Projekt, welches für die zweite Woche angesetzt ist, begleiten. 

Mein Ziel ist nicht nur das Projekt, sondern auch, dass er auch einen Einblick in den Beruf des Fachinformatikers für Daten- und Prozessanalyse bekommt und sieht, dass QC und Daten- und Prozessanalyse sehr stark miteinander korrelieren.
[[DOCUMENTATION#Tag 18 (27.06.2025)]] 


# Tag 19 (01.07.2025):
- Vorbereiten und Bereitstellen von Aufgaben für Jonas
	- Tagesaufgabe für Jonas in Qunatencomputing und Datenverarbeitung:
	- Aus dem Buch oder via Internetrecherche
		Deutsch-Josza-Algorithmus
		Grover-Algorithmus
		Shor-Algrthmus

		Schaltkreise (Wie beeinflussen Gatter die Qubits?)
		Hadamard-Gatter
		X-Gatter 
		CNOT-Gatter
- Funktionalität von Quantum Composer ergründen
	- [Youtube](https://www.youtube.com/watch?v=j1NFdDx2tIQ) 

- Datenverarbeitung in Jupyter Notebook:
	- Daten aus CSV einlesen, visualisieren und als Bild speichern
	- Fehlererkennung im Code: Symantische, logische und Syntaxfehler
- Arbeit mit Jonas an den Aufgaben Datenverarbeitung und Visualisierung
- Einrichtung Account bei IBM für Open Plan (10 Minuten pro Monat)
- Planung morgiger Tag: Einrichtung Jupyter Lab Collboration

Der heutige Tag geht zeitlich sehr in die Vorbereitung der Aufgaben, die ich dem Praktikanten bereitstelle. Allerdings festigt es auch meine Kenntnisse in den Themen selbst.  Weiter betreue 
ich Jonas, wobei er keine wirkliche Betreuung benötigt und selbstständig lernt. Dinge, die er nicht weiß schlägt er einfach nach. Bisher hat er keine Fragen gestellt und die Aufgaben zu meiner vollsten Zufriedenheit gelöst. Wie er die Aufgaben löst, ist ihm freigestellt. 

Am Nachmittag arbeiteten wir gemeinsam an Aufgaben, die ich ihm gestellt habe. Thema: Datenverarbeitung und Visualisierung mit Jupyter Notebook. 

[[DOCUMENTATION#Tag 19 (01.07.2025)]] 


# Tag 20 (02.07.2025):
- Juan: 
	- IBM Account eingerichtet und erste Instanz erstellt (noch nicht genutzt)
		- 20 Minuten 0€/mon., Nur Rechenzeit wird abgezogen
		- Kreditkarte hinterlegt
	- Betreuung Jonas, 
	- Vorbereitung Aufgaben für Jonas (Sortieralgorithmen in Python)
	- Einrichtung Jupyter Lab Collaboration aus Sicherheitsbedenken abgebrochen
- Jonas:
	- Quantenalgorithmen (Deutsch, Grover und Shor) verstehen, aufschreiben in eigenen   Worten, was er versteht
	- Webscraping, Datenaufbereitung, Visualisierung, Einlesen, Speichern (Python)
	- Fehlersuche in Python-Code (Syntax, Semantik, Logik)

Jonas kommt sehr schnell voran. Ich gebe ihm unter anderem meist die Aufgaben, die wir für unser geplantes Miniprojekt brauchen werden. Ziel ist es ja den echten Zufall zu messen und diesen mit klassischen Zufallsalgorithmen zu vergleichen und statistisch auszuwerten. Er benötigt Kenntnisse in Python, Qiskit und Q# sowie den klassischen und Quantenalgorithmen. Das Projekt planen wir, nächste Woche, den 07.07.2025 zu beginnen. 

Heute ist viel wieder viel Zeit ins Land gegangen für Fehlerbehebungen. Die Aufgabe in Webscraping konnte Jonas nicht erfüllen, weil die Webseite, von der ich zuvor eine schriftliche Genehmigung für den Download ihrer Daten (Koordinaten von Hauptstädten) eingeholt hatte, nicht auf unsere Requests durch Python geantwortet hatte. Nachdem mittlerweile noch 2 weitere Kolllegen in unser Problem involviert waren, konnte uns Kai immerhin eine html-Datei mit dem Programm Curl beschafft. Gedacht war, dass wir in Python uns den Text der Seite anezigen lass und die Daten dort rausziehen und weiterverarbeiten.

Weiter fehlte plötzlich mein Notebook in Jupyter, welches ich im Browser laufen habe, was über Anaconda bereitgestellt wird.  Wo war es? Es war da, wurde aber nicht angezeigt, weil ich eine neuere Version von Jupyter installiert hatte (ver. 4.4.0), die nicht mit Notebook kompatibel war. 
Natürlich konnte mir keiner helfen, aber man ist umso glücklicher, wenn man es doch allein hinbekommt das Problem aufzudecken. Nach unzähligen Versuchen irgendwie Kernel und Packages zu de- und zu reinstallieren, gab ich dann auch nach und habe Anaconda, welches Jupyter bereitstellt komplett vom Rechner gefegt und wieder neu installiert. Den Browsercache habe ich auch gleich gelöscht. Und Hura das Problem bestand immer noch, dass Jupyter mir kein Notebook angezeigt hatte. Probleme und oder Fehler zu finden kann viel Zeit in Anspruch nehmen. Es bedarf auch einer gewissen Beharrlichkeit nicht locker zu lassen und vor allem, nicht auszurasten Ò.ó
[[DOCUMENTATION#Tag 20 (02.07.2025)]] 

# Tag 21 (03.07.2025):
- Juan: Mit Jonas Qiskit Einführung in Jupyter Notebook gemacht
	- Simulation von diversen Schaltkreisen mit einem, zwei und mehr Qubits
	- Aufgaben vorbereitet: 
	- Neuronale Netzwerke - Neuronenales Netz erstellen mit Test- und Lerndaten füttern, Ergebnisse Auswerten
	- 
	 Vorbereitung in Jupyter Notebook auf echte Quantenhardware
- Jonas: Introduction to Qiskit by IBM in Jupyter Notebook
	- Neuronale Netzwerke in Python

Die Einführung in Qiskit bei IBM war auf Englisch. Glücklicherweise kann Jonas sehr gut englisch verstehen und er mir bei einigen Stellen ausgeholfen hat. Wir haben Qiskit insoweit vorbereitet, dass wir nächste Woche zum Projekt zusammen den Zufallsalgorithmus auf einem echten Quantencomputer laufen lassen können. Wir sind somit einen bedeutenden Schritt weiter.

Jonas interessiert sich auch für maschinelles Lernen und hat Aufgaben von mir bekommen an denen er heute ein wenig zu beißen hatte. Wir haben einige Hürden zusammen gelöst und er wird morgen noch weiter daran arbeiten. Er erstellt ein neuronales Netzwerk (NN) in Python und soll es morgen trainieren mit Trainingsdaten und eine Besonderheit beim Maschinellen Lernen feststellen, nämlich wie das Delta Präzision des NN im Verhältnis zur Häufigkeit der Durchgänge von Trainingsdaten verhält. Er wird feststellen, umso öfter er das Netzwerk über die Traningsdaten laufen lässt, umso besser wird die Präzision bis zu einem gewissen Punkt allerdings nur.

Zu Jonas: Jonas Leistungen sind beachtlich. Er arbeitet so gut wie allein. Er braucht keine Hilfe, um
Fortschritte zu erzielen. Hier und da habe ich ihm ausgeholfen, aber mit der Zeit hätte er es auch selbst herausgefunden. Er ist frei im Bearbeiten der Aufgaben. Er schlägt oft auf Webseiten nach oder nutzt die ihm zur Verfügung stehende Literatur. 
Er ist ein sehr ruhiger und in sich gekehrter junger Mann. Er arbeitet sehr viel und vergisst oder will vielleicht auch keine Pause machen, zumindest heute erscheint es mir so. Ihm scheint es hier zu gefallen. Auf jeden Fall liegt ihm Informatik, Physik und Mathematik. 
Weiter ist mir aufgefallen, dass er fast zu ruhig ist. Das Reden mit ihm führt nie zu Gesprächen. Er antwortet atomar. Auch bekommt er manchmal den Mund nicht auf, als redet er in sich hinein, wo man, weil man ihn nicht versteht, nachfragen muss, was er denn gesagt hat. Sein Arbeitstempo ist moderat. Ich weiß von Menschen mit ähnlichen Zügen wie seinen, dass diese mit Stress nicht umgehen können, gerade wenn es darum geht Termine einzuhalten. Inwieweit, das Einfluss auf seine Karriere haben könnte, mag ich nicht zu beurteilen. 

Wenn wir das Projekt beendet haben, wird vielleicht noch etwas Zeit bleiben, weiter in Quantencomputing zu kommen. Für mich steht aber an erster Stelle sein Projekt, das  er bei Bewerbungen mit angeben kann. 


# Tag 22 (04.07.2025):

- Testen des Spiels SQL Spiels: Maja & Sophie
- Pflege und Korrektur meiner Obsidian-Vault:
	- Wissensdatenbankerweiterung: [[Python - Funktionen]] 
- Lineare Algebra: Mengen [[Lineare Algebra#Mengennotation]]  
- Jonas Tagesaufgabe: Alles gelernte der Woche nochmal kurz zu überfliegen,  Einführung in SQL mittels bereitgestellter Materialien und Lernspiel https://sql-island.informatik.uni-kl.de/
[[DOCUMENTATION#Tag 22 (04.07.2025)]] 


Das SQL Spiele Maja & Sophie weißt erhebliche Mängel auf. Angefangen mit dem ersten SQL-Befehl der eigentlich lediglich "SELECT Sternchen" beinhalten sollte bis hin zum Layout. Das Spiel ist noch lange nicht fertig meines Erachtens. 

Meine Obdsidian-Vault wächst und gedeiht. Mit den heutigen Tag werde ich die Struktur etwas anpassen und alles gelernte mit aufnehmen. Gerade die ersten 12 Tage meines Praktikums habe ich einiges gelernt und nicht festgehalten in der Obsidian-Vault sondern größtenteils außerhalb. Jedes Wissen, was hinzukommt soll in dieser Vault mit ins Netzwerk eingebunden und verknüpft werden.

Heute bin ich endlich ein Stück weiter in der Algebra gekommen und habe mir die Mengennotationen angeschaut. Und das war verdammt nötig, denn das Buch von Kaveh Bashiri "Quanen Computing" erscheint mir noch zu kryptisch mit seinen mathematischen Ausdrücken, aber so langsam entschlüsselt sich das Ganze. Es ist wirklich essentiell sich die mathematischen Grundlagen anzueignen, weil man sonst nicht weiter kommt.

Jonas legt heute wieder top Leistungen hin. Mich bestärkt das Gefühl, dass es ihm hier sehr gut gefällt. Er scheint sich hier wohl zu fühlen. Es ist auch ein gutes Gefühl, zu sehen, wie er Fortschritte macht. 


# Tag 23 (07.07.2025):

- Jonas und Juan: Für das Miniprojekt Zufallsalgorithmen nachschlagen, Beweisen von Zufällen mittels statistischer Mittel.

- Brainstorming mit Jonas zum Projektablauf
- Gespräch mit Jonas bezüglich seiner Zukunftschancen in der Daten- und Prozessanalyse im Bereich Quantencomputing.



Heute bin ich für unser kleines Projekt, mit dem wir mit statistischen Mitteln Zufallsalgorithmen in Python der Pseudozufälligkeit überführen wollen, auf ein kleines Problem gestoßen, welches wohlmöglich das Mini-Projekt zu einem großen oder gar undurchführbaren Projekt macht. 

Mit statistischen Mitteln eine Ausgabe von zufällig oder vermeintlich zufälligen Nullen und Einsen statistisch endgültig als Pseudozufall oder echten Zufall zu beweisen ist nicht möglich. Der Satz von Rice besagt, dass kein Programm eine zufällige Bitfolge als zufällige Bitfolge definitiv bestimmen kann. Meine Idee war, dass ich mit statistischen Mitteln Zufallsgeneratoren in Jupyter (Python) gegen den Zufall eines echten Quantencomputers, mittels Qiskit IBM antreten zu lassen. Der Quantencomputer generiert ja Zufällige Nullen und Einsen indem er das Qubit durch das Hadamard-Gatter laufen lässt. Das Problem hierbei, eine zufällige Abfolge von Bits könnte ein Muster erzeugen, dass in der statistischen Auswertung vermeintlich ein Muster erkennen lässt, dass wiederum als Pseudozufall gewertet werden kann sowie ein Pseudozufall statistisch als Nicht-Pseudozufall gewertet werden kann. Somit entsteht ein Dilemma bei der Beweisführung. 
Den ganzen Tag haben wir damit zugebracht uns mit Algorithmen und ihrer Pseudozufälligkeit zu beschäftigen und mit der Frage, wie man eine Ausgabe von 100.000 Nullen und Einsen statistisch als Zufall oder Pseudozufall überführen kann. 
Der random-Generator in Python zum Beispiel kann mit einem festen Seed von der Menge der ganzen Zahlen Z={..., -3,-2,-1,0,1,2,3, ...} gefüttert werden und gibt darauf hin eine pseudozufällige Zahl aus. Bleibt man bei der Eingabe des Seeds bei der Eins, wird auch immer der gleiche Wert ausgegeben, die generierte Abfolge deterministisch ist. Lässt man den Seed ganz weg, orientiert sich der Zufallsgenerator an Entropiequellen wie zum Beispiel der Systemzeit. Das macht Ausgabe keinesfalls zu einem zufälligen Ergebnis. Mit Hilfe des Run-Tests, Lempel-Ziv-Tests, Chi-Quadrat-Tests und der Autokorrelation lassen sich Tendenzen aufzeigen aber sie dienen nicht dazu, um mit absoluter Genauigkeit echten oder unechten Zufall zu bestimmen. 
Das Projekt werden wir dennoch wie gehabt fortführen und die Ergebnisse präsentieren, auch wenn wir die Beweisführung nicht zur Absolute bringen können. Dafür können wir am Ende die technische Beweisführung für die Pseudozufälligkeit bringen und die theoretische Zufälligkeit des Qubits bei seiner Messung beschreiben. Wir haben dann somit bewiesen, dass wir etwas nicht beweisen können und das erachte ich als mindestens genauso wertvoll an.

[[DOCUMENTATION#Tag 23 (07.07.2025)]] 

# Tag 24 (08.07.2025):
- Jonas: 
	- Quantenalgorithmus mit Qiskit programmieren (Simulation) mit 100.000 Shots, Speicherfunktion implementieren zur Weiterverarbeitung, statistische Untersuchungsfunktionen implementieren
	- Recherche: Wird IBM nach den 10 Minuten / Monat abgerechnet, falls der Job länger als die 10 Minuten dauert?
- Juan:
	- Morgenmeeting mit Ricarda -> (siehe [[DOCUMENTATION#Tag 24 (08.07.2025)]])
	- Vorbereitung und Bereitstellung Tagesaufgaben für Jonas
	- Start der schriftlichen Führung des Projekt: Zufall
		- Einführung
		- Technische Mittel
		- Klassische Zufallsgeneratoren (PRNG)
		- Quantenzufallsgeneratoren (QRNG)
		- Statistische Analyse und Theoretische Grenzen

Nach dem wir bemerkt hatten, dass wir mit unseren statistischen Mitteln keine absoluten Beweise liefern können, haben wir uns heute aufgemacht, das Projekt Zufall zu starten. Die nächste Frage, die uns ereilte war, ob die 10 Minuten, die uns monatlich von IBM zur Verfügung gestellt werden, ausreichen werden, um 100.000 mal ein Qubit in den Superpositionszustand zu versetzen, um von diesem ebenso viele zufällige Bits zurückzuerhalten. Wir überlegen es mit 10.000 Shots erstmal zu versuchen, denn uns liegt etwas die Zeit im Nacken. Der IBM Q-Computer wird auch von deren genutzt und wir kommen somit in eine Warteschleife, für die man aber nicht zur Kasse gebeten wird. Allerdings kann es je nach Aufkommen bis zu 24 Stunden dauern, bis die Anfrage ausgeführt wird. Für das Projekt haben wir nur noch drei Tage. Drei Tage, die der Praktikant noch hier ist. Hinzu kommt noch, dass wir nicht wissen, in welcher Form wir einen beendeten Vorgang bei IBM zurück bekommen. Liefern sie uns eine JSON oder sonstiges Format zurück oder bekommen wir die Antwort direkt an unser Programm übermittelt?

Während ich hier schreibe wurde unser erster Auftrag von IBM´s Quantencomputer erledigt. Es hat nur eine Sekunde gedauert für 1.000 Shots. Wir haben eine "echte" zufällige Reihe von Nullen und Einsen. Morgen werden wir die 100.000 Shots an IBM übergeben und sind gespannt, was dabei

# Tag 25 (09.07.2025):
- Jonas: 
	- Projektdurchführung: 100.000 Shots in den Quantencomputer (IBM) gemeinsam
	- Auswertung und Visualisierung der Daten des Quantencomputers
	- Programmierprobleme in Qiskit beheben.
- Juan:
	- Morgenmeeting mit Ricarda -> (Installation Reinigungsroboter)
	- Projektdurchführung: 100.000 Shots in den Quantencomputer (IBM) gemeinsam
	- Schriftlich: Dokumentation der Auswertung und Ergebnisse









[[DOCUMENTATION#Tag 25 (09.07.2025)]] 




# Tag 26 (10.07.2025):
Jonas: 
- schriftliche Dokumentation und Abschluss des Projektes
- Korrekturen vorgenommen
- SQL lernen


Juan: 
- schriftliche Dokumentation und Abschluss des Projektes
- Korrekturen vorgenommen
- Antrag für bessere Hardware (Laptop)
- Teams- und Maileinrichtung bei Iniationware
- Firmenkultur: Arbeiten mit KI




[[DOCUMENTATION#Tag 26 (10.07.2025)]]

