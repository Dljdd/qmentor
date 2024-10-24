from qiskit import QuantumCircuit, transpile

def transform_to_basis(circuit: QuantumCircuit) -> QuantumCircuit:
    """
    Transform a general Quantum Circuit to the gate basis {CX, ID, RZ, SX, X}.
    
    Args:
    circuit (QuantumCircuit): The input quantum circuit
    
    Returns:
    QuantumCircuit: The transformed quantum circuit
    """
    basis_gates = ['cx', 'id', 'rz', 'sx', 'x']
    
    # Use Qiskit's transpile function to convert the circuit to the desired basis
    # while preserving the original circuit structure
    transformed_circuit = transpile(
        circuit,
        basis_gates=basis_gates,
        optimization_level=3,
        layout_method='trivial',
        routing_method='none'
    )
    
    return transformed_circuit
