
import json, joblib
import pandas as pd
from pathlib import Path

def load_artifact(art_dir: str | Path):
    art_dir = Path(art_dir)
    model = joblib.load(art_dir/"model.pkl")
    meta  = json.loads((art_dir/"model_meta.json").read_text(encoding="utf-8"))
    return model, meta

def _ensure_features(df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
    # garde l'ordre exact, crée les colonnes manquantes à NaN (imputer du pipeline gère)
    X = df.reindex(columns=features)
    return X

def predict_df(df: pd.DataFrame, model, meta, return_proba=True) -> pd.DataFrame:
    cols = meta["features"]
    t = float(meta["threshold"])
    X = _ensure_features(df, cols)
    proba = model.predict_proba(X)[:, 1]
    yhat = (proba >= t).astype(int)
    out = df.copy()
    out["proba"] = proba
    out["risk"]  = yhat
    return out if return_proba else yhat

def predict_records(records: list[dict], model, meta):
    df = pd.DataFrame.from_records(records)
    out = predict_df(df, model, meta)
    return out[["proba","risk"]].to_dict(orient="records")
