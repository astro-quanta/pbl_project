from app.surrogate_model import predict_property

def test_surrogate_prediction():
    features = {"atomic_number_sum": 3.0, "bond_count": 2.0}
    out = predict_property(features)
    assert "predicted_energy" in out
    assert isinstance(out["predicted_energy"], float)
