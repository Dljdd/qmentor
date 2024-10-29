import numpy as np
from qiskit import QuantumCircuit

def qft(n: int) -> QuantumCircuit:
    """
    Implement the Quantum Fourier Transform.
    
    Args:
    n (int): Number of qubits
    
    Returns:
    QuantumCircuit: The QFT circuit
    """
    circuit = QuantumCircuit(n)
    
    for j in range(n):
        for k in range(j):
            circuit.cp(np.pi / float(2**(j-k)), k, j)
        circuit.h(j)
    
    # Swap qubits
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)
    
    return circuit

def inverse_qft(n: int) -> QuantumCircuit:
    """
    Implement the inverse Quantum Fourier Transform.
    
    Args:
    n (int): Number of qubits
    
    Returns:
    QuantumCircuit: The inverse QFT circuit
    """
    return qft(n).inverse()
