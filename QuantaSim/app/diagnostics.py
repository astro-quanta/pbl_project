from typing import Dict, Any, List

def check_simulation_params(params: Dict[str, Any]) -> List[str]:
    warnings: List[str] = []

    t_final = params.get("t_final", 10.0)
    steps = params.get("steps", 100)

    if t_final <= 0:
        warnings.append("t_final must be positive.")

    if steps < 10:
        warnings.append("steps is very small; results may be low resolution.")

    if steps > 5000:
        warnings.append("steps is very large; simulation may be slow.")

    return warnings
