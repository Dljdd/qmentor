import numpy as np

def sample_from_statevector(statevector, num_samples=1000):
    """Sample from the final states in the statevector representation."""
    probabilities = np.abs(statevector)**2
    states = np.arange(len(statevector))
    samples = np.random.choice(states, size=num_samples, p=probabilities)
    return samples

def sample_from_tensor(state_tensor, num_samples=1000):
    """Sample from the final states in the tensor representation."""
    probabilities = np.abs(state_tensor.flatten())**2
    states = np.arange(state_tensor.size)
    samples = np.random.choice(states, size=num_samples, p=probabilities)
    return samples

def compute_expectation_value(statevector, operator):
    """Compute the expectation value <Ψ| Op |Ψ>."""
    return np.real(np.dot(np.conj(statevector), np.dot(operator, statevector)))

# Example usage
if __name__ == "__main__":
    # Assume we have a statevector from a previous simulation
    statevector = np.array([0.5, 0.5, 0.5, 0.5])
    
    # Sampling from statevector
    samples = sample_from_statevector(statevector)
    print("Samples from statevector:", samples)
    
    # Assume we have a state tensor from a previous simulation
    state_tensor = statevector.reshape(2, 2)
    
    # Sampling from tensor
    samples = sample_from_tensor(state_tensor)
    print("Samples from tensor:", samples)
    
    # Computing expectation value
    # Example: Pauli-Z operator on the first qubit
    Z = np.array([[1, 0], [0, -1]])
    Z_full = np.kron(Z, np.eye(2))
    expectation_value = compute_expectation_value(statevector, Z_full)
    print("Expectation value of Z on first qubit:", expectation_value)
