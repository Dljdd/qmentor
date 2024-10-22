import numpy as np
import matplotlib.pyplot as plt
import time

# Import functions from matrix-based simulation
from task_1.quantum_simulator import run_circuit
from task_1.tensor_simulation import run_circuit
from task_1.quantum_simulator import H, X, CNOT
from task_1.tensor_simulation import H, X, CNOT

def compare_runtimes(max_qubits):
    """Compare runtimes of matrix-based and tensor-based simulations."""
    matrix_runtimes = []
    tensor_runtimes = []
    qubit_range = range(2, max_qubits + 1)
    
    for n_qubits in qubit_range:
        gates = [
            (H, 0, None),
            (X, 1, None),
            (CNOT, 1, 0),
            (H, 0, None)
        ]
        
        # Matrix-based simulation
        start_time = time.time()
        run_circuit(n_qubits, gates)  # From quantum_simulator.py
        matrix_runtimes.append(time.time() - start_time)
        
        # Tensor-based simulation
        start_time = time.time()
        run_circuit(n_qubits, gates)  # From tensor_simulation.py
        tensor_runtimes.append(time.time() - start_time)
    
    return qubit_range, matrix_runtimes, tensor_runtimes

def plot_comparison(qubit_range, matrix_runtimes, tensor_runtimes):
    """Plot the runtime comparison."""
    plt.figure(figsize=(10, 6))
    plt.plot(qubit_range, matrix_runtimes, marker='o', label='Matrix-based')
    plt.plot(qubit_range, tensor_runtimes, marker='s', label='Tensor-based')
    plt.title('Runtime Comparison: Matrix-based vs Tensor-based Simulation')
    plt.xlabel('Number of Qubits')
    plt.ylabel('Runtime (seconds)')
    plt.yscale('log')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the comparison and plot the results
max_qubits = 20  # Adjust this value based on your computer's capabilities
qubit_range, matrix_runtimes, tensor_runtimes = compare_runtimes(max_qubits)
plot_comparison(qubit_range, matrix_runtimes, tensor_runtimes)
