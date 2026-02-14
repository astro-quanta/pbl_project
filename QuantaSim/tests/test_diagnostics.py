from app.diagnostics import check_simulation_params

def test_diagnostics():
    warns = check_simulation_params({"t_final": -1, "steps": 5})
    assert any("t_final" in w for w in warns)
    assert any("steps is very small" in w for w in warns)
