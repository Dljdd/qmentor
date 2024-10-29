from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qft import qft, inverse_qft
import numpy as np

def quantum_sum(a: int, b: int, n: int) -> QuantumCircuit:
    """
    Implement the Draper adder algorithm to add two numbers.
    
    Args:
    a (int): First number to add
    b (int): Second number to add
    n (int): Number of qubits to use (should be sufficient to represent a + b)
    
    Returns:
    QuantumCircuit: The quantum circuit for addition
    """
    qr = QuantumRegister(2*n)
    cr = ClassicalRegister(n)
    circuit = QuantumCircuit(qr, cr)
    
    # Initialize registers with a and b
    for i in range(n):
        if (a & (1 << i)) != 0:
            circuit.x(qr[i])
        if (b & (1 << i)) != 0:
            circuit.x(qr[i + n])
    
    # Apply QFT to the first register
    circuit.append(qft(n), qr[:n])
    
    # Apply controlled phase rotations
    for i in range(n):
        for j in range(n-i):
            angle = 2 * np.pi / (2**(j+1))
            circuit.cp(angle, qr[i+n], qr[n-j-1])
    
    # Apply inverse QFT
    circuit.append(inverse_qft(n), qr[:n])
    
    # Measure the result
    circuit.measure(qr[:n], cr)
    
    return circuit
