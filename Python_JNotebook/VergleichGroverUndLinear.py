import time
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, transpile


def linear_search(items, target):
    """Klassische lineare Suche mit größeren Datenmengen"""
    return items.index(target) if target in items else -1


def grover_simulation(n_qubits):
    """Optimierte Grover-Simulation für bis zu 7 Qubits (max. 2097152 Items)"""
    qc = QuantumCircuit(n_qubits)

    qc.h(range(n_qubits))
    for _ in range(int(np.pi / 4 * np.sqrt(2 ** n_qubits))):  # Grover-Iterationen
        qc.append(QuantumCircuit(n_qubits).to_gate(), range(n_qubits))  # Platzhalter-Orakel
        qc.h(range(n_qubits))
        qc.x(range(n_qubits))
        qc.h(n_qubits - 1)
        if n_qubits > 1:
            qc.mcx(list(range(n_qubits - 1)), n_qubits - 1)
        else:
            qc.x(n_qubits - 1)
        qc.h(n_qubits - 1)
        qc.x(range(n_qubits))
        qc.h(range(n_qubits))

    simulator = Aer.get_backend('aer_simulator')
    start = time.time()
    transpile(qc, simulator, optimization_level=1)
    return time.time() - start


def compare_algorithms():
    """Vergleich mit bis zu 2097152 Items und verbesserter Visualisierung"""
    sizes = [2 ** n for n in range(1, 21)]  # 2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536, 131072, 262144, 524288, 1048576, 2097152
    classical_times = []
    quantum_times = []

    for size in sizes:
        items = list(range(size))
        target = size - 1

        classical_time = np.mean([
            timeit.timeit(lambda: linear_search(items, target), number=1000)
            for _ in range(3)
        ])

        # Quantensimulation jetzt bis 128 Items
        if size >= 4 and size <= 2097152:
            quantum_time = grover_simulation(int(np.log2(size)))
        else:
            quantum_time = np.nan

        classical_times.append(classical_time)
        quantum_times.append(quantum_time)
        print(f"Größe {size}: Klassisch={classical_time:.6f}s | Quanten={quantum_time:.6f}s")

    # NaN-Werte herausfiltern für den Plot
    valid_quantum_times = [qt for qt in quantum_times if not np.isnan(qt)]
    valid_sizes = [s for s, qt in zip(sizes, quantum_times) if not np.isnan(qt)]

    plt.figure(figsize=(12, 7))
    plt.plot(sizes, classical_times, 'b-o', label='Lineare Suche (O(n))')
    plt.plot(valid_sizes, valid_quantum_times, 'r--o', label='Grover-Simulation (O(√n))')
    plt.xscale('log', base=2)
    plt.yscale('log')
    plt.xlabel('Anzahl der Elemente (log-Skala)')
    plt.ylabel('Zeit (Sekunden, log-Skala)')
    plt.title('Leistungsvergleich: Klassisch vs. Quanten (bis 2097152 Elemente)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig('vergleich_2097152.png', dpi=600, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    import timeit
    print("=== Leistungsvergleich (bis zu 2097152 Elemente) ===")
    compare_algorithms()
