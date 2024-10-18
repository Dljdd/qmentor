# quantum_simulation_qiskit.py

from qiskit import QuantumCircuit, Aer, execute
import numpy as np
import matplotlib.pyplot as plt
import time

# Function to simulate a quantum circuit
def simulate_circuit(n):
    # Create a quantum circuit with n qubits
    circuit = QuantumCircuit(n)

    # Apply gates
    circuit.h(0)  # Apply Hadamard to the first qubit
    circuit.x(0)  # Apply X gate to the first qubit
    # Add more gates as needed

    # Use the statevector simulator
    simulator = Aer.get_backend('statevector_simulator')
    result = execute(circuit, simulator).result()
    statevector = result.get_statevector()

    return statevector

# Measure runtime
def measure_runtime(n):
    start_time = time.time()
    simulate_circuit(n)
    return time.time() - start_time

# Plot runtime
def plot_runtime(max_qubits):
    runtimes = []
    for n in range(1, max_qubits + 1):
        runtimes.append(measure_runtime(n))
    
    plt.plot(range(1, max_qubits + 1), runtimes)
    plt.xlabel('Number of Qubits')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime vs Number of Qubits (Qiskit)')
    plt.show()

# Example usage
plot_runtime(10)  # Adjust the number of qubits as needed