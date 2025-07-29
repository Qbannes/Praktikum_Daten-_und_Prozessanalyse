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

def solve(event=None):
    # Diese Funktion wird aufgerufen, wenn der Button "Route berechnen" geklickt wird.
    # Die Funktion 'solve' erwartet ein optionales Argument 'event',
    # das standardmäßig auf None gesetzt ist, falls kein Ereignis übergeben wird. 
    ## ax.clear()
    # ax ist hier eine Variable ein sogenanntes Achsenobjekt, die eine Achse (axis) in Matplotlib repräsentiert. 
    # ax ist mit der Funktion/Methode clear() durch einen Punkt '.' verbunden, wodurch die Variable auf die Methode clear() zugreift.
    # ax.clear() bleibt hier auskommentiert, das es nicht gebraucht wird, erst dann, wenn sich die Struktur der ANzeige stark ändert z.B.
    # von Karte zu Statistik.
    ax.scatter(staedte[:, 0], staedte[:, 1], c='blue', label='Kunden')
    # scatter ist eine Methode von Matplotlib, die Punkte auf ein 2D-Diagramm zeichnet. 
    # 
    ax.scatter(staedte[fixer_punkt, 0], staedte[fixer_punkt, 1], c='red', s=100, marker='X', label='Fixpunkte (inkl. Start)')
    ax.scatter(staedte[startpunkt, 0], staedte[startpunkt, 1], c='black', s=140, marker='o',
               edgecolors='yellow', linewidths=3, label='Start/Ende')

    if len(fixer_punkt) < 2:
        ax.set_title("Bitte zuerst mindestens einen Prioritätskunden (roter Punkt) wählen!")
        ax.legend()
        plt.draw()
        return

    depot = startpunkt
    pri_idx = fixer_punkt[1]
    arrival_limit = priority_time_dict[pri_idx]

    all_indices = set(range(stadtzahl))
    stops_hinweg = [depot]
    t = 0
    curr = depot
    unbesucht = all_indices - set([depot, pri_idx])

    while True:
        next_options = []
        for k in unbesucht:
            t_to_k = fahrzeit(curr, k)
            t_k_to_prio = fahrzeit(k, pri_idx)
            if t + t_to_k + t_k_to_prio <= arrival_limit:
                next_options.append((t_to_k, k))
        if not next_options:
            break
        _, nxt = min(next_options)
        t += fahrzeit(curr, nxt)
        stops_hinweg.append(nxt)
        curr = nxt
        unbesucht.remove(nxt)

    t_to_prio = fahrzeit(curr, pri_idx)
    if t + t_to_prio > arrival_limit:
        route = stops_hinweg
        info = f"Route nicht möglich: Mindestens zum Prioritätskunden pünktlich ankommen!"
        show_route(route + [depot], info)
        return

    t += t_to_prio
    stops_hinweg.append(pri_idx)

    stops_rueckweg = []
    curr = pri_idx
    while unbesucht:
        next_options = []
        for k in unbesucht:
            t_to_k = fahrzeit(curr, k)
            t_k_to_depot = fahrzeit(k, depot)
            if t + t_to_k + t_k_to_depot <= max_fahrzeit:
                next_options.append((t_to_k, k))
        if not next_options:
            break
        _, nxt = min(next_options)
        t += fahrzeit(curr, nxt)
        stops_rueckweg.append(nxt)
        curr = nxt
        unbesucht.remove(nxt)

    t_to_depot = fahrzeit(curr, depot)
    if t + t_to_depot > max_fahrzeit:
        route = stops_hinweg + stops_rueckweg
        info = f"Route nicht möglich: Fahrer schafft Rückweg zu Depot nicht mehr innerhalb von 9 Stunden!"
        show_route(route + [depot], info)
        return

    route = stops_hinweg + stops_rueckweg + [depot]
    info = f"Beste Route: Fahrzeit {t + t_to_depot:.1f} min, {len(route) - 1} Kunden besucht"
    show_route(route, info)

def show_route(route, info):
    # Fixpunkte und Start/Ende nochmal für saubere Anzeige
    ax.scatter(staedte[fixer_punkt, 0], staedte[fixer_punkt, 1], c='red', s=100, marker='X', label='Fixpunkte (inkl. Start)')
    ax.scatter(staedte[startpunkt, 0], staedte[startpunkt, 1], c='black', s=140, marker='o',
               edgecolors='yellow', linewidths=3, label='Start/Ende')
    arr = np.array([staedte[i] for i in route])
    if len(arr) > 1:
        for i in range(len(arr) - 1):
            start = arr[i]
            end = arr[i + 1]
            vec = end - start
            ax.plot([start[0], end[0]], [start[1], end[1]], color='green', linestyle='--', linewidth=2, alpha=0.8)
            ## ax.arrow(start[0], start[1], vec[0]*0.4, vec[1]*0.4, head_width=4, head_length=7, fc='green', ec='green', length_includes_head=True, alpha=0.9, linewidth=2)
            time_seg = fahrzeit(route[i], route[i + 1])
            mid = (start + end) / 2
            ax.text(mid[0], mid[1], f'{time_seg:.0f} min', color='darkgreen', fontsize=8,
                    ha='center', va='center', bbox=dict(facecolor='black', alpha=0.4, boxstyle='round,pad=0.2'))

    ax.set_title(info)
    ax.legend()
    plt.draw()

def onclick(event):
    if event.inaxes == ax:
        x, y = event.xdata, event.ydata
        distanzen = np.linalg.norm(staedte - np.array([x, y]), axis=1)
        closest = np.argmin(distanzen)
        if closest not in fixer_punkt and closest != startpunkt:
            root = tk.Tk()
            root.withdraw()
            min_time = int(fahrzeit(startpunkt, closest)) + 1
            prompt = f"Ankunftszeit am Fixpunkt {closest} in Minuten ab Start (mind. {min_time}):"
            user_time = askinteger("Zielzeit angeben", prompt, minvalue=min_time, maxvalue=max_fahrzeit)
            root.destroy()
            if user_time is None:
                return
            fixer_punkt.append(closest)
            priority_time_dict[closest] = user_time
            solve()

fig, ax = plt.subplots(figsize=(12, 7))
scatter = ax.scatter(staedte[:, 0], staedte[:, 1], c='blue', label='Kunden')
ax.scatter(staedte[startpunkt, 0], staedte[startpunkt, 1], c='black', s=140, marker='o',
           edgecolors='yellow', linewidths=3, label='Start/Ende')
plt.title("Klicken Sie auf Punkte um Prioritätskunden zu wählen")
ax_button = plt.axes([0.7, 0.02, 0.2, 0.05])
button = Button(ax_button, 'Route berechnen', color='lightgoldenrodyellow', hovercolor='0.975')
button.on_clicked(solve)
fig.canvas.mpl_connect('button_press_event', onclick)
def on_key(event):
    if event.key == 'escape':
        plt.close(event.canvas.figure)
fig.canvas.mpl_connect('key_press_event', on_key)
ax.legend()
plt.tight_layout()
plt.show()
print(priority_time_dict)