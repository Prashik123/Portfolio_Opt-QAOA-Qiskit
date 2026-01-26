import time
import numpy as np
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

from data.fetch_data import fetch_returns
from classical.cvar import compute_cvar
from quantum.hamiltonian import build_cvar_markowitz_hamiltonian
from quantum.qaoa_runner import run_qaoa
from utils.complexity import circuit_metadata

#  USER INPUT 
N = int(input("Enter number of stocks (<=10): "))
p = int(input("Enter QAOA layers p: "))

NIFTY_50_TOP = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "SBIN.NS",
    "LT.NS",
    "ITC.NS",
    "HINDUNILVR.NS",
    "BHARTIARTL.NS"
]

assets = NIFTY_50_TOP[:N]

#  DATA 
returns = fetch_returns(assets)
mu = returns.mean(axis=0)
sigma = np.cov(returns.T)

# CVaR 
cvar = compute_cvar(returns)

#  HAMILTONIAN
H = build_cvar_markowitz_hamiltonian(
    mu, sigma, cvar,
    lam=0.5,
    eta=0.8
)

#  QAOA 
start = time.time()
result, qaoa = run_qaoa(H, p)
end = time.time()

counts = result.eigenstate.binary_probabilities()

#  METADATA 
backend = AerSimulator()
meta = circuit_metadata(qaoa, backend)

print("\nOptimal Portfolio Distribution:")
print(counts)

print("\nQuantum Metadata: ")
print("QAOA layers (p):", meta["layers"])
print("Qubits:", meta["qubits"])
print("Circuit depth:", meta["depth"])
print("Gate counts:", meta["gate_counts"])
print("Runtime (s):", end - start)

# VISUALS 
plot_histogram(counts)
qaoa.ansatz.draw("mpl")
