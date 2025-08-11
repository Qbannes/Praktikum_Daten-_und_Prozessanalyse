from qiskit import QuantumCircuit
print("✅ Qiskit ist bereit!")
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
print(qc.draw())
