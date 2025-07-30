# Dieses Programm berechnet eine Route für einen Lieferfahrer, der mitunter einen Prioritätskunden besuchen muss.

import numpy as np # NumPy ist eine Bibliothek für numerische Berechnungen in Python.
# Sie bietet Unterstützung für große, mehrdimensionale Arrays und Matrizen sowie eine Vielzahl von mathematischen Funktionen.
import matplotlib.pyplot as plt # Matplotlib ist eine Bibliothek zum Erstellen von Grafiken und Diagrammen in Python.
# Sie ermöglicht die Visualisierung von Daten in Form von Plots, Diagrammen und anderen grafischen Darstellungen.
from matplotlib.widgets import Button # Button ist ein Widget aus Matplotlib, das es ermöglicht, interaktive Schaltflächen in Plots zu erstellen.
# Diese Schaltflächen können verwendet werden, um Aktionen auszulösen, wenn sie angeklickt werden.
import tkinter as tk # Tkinter ist die Standard-GUI-Bibliothek für Python.
# Sie ermöglicht die Erstellung von grafischen Benutzeroberflächen (GUIs) in Python-Anwendungen
from tkinter.simpledialog import askinteger # askinteger ist eine Funktion aus Tkinter, die ein Dialogfeld öffnet, in dem der Benutzer eine ganze Zahl eingeben kann.

np.random.seed(84326)
# das Endprodukt Zufallszahl bekommt einen festen Startwert,
# damit die Zufallszahlen immer gleich sind, wenn das Programm gestartet wird.
stadtzahl = 50
# 50 wird der Variablen stadtzahl zugewiesen.
staedte = np.random.rand(stadtzahl, 2) * 100 
# np.random.rand eine Funktion aus NumPy sie erzeugt ein Arry mit Zufallszahlen. 
# Die Argumente (stadtzahl, 2) geben die Dimensionen des Arrays an, also 50 
# Städte mit jeweils 2 Spalten/Koordinaten (x, y). np.random.rand() gibt 
# immer Werte zwischen 0 und 1 zurück, die dann mit 100 multipliziert werden.
# Dieser Wert wird dann der Variablen 'staedte' zugewiesen, die ein Array mit den Koordinaten der Städte enthält. 
speed = 60
# 60 Km/h wird der Variablen speed zugewiesen,
# die die Geschwindigkeit in km/h repräsentiert.
max_fahrzeit = 9 * 60  
# 9 mal 60 Minuten also 9 Stunden Lenkzeit wird der Variablen max_fahrzeit zugewiesen.
startpunkt = 0 
# 0 wird der Variablen startpunkt zugewiesen,
# die den Index des Startpunkts (Depot) repräsentiert.
fixer_punkt = [startpunkt] 
# Eine neue Liste namens fixer_punkt wird erstellt, und sie enthält zunächst nur den Wert von startpunkt (also 0).
# Am Anfang enthält diese Liste nur den Startpunkt (Depot), da hier noch kein weiterer Prioritätskunde ausgewählt wurde.
priority_time_dict = {startpunkt: 0}
# Initalisierung eines Wörterbuchs '{     }'namens priority_time_dict,
# das die Ankunftszeiten des Prioritätskunden speichert.
# Der Schlüssel ist 'startpunkt' mit dem Wert 0 --> 'startpunkt: 0'
# Dieses Dictionary speichert für jeden Fixpunkt (Prioritätskunden) die späteste erlaubte Ankunftszeit in Minuten ab Start (0 Minuten = Startzeit).
# Für den Startpunkt (startpunkt = 0) ist klar, dass die Ankunftszeit 0 Minuten ist — denn dort beginnt die Route.
# Später, wenn der Nutzer in der GUI einen Prioritätskunden (Fixpunkt) auswählt, z.B. die Stadt Nr. 12, gibt es einen Eintrag: priority_time_dict[12] = 120

def fahrzeit(a, b):
    distanz = np.linalg.norm(staedte[a] - staedte[b])
    # a) staedte[a] UND staedte[b]
    # staedte ist ein Array (Liste) von 2D-Punkten (Koordinaten).
    # staedte[a] holt den Koordinaten-Wert der Stadt mit Index a.
    # Zum Beispiel könnte staedte = [45.3, 12.7] sein (x,y).
    # staedte[b] holt den Koordinaten-Wert der Stadt mit Index b.
    # Zum Beispiel könnte staedte = [50.1, 10.5] sein (x,y).
    # b) staedte[a] - staedte[b]
    # Das ist eine Subtraktion zwischen zwei Koordinaten (zwei Vektoren).
    # Beispiel:
    # [45.3, 12.7] - [20.0, 5.0] = [25.3, 7.7]
    # 25.3 und 7.7 jeweils zum Quadrat in der Summe ergeben und daraus die Wurzel ergibt die Distanz (84,59) der beiden Punkte 
    # [45.3, 12.7] und [20.0, 5.0].
    # Zusammenfassend: dist = np.linalg.norm(staedte[a] - staedte[b]) Berechnet Luftlinie zwischen den Städten a und b.

    return distanz / speed * 60 
    # return = Schlüsselwort in Python. Was wird an der Stelle zurückgegeben, wo die Funktion 'fahrzeit' aufgerufen wurde?
    # gibt zurück die Umrechnung von km/h in min/km also die DIstanz (84,59) geteilt durch die Geschwindigkeit (60 km/h) mal 60
    # = 84,59 / 60 * 60 = 84,59 Minuten.

def plot_staedte_und_fixpunkte():
    # Diese Funktion zeichnet alle Kunden (Städte), alle bisher ausgewählten Fixpunkte (inkl. Startpunkt) und den Startpunkt selbst in unterschiedlichen Farben und mit unterschiedlichen Symbolen ins Diagramm.
    ax.scatter(staedte[:, 0], staedte[:, 1], c='blue')
    # Alle Kunden werden als blaue Punkte ins Diagramm gezeichnet. Dabei stehen die Werte in der ersten Spalte (Index 0) für die x-Koordinate und in der zweiten Spalte (Index 1) für die y-Koordinate.
    ax.scatter(staedte[fixer_punkt, 0], staedte[fixer_punkt, 1], c='red', s=100, marker='X')
    # Die Fixpunkte (ausgewählte wichtige Städte inkl. Start) werden als rote Kreuze (X) und größer (s=100) markiert. fixer_punkt ist dabei eine Liste mit den Indizes der Fixpunkte.
    ax.scatter(staedte[startpunkt, 0], staedte[startpunkt, 1], c='black', s=500, marker='o',
               edgecolors='yellow', linewidths=6)
    # Der Startpunkt (meist Index 0, also das Depot) wird als besonders großer schwarzer Punkt mit einem dicken gelben Rand gezeichnet, damit er sofort auffällt.



def pruefe_prioritaetskunden():
    # Diese Funktion prüft, ob mindestens ein Prioritätskunde (neben dem Startpunkt) ausgewählt wurde.
    if len(fixer_punkt) < 2:
        # Wenn es weniger als zwei Fixpunkte gibt (also nur den Startpunkt), 
        # dann zeigt das Programm dem Nutzer einen Hinweis an:
        ax.set_title("Bitte zuerst mindestens einen Prioritätskunden (aus den Punkten) wählen!")
        # Im Diagramm steht oben dann dieser Hinweis als Überschrift.
        ax.legend()
        # Die Legende (Erklärung der Farben/Symbole) wird aktualisiert/angezeigt.
        plt.draw()
        # Das Diagramm wird neu gezeichnet, damit der Hinweis sofort sichtbar ist.
        return False
        # Die Funktion gibt False zurück, damit im weiteren Verlauf keine Route berechnet wird.
    return True
    # Wenn ein Prioritätskunde ausgewählt wurde, gibt die Funktion True zurück, sodass das Programm mit der Routenberechnung fortfährt.



def berechne_route():
    # Diese Funktion berechnet die beste Route zum Prioritätskunden und wieder zurück zum Depot,
    # unter Berücksichtigung der Zeitvorgaben.

    depot = startpunkt  # Der Startpunkt (meist Index 0 des Arrays)
    pri_idx = fixer_punkt[1]  # Der Prioritätskunde ist der zweite Eintrag in fixer_punkt.
    arrival_limit = priority_time_dict[pri_idx]  # Späteste erlaubte Ankunftszeit für diesen Prioritätskunden in Minuten

    all_indices = set(range(stadtzahl))  # Erstellt eine Menge mit allen Stadt-Indizes von 0 bis stadtzahl-1.
    stops_hinweg = [depot]  # Liste mit den Indizes der Städte auf dem Hinweg; Start ist immer das Depot.
    t = 0  # Gesamtfahrzeit bisher (in Minuten); startet bei 0.
    curr = depot  # Der aktuelle Standort des Fahrers; startet am Depot.
    unbesucht = all_indices - set([depot, pri_idx])  
    # Alle Städte, die noch nicht besucht wurden, außer dem Depot und dem Prioritätskunden.

    # Jetzt wird der Hinweg geplant, indem möglichst viele Städte besucht werden,
    # aber trotzdem rechtzeitig beim Prioritätskunden angekommen wird:
    while True:
        next_options = []  # Hier werden mögliche nächste Städte gesammelt.
        for k in unbesucht:
            t_to_k = fahrzeit(curr, k)  # Zeit von aktuellem Standort zur Stadt k.
            t_k_to_prio = fahrzeit(k, pri_idx)  # Zeit von Stadt k zum Prioritätskunden.
            if t + t_to_k + t_k_to_prio <= arrival_limit:
                # Nur Städte, die man einbauen kann, ohne den Prioritätskunden zu spät zu erreichen, werden gespeichert.
                next_options.append((t_to_k, k))
        if not next_options:
            # Wenn es keine passenden Städte mehr gibt, endet die Suche.
            break
        _, nxt = min(next_options)
        # Es wird der Ort mit der kürzesten Fahrtzeit vom aktuellen Standpunkt ausgewählt.
        t += fahrzeit(curr, nxt)
        # Die Gesamtfahrzeit wird entsprechend erhöht.
        stops_hinweg.append(nxt)
        curr = nxt
        unbesucht.remove(nxt)
        # Die besuchte Stadt wird aus der Liste der unbesuchten entfernt.

    # Prüft, ob die Fahrtzeit bis zum Prioritätskunden überhaupt reicht.
    t_to_prio = fahrzeit(curr, pri_idx)
    if t + t_to_prio > arrival_limit:
        # Wenn die Fahrt zu lang dauert und man zu spät beim Prioritätskunden wäre,
        # wird die Hinweg-Route beendet und ein Hinweis ausgegeben.
        route = stops_hinweg
        info = f"Route nicht möglich: Mindestens zum Prioritätskunden pünktlich ankommen!"
        return route + [depot], info

    # Wenn der Prioritätskunde rechtzeitig erreicht wird, 
    # fährt der Fahrer weiter zum Prioritätskunden und die Zeit wird dazu addiert.
    t += t_to_prio
    stops_hinweg.append(pri_idx)

    # Nun wird der Rückweg geplant: Von dort können weitere, noch unbesuchte Kunden besucht werden,
    # solange der Fahrer rechtzeitig ins Depot zurückkehrt.
    stops_rueckweg = []
    curr = pri_idx
    while unbesucht:
        next_options = []
        for k in unbesucht:
            t_to_k = fahrzeit(curr, k)
            t_k_to_depot = fahrzeit(k, depot)
            if t + t_to_k + t_k_to_depot <= max_fahrzeit:
                # Nur Städte, die man besuchen kann und danach noch rechtzeitig zum Depot kommt, werden berücksichtigt.
                next_options.append((t_to_k, k))
        if not next_options:
            break
        _, nxt = min(next_options)
        t += fahrzeit(curr, nxt)
        stops_rueckweg.append(nxt)
        curr = nxt
        unbesucht.remove(nxt)

    # Prüft abschließend, ob am Ende der direkte Rückweg zum Depot noch erlaubt ist:
    t_to_depot = fahrzeit(curr, depot)
    if t + t_to_depot > max_fahrzeit:
        # Falls nicht: Route abbrechen und Fehlermeldung mit Route zurückgeben.
        route = stops_hinweg + stops_rueckweg
        info = f"Route nicht möglich: Fahrer schafft Rückweg zu Depot nicht mehr innerhalb von 9 Stunden!"
        return route + [depot], info

    # Die komplette Route besteht aus Hinweg, Besuch beim Prioritätskunden,
    # dann Rückweg über alle weiteren noch besuchten Kunden zum Depot.
    route = stops_hinweg + stops_rueckweg + [depot]
    info = f"Beste Route: Fahrzeit {t + t_to_depot:.1f} min, {len(route) - 1} Kunden besucht"
    return route, info



def solve(event=None):
    # Diese Funktion ist das "Herzstück" des Programms und wird ausgeführt,
    # wenn der Button "Route berechnen" geklickt wird.
    plot_staedte_und_fixpunkte()  # Zeichnet alle Kunden, Fixpunkte und Startpunkt im Plot.

    if not pruefe_prioritaetskunden():
        # Prüft, ob der Nutzer schon einen Prioritätskunden ausgewählt hat.
        # Falls nicht, Rückgabe und keine weitere Ausführung!
        return

    route, info = berechne_route()  # Berechnet die Route zum Prioritätskunden und zurück.

    show_route(route, info)  # Zeigt die gefundene Route und Info im Plot an.


def show_route(route, info):
    # Zeigt eine berechnete Route im Plot grafisch an und gibt Zusatzinfos aus.
    # Erst werden die Fixpunkte und der Startpunkt nochmal hervorgehoben.
    ax.scatter(staedte[fixer_punkt, 0], staedte[fixer_punkt, 1], c='red', s=100, marker='X')
    ax.scatter(staedte[startpunkt, 0], staedte[startpunkt, 1], c='black', s=140, marker='o',
               edgecolors='yellow', linewidths=6)
    arr = np.array([staedte[i] for i in route])  # Erstellt ein Array mit den Koordinatenpunkten der Route.
    if len(arr) > 1:
        for i in range(len(arr) - 1):
            start = arr[i]
            end = arr[i + 1]
            vec = end - start
            # Es wird eine gestrichelte grüne Linie zwischen Start und Zielpunkt jedes Segments gezeichnet.
            ax.plot([start[0], end[0]], [start[1], end[1]], color='green', linestyle='--', linewidth=2, alpha=0.8)
            # Optional (auskommentiert): Zeichnen von Pfeilen für die Richtung.
            time_seg = fahrzeit(route[i], route[i + 1])
            mid = (start + end) / 2
            # Die Fahrtzeit für jedes Teilstück wird als kleiner grüner Wert in die Mitte des Segments geschrieben.
            ax.text(mid[0], mid[1], f'{time_seg:.0f} min', color='darkgreen', fontsize=8,
                    ha='center', va='center', bbox=dict(facecolor='black', alpha=0.4, boxstyle='round,pad=0.2'))

    ax.set_title(info)
    # Überschrift: Liefert die Info/Resultat zur Route.
    ax.legend()
    plt.draw()
    # Das Diagramm wird mit allen neuen Elementen aktualisiert angezeigt.


def onclick(event):
    # Diese Funktion wird ausgeführt, wenn der Benutzer im Plot auf einen Punkt (Kunden) klickt.
    if event.inaxes == ax:
        # Sicherstellen, dass der Klick im Bereich der Achsen (des Diagramms) passiert ist.
        x, y = event.xdata, event.ydata
        # Die Koordinaten des Klicks werden gespeichert.
        distanzen = np.linalg.norm(staedte - np.array([x, y]), axis=1)
        # Für jede Stadt wird nun der Abstand des Klickpunkts (x, y) zu deren Koordinaten berechnet.
        closest = np.argmin(distanzen)
        # Index des Punktes, zu dem der Klick am nächsten ist, wird ermittelt.
        if closest not in fixer_punkt and closest != startpunkt:
            # Nur falls noch nicht als Fixpunkt ausgewählt und nicht der Startpunkt
            root = tk.Tk()
            # Ein unsichtbares Fenster wird erzeugt, um später ein Eingabefeld zu öffnen.
            root.withdraw()
            min_time = int(fahrzeit(startpunkt, closest)) + 1
            # Mindestzeit von Start zum gewählten Punkt (als Vorschlag für den Benutzer).
            prompt = f"Ankunftszeit am Fixpunkt {closest} in Minuten ab Start (mind. {min_time}):"
            # Der Benutzer wird gefragt, wie spät er am Fixpunkt ankommen darf (zwischen min_time und max_fahrzeit).
            user_time = askinteger("Zielzeit angeben", prompt, minvalue=min_time, maxvalue=max_fahrzeit)
            root.destroy()
            # Das unsichtbare Fenster wird geschlossen.
            if user_time is None:
                # Falls der Benutzer den Dialog abbricht, passiert nichts.
                return
            fixer_punkt.append(closest)
            # Der gewählte Punkt wird zu den Fixpunkten hinzugefügt.
            priority_time_dict[closest] = user_time
            # Für diesen Fixpunkt wird die gewünschte Ankunftszeit gespeichert.
            solve()
            # Die neue Route wird sofort berechnet und angezeigt.


fig, ax = plt.subplots(figsize=(12, 7))
# Hier wird ein neues Fenster mit einer Zeichenfläche ("Plot") erzeugt,
# auf die später alle Kunden, Routen usw. gemalt werden können.
scatter = ax.scatter(staedte[:, 0], staedte[:, 1], c='blue', label='Kunden')
# Die Kunden werden als blaue Punkte angezeigt. Das Label dient dazu, die Beschriftung in der Legende zu ermöglichen.
ax.scatter(staedte[startpunkt, 0], staedte[startpunkt, 1], c='black', s=300, marker='o',
           edgecolors='yellow', linewidths=4, label='Start/Ende')
# Der Startpunkt wird groß und besonders auffällig mit gelbem Rand markiert.
plt.title("Klicken Sie auf Punkte um Prioritätskunden zu wählen")
# Überschrift des Fensters: Der Nutzer erhält eine Handlungsanweisung.
ax_button = plt.axes([0.7, 0.02, 0.2, 0.05])
# Es wird ein zusätzlicher Bereich für einen Button angelegt (unten, breit).
button = Button(ax_button, 'Route berechnen', color='lightgoldenrodyellow', hovercolor='0.975')
# Ein Button mit Beschriftung "Route berechnen" wird erstellt.
button.on_clicked(solve)
# Beim Klick auf den Button wird die Funktion solve() ausgeführt.
fig.canvas.mpl_connect('button_press_event', onclick)
# Wenn der Nutzer auf einen Punkt im Diagramm klickt, wird die Funktion onclick ausgeführt.
def on_key(event):
    if event.key == 'escape':
        plt.close(event.canvas.figure)
# Wenn der Nutzer die Escape-Taste drückt, schließt sich das Plot-Fenster.
fig.canvas.mpl_connect('key_press_event', on_key)
# Verbindet die Funktion on_key mit Tasteneingaben im Plot-Fenster.
ax.legend()
# Die Legende (Erklärung der Symbole) wird hinzugefügt.
plt.tight_layout()
# Optimiert die Verteilung der Grafik-Elemente im Fenster.
plt.show()
# Zeigt das Fenster mit dem Plot an und wartet auf Maus- oder Tastatureingaben des Nutzers.



print('\n\n\n\n--------------\n\n\n')
# Gibt ein paar Zeilen Abstand und eine Auffällige Linie zur Trennung in der Konsolenausgabe aus.
print('Ausgaben zum besseren Verständnis der Variablen:')
# Hinweistext für die folgende Schlaufausgabe
print(f'Zeit, um zum Prioritätskunden zu gelangen (priority_time_dict):{priority_time_dict}')
# Gibt das aktuelle Dictionary mit allen erlaubten Ankunftszeiten zu den Fixpunkten aus.
print(f'Liste fixer_punkt:{fixer_punkt}')
# Gibt die Liste aller aktuell als Fixpunkte markierten Städte (Start und gewählte Prioritätskunden) aus.
