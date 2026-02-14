from typing import Dict, Any

import torch
from torch import nn

# For a full GNN: from torch_geometric.nn import GCNConv, global_mean_pool

class SimpleSurrogateNet(nn.Module):
    """
    Placeholder surrogate model: takes a feature vector and returns
    a single scalar (e.g. predicted energy). You can extend to a real GNN.
    """
    def __init__(self, in_dim: int = 8, hidden_dim: int = 32):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


_model: SimpleSurrogateNet | None = None


def load_surrogate_model() -> SimpleSurrogateNet:
    global _model
    if _model is None:
        _model = SimpleSurrogateNet()
        # TODO: load real weights from config.SURROGATE_MODEL_PATH if available
        _model.eval()
    return _model


def predict_property(features: Dict[str, float]) -> Dict[str, Any]:
    """
    Takes a dict of numeric features -> returns a scalar prediction.
    For now, we just map to an 8-dim vector with defaults.
    """
    keys = sorted(features.keys())
    vec = [features[k] for k in keys]
    # pad or trim to 8
    vec = (vec + [0.0] * 8)[:8]
    x = torch.tensor(vec, dtype=torch.float32).unsqueeze(0)

    model = load_surrogate_model()
    with torch.no_grad():
        y = model(x).item()

    return {
        "input_features": {k: features[k] for k in keys},
        "predicted_energy": y,
    }
