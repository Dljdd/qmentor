import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error

from quantum_sum import quantum_sum
from basis_transform import transform_to_basis
from noise_model import add_noise

def run_noisy_addition(a: int, b: int, n: int, p1: float, p2: float, shots: int = 1000):
    """
    Run the noisy quantum addition and return the results.
    
    Args:
    a (int): First number to add
    b (int): Second number to add
    n (int): Number of qubits
    p1 (float): Probability of noise after one-qubit gates
    p2 (float): Probability of noise after two-qubit gates
    shots (int): Number of shots for the simulation
    
    Returns:
    dict: Measurement results
    """
    try:
        circuit = quantum_sum(a, b, n)
        print(f"Original circuit qubits: {circuit.num_qubits}")
        print(f"Original circuit operations: {[inst.operation.name for inst in circuit.data]}")
        
        basis_circuit = transform_to_basis(circuit)
        print(f"Basis circuit qubits: {basis_circuit.num_qubits}")
        print(f"Basis circuit operations: {[inst.operation.name for inst in basis_circuit.data]}")
        
        noisy_circuit = add_noise(basis_circuit, p1, p2)
        print(f"Noisy circuit qubits: {noisy_circuit.num_qubits}")
        print(f"Noisy circuit operations: {[inst.operation.name for inst in noisy_circuit.data]}")
        
        # Create a noise model
        noise_model = NoiseModel()
        
        # Add depolarizing error to all single qubit gates
        error_1 = depolarizing_error(p1, 1)
        noise_model.add_all_qubit_quantum_error(error_1, ['u1', 'u2', 'u3'])
        
        # Add depolarizing error to all two qubit gates
        error_2 = depolarizing_error(p2, 2)
        noise_model.add_all_qubit_quantum_error(error_2, ['cx'])
        
        backend = AerSimulator(noise_model=noise_model)
        job = backend.run(noisy_circuit, shots=shots)
        return job.result().get_counts()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        return None

def analyze_noise_effects():
    a, b = 3, 5
    n = 4  # number of qubits
    noise_levels = [0, 0.01, 0.05, 0.1, 0.2]
    
    plt.figure(figsize=(15, 10))
    
    for i, p in enumerate(noise_levels):
        print(f"\nNoise level: {p}")
        results = run_noisy_addition(a, b, n, p, p)
        if results:
            plt.subplot(2, 3, i+1)
            plot_histogram(results)
            plt.title(f"Noise level: {p}")
        else:
            print(f"Skipping noise level {p} due to an error")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    analyze_noise_effects()
