from qiskit import transpile

def circuit_metadata(qaoa, backend):
    qc = qaoa.ansatz
    tqc = transpile(qc, backend, optimization_level=3)

    return {
        "qubits": tqc.num_qubits,
        "depth": tqc.depth(),
        "gate_counts": tqc.count_ops(),
        "layers": qaoa.reps
    }
