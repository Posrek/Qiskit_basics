# Statevector class provides functionality for defining and manipulating quantum state vectors
from qiskit.quantum_info import Statevector

# Operators
from numpy import sqrt
from qiskit.quantum_info import Operator

X = Operator([[0, 1], [1, 0]])
Y = Operator([[0, -1.0j], [1.0j, 0]])
Z = Operator([[1, 0], [0, -1]])
H = Operator([[1 / sqrt(2), 1 / sqrt(2)], [1 / sqrt(2), -1 / sqrt(2)]])
S = Operator([[1, 0], [0, 1.0j]])
T = Operator([[1, 0], [0, (1 + 1.0j) / sqrt(2)]])

v = Statevector([1, 0])

from qiskit import QuantumCircuit

circuit = QuantumCircuit(1)

# Set up the sequence of unitary operators
circuit.h(0)
circuit.t(0)
circuit.h(0)
circuit.t(0)
circuit.z(0)

# Draw the circuit
circuit.draw()

# Initialization of a quantum circuit
ket0 = Statevector([1, 0])
v = ket0.evolve(circuit)

v.draw("text")
v.draw("latex") # !check why is the visualization not working as intended

# visualization of the measurement
from qiskit.visualization import plot_histogram
statistics = v.sample_counts(4000)
plot_histogram(statistics) # !check why is the visualization not working as intended
