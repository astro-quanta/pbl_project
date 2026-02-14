from app.quantum_sim import simulate_two_level_system

def test_two_level_sim_runs():
    out = simulate_two_level_system()
    assert "t" in out and "expect_x" in out
    assert len(out["t"]) == len(out["expect_x"])
