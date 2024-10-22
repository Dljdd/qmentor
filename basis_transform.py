from qiskit import QuantumCircuit
from qiskit.circuit.library import UGate

def transform_to_basis(circuit: QuantumCircuit) -> QuantumCircuit:
    """
    Transform the given circuit to the basis gates (U and CX).
    
    Args:
    circuit (QuantumCircuit): The input quantum circuit
    
    Returns:
    QuantumCircuit: The transformed quantum circuit
    """
    basis_circuit = QuantumCircuit(circuit.num_qubits, circuit.num_clbits)
    
    for instruction in circuit.data:
        if instruction.operation.name in ['u', 'cx']:
            basis_circuit.append(instruction)
        else:
            # Decompose other gates into U and CX gates
            decomposed = instruction.operation.definition
            if decomposed is not None:
                for decomposed_instruction in decomposed.data:
                    # Map the qubits from the decomposed instruction to the original circuit
                    qargs = [instruction.qubits[decomposed.qubits.index(q)] for q in decomposed_instruction.qubits]
                    cargs = [instruction.clbits[decomposed.clbits.index(c)] for c in decomposed_instruction.clbits if c in decomposed.clbits]
                    basis_circuit.append(decomposed_instruction.operation, qargs, cargs)
            else:
                # If the gate can't be decomposed, just add it as is
                basis_circuit.append(instruction)
    
    return basis_circuit
