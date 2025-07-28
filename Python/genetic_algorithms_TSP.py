import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import tkinter as tk
from tkinter.simpledialog import askinteger

np.random.seed(42)
num_cities = 50
cities = np.random.rand(num_cities, 2) * 300
speed = 60  # km/h
max_drive_time = 9 * 60  # Minuten
start_point = 0
fixed_points = [start_point]
priority_time_dict = {start_point: 0}

def drive_time(a, b):
    dist = np.linalg.norm(cities[a] - cities[b])
    return dist / speed * 60

def solve(event=None):
    ax.clear()
    # Kunden
    ax.scatter(cities[:, 0], cities[:, 1], c='blue', label='Kunden')
    # Fixpunkte und Start/Ende
    ax.scatter(cities[fixed_points, 0], cities[fixed_points, 1], c='red', s=100, marker='X', label='Fixpunkte (inkl. Start)')
    ax.scatter(cities[start_point, 0], cities[start_point, 1], c='black', s=140, marker='o',
               edgecolors='yellow', linewidths=3, label='Start/Ende')

    if len(fixed_points) < 2:
        ax.set_title("Bitte zuerst mindestens einen Prioritätskunden (roter Punkt) wählen!")
        ax.legend()
        plt.draw()
        return

    depot = start_point
    pri_idx = fixed_points[1]
    arrival_limit = priority_time_dict[pri_idx]

    all_indices = set(range(num_cities))
    stops_hinweg = [depot]
    t = 0
    curr = depot
    unvisited = all_indices - set([depot, pri_idx])

    while True:
        next_options = []
        for k in unvisited:
            t_to_k = drive_time(curr, k)
            t_k_to_prio = drive_time(k, pri_idx)
            if t + t_to_k + t_k_to_prio <= arrival_limit:
                next_options.append((t_to_k, k))
        if not next_options:
            break
        _, nxt = min(next_options)
        t += drive_time(curr, nxt)
        stops_hinweg.append(nxt)
        curr = nxt
        unvisited.remove(nxt)

    t_to_prio = drive_time(curr, pri_idx)
    if t + t_to_prio > arrival_limit:
        route = stops_hinweg
        info = f"Route nicht möglich: Mindestens zum Prioritätskunden pünktlich ankommen!"
        show_route(route + [depot], info)
        return

    t += t_to_prio
    stops_hinweg.append(pri_idx)

    stops_rueckweg = []
    curr = pri_idx
    while unvisited:
        next_options = []
        for k in unvisited:
            t_to_k = drive_time(curr, k)
            t_k_to_depot = drive_time(k, depot)
            if t + t_to_k + t_k_to_depot <= max_drive_time:
                next_options.append((t_to_k, k))
        if not next_options:
            break
        _, nxt = min(next_options)
        t += drive_time(curr, nxt)
        stops_rueckweg.append(nxt)
        curr = nxt
        unvisited.remove(nxt)

    t_to_depot = drive_time(curr, depot)
    if t + t_to_depot > max_drive_time:
        route = stops_hinweg + stops_rueckweg
        info = f"Route nicht möglich: Fahrer schafft Rückweg zu Depot nicht mehr innerhalb von 9 Stunden!"
        show_route(route + [depot], info)
        return

    route = stops_hinweg + stops_rueckweg + [depot]
    info = f"Beste Route: Fahrzeit {t + t_to_depot:.1f} min, {len(route) - 1} Kunden besucht"
    show_route(route, info)

def show_route(route, info):
    # Fixpunkte und Start/Ende nochmal für saubere Anzeige
    ax.scatter(cities[fixed_points, 0], cities[fixed_points, 1], c='red', s=100, marker='X', label='Fixpunkte (inkl. Start)')
    ax.scatter(cities[start_point, 0], cities[start_point, 1], c='black', s=140, marker='o',
               edgecolors='yellow', linewidths=3, label='Start/Ende')
    arr = np.array([cities[i] for i in route])
    if len(arr) > 1:
        for i in range(len(arr) - 1):
            start = arr[i]
            end = arr[i + 1]
            vec = end - start
            ax.plot([start[0], end[0]], [start[1], end[1]], color='green', linestyle='--', linewidth=2, alpha=0.8)
            ax.arrow(start[0], start[1], vec[0]*0.4, vec[1]*0.4, head_width=4, head_length=7, fc='green', ec='green', length_includes_head=True, alpha=0.9, linewidth=2)
            time_seg = drive_time(route[i], route[i + 1])
            mid = (start + end) / 2
            ax.text(mid[0], mid[1], f'{time_seg:.0f} min', color='darkgreen', fontsize=8,
                    ha='center', va='center', bbox=dict(facecolor='black', alpha=0.4, boxstyle='round,pad=0.2'))

    ax.set_title(info)
    ax.legend()
    plt.draw()

def onclick(event):
    if event.inaxes == ax:
        x, y = event.xdata, event.ydata
        distances = np.linalg.norm(cities - np.array([x, y]), axis=1)
        closest = np.argmin(distances)
        if closest not in fixed_points and closest != start_point:
            root = tk.Tk()
            root.withdraw()
            min_time = int(drive_time(start_point, closest)) + 1
            prompt = f"Ankunftszeit am Fixpunkt {closest} in Minuten ab Start (mind. {min_time}):"
            user_time = askinteger("Zielzeit angeben", prompt, minvalue=min_time, maxvalue=max_drive_time)
            root.destroy()
            if user_time is None:
                return
            fixed_points.append(closest)
            priority_time_dict[closest] = user_time
            solve()

fig, ax = plt.subplots(figsize=(12, 7))
scatter = ax.scatter(cities[:, 0], cities[:, 1], c='blue', label='Kunden')
ax.scatter(cities[start_point, 0], cities[start_point, 1], c='black', s=140, marker='o',
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
