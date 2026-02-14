import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Where models and logs live
MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

# Example: path to saved surrogate model
SURROGATE_MODEL_PATH = os.path.join(MODEL_DIR, "gnn_surrogate.pt")
