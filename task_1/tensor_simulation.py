import numpy as np
import matplotlib.pyplot as plt
import time

# Define basic quantum gates as tensors
I = np.array([[1, 0], [0, 1]])
X = np.array([[0, 1], [1, 0]])
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]).reshape(2, 2, 2, 2)

def initialize_state(n_qubits):
    """Initialize the state tensor for n qubits."""
    return np.array([1] + [0] * (2**n_qubits - 1)).reshape([2] * n_qubits)

def apply_single_qubit_gate(state, gate, target_qubit):
    """Apply a single qubit gate to the state tensor."""
    return np.tensordot(state, gate, axes=([target_qubit], [1])).transpose(np.roll(range(state.ndim), 1))

def apply_cnot(state, control_qubit, target_qubit):
    """Apply a CNOT gate to the state tensor."""
    return np.tensordot(state, CNOT, axes=([control_qubit, target_qubit], [2, 3])).transpose(np.roll(range(state.ndim), 2))

def run_circuit(n_qubits, gates):
    """Run a quantum circuit with the given gates."""
    state = initialize_state(n_qubits)
    for gate, target, control in gates:
        if control is None:
            state = apply_single_qubit_gate(state, gate, target)
        else:
            state = apply_cnot(state, control, target)
    return state

def measure_runtime(max_qubits):
    """Measure the runtime of the simulation for different numbers of qubits."""
    runtimes = []
    qubit_range = range(2, max_qubits + 1)
    
    for n_qubits in qubit_range:
        gates = [
            (H, 0, None),
            (X, 1, None),
            (CNOT, 1, 0),
            (H, 0, None)
        ]
        
        start_time = time.time()
        run_circuit(n_qubits, gates)
        end_time = time.time()
        
        runtimes.append(end_time - start_time)
    
    return qubit_range, runtimes

def plot_runtime(qubit_range, runtimes):
    """Plot the runtime as a function of the number of qubits."""
    plt.figure(figsize=(10, 6))
    plt.plot(qubit_range, runtimes, marker='o')
    plt.title('Runtime vs Number of Qubits (Tensor Simulation)')
    plt.xlabel('Number of Qubits')
    plt.ylabel('Runtime (seconds)')
    plt.yscale('log')
    plt.grid(True)
    plt.show()

# Run the simulation and plot the results
max_qubits = 20  # Adjust this value based on your computer's capabilities
qubit_range, runtimes = measure_runtime(max_qubits)
plot_runtime(qubit_range, runtimes)
