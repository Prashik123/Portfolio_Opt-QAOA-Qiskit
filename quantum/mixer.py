from qiskit.circuit import QuantumCircuit

def constraint_preserving_mixer(n, beta):
    
   # Number-conserving XY mixer
    
    qc = QuantumCircuit(n)
    for i in range(n-1):
        qc.rxx(2 * beta, i, i+1)
        qc.ryy(2 * beta, i, i+1)
    return qc
