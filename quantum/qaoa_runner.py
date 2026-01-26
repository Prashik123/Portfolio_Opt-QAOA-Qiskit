from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import SPSA
from qiskit.primitives import Sampler

def run_qaoa(hamiltonian, p):
    optimizer = SPSA(maxiter=300)

    qaoa = QAOA(
        sampler=Sampler(),
        optimizer=optimizer,
        reps=p
    )

    result = qaoa.compute_minimum_eigenvalue(hamiltonian)
    return result, qaoa
