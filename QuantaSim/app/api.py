from flask import Flask, request, jsonify
from flask_cors import CORS

from app.quantum_sim import simulate_two_level_system
from app.surrogate_model import predict_property
from app.diagnostics import check_simulation_params

app = Flask(__name__)
CORS(app)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/simulate", methods=["POST"])
def simulate():
    data = request.get_json(force=True) or {}
    h_coeff = float(data.get("h_coeff", 0.5))
    t_final = float(data.get("t_final", 10.0))
    steps = int(data.get("steps", 100))

    params = {"h_coeff": h_coeff, "t_final": t_final, "steps": steps}
    warnings = check_simulation_params(params)

    sim_result = simulate_two_level_system(
        h_coeff=h_coeff, t_final=t_final, steps=steps
    )
    sim_result["warnings"] = warnings
    return jsonify(sim_result)


@app.route("/surrogate_predict", methods=["POST"])
def surrogate_predict():
    data = request.get_json(force=True) or {}
    # You can parse real features from frontend later
    features = data.get("features", {"atomic_number_sum": 2.0, "bond_count": 1.0})

    result = predict_property(features)
    return jsonify(result)
