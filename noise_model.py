import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import PauliGate

def add_noise(circuit: QuantumCircuit, p1: float, p2: float) -> QuantumCircuit:
    """
    Add noise to the quantum circuit.
    
    Args:
    circuit (QuantumCircuit): The input quantum circuit
    p1 (float): Probability of noise after one-qubit gates
    p2 (float): Probability of noise after two-qubit gates
    
    Returns:
    QuantumCircuit: The quantum circuit with added noise
    """
    # Create a new circuit with the same structure as the original
    noisy_circuit = QuantumCircuit(*circuit.qregs, *circuit.cregs)
    
    for instruction in circuit.data:
        noisy_circuit.append(instruction)
        
        # Determine if it's a one-qubit or two-qubit gate
        num_qubits = len(instruction.qubits)
        
        if num_qubits == 1 and np.random.random() < p1:
            pauli = np.random.choice(['X', 'Y', 'Z'])
            noisy_circuit.append(PauliGate(pauli), instruction.qubits)
        elif num_qubits == 2 and np.random.random() < p2:
            for qubit in instruction.qubits:
                pauli = np.random.choice(['X', 'Y', 'Z'])
                noisy_circuit.append(PauliGate(pauli), [qubit])
    
    return noisy_circuit
