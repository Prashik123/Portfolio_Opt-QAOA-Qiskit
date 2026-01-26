from qiskit.quantum_info import SparsePauliOp

def build_cvar_markowitz_hamiltonian(mu, sigma, cvar, lam, eta):
    n = len(mu)
    paulis = []
    coeffs = []

    # Expected return term
    for i in range(n):
        paulis.append("I"*i + "Z" + "I"*(n-i-1))
        coeffs.append(-mu[i])

    # Risk (covariance) term
    for i in range(n):
        for j in range(i+1, n):
            paulis.append(
                "I"*i + "Z" + "I"*(j-i-1) + "Z" + "I"*(n-j-1)
            )
            coeffs.append(lam * sigma[i, j])

    # CVaR tail-risk penalty
    paulis.append("I"*n)
    coeffs.append(eta * cvar)

    return SparsePauliOp(paulis, coeffs)
