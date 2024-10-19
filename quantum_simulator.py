import numpy as np
import matplotlib.pyplot as plt
import time

# Define basic quantum gates
I = np.array([[1, 0], [0, 1]])
X = np.array([[0, 1], [1, 0]])
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]])

def initialize_state(n_qubits):
    """Initialize the state vector for n qubits."""
    return np.array([1] + [0] * (2**n_qubits - 1))

def apply_single_qubit_gate(state, gate, target_qubit, n_qubits):
    """Apply a single qubit gate to the state vector."""
    gate_expanded = np.eye(2**n_qubits, dtype=complex)
    gate_expanded = np.kron(np.eye(2**target_qubit), np.kron(gate, np.eye(2**(n_qubits-target_qubit-1))))
    return np.dot(gate_expanded, state)

def apply_cnot(state, control_qubit, target_qubit, n_qubits):
    """Apply a CNOT gate to the state vector."""
    if n_qubits < 2:
        raise ValueError("CNOT gate requires at least 2 qubits")
    
    control_mask = 1 << control_qubit
    target_mask = 1 << target_qubit
    
    new_state = state.copy()
    for i in range(2**n_qubits):
        if i & control_mask:
            j = i ^ target_mask
            new_state[i], new_state[j] = new_state[j], new_state[i]
    
    return new_state

def apply_gate(state, gate, target_qubit, n_qubits, control_qubit=None):
    """Apply a quantum gate to the state vector."""
    if control_qubit is None:
        return apply_single_qubit_gate(state, gate, target_qubit, n_qubits)
    else:
        return apply_cnot(state, control_qubit, target_qubit, n_qubits)

def run_circuit(n_qubits, gates):
    """Run a quantum circuit with the given gates."""
    state = initialize_state(n_qubits)
    for gate, target, control in gates:
        state = apply_gate(state, gate, target, n_qubits, control)
    return state

def measure_runtime(max_qubits):
    """Measure the runtime of the simulation for different numbers of qubits."""
    runtimes = []
    qubit_range = range(2, max_qubits + 1)  # Start from 2 qubits
    
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
    plt.title('Runtime vs Number of Qubits')
    plt.xlabel('Number of Qubits')
    plt.ylabel('Runtime (seconds)')
    plt.yscale('log')
    plt.grid(True)
    plt.show()

# Run the simulation and plot the results
max_qubits = 20  # Adjust this value based on your computer's capabilities
qubit_range, runtimes = measure_runtime(max_qubits)
plot_runtime(qubit_range, runtimes)
