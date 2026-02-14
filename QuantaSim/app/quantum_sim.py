from typing import Dict, Any, List

import numpy as np
from qutip import basis, sigmax, mesolve, Qobj


def simulate_two_level_system(
    h_coeff: float = 0.5,
    t_final: float = 10.0,
    steps: int = 100,
) -> Dict[str, Any]:
    """
    Simple two-level system with Hamiltonian H = h_coeff * sigma_x.
    Returns time list and expectation values for sigma_x.
    """
    psi0: Qobj = basis(2, 0)                # |0>
    H: Qobj = h_coeff * sigmax()

    t_list: np.ndarray = np.linspace(0, t_final, steps)
    result = mesolve(H, psi0, t_list, [], [sigmax()])

    return {
        "t": t_list.tolist(),
        "expect_x": result.expect[0].tolist(),
        "h_coeff": h_coeff,
    }
