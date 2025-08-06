# Auf diesem Bild wird ein Vortrag oder Webinar über „Boltzmann Sampling using Quantum Annealer“ gezeigt. Dabei geht es um die Anwendung des Boltzmann-Samplings mit Hilfe eines Quantenannealers, einer speziellen Quantenmaschine für Optimierungsaufgaben.

Worum geht es?
- Das Thema ist, wie man mit einem Quantum Annealer sogenannte Boltzmann-Verteilungen abtastet (Sampling), um Optimierungsprobleme zu lösen.
- Erwünscht: Ideally, optimal solution in 1 measurement. Das Ziel ist es, in einer Messung die optimale Lösung zu finden.
- Realität: Approximate optimization, probabilistische Ergebnisse. In der Praxis liefert der Quantenannealer meist eine angenäherte und keine exakt optimale Lösung, und die Ergebnisse sind probabilistisch – das heißt, nicht jedes Mal exakt gleich reproduzierbar.
- Sampling: Probabilistisch, aber systematisch. Die Stichprobenziehung (Sampling) aus der Boltzmann-Verteilung erfolgt nicht rein zufällig, sondern nach festen mathematischen Regeln.

Formel unten:

$$p(\{\sigma_i^z\}) = \frac{1}{Z} e^{-\beta E(\{\sigma_i^z\})}$$

Hier wird die Wahrscheinlichkeit gezeigt, mit der eine Lösung in der Verteilung vorkommt. 
- $$ Z $$ ist die sogenannte Zustandssumme (normierende Konstante).
- $$ \beta $$ ist die inverse Temperatur, ein Parameter, der die „Schärfe“ der Verteilung bestimmt.
- $$ E(\{\sigma_i^z\}) $$ ist die Energie der jeweiligen Konfiguration.

Kurz gesagt: 
Der Quantum Annealer liefert Lösungen für komplexe Optimierungsprobleme, indem er Zustände gemäß einer Boltzmann-Verteilung abtastet. Das Sampling ist probabilistisch und bildet die Grundlage für moderne Quantenoptimierung.



# Dieses Bild zeigt eine weitere Folie aus dem Vortrag zum Thema „Boltzmann Sampling using Quantum Annealer“. Hier wird die zugrunde liegende Idee weiter illustriert, indem die Wahrscheinlichkeit, mit der bestimmte Energiestufen $$E_0, E_1, E_2, E_3$$ gesampelt werden, grafisch dargestellt wird.

Was ist zu sehen?
- Auf der rechten Seite sieht man ein Balkendiagramm, das die Wahrscheinlichkeit unterschiedlicher Energiestufen beim Sampling zeigt. Die niedrigste Energie $$E_0$$ („optimale“ Lösung) hat die höchste Wahrscheinlichkeit und damit den längsten Balken. Höhere Energiestufen ($$E_1, E_2, E_3$$) kommen mit zunehmend geringerer Wahrscheinlichkeit vor.
- Links bleibt die schriftliche Erklärung identisch zur Vorfolie:
  - Desired: Optimal in einer Messung die beste Lösung finden.
  - Reality: Nur näherungsweise optimale Lösung, und Ergebnisse sind probabilistisch, d.h. zufallsbasiert.
  - Sampling: Zwar zufällig, aber nach klaren mathematischen Regeln („systematic“), basierend auf der Boltzmann-Verteilung.

Die Kernaussage:
Die Wahrscheinlichkeit, mit der ein Quantenannealer bestimmte Zustände (Lösungen) findet, ist umso höher, je niedriger deren Energie ist. Dennoch können auch weniger optimale Zustände (mit höherer Energie) auftreten, allerdings mit geringer Wahrscheinlichkeit. Genau dies beschreibt die Formel und das Diagramm anschaulich: Lösungen mit niedriger Energie sind wahrscheinlicher, aber das Ergebnis ist generell zufallsgesteuert und folgt einer systematischen Verteilung.

Fachlicher Hintergrund:
- Das Boltzmann-Sampling sorgt dafür, dass das Auffinden der optimalen Lösung nicht garantiert, aber deutlich wahrscheinlicher ist als das Auftreten suboptimaler Lösungen.
- Dies ist ein zentrales Prinzip in der Optimierung mit Quantencomputern und Quantenannealern, vor allem bei komplexen Problemen, bei denen exakte Lösungen schwer zu berechnen sind.

Zusammengefasst: Das Bild veranschaulicht die Wahrscheinlichkeitsverteilung von Lösungen beim Quantum Annealing anhand von Energiezuständen, wobei optimale Lösungen bevorzugt, aber nicht garantiert sind.


# Auf dieser Folie wird die Bedeutung der Boltzmann-Verteilung in der Physik erläutert, insbesondere im Zusammenhang mit magnetischen Materialien und Objekten im thermischen Gleichgewicht.

Worum geht es?
- Boltzmann-Verteilung: Sie beschreibt, wie wahrscheinlich es ist, dass sich ein physikalisches System in einem bestimmten Zustand mit Energie $$ E $$ befindet, wenn es sich im thermischen Gleichgewicht befindet.
- Für magnetische Materialien: Die Formel gibt an, mit welcher Wahrscheinlichkeit ein bestimmter magnetischer Zustand ($$\{\sigma_i^z\}$$) auftritt.
  
  $$
  p(\{\sigma_i^z\}) = \frac{1}{Z} e^{-\frac{1}{k_BT} E(\{\sigma_i^z\})}
  $$
  - $$ Z $$ ist die Zustandssumme (Normierung).
  - $$ k_B $$ ist die Boltzmann-Konstante.
  - $$ T $$ ist die Temperatur.
  - $$ E(\{\sigma_i^z\}) $$ ist die Energie des Zustands.

Grafik unten:
- Die Grafik zeigt Balken für verschiedene Energieniveaus ($$E_0, E_1, E_2, E_3$$). Bei niedriger Temperatur ($$T$$ klein, daher $$\beta = 1/(k_B T)$$ groß) ist die Wahrscheinlichkeit sehr hoch, sich im Zustand mit der niedrigsten Energie ($$E_0$$) zu befinden. Die Wahrscheinlichkeit für höhere Energien wird schnell sehr klein.
- Kommentar in der Grafik: „Small T, large $$\beta$$“ deutet auf diesen Sachverhalt hin.

Zusammenfassung:
Die Boltzmann-Verteilung ist ein fundamentales physikalisches Prinzip, das beschreibt, wie sich Zustände nach ihrer Energie im Gleichgewicht aufteilen. Bei niedrigen Temperaturen dominieren die energieärmsten Zustände. Das gleiche Prinzip wird beim Quantum Annealing und in der klassischen Physik (z.B. für magnetische Materialien) genutzt.


# Dieses Bild vertieft die Erklärung zur Boltzmann-Verteilung und ihrer Relevanz für die Physik, speziell für magnetische Materialien.

Inhalt der Folie:
- Es wird erneut deutlich, dass die Boltzmann-Verteilung die Wahrscheinlichkeit beschreibt, mit der sich ein physikalisches System (z.B. ein magnetisches Material) im thermischen Gleichgewicht in einem bestimmten Zustand befindet.
- Die Wahrscheinlichkeit eines Zustands $$\{\sigma_i^z\}$$ mit Energie $$E(\{\sigma_i^z\})$$ folgt:
  $$
  p(\{\sigma_i^z\}) = \frac{1}{Z} e^{-\frac{1}{k_B T} E(\{\sigma_i^z\})}
  $$
  mit
  - $$ k_B $$: Boltzmann-Konstante
  - $$ T $$: Temperatur
  - $$ Z $$: Zustandssumme (Normierung)

Erklärung zu den zwei Diagrammen:
- Links („Small T, large $$\beta$$”): Niedrige Temperatur bedeutet, dass sich das System fast ausschließlich im energieärmsten Zustand ($$E_0$$) befindet. Nur sehr selten werden höhere Energienivieaus ($$E_1, E_2, E_3$$) besetzt.
- Rechts („Large T, small $$\beta$$”): Bei hoher Temperatur verteilen sich die Wahrscheinlichkeiten viel gleichmäßiger auf alle Energieniveaus. Nicht nur der Grundzustand ($$E_0$$), sondern auch höhere Zustände ($$E_1, E_2, E_3$$) werden relativ häufig angetroffen.

Fazit:
- Die Boltzmann-Verteilung erklärt, wie die Temperatur das Verhalten eines Systems bestimmt: Bei niedriger Temperatur dominieren tiefe Energien, bei hoher Temperatur sind viele verschiedene Energieniveaus besetzt.
- Genau dieses Prinzip ist grundlegend im Verständnis von thermischem Gleichgewicht und spielt eine zentrale Rolle sowohl in der klassischen als auch in der Quantenphysik (z.B. beim Quantum Annealing).


# Auf dieser Folie wird der Mechanismus des Quantum Annealing mathematisch dargestellt.

Was ist zu sehen?
- Die Folie beschreibt, wie das Hamilton-Operator ($$H(t)$$), der die Energie und das Verhalten des Systems bestimmt, sich mit der Zeit verändert:
  $$
  H(t) = A(t) H_x + B(t) H_z
  $$
- Zeitlicher Ablauf:
  - Zu Beginn ($$t=0$$) dominiert der Term $$H_x$$ (typischerweise ein sogenannter „Transverse Field“-Operator, der Quantensuperpositionen erzeugt).
  - Mit der Zeit wird $$H_x$$ immer schwächer und $$H_z$$ (das Problem-Hamiltonian, das die zu lösende Aufgabe kodiert) immer stärker, bis bei $$t = t_a$$ nur noch $$H_z$$ übrig ist.
  - Die Funktionen $$A(t)$$ und $$B(t)$$ geben an, wie stark die jeweiligen Teile zu jedem Zeitpunkt beitragen.

Bedeutung:
- Das System startet in einem leicht zu erreichenden Grundzustand von $$H_x$$ und entwickelt sich – falls langsam genug („adiabatisch“) – in den Grundzustand von $$H_z$$, der die Lösung des Optimierungsproblems darstellt.
- Dieses Prinzip ermöglicht es Quantencomputern, komplexe Probleme auf Basis von physikalischen Prozessen zu lösen.


# Diese Folie erklärt, wie der Mechanismus des Quantum Annealing zeitlich abläuft und welche Rolle die Umwelteinflüsse spielen.

Mathematischer Mechanismus:
- Wie auf der vorherigen Folie bleibt die zentrale Gleichung:
  $$
  H(t) = A(t) H_x + B(t) H_z
  $$
  Der Hamiltonian $$H(t)$$ wandelt sich im Zeitverlauf von $$H_x$$ (Anfangszustand, typischerweise ein einfach zu präparierender Quantenzustand) zu $$H_z$$ (dem Problem-Hamiltonian).

Zeitlicher Ablauf und Parameter:
- Die Annealing-Zeit $$ t_a $$ liegt typischerweise im Bereich von 5 ns bis 500 ns.
- Fast annealing: Zu Beginn (bei sehr kurzen Annealing-Zeiten) spricht man von „fast annealing“.
- Coherent evolution: In dieser Phase entwickelt sich das Quantensystem möglichst ungestört (kohärent), d.h. rein unter dem Einfluss seines eigenen Hamiltonians.
- Increasing Annealing Time: Je länger die Annealing-Zeit gewählt wird, desto mehr können Umwelteinflüsse (Dekoherenz, thermische Effekte etc.) eingreifen.
- Increasing role of the environment: Mit zunehmender Annealing-Dauer wird die Rolle der Umgebung (z.B. Störungen, Verluste, thermische Effekte) größer, was die ideale Quantenentwicklung beeinträchtigen kann.

Zusammengefasst:  
Die Steuerung der Annealing-Zeit und das Verständnis, wann das System noch eine weitgehend ideale Quantenevolution (kohärent) durchlebt und wann Umwelteinflüsse dominieren, ist entscheidend für die Leistung eines Quantum Annealers. Optimal ist die Balance: Langsam genug, um dem System die Chance zu geben, das globale Minimum zu finden (adiabatisch), aber nicht so langsam, dass Umwelteinflüsse überhandnehmen und Störungen das Ergebnis verfälschen.


# Diese Folie vertieft den Einfluss der Annealing-Zeit ($$ t_a $$) beim Quantum Annealing und erklärt, wie sich unterschiedliche Zeitbereiche auf den physikalischen Ablauf auswirken:

Zwei Zeitbereiche:
- Fast annealing ($$ t_a \in [5\,\mathrm{ns}, 500\,\mathrm{ns}] $$):  
  - In diesem kurzen Zeitfenster dominiert die "coherent evolution", also eine weitgehend ungestörte Quantenentwicklung, bei der das System nur minimal von der Umgebung beeinflusst wird.
- Slow annealing ($$ t_a \in [0.5\,\mathrm{\mu s}, 2000\,\mathrm{\mu s}] $$):  
  - Bei längeren Annealing-Zeiten nimmt der Einfluss der Umgebung zu. Neben der kohärenten Entwicklung tritt nun insbesondere die "thermalization of qubits" auf, also der Einfluss thermischer Prozesse auf die Qubits – sie können mit ihrer Umgebung Energie austauschen und thermisch ins Gleichgewicht geraten.

Zentrales Prinzip:  
Mit zunehmender Annealing-Zeit wird die Rolle von Störungen durch die Umgebung immer größer („Increasing role of the environment“). Je schneller das Annealing, desto eher bleibt das System kohärent (ideale Quantendynamik). Je langsamer, desto stärker machen sich thermische und andere Umwelteinflüsse bemerkbar. Die Wahl der richtigen Annealing-Dauer ist daher ein Balanceakt zwischen Quanteneigenschaften und Umweltkontrolle – entscheidend für ein optimales Ergebnis beim Quantum Annealing.


# Auf dieser Folie wird der Mechanismus des Quantum Annealing zusammengefasst und um Anwendungsbeispiele ergänzt:

Mechanismus:  
- Das System startet mit einem Start-Hamiltonian $$ H_x $$ (bei $$ t = 0 $$), der sich über die Zeit in das Problem-Hamiltonian $$ H_z $$ (bei $$ t = t_a $$) überführt:
  $$
  H(t) = A(t) H_x + B(t) H_z
  $$
  Dabei steuern die zeitabhängigen Funktionen $$A(t)$$ und $$B(t)$$, wie stark jeder Anteil ins Gewicht fällt.

Annealing-Zeitbereiche:
- Fast annealing ($$ t_a \in [5\,\text{ns}, 500\,\text{ns}] $$):  
  In dieser Phase dominiert die coherent evolution – eine nahezu ideale, störungsfreie Quantenentwicklung.
- Slow annealing ($$ t_a \in [0,5\,\mu\text{s}, 2000\,\mu\text{s}] $$):  
  Hier treten vermehrt Umwelteinflüsse auf, die zur Thermalisierung der Qubits führen, also zum Austausch von Energie mit der Umgebung und zu thermischem Gleichgewicht.
- Mit zunehmender Annealing-Zeit steigt der Einfluss der Umwelt weiter an.

Mögliche Anwendungen:  
- Machine Learning: Quantum Annealing kann für bestimmte Optimierungsprobleme im maschinellen Lernen genutzt werden, etwa zur effizienten Suche nach optimalen Parametern.
- Quantum Spin Models: Analyse und Simulation quantenmechanischer Vielteilchensysteme, insbesondere bei magnetischen Materialien oder Spingläsern.

Fazit:  
Quantum Annealing bietet spannende Möglichkeiten für Problemlösungen in Physik und Informatik, wobei das richtige Management der Annealing-Zeit und der Umgebungseinflüsse entscheidend für den Erfolg ist.


# Diese Folie behandelt die Herausforderungen ("Challenges") beim Einsatz von Quantum Annealers für Boltzmann-Sampling und verwandte Aufgaben:

### Herausforderungen im Überblick

1. Scrutiny:
- Es steht die Qualität des Samplings im Fokus, also wie gut und exakt der Quantum Annealer tatsächlich Boltzmann-verteilte Stichproben erzeugt. Hierzu gibt es intensivere Analysen und Vergleiche[1].

2. High Quality Sampling at LANL:
- Hohe Sampling-Qualität konnte jüngst am Los Alamos National Laboratory (LANL) beobachtet werden.
  - Verwendete Metriken: Total Variation Distance (TVD) und inverse Ising learning.
  - Für bestimmte Parameterbereiche wurde ein TVD von weniger als 5% erreicht, was auf sehr gute Nähe zur idealen Boltzmann-Verteilung hindeutet.

3. Kontrolle der Temperatur im System:
- Eine offene Herausforderung ist die Temperaturkontrolle, da die Temperatur das Sampling und die physikalischen Zustände direkt beeinflusst.
- Ansatz: Die Temperatur $$T$$ hängt umgekehrt proportional von der Kopplungsstärke $$J$$ im Modell ab ($$T \propto J^{-1}$$).
- Es gibt qualitative Beobachtungen, und für bestimmte physikalische Modelle passen diese Beobachtungen mit der Theorie überein.
- Forschungen zur Temperaturschätzung sind weiterhin ein wichtiges Feld.

Zusammengefasst:  
Zentrale Herausforderungen beim Quantum Annealing betreffen die Stichprobenqualität und die Kontrolle der (effektiven) Temperatur, die beide für zuverlässige physikalische und informationstechnische Anwendungen des Boltzmann-Samplings entscheidend sind. Fortschritte wie am LANL zeigen jedoch, dass unter optimierten Bedingungen hochwertige Ergebnisse erreichbar sind.


# Diese Folie behandelt den Ansatz zur Temperaturkontrolle beim Quantum Annealing (QA), insbesondere am Beispiel von D-Wave-Quantencomputern.

### Temperaturkontrolle beim Quantum Annealing

1. Einfaches Modell für den Quantum Annealer:
- Man gibt einen Problemhamiltonian $$ H_\text{input} $$ als Eingabe in den Annealer und führt eine „slow forward anneal“ durch (langsamer Anneal-Vorgang).
- Das System sampelt gemäß:
  $$
  P(\{\sigma_z^{(i)}\}) \propto e^{-\beta_\text{sampler} H_\text{input}(\{\sigma_z^{(i)}\})}
  $$
  - Hierbei ist $$ \beta_\text{sampler} $$ (die inverse Temperatur des Quantum Annealers) oft unbekannt und schwer exakt zu bestimmen.

2. Sampling für gezieltes $$ H $$:
- Will man für einen bestimmten Hamiltonian $$ H $$ eine kontrollierbare Effektivtemperatur realisieren, so skaliert man den Hamiltonian mit einem Faktor $$ J $$:
  - $$ H_\text{input} = JH $$
- Die neue Verteilung lautet:
  $$
  P(\{\sigma_z^{(i)}\}) \propto e^{-J\beta_\text{sampler} H(\{\sigma_z^{(i)}\})}
  $$
  Das ergibt eine effektive inverse Temperatur $$ \beta_\text{eff} = J \beta_\text{sampler} $$.

3. Fazit:
- Durch Skalieren des Hamiltonians ($$ J $$) kann man im Experiment auf verschiedene effektive Temperaturen zugreifen, auch wenn die reale Inverse Temperatur $$ \beta_\text{sampler} $$ des Annealers selbst unbekannt bleibt.
- Diese Methode ermöglicht es, verschiedene Temperaturbereiche künstlich zu simulieren und gezielt Sampling-Experimente durchzuführen, indem die Energie-Skala variiert wird.

Damit ist die Temperaturkontrolle beim Quantum Annealing zwar nicht direkt möglich, wird aber über das Reskalieren des Eingabehambamiltonians effektiv realisiert.


# Diese Folie behandelt das Konzept des Phasendiagramms und erläutert, wie sich bei bestimmten Bedingungen die Eigenschaften eines physikalischen Systems qualitativ verändern.

### Phase Diagram – Was ist das?

- Ein Phasendiagramm zeigt, in welchen Aggregatzuständen (z.B. fest, flüssig, gasförmig) sich eine Substanz in Abhängigkeit von Temperatur und Druck befindet.
- Es illustriert die qualitativen Änderungen der Systemeigenschaften: Geht das System von einer Phase in eine andere (z.B. von „Solid“ zu „Liquid“), ändern sich physikalische Eigenschaften sprunghaft.

### Beschreibung der Abbildung

- Die Grafik im Zentrum zeigt ein typisches Phasendiagramm, das auf der y-Achse den Druck und auf der x-Achse die Temperatur abbildet.
- Die Diagrammflächen sind farblich unterschieden für:
  - Solid (fest)
  - Liquid (flüssig)
  - Gas (gasförmig)
- Wichtige Punkte im Diagramm:
  - Freezing point at 1 atm: Der Gefrierpunkt, an dem Flüssigkeiten zu Feststoffen werden.
  - Boiling point at 1 atm: Der Siedepunkt, an dem Flüssigkeiten zu Gasen werden.
  - Triple point: Der Punkt, an dem alle drei Phasen im Gleichgewicht sind.
  - Critical point: Der Punkt, oberhalb dessen keine Unterscheidung zwischen Flüssigkeit und Gas mehr möglich ist.

### Zentrale Aussage

- Phase transitions: Das Diagramm visualisiert, wie kleine Änderungen von Temperatur oder Druck zu drastischen, qualitativen Zustandsänderungen führen können – ein fundamentaler Gedanke sowohl in der klassischen Thermodynamik als auch in modernen quantentechnologischen Anwendungen.


# Auf dieser Folie wird darauf hingewiesen, dass bestimmte Aspekte von Phasendiagrammen und Phasenübergängen besondere Aufmerksamkeit verdienen:

- Grenzlinien zwischen den Phasen:  
  Besonders wichtig sind die Grenzen, die verschiedene Phasen trennen, also die sogenannten kritischen Punkte und Linien. An diesen Stellen ändern sich die Eigenschaften des Systems sprunghaft und es kommt zu Phasenübergängen, wie z.B. beim Siedepunkt von Wasser.

- Universality und kritische Exponenten:  
  Diese Bereiche sind deshalb besonders interessant, weil sie universelle Eigenschaften zeigen, die unabhängig vom spezifischen Material gelten. Dieses Phänomen nennt man Universalität.  
  Hier spielen die sogenannten kritischen Exponenten eine zentrale Rolle – mathematische Größen, die beschreiben, wie sich physikalische Größen in der Nähe eines kritischen Punktes verhalten. Diese Exponenten sind universell für ganze Klassen von Systemen und erleichtern so das Verständnis fundamentaler Naturgesetze, sowohl in der klassischen als auch in der Quantenphysik.

Fazit:  
Die Untersuchung der Grenzen zwischen verschiedenen Phasen und der kritischen Phänomene erlaubt grundlegende Einblicke in die Natur und das Verhalten komplexer Systeme.


# Diese Folie nennt die zwei Hauptziele bei der Untersuchung von Modellen in der Physik (z.B. mit Hilfe von Quantencomputern oder im Kontext von Phasenübergängen):

### Zwei Hauptziele

1. „Map out“ the phase diagram:  
- Für ein gegebenes Modell soll das Phasendiagramm vollständig kartiert werden.  
- Ziel ist es, herauszufinden, in welchen Bereichen der Parameter- und Temperaturachsen sich verschiedene Phasen (z.B. Phase 1, Phase 2, Phase 3) befinden.  
- Dies gibt Aufschluss darüber, unter welchen Bedingungen das System einen qualitativen Zustandswechsel erfährt.

2. Extract critical exponents across critical lines:  
- An den Linien, an denen Phasenübergänge passieren (kritische Linien), sollen die kritischen Exponenten bestimmt werden.  
- Diese Exponenten charakterisieren, wie sich physikalische Größen in der Nähe des Phasenübergangs verhalten und erlauben es, fundamentale Gesetzmäßigkeiten („Universalität“) zu untersuchen.

Zusammengefasst:  
Forscher möchten zum einen das Phasendiagramm exakt bestimmen und zum anderen die kritischen Exponenten extrahieren, um ein tieferes Verständnis von Phasenübergängen und universellen Eigenschaften im betrachteten Modell zu gewinnen.


Diese Folie gibt einen Überblick über bereits durchgeführte Arbeiten mit D-Wave-Annealing-Quantencomputern im Zusammenhang mit der Erforschung von Phasendiagrammen und kritischen Exponenten.

### Bisherige Arbeiten („Prior work“)

D-Wave’s Annealer – Anwendung:
- D-Waves Annealer wurden gezielt für die Untersuchung von Phasendiagrammen und die Bestimmung kritischer Exponenten eingesetzt.

Konkrete Beispiele:

- Quantenphasentransitionen:
  - Triangular Ising anti-ferromagnet with transverse field: 
    Untersucht wurde ein Ising-Modell auf einem dreieckigen Gitter mit einem Querfeld[1].
  - Kibble-Zurek scaling in 1d TFIM using fast quantum quenches: 
    Das Kibble-Zurek-Skalierungsgesetz (wie sich Defekt-Dichten beim schnellen Durchlaufen eines Phasenübergangs verhalten) wurde am eindimensionalen Transversal-Field Ising Model (TFIM) mit schnellen Quantum Quenches überprüft.

- Klassische Phasenübergänge:
  - 3D Spin Glass Modell: 
    Auch klassische Phasenübergänge, wie beim 3D-Spinglas-Modell, wurden mit den Quantum Annealern analysiert.

Fazit:  
D-Wave-Quantencomputer werden bereits aktiv für die Kartierung komplexer Phasendiagramme und die Untersuchung sowohl quantenmechanischer als auch klassischer Phasenübergänge genutzt. Ein Fokus liegt dabei auf der experimentellen Bestimmung kritischer Exponenten und universeller Skalengesetze in verschiedenen Modellen.


# Diese Folie ergänzt die bisherigen Arbeiten („Prior work“) zur Nutzung von D-Wave-Quantum-Annealing für die Erforschung von Phasendiagrammen und legt zusätzliche Schwerpunkte:

### Weitere Schwerpunkte der bisherigen Arbeiten

1. Obtaining critical exponents:  
- Quantum phase transitions:  
  - Triangular Ising anti-ferromagnet with transverse field: Kritische Exponenten wurden für Quantenphasentransitionen in Ising-Modellen mit Querfeld bestimmt.
  - Kibble-Zurek scaling in 1D TFIM using fast quantum quenches: Experimente zur Kibble-Zurek-Skalierung bei schnellen Quenches am 1D Transversal-Field Ising Model.

- Classical phase transitions:  
  - Untersucht beispielsweise im 3D Spin Glass Modell.

2. Ground state phase diagram:  
- Es wurde das Phasendiagramm für Grundzustände ($$T=0$$ bzw. $$\beta=\infty$$) wie beim Shastry-Sutherland-Modell untersucht.

3. Kinetics in spin Ice models:  
- D-Wave-Annealer wurden auch zur Untersuchung der Kinetik (dynamische Prozesse) in Spin-Ice-Modellen eingesetzt.

Zusatzhinweis (blauer Kasten):  
- Trotz der zahlreichen Anwendungen („Numerous, but no temperature control“) fehlt bislang eine direkte Temperaturkontrolle bei diesen Experimenten. Die Studien erfolgten meist bei effektiver Nulltemperatur oder bei fest vorgegebenen Parametern; freie Wahl oder gezielte Steuerung der Temperatur war bisher nicht etabliert.

Fazit:  
D-Wave-Quantencomputer wurden bereits erfolgreich für die experimentelle Untersuchung und Modellierung von Phasendiagrammen, kritischen Exponenten und dynamischen Effekten in verschiedenen klassischen und quantenmechanischen Modellen eingesetzt. Eine offene Herausforderung bleibt jedoch weiterhin die präzise Kontrolle und Einstellung der Temperatur im Annealing-Prozess.


# Auf dieser Folie wird die Auswahl eines geeigneten Modells zur Leistungsbewertung („Benchmarking“) von Quantum Annealern angesprochen.

### Welches Modell soll untersucht werden?

Ziele für die Modellauswahl:
- Exakte Lösung bekannt:  
  Das Modell muss eine exakt bekannte Lösung besitzen, damit die Ergebnisse des Quantum Annealers objektiv überprüft und verglichen werden können.
- Kontrollierbarer geometrischer Frustationsgrad:  
  Es soll möglich sein, den Grad der geometrischen Frustration gezielt einzustellen. Geometrische Frustration beschreibt Situationen, in denen nicht alle lokalen Wechselwirkungen gleichzeitig energetisch günstig erfüllt werden können – ein entscheidender Aspekt vieler spannender physikalischer Systeme.

Kernaussage:  
Das Team hat ein perfektes Modell gefunden, das genau diese Bedingungen erfüllt. Dieses Modell eignet sich optimal für präzise Leistungs-Benchmarks und erlaubt vielfältige experimentelle Varianten bei bekannter Soll-Lösung.

Damit wird die Grundlage für die nächsten Schritte gelegt, in denen das ausgewählte Modell detailliert vorgestellt und in Messungen mit dem Quantum Annealer analysiert wird.

![Folie](5806805310885706191.jpg)


# Auf dieser Folie wird das sogenannte Piled-Up Dominoes (PUD) Modell vorgestellt, das als Benchmark für Quantum Annealer verwendet wird.

### Piled-Up Dominoes (PUD) Model

Eigenschaften des Modells:
- Das PUD-Modell interpoliert zwischen zwei physikalisch wichtigen Grenzfällen:
  - Dem klassischen 2D Square Ising Model ($$H_\text{Ising}$$), ein genau lösbares Modell aus der statistischen Physik[1].
  - Dem sogenannten Villain's ‘odd model’ ($$H_\text{Villain}$$), das eine spezielle Form von Frustration beinhaltet.

Mathematische Formulierung:
$$
H(s) = s H_\text{Villain} + (1 - s) H_\text{Square Ising}
$$
Mit expliziter Ausformulierung (siehe Formel auf der Folie):
$$
H(s) = -\sum_{\langle i,j \rangle_\text{blue}} \sigma_z^i \sigma_z^j - (1-2s) \sum_{\langle i,j \rangle_\text{red}} \sigma_z^i \sigma_z^j
$$
- $$\langle i,j \rangle_\text{blue}$$: Bindungen/Kanten auf dem Gitter mit Kopplung $$1$$ (blau markiert).
- $$\langle i,j \rangle_\text{red}$$: Bindungen/Kanten mit kopplungsabhängigem Wert $$1-2s$$ (rot markiert).
- Durch Variation von $$s$$ kann der Frustrationsgrad im System stufenlos geregelt werden.

Gitter-Darstellung:
- Rechts im Bild ist ein quadratisches Gitter abgebildet, auf dem die unterschiedlichen Wechselwirkungen (blau/rot) visualisiert sind.
- Die Balken oben zeigen die Stärke der jeweiligen Kopplungen in Abhängigkeit von $$s$$.

Warum dieses Modell?
- Es erlaubt einen kontrollierten Übergang zwischen einem einfach lösbaren und einem stark frustrierten, komplexen System.
- So kann systematisch getestet werden, wie gut der Quantum Annealer mit exakt bekannten Lösungen und unterschiedlichen Schwierigkeitsstufen zurechtkommt.
  
Fazit:  
Das PUD-Modell ist hervorragend geeignet, um sowohl die Leistungsfähigkeit als auch die Grenzen von Quantum Annealern hinsichtlich Komplexität, Frustration und Benchmarking objektiv zu bewerten.

![alt text](5806366360933087808.jpg)


# Diese Folie vertieft die Darstellung zum Piled-Up Dominoes (PUD) Modell und zeigt noch einmal, wie es zwei wichtige Grenzfälle in einem Modell vereinigt:

### Eigenschaften des PUD-Modells

Interpolation zwischen zwei Grenzfällen:
- Für $$s=0$$:
  - Das Modell reduziert sich exakt auf das 2D Square Ising Modell ($$H_\text{Ising}$$), ein Standardmodell der statistischen Physik mit rein blauen Kanten (Kopplung $$1$$).
- Für $$s=1$$:
  - Es entspricht Villain’s odd model ($$H_\text{Villain}$$), wobei die roten Kanten maximal negativ gekuppelt sind.

Allgemeine Form:
$$
H(s) = s H_\text{Villain} + (1-s) H_\text{Square Ising}
$$
bzw.
$$
H(s) = -\sum_{\langle i,j \rangle_{\text{blue}}} \sigma_z^i \sigma_z^j - (1-2s) \sum_{\langle i,j \rangle_{\text{red}}} \sigma_z^i \sigma_z^j
$$

- Die grafische Darstellung des Gitters rechts zeigt die beiden Kopplungsarten:
  - Blaue Linien: Immer Kopplungsstärke $$1$$
  - Rote Linien: Kopplung $$1-2s$$, d.h. sie gehen von $$+1$$ (bei $$s=0$$) bis $$-1$$ (bei $$s=1$$), sodass sich der Frustrationsgrad gezielt regulieren lässt.

Zusammenfassung:  
Das PUD-Modell vereint das klassische Ising-Modell und das stärker frustrierte Villain-Modell in einem einzigen, durch $$s$$ steuerbaren Rahmen. Diese Flexibilität macht es zum idealen Prüfstein, um die Leistungsfähigkeit von Quantum Annealern unter verschiedenen Bedingungen exakt und nachvollziehbar zu testen und zu benchmarken.

![alt text](5808755217448155413.jpg)


# Diese Folie zeigt, dass die exakte Lösung für das Piled-Up Dominoes (PUD) Modell bekannt ist und als theoretischer Referenzpunkt genutzt werden kann.

### Exakte Lösung des PUD-Modells

- Die exakte Lösung wurde in der Fachliteratur publiziert[1] und ermöglicht einen direkten Vergleich zwischen Theorie und Experiment (z.B. auf einem Quantum Annealer).
- Die zentralen Größen wie die Zustandssumme $$\mathcal{Z}$$ und die kritische Temperatur $$T_c(s)$$ des Modells sind analytisch bekannt.

Phasendiagramm (Grafik links):
- Die Grafik zeigt das Phasendiagramm des Modells in Abhängigkeit vom Parameter $$s$$ (Frustrationsgrad, y-Achse) und der Temperatur $$T$$ (x-Achse).  
- Es gibt drei Regionen:
  - Ferromagnetisch: Ordnung, Spins zeigen überwiegend in eine Richtung.
  - Antiferromagnetisch: Ordnung, Spins wechseln sich regelmäßig ab.
  - Paramagnetisch: Unordnung, Spins sind zufällig verteilt.
- Die Phasengrenzen sind analytisch bekannt – sie werden durch die exakte Lösung exakt berechnet.

Analytische Formel für die Phasengrenze:
$$
s_{\pm}(T) = 1 - \frac{T}{2} \sinh^{-1} \left(\frac{\pm 1}{\sinh(2/T)} \right)
$$
Diese Formel definiert die Grenzlinien im Phasendiagramm, die die verschiedenen Phasen voneinander abgrenzen.

Bedeutung für Quantum Annealing:
- Da die exakte Lösung gegeben ist, können Simulationen oder Messungen mit dem Quantum Annealer direkt mit der Theorie verglichen werden.
- So lassen sich Performance und Genauigkeit des Quantencomputers objektiv bewerten und gezielte Aussagen zu Abweichungen, Sampling-Qualität und Effekten von Temperatur und Frustration treffen.

Fazit:  
Das PUD-Modell eignet sich aufgrund seiner analytischen Lösbarkeit und der bekannten Phasengrenzen ideal als Benchmark für Quantum Annealer und erlaubt eine systematische Verbindung von experimenteller Quantenphysik mit theoretischer Statistikphysik.

![alt text](5808829507497474326.jpg)


# Diese Folie erklärt, wie man das Phasendiagramm experimentell mit einem Quantum Annealer, wie dem D-Wave-System, ermitteln kann:

### Vorgehensweise zur Bestimmung des Phasendiagramms

Schritte:
- Systemgröße wählen:  
  Es wird zunächst ein ausreichend großes physikalisches System (z.B. ein großes Gitter für das Modell) ausgewählt, um aussagekräftige Ergebnisse zu erhalten.
- Auf dem QPU einbetten:  
  Das Modell wird auf die Hardware-Architektur der Quantum Processing Unit (QPU), also den Quantenannealer, übertragen/abgebildet.
- Gitter aus Parametern untersuchen:  
  Für verschiedene Wertepaare von $$ (J^{-1}, s) $$ (inverse Kopplungsstärke und Frustrationsparameter) werden Messungen durchgeführt.
- An jedem Gitterpunkt berechnen:  
  Für jeden Punkt im Parameterraster werden die folgenden observablen Größen berechnet:

Gemessene Observablen:
- Mittlere Magnetisierung ($$ m $$):
  $$
  m = \frac{1}{N} \left| \sum_i \sigma_z^{(i)} \right|
  $$
  Sie gibt an, wie stark alle Spins (Qubits) im Mittel in dieselbe Richtung zeigen. Hohe Magnetisierung deutet auf eine geordnete (ferromagnetische) Phase hin.

- Mittlere gestaffelte Magnetisierung ($$ m_\text{AFM} $$):
  $$
  m_\text{AFM} = \frac{1}{N} \left| \sum_i (-1)^{x_i + y_i} \sigma_z^{(i)} \right|
  $$
  Diese Größe misst die antiferromagnetische Ordnung: Dabei wird zwischen benachbarten Gitterplätzen abwechselndes Vorzeichen berücksichtigt. Ein hoher Wert zeigt eine antiferromagnetische Phase an.

Ergebnis:  
Durch systematisches Abscannen des Parameterraums und die Berechnung dieser Observablen bei jedem Parameterpunkt lässt sich das vollständige Phasendiagramm des Modells experimentell rekonstruieren. Die unterschiedlichen Phasen werden anhand charakteristischer Werte von $$ m $$ und $$ m_\text{AFM} $$ erkannt. So können die theoretischen Phasengrenzen mit den realen, mittels Quantum Annealing erhaltenen, verglichen werden.

![alt text](5808955100931144043.jpg)


# Auf dieser Folie wird ein erster praktischer Schritt bei der Durchführung von Quantum Annealing-Experimenten vorgestellt:

### Main Steps with QA

Schritt 1: Systemgröße wählen
- Für das Experiment wird zunächst ein System (Gitter) mit festgelegter Größe ausgewählt.
- Das Beispiel auf der Folie zeigt ein 6 × 6 Torus-Gitter.
  - Ein Torus bedeutet, dass die Kanten des Gitters periodisch miteinander verbunden sind; das System hat also keine Ränder, sondern jede Seite ist mit der gegenüberliegenden verbunden. Das ist in der Physik üblich, um Randeffekte zu vermeiden und ein möglichst „unendliches“ System zu simulieren.

Illustration:
- Die Abbildung zeigt ein regelmäßiges Quadratgitter, auf das der PUD-Modell-Hamiltonian angewandt wird.

Bedeutung:  
Die Wahl der Systemgröße ist entscheidend, da sie die Balance zwischen Experimentierbarkeit auf echter Hardware und Aussagekraft zur Physik des Modells bestimmt. Kleinere Systeme sind einfacher auf Quantenhardware umzusetzen, größere Systeme liefern aussagekräftigere Ergebnisse in Bezug auf Phasenübergänge und Skalierungseffekte.

![alt text](5806452517977045572.jpg)


# Auf dieser Folie wird ein Beispiel für das „Embedding“ eines physikalischen Modells auf einem echten Quantenprozessor vorgestellt.

### Embedding: Example

Was bedeutet „Embedding“?
- Beim Quantum Annealing müssen theoretische Probleme (wie z.B. ein 2D-Gittermodell) physikalisch in die Hardware-Architektur des Quantencomputers übersetzt werden. Dieser Schritt heißt „Embedding“.
- Nicht jeder Knoten oder jede Kante des physikalischen Problems passt direkt auf die Hardware, weil reale Quantenprozessoren wie die von D-Wave spezielle Verbindungsmuster zwischen Qubits haben.

Details zum verwendeten Quantenchip:
- Advantage2_prototype2.6 device
  - Zephyr connectivity: Ein spezielles, hochvernetztes Architektur-Layout des D-Wave-Quantenprozessors.
  - 1248 Qubits: So viele Qubits stehen für das Embedding zur Verfügung.
  - 10,788 Couplers: Anzahl der Kopplungselemente, also Verbindungslinien zwischen den Qubits.

Spezifisches Beispiel:
- Die Grafik stellt ein reales Embedding dar:  
  In diesem Fall wurden 6 Einbettungen des Problems (z.B. mehrere Gitterkopien oder Experimente parallel) erfolgreich auf den Chip abgebildet.

Bedeutung:  
Das effiziente Embedding ist ein kritischer Schritt, um aus der Quantenhardware das Maximum herauszuholen. Je besser das Problem auf die verfügbare Chipstruktur übertragen wird, desto größer und komplexer können die analysierten Modelle ausfallen. Moderne D-Wave-Systeme mit Zephyr-Architektur und tausenden von Qubits ermöglichen heute die simultane Embeddierung mehrerer komplexer Modelle auf einem einzelnen Quantenprozessor.

![alt text](5806484262080330296.jpg)


# ### Vergleiche: Theorie & Quantenannealer

Links:  
- Exakte Lösung (Theory):  
  - Das Phasendiagramm zeigt die drei Hauptphasen (ferromagnetisch, antiferromagnetisch, paramagnetisch) für verschiedene Werte des Frustrationsparameters $$s$$ (y-Achse) und der Temperatur $$T$$ (x-Achse).
  - Gelbe Bereiche = ferromagnetisch, obere gelbe Ecke = antiferromagnetisch, lila Bereich = paramagnetisch.

Mitte:  
- Quantum-Annealing-Ergebnis (Average Magnetization):  
  - Das experimentelle Phasendiagramm wurde mit dem D-Wave Advantage2 QPU bestimmt.
  - Die Farbkodierung zeigt die durchschnittliche Magnetisierung: Gelbe Regionen entsprechen hoher magnetischer Ordnung (ferromagnetisch), dunkle Bereiche geringer Magnetisierung (paramagnetisch).

Rechts:  
- Quantum-Annealing-Ergebnis (Staggered Magnetization):  
  - Hier wird die sogenannte „staggered magnetization“ gezeigt, die speziell antiferromagnetische Ordnung misst.
  - Gelbe Bereiche deuten auf eine antiferromagnetische Phase hin.

### Hauptaussagen

- Die experimentellen Ergebnisse stimmen qualitativ sehr gut mit der exakten Theorie überein: Die gelben und lila/grauen Zonen in den Diagrammen entsprechen denselben Phasen wie im theoretischen Modell.
- Das Quantum Annealing auf echter Hardware (D-Wave Advantage2) kann somit die Hauptphasen und deren Grenzen des PUD-Modells korrekt abbilden.
- Ein solches Experiment demonstriert, dass moderne Quantum Annealer in der Lage sind, komplexe Phasendiagramme realitätsnah und quantitativ zu rekonstruieren – ein wichtiger Schritt für Benchmarking und weitergehende physikalische Forschung.

Fazit:  
Die Phasendiagramme, die mit Quantum Annealing erzeugt wurden, zeigen eine hohe Übereinstimmung mit der analytischen Lösung – sowohl für die ferromagnetischen als auch für die antiferromagnetischen Ordnungsparameter. Damit wird demonstriert, wie Quantum Annealer zur quantitativen Exploration komplexer physikalischer Systeme genutzt werden können.

![alt text](5808822102973856132.jpg)


# ### Calibration Refinement

Warum ist das notwendig?
- Messfehler oder Ungenauigkeiten können zu Nicht-Uniformitäten im Antwortverhalten des Quantenprozessors führen. Diese Nicht-Uniformitäten verzerren die Ergebnisse und können die Qualität der physikalischen Experimente oder Optimierungsaufgaben erheblich verschlechtern.

Was wird angepasst?
- Einzelne Kopplerstärken:  
  Jeder Koppler (die Kopplung zwischen zwei Qubits) muss individuell feinjustiert werden, da Abweichungen zu unterschiedlichen Stärken im tatsächlichen Quantenprozessor führen können.
- Individuelle Flux-Bias-Offsets (FBOs):  
  Die Flux-Bias-Offsets der einzelnen Qubits werden ebenfalls justiert, um lokal auftretende Abweichungen zu kompensieren.

Wie werden die Anpassungen vorgenommen?
- Verwendung von Graphsymmetrien:  
  Durch die Ausnutzung von Symmetrien im zugrundeliegenden Probleminstanz-Graphen kann die Gleichförmigkeit der Hardware-Antwort weiter verbessert werden. Symmetrische Konfigurationen sollten in der Statistik ähnliche Ergebnisse liefern; Abweichungen weisen gezielt auf Kalibrierungsfehler hin und können so korrigiert werden[1].

Diagramme rechts:
- Die eingeblendeten Plots und Histogramme illustrieren den Prozess: Sie zeigen die Verteilung und Entwicklung von Messwerten vor und nach der Kalibrierung, wobei eine Erfolgsverbesserung und Gleichmäßigkeit der Auswertung sichtbar wird.

Fazit:  
Eine präzise, detaillierte Kalibrierung ist essenziell, um systematische Fehler und Nicht-Uniformitäten in Quantenannealern auszuschließen. Dadurch wird gewährleistet, dass Experimente reproduzierbar, robust und theoretisch vergleichbar bleiben. Optimierte Kalibrierung verbessert sowohl die physikalische Zuverlässigkeit als auch die Leistungsfähigkeit bei quantenbasierten Optimierungs- und Simulationsaufgaben.

![alt text](5806767579598010692.jpg)


# Die Folie zeigt eine Sammlung von Auswertungsdiagrammen, die verschiedene Statistiken und Histogramme aus dem Kalibrierungsprozess eines Quantum-Annealers visualisieren:

### Ausgewertete Diagramme und ihre Bedeutung

- Oben links & Unten links:  
  Hier werden individuelle Verläufe für die Flux-Bias-Offets (oben) und die Koppler-Konfigurationen (unten) über verschiedene Iterationen dargestellt. Verschiedene Farben stehen jeweils für unterschiedliche Qubits oder Koppler im QPU-Chip.
  - Die Plots zeigen, wie sich die Einzelwerte im Verlauf der Kalibrierung anpassen und annähern.

- Mittlere Diagramme:  
  Die mittleren Spalten zeigen die Entwicklung der Standardabweichung der gemessenen Mittelwerte (oben: Magnetisierung, unten: Frustration).  
  - Je niedriger diese Werte, desto gleichförmiger und störungsarmer ist die Hardware-Antwort – ein Zeichen für erfolgreiche Kalibrierung und verbesserte Reproduzierbarkeit.

  Rechts daneben befinden sich Histogramme, die die Verteilung der Magnetisierungen (oben) bzw. Frustrationen der Koppler (unten) vor und nach der Kalibrierung zeigen.  
  - Die Histogramme sind typischerweise nach der Kalibrierung schmaler und höher, was auf eine gleichmäßigere Verteilung hindeutet.

- Rechte Diagramme:  
  Diese zeigen offenbar die Entwicklung eines Fehlermaßes oder einer Metrik (beispielsweise $$d_{xx}$$), das die Annäherung an einen Zielwert dokumentiert.  
  - Ein schnelles Absinken dieser Werte spricht für eine effiziente und zielgerichtete Justierung.

### Zusammengefasst

Diese Diagramme sind Teil der Qualitätskontrolle und des Kalibrierungsprozesses bei komplexen Quantum Annealing-Experimenten. Sie ermöglichen es, die Hardware optimal einzustellen und sicherzustellen, dass sie für wissenschaftliche Benchmarks (z.B. zur Bestimmung von Phasendiagrammen) präzise und verlässliche Ergebnisse liefert.

![alt text](5806712067145710100.jpg)


# Auf dieser Folie wird erklärt, wie kritische Punkte (zum Beispiel Phasenübergänge) im Phasendiagramm experimentell bestimmt werden können:

### Critical Points – Die Rolle des Binder-Kumulanten

- Binder-Kumulant ($$U$$):  
  Ein zentrales Werkzeug zur Identifikation von kritischen Punkten und Phasenübergängen in numerischen (und experimentellen) Simulationen ist der sogenannte Binder-Kumulant.  
  Die Definition lautet:
  $$
  U = 1 - \frac{\langle M^4 \rangle}{3\langle M^2 \rangle^2}
  $$
  Hierbei ist $$M$$ die Magnetisierung (bzw. der Ordnungsparameter), und die spitzen Klammern $$\langle \cdot \rangle$$ stehen für den Mittelwert über alle Samples.

- Warum ist der Binder-Kumulant wichtig?  
  Der Binder-Kumulant ermöglicht es, Phasenübergänge unabhängig von der Systemgröße exakt zu identifizieren:
  - Wird $$U$$ für verschiedene Systemgrößen (hier $$L_1$$ und $$L_2$$) über die Temperatur $$T$$ aufgetragen, so schneiden sich die Kurven im Plot typischerweise genau bei der kritischen Temperatur $$T_c$$.
  - Dies ist im Diagramm links illustriert, wo sich die beiden Kurven im Bereich des Phasenübergangs schneiden.

- Praktische Anwendung:  
  Diese Methode ist besonders robust gegenüber endlichen Systemgrößen (finite-size scaling) und daher ein Standardverfahren sowohl in der klassischen als auch in der Quantenstatistikphysik zur Bestimmung von Übergangs- und kritischen Punkten.

Fazit:  
Mit dem Binder-Kumulanten steht ein leistungsfähiges, etabliertes Werkzeug zur Verfügung, um kritische Punkte in komplexen Modellen unkompliziert und zuverlässig auch auf aktuellen Quantencomputern experimentell zu bestimmen.

![alt text](5806394428544366903.jpg)


# Diese Folie zeigt die experimentellen Ergebnisse für das sogenannte Binder-Kumulanten-Kreuzungs-Kriterium beim Wert $$s = 0$$, also im klassischen Ising-Modell:

### Binder Cumulant Crossing at $$ s = 0 $$

Was ist dargestellt?
- Auf der y-Achse wird $$1 - U$$ (wobei $$U$$ der Binder-Kumulant ist) in logarithmischer Skala dargestellt.
- Auf der x-Achse ist $$J^{-1}$$ aufgetragen (inverse Kopplungsstärke, entspricht der „Temperaturachse“).
- Jeder Graph repräsentiert eine andere Systemgröße ($$N, L$$), wie in der Legende rechts aufgeführt.

Zentrales Messprinzip:
- Das Kreuzungskriterium des Binder-Kumulanten wird angewendet:  
  Die Kreuzungspunkte der Kurven für verschiedene Systemgrößen entsprechen dem kritischen Punkt (dem Phasenübergang), hier zum Beispiel dem Übergang zwischen geordneter (ferromagnetischer) und ungeordneter (paramagnetischer) Phase.
- Genau diese Kreuzung ist durch die vertikale gestrichelte Linie markiert.

Wissenschaftliche Bedeutung:
- Das Verfahren ist ein etablierter Standard, um den kritischen Punkt („critical point“) experimentell und systemgrößenunabhängig zu bestimmen, auch auf echten Quantenprozessoren.
- Die Darstellung zeigt, dass der kritische Punkt mit guter Präzision identifiziert werden kann – ein weiteres Zeichen dafür, dass die Methode des Quantum Annealing sich für das quantitative Benchmarking komplexer physikalischer Systeme eignet.

Fazit:  
Mit Hilfe des Binder-Kumulanten-Kreuzungs-Kriteriums lässt sich der Phasenübergang im untersuchten Modell experimentell exakt bestimmen; die Illustration demonstriert, dass Quantum Annealing auch in der Praxis leistungsfähige Methoden für die quantitative Analyse von Phasen und kritischen Punkten in Spinmodellen bietet.

![alt text](5806443455596050860.jpg)


# Diese Folie illustriert, wie das Kreuzungs-Kriterium des Binder-Kumulanten für viele verschiedene Werte von $$ s < 1 $$ (also im intermediären Bereich zwischen Ising- und Villain-Modell) zur Bestimmung kritischer Punkte angewendet wird.

### Analyse für viele $$ s < 1 $$ – Kritische Linie im Phasendiagramm

3D-Darstellung:
- Auf der Hauptgrafik (schräger 3D-Plot) sind die Bindercumulanten ($$\log_2(1-U)$$) in Abhängigkeit von $$ J^{-1} $$ (x-Achse, „inverse Kopplungsstärke“ bzw. „Temperatur“) und dem Parameter $$ s $$ (y-Achse, Frustrationsgrad) für viele verschiedene Werte aufgetragen.
- Die Kreuzungspunkte („crossings“) für unterschiedliche Systemgrößen sind als rote Linien sichtbar und ergaben jeweils experimentell bestimmte kritische Punkte.
- Die schwarze Linie auf dem Boden des Plots zeigt die zugehörige (analytisch berechnete) kritische Linie der Theorie.
- Die Farbskala rechts markiert die durchschnittliche Magnetisierung, was unterschiedliche Phasen anzeigt (z.B. hohe Magnetisierung in geordneten Phasen).

Inset (kleiner Plot rechts oben):
- Der kleine Plot bringt die experimentell bestimmte kritische Kopplungsstärke $$ J^{-1} $$ für verschiedene Werte der effektiven Temperatur $$ T_\text{effective} $$ in Zusammenhang – ein weiteres Indiz für die quantitative Übereinstimmung zwischen Experiment und Theorie.

### Aussage der Darstellung

- Die Methode liefert für praktisch alle $$ s < 1 $$ zuverlässig Kreuzungspunkte, also kritische Werte für den Phasenübergang im PUD-Modell.
- Die experimentell bestimmten Übergangslinien stimmen mit der theoretisch berechneten Phasengrenze eng überein – ein Gütesiegel für die Qualität des Quantum Annealing-Ansatzes auf moderner Hardware.
- Die Verbindung zwischen experimenteller und theoretischer kritischer Temperatur ist nahezu linear, wie das Inset oben rechts zeigt.

Fazit:  
Mit dem Binder-Kumulanten-Kreuzungs-Kriterium lassen sich nicht nur einzelne, sondern ganze Linien von Phasenübergängen im Parameterraum ($$s, J^{-1}$$) systematisch und experimentell exakt bestimmen – und das mit Daten, die auf einem Quantum Annealer wie D-Wave Advantage2 QPU gewonnen wurden. Dies ist ein signifikanter Schritt hin zur präzisen, quantitativen physikalischen Exploration komplexer Modelle mittels Quantenhardware.

![alt text](5806287960600066407.jpg)


# Auf dieser Folie geht es um kritische Exponenten – zentrale Kennzahlen zur Beschreibung des physikalischen Verhaltens in der Nähe eines Phasenübergangs, sowohl in exakten Modellen als auch bei der Simulation mit Markov Chain Monte Carlo (MCMC).

### Critical Exponents: Überblick

Nahe eines Phasenübergangs gilt allgemein (mit $$ t = \frac{|T - T_c|}{T_c} $$, $$ T_c $$ kritische Temperatur):

- Magnetisierungs-Suszeptibilität:  
  $$\chi \propto t^{-\gamma}$$  
  Misst, wie stark das System auf ein äußeres Magnetfeld reagiert. Die Divergenz bei $$ T \to T_c $$ ist durch $$\gamma$$ charakterisiert.

- Wärmekapazität:  
  $$C_V \propto t^{-\alpha}$$  
  Gibt an, wie die gespeicherte Energie beim Übergang „explodiert“ oder sanft verläuft ($$\alpha$$).

- Korrelationslänge:  
  $$\xi \propto t^{-\nu}$$  
  Beschreibt die Reichweite, über die Spins (oder andere Freiheitsgrade) miteinander korreliert sind – sie divergiert bei $$ T_c $$ mit Exponent $$\nu$$.

- Mittlere Magnetisierung:  
  $$M \propto t^{\beta}$$  
  Die Ordnung nimmt in Richtung kritischer Punkt mit charakteristischem Exponenten $$\beta$$ ab.

### Für das 2d-Ising-Modell exakt bekannt:

- $$\nu = 1$$
- $$\gamma = 1{,}75$$
- $$\alpha = 0$$
- $$\beta = 0{,}125$$

Diese Werte sind universell und erlauben die experimentelle (oder rechnerische) Einordnung verschiedener Modelle, Methoden (hier MCMC, Quantum Annealing etc.) in universelle Klassen kritischer Phänomene.

Fazit:  
Die Bestimmung dieser Exponenten ist ein Schlüssel zur Charakterisierung von Phasenübergängen: Sie erlauben es, die Realexperimente und Simulationen direkt mit exakten (theoretischen) Lösungen zu vergleichen – ein zentrales Ziel moderner Quanten- und Computerphysik.

![alt text](5808646090919098808.jpg)


# Diese Folie zeigt Ergebnisse von Markov Chain Monte Carlo (MCMC) Simulationen zur Bestimmung der kritischen Exponenten des untersuchten Modells (z.B. des Piled-Up Dominoes / PUD-Modells).

### Markov Chain Monte Carlo simulations – Ergebnisse

Linkes Diagramm:  
- Hier ist die Feinstruktur der magnetischen Suszeptibilität $$\chi$$ dargestellt, die skaliert wurde als $$\chi(L,t) L^{-\gamma/\nu}$$, aufgetragen gegen $$tL^{1/\nu}$$ (mit $$t$$ als reduzierter Temperatur und $$L$$ als Systemgröße).
- Durch den Kollaps der Kurven für verschiedene Systemgrößen auf eine Masterkurve können die kritischen Exponenten $$\nu$$ und $$\gamma$$ extrahiert werden.
- Die gemessenen Werte ($$\nu = 0.97 \pm 0.04$$, $$\gamma = 1.71 \pm 0.12$$) stimmen sehr gut mit den exakten Werten aus der Theorie für das 2D-Ising-Modell überein.

Mittlere Grafik:  
- Eine 3D-Visualisierung zeigt vermutlich (abhängig von Kontext und Farbskala) den Verlauf der magnetischen Suszeptibilität oder einer anderen beobachtbaren Größe über den relevanten Parameterraum ($$t, L$$).

Rechtes Diagramm:  
- Hier sind die extrahierten Exponenten $$\nu$$, $$\gamma$$ und $$\beta$$ als Funktion des Interpolationsparameters $$s$$ (der den Frustrationsgrad im PUD-Modell regelt) aufgetragen.
- Die Exponenten bleiben über den gesamten Bereich von $$s$$ praktisch konstant (“Exponents unchanged with s”) und passen zu den vorhergesagten universellen Werten des 2D-Ising-Modells.

Fazit:  
Markov Chain Monte Carlo Simulationen bestätigen, dass die kritischen Exponenten des Modells im gesamten Bereich des Interpolationsparameters $$s$$ unverändert und universell bleiben. Die Ergebnisse liegen im Einklang mit der exakten Theorie – ein starkes Indiz dafür, dass das Modell in eine klare universelle Klasse fällt, und ein wichtiger Referenzpunkt für Vergleiche mit Experimenten auf Quantum Annealern.

![alt text](5808549050428012891.jpg)


# Diese Folie zeigt exemplarisch den Verlauf zweier wichtiger physikalischer Größen am Beispiel $$s = 0$$, also für das klassische 2D-Ising-Modell:

### Beispiel: $$\chi / \beta$$ und $$C_V / \beta^2$$ bei $$s = 0$$

Linkes Diagramm – Magnetische Suszeptibilität $$\chi / \beta$$:
- Die y-Achse zeigt die magnetische Suszeptibilität, normiert auf die inverse Temperatur ($$\beta$$).
- Die x-Achse ist $$J^{-1}$$ – die inverse Kopplungsstärke beziehungsweise Temperatur.
- Für verschiedene Systemgrößen (Farbcodierung und Legende) zeigt sich ein deutlicher Peak:  
  Dieser Peak markiert den kritischen Punkt (Phasenübergang zwischen Paramagnet und Ferromagnet).
- Mit wachsender Systemgröße („finite size scaling“) werden die Peaks schärfer und verschieben sich nur wenig.

Rechtes Diagramm – Normierte Wärmekapazität $$C_V / \beta^2$$:
- Die Wärmekapazität pro System und normiert durch $$\beta^2$$ ist ebenfalls gegen $$J^{-1}$$ aufgetragen.
- Auch hier ist deutlich ein Peak zu erkennen, der mit zunehmender Systemgröße höher und schmaler wird.
- Die Lage und Form dieses Peaks liefert direkte Informationen über die kritische Temperatur und die kritischen Exponenten des Modells.

Wissenschaftliche Bedeutung:
- Die Peak-Struktur in beiden Observablen ist charakteristisch für Phasenübergänge zweiter Ordnung und zeigt, dass sowohl Magnetisierungsschwankungen als auch Energiefluktuationen am kritischen Punkt maximal sind.
- Die Finite-Size-Analyse erlaubt eine präzise Bestimmung der kritischen Parameter.

Fazit:  
Solche Diagramme sind wesentliche Werkzeuge in der numerischen und experimentellen Festkörperphysik, um Phasenübergänge, kritische Punkte und universelle Eigenschaften von Modellen wie dem 2D-Ising-Modell quantitativ zu charakterisieren.

![alt text](5808959988603926911.jpg)


# Diese Folie zeigt das Verhältnis der kritischen Exponenten $$\gamma/\nu$$ als Funktion des Frustrationsparameters $$s$$ für das untersuchte PUD-Modell:

### $$\gamma/\nu$$ als Funktion von $$s$$

- y-Achse:  
  Das Verhältnis $$\gamma/\nu$$, eine universelle kritische Größenordnung, die zum Beispiel beschreibt, wie sich die maximale Suszeptibilität mit der Systemgröße skalieren sollte.

- x-Achse:  
  Der Interpolations- bzw. Frustrationsparameter $$s$$, der systematisch von 0 (Ising-Modell) bis knapp unter 1 (Villain-Modell) durchlaufen wird.

- Drei Datensets:  
  - Schwarz (Kreise, gestrichelte Linie): Werte, die direkt aus Markov Chain Monte Carlo (MCMC) Simulationen abgeleitet wurden – als Referenzmaßstab.
  - Blau (Kreuze): Werte, die aus der normierten Suszeptibilität $$\chi/\beta$$ berechnet wurden.
  - Hellblau (Quadrate): Werte, aus alternativer Normierung $$\chi/(\beta \times J)$$, die nach Anmerkung auf der Folie besonders robuste Exponenten liefern („Better exponents“).

### Interpretation

- Für alle Werte von $$s$$ bleibt $$\gamma/\nu$$ nahezu konstant, was die Universalität des Phasenübergangs im gesamten Modellbereich bestätigt.
- Die horizontal gestrichelte Linie markiert die Referenz aus exakten Modellen (MCMC), und die experimentellen Werte (blau, schwarz) liegen in sehr guter Übereinstimmung damit.
- Kleinere Streuungen und konstanter Verlauf bei den hellblauen („besseren“) Exponenten zeigen, dass die Methode robust und zuverlässig ist.

Fazit:  
Das Verhältnis der kritischen Exponenten $$\gamma/\nu$$ bleibt über das gesamte Intervall von $$s$$ hinweg konstant und bestätigt die universelle Natur des Phasenübergangs im PUD-Modell. Damit wird gezeigt, dass die Methoden zur exponent-Bestimmung – sei es mit MCMC oder experimentell via Quantum Annealing – quantitativ verlässliche Resultate liefern und die fundamentalen eigenschaftlichen Ordnungen exakt erfassen können.

![alt text](5808994683349743934.jpg)


# Diese Folie beantwortet die zentrale Frage, warum man überhaupt Quantum Annealing einsetzt, obwohl Monte Carlo Simulationen bereits sehr leistungsfähig („good“) sind:

### Warum Quantum Annealing statt (nur) Monte-Carlo-Simulationen?

Frage:  
Warum sollte man Quantum Annealing für das Boltzmann-Sampling oder die Bestimmung von Phasendiagrammen verwenden, wenn klassische Monte-Carlo-Methoden schon sehr gute Resultate liefern?

Antwort:  
Um „critical slowing down“ zu vermeiden.

Hintergrund:
- Beim klassischen Monte Carlo tritt das Phänomen des critical slowing down auf:  
  In der Nähe eines Phasenübergangs werden die Korrelationen im System sehr langreichweitig und die Algorithmen benötigen deutlich mehr Schritte, um unabhängige Stichproben („Samples“) zu erzeugen. Das bedeutet drastisch erhöhten Rechenaufwand und lange Konvergenzzeiten in der Umgebung des kritischen Punktes.
- Quantum Annealing hingegen kann – zumindest im Prinzip und für bestimmte Problemklassen – diese kritische Verzögerung umgehen, da Quantentunneln und Quantenfluktuationen es ermöglichen, das System effizient und schnell zwischen verschiedenen Konfigurationen zu bewegen, selbst nahe kritischer Punkte.

Fazit:  
Quantum Annealing bietet gerade dort Vorteile, wo klassische Methoden wie Monte Carlo durch kritische Verlangsamung stark ausgebremst werden: zum Beispiel bei der effizienten Exploration kritischer Phasenräume, komplexer Spinglas-Landschaften oder bei Optimierungsaufgaben mit vielen lokalen Minima.

![alt text](5806275359166019972.jpg)


# Hier werden die Hintergründe und mögliche Lösungsansätze für das Problem des critical slowing down in Monte-Carlo-Simulationen erläutert:

### Critical Slowing Down (Kritische Verlangsamung)

- In der Nähe eines kritischen Punktes:  
  Die Konvergenz von MCMC-Algorithmen (Markov Chain Monte Carlo) wird sehr langsam, insbesondere:
  - Dies verschärft sich bei Frustration im System – also in Modellen, bei denen nicht alle lokalen Wechselwirkungen gleichzeitig erfüllt werden können.
  - Der Effekt tritt besonders stark auf, wenn die reduzierte Temperatur $$ t \to 0 $$ (also nahe der kritischen Temperatur) und die Systemgröße $$ L \to \infty $$ wächst.

- Verbesserte Algorithmen als Gegenmaßnahme:  
  Es gibt Algorithmen, die darauf abzielen, das critical slowing down abzumildern:
    - Cluster Moves: Statt einzelner Spins werden ganze Cluster gemeinsam bewegt, was die Dynamik beschleunigen kann.
    - Parallel Tempering: Das gleichzeitige Simulieren bei verschiedenen Temperaturen, was Tunnelprozesse verstärkt und Barrieren effizienter überwindet.
  - Jedoch: Es gibt keine allgemeingültige Methode, um das kritische Verlangsamen in allen Fällen zuverlässig zu vermeiden. Für besonders große und stark frustrierte Systeme stoßen auch die besten klassischen Algorithmen an ihre Grenzen.

Fazit:  
Critical slowing down bleibt eine fundamentale Herausforderung bei klassischen Simulationen komplexer Systeme. Trotz kluger algorithmischer Ansätze bleibt der Bedarf an Alternativen wie Quantum Annealing bestehen, die physikalisch neue Mechanismen für die effiziente Erzeugung unabhängiger Stichproben bieten.

![alt text](5806452573811620228.jpg)


# Auf dieser Folie wird anhand eines Beispiels gezeigt, wie sich die Autokorrelationsfunktion im Sampling-Verhalten von klassischen Monte-Carlo-Simulationen (MCMC) und Quantum Annealing (QA) unterscheidet:

### Autocorrelation Function Comparison ($$s = 0$$)

Diagramm-Inhalt:
- Die Grafik stellt die normierte Autokorrelationsfunktion $$ \chi(t)/\chi(0) $$ in Abhängigkeit von der Zeit (bzw. von der Anzahl der Simulation-Schritte) für zwei Methoden dar:
  - MCMC (schwarz, Punkte):  
    - Hier nimmt die Autokorrelation mit der Zeit langsam ab.
    - Es braucht viele Schritte, bis die Stichproben voneinander statistisch unabhängig werden – ein Hinweis auf das oben besprochene „critical slowing down“.
  - Quantum Annealing (rot, Dreiecke):  
    - Die Autokorrelationsfunktion bleibt praktisch bei Null – die Ausgaben (Samples) sind von Anfang an statistisch unabhängig.
    - Dies ist explizit so im Design von Quantum Annealern vorgesehen: Jedes Sample entsteht physikalisch unabhängig vom vorherigen.

Wissenschaftliche Bedeutung:
- Während bei klassischen Monte Carlo-Verfahren nahe am kritischen Punkt viele Schritte nötig sind, um voneinander unabhängige Stichproben zu erhalten, liefern Quantum Annealer diese sofort und ohne Autokorrelation.
- Das behebt fundamental das Problem des „critical slowing down“, das für klassische Algorithmen charakteristisch ist, und bietet bei bestimmten Anwendungen einen klaren Vorteil für Quantum Annealing.

Fazit:  
Der Vergleich der Autokorrelationsfunktionen demonstriert eindrucksvoll, dass Quantum Annealing – im Gegensatz zu klassischen Monte-Carlo-Methoden – von Natur aus unabhängige Stichproben erzeugt. Das macht die Methode in Kontexten mit critical slowing down, insbesondere bei physikalisch oder kombinatorisch schwierigen Problemen, besonders attraktiv.

![alt text](5806559776195328504.jpg)


# Conclusion and Outlook – Hauptaussagen

- Quantum Annealer als Werkzeug für die statistische Physik:  
  Sie können erfolgreich eingesetzt werden, um anspruchsvolle Modelle quantitativ zu analysieren. Wichtige Anwendungsfälle sind:
    - Kartierung von Phasendiagrammen bei endlichen Temperaturen.
    - Identifizierung kritischer Punkte und Exponenten, was essentielle Kennzahlen zur Charakterisierung von Phasenübergängen liefert.

- Praktischer Nutzen trotz nicht-idealem Sampling:  
  Auch wenn Quantum Annealer nicht exakt die Gibbs-Verteilung (das ideale, thermische Gleichgewicht) sampeln, sind sie dennoch sehr nützlich. Für viele Anwendungen reichen Mittelwerte bis hin zu den 4. Ordnungsmomenten aus (z.B. für Binder-Kumulanten oder zur Identifikation kritischer Punkte) – präzise Gibbs-Samples sind also oft gar nicht zwingend notwendig.

- Kein critical slowing down:  
  Ein klarer Vorteil der Methode: Quantum Annealer zeigen kein „critical slowing down“. Das bedeutet, selbst nahe am kritischen Punkt (Phasenübergang) werden schnell und effizient statistisch unabhängige Stichproben generiert – im Gegensatz zu klassischen Monte Carlo-Algorithmen, die in solchen Situationen oft sehr langsam konvergieren.  
  → Dies bietet einen potenziellen Vorteil für quantenbasierte Verfahren gegenüber herkömmlichen klassischen Algorithmen, besonders für große, frustrierte oder komplexe Systeme.

Zusammengefasst:  
Quantum Annealer eröffnen neue Möglichkeiten in der physikalischen Forschung: Sie ermöglichen die systematische und effiziente experimentelle Erkundung von Phasendiagrammen und kritischen Phänomenen, sind robust gegenüber kritischer Verlangsamung und liefern auch bei nicht-idealen Gibbs-Samples ausreichend exakte Ergebnisse für viele statistisch-physikalische Fragestellungen.

![alt text](5806775374963653143.jpg)



# Conclusio, Quintessenz und Fazit

## 1. Was ist Quantum Annealing und Boltzmann-Sampling?

- **Quantum Annealing** ist eine Methode, mit der Quantencomputer Probleme lösen, indem sie das System in einen Zustand mit möglichst geringer Energie bringen.
    
- Dabei probiert das System viele mögliche Lösungen gleichzeitig aus und „sucht“ dann die beste oder eine gute Lösung.
    
- Das Ergebnis ist **nicht immer perfekt**, sondern probabilistisch, also zufällig mit einer gewissen Wahrscheinlichkeit besserer oder schlechterer Lösungen.
    
- Diese Wahrscheinlichkeiten folgen einer sogenannten **Boltzmann-Verteilung**: Lösungen mit niedriger Energie (gute Lösungen) tauchen häufiger auf, Lösungen mit höherer Energie (weniger gute) seltener.
    
- Man kann sich das so vorstellen, als würde man aus einem Sack voller unterschiedlicher Lösungsbälle ziehen: Die "guten" sind öfter drin, aber auch die "weniger guten" können gezogen werden.
    

## 2. Wie funktioniert Quantum Annealing physikalisch?

- Ein sogenannter Hamiltonian (eine mathematische Beschreibung des Systems) verändert sich mit der Zeit von einem einfachen Startzustand (viele Lösungen gleichzeitig) zu einem Zustand, der die Lösung des Problems beschreibt.
    
- Die Zeit, über die dieser Prozess abläuft, nennt man **Annealing-Zeit**. Sie beeinflusst, wie gut und stabil das Ergebnis ist.
    
- Zu kurze Zeit bedeutet schnelle, nicht perfekte Lösungen. Zu lange Zeit erlaubt Störungen von außen, die das Ergebnis beeinträchtigen können.
    
- Es ist ein Balanceakt, die optimale Annealing-Zeit zu finden.
    

## 3. Herausforderungen: Temperatur und Kalibrierung

- Die **Temperatur** des Systems beeinflusst, wie das Sampling erfolgt – je kälter, desto besser sind die niedrigen Energiezustände besetzt.
    
- Die exakte Temperatur des Quantum Annealers ist schwer direkt zu kontrollieren, wird aber durch Anpassung der Eingangsparameter gesteuert.
    
- Außerdem wird die Hardware kalibriert, d.h. kleine Ungenauigkeiten in den Verbindungen (Kopplern und Qubits) werden korrigiert, damit die Ergebnisse stabil und vergleichbar sind.
    

## 4. Was sind Phasendiagramme und kritische Punkte?

- Ein **Phasendiagramm** zeigt, in welchem Zustand sich ein System bei unterschiedlichen Bedingungen (z.B. Temperartur, Druck) befindet. Man kennt das z.B. bei Wasser (fest, flüssig, gasförmig).
    
- **Phasenübergänge** sind Punkte oder Linien, an denen das System akut von einem Zustand in einen anderen wechselt.
    
- Diese Übergänge werden durch **kritische Punkte** im Diagramm markiert.
    
- Physikalische Systeme zeigen an diesen Punkten besondere Verhaltensweisen, z.B. stark schwankende Größen.
    
- **Kritische Exponenten** beschreiben, wie sich verschiedene Eigenschaften des Systems um diesen kritischen Punkt verändern.
    

## 5. Forschungsarbeit mit Quantum Annealing

- Am Beispiel eines speziellen **Piled-Up Dominoes (PUD) Modells** wurde mit Quantum Annealing das gesamte Phasendiagramm untersucht.
    
- Das PUD-Modell kann von einfachen Zuständen (leicht zu lösen) bis zu komplexen, frustrierten Systemen interpolieren.
    
- Die experimentell mit Quantum Annealing erstellten Phasendiagramme stimmen sehr gut mit den theoretisch bekannten Ergebnissen überein.
    
- Es konnten kritische Punkte exakt bestimmt und kritische Exponenten gemessen werden, die bestätigen, dass Quantum Annealer realistische physikalische Bedingungen nachbilden können.
    

## 6. **Wichtigste Erkenntnis: Quantum Annealer umgehen das Problem des „Critical Slowing Down“**

- Klassische Simulationsmethoden wie Monte Carlo leiden an dieser Verlangsamung, besonders nahe Phasenübergängen: Die Berechnungen brauchen viel Zeit, um neue, unabhängige Samples zu erzeugen.
    
- Quantum Annealer liefern dagegen von Anfang an weitgehend unabhängige Samples, weil jede Messung physikalisch ein neues, unabhängiges Ergebnis erzeugt.
    
- Das bedeutet: Quantum Annealing ist schneller beim Erkunden kritischer und komplexer Systeme und bietet dadurch einen großen Vorteil.
    

## 7. Fazit & Quintessenz

Stell dir vor, du willst die beste Lösung für ein super schweres Puzzle finden. Klassische Computer probieren Stück für Stück, viele Minuten oder Stunden lang, bis sie nah an die beste Lösung kommen. Sie bleiben oft dabei an Stellen hängen, an denen es schwierig ist weiterzukommen. Das ist das Problem des „critical slowing down“ – sie werden dabei langsamer und langsamer.

Ein Quantum Annealer ist wie ein Zauberer, der viele Puzzleteile gleichzeitig hebt und durch geheimnisvolle Quantenzauber „durch Wände hindurchgehen“ kann, um schnell ziemlich gute Lösungen zu finden, auch wenn es viele Hindernisse gibt.

Obwohl dieser Zauberer nicht immer die allerbeste Lösung auf Anhieb zeigt, schafft er es meistens, sehr nah dran zu sein. Und das macht ihn super wertvoll, um wirklich schwierige Probleme schneller zu lösen als klassische Computer.

Forscher haben mit echten Quantum Annealern schon gezeigt, dass man damit physikalische Phasen-Wechsel und kritische Verhaltensweisen genau untersuchen kann – also viele spannende Fragen aus Physik und Technik lösen kann. Das ist ein großer Schritt Richtung Quanten-Zukunft!
