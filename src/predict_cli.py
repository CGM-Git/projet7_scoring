
import argparse, json
from pathlib import Path
import pandas as pd, numpy as np, joblib

def main():
    parser = argparse.ArgumentParser(description="Prédire avec le modèle RF baseline")
    parser.add_argument("--input", required=True, help="CSV featuré (colonnes = features du modèle)")
    parser.add_argument("--output", required=True, help="CSV de sortie (avec proba et prédiction)")
    args = parser.parse_args()

    ROOT = Path(__file__).resolve().parents[1]
    MODELS = ROOT/"models"
    meta = json.load(open(MODELS/"model_meta.json"))
    feat = meta["features"]; thr = meta["threshold"]

    rf  = joblib.load(MODELS/"rf_model.joblib")
    imp = joblib.load(MODELS/"imputer.joblib")

    df = pd.read_csv(args.input)
    # sécurité: créer colonnes manquantes à NaN, et garder l'ordre
    for c in feat:
        if c not in df.columns:
            df[c] = np.nan
    X = df[feat].astype(float).values
    X = imp.transform(X)
    proba = rf.predict_proba(X)[:,1]
    pred  = (proba >= thr).astype(int)

    out = df.copy()
    out["proba"] = proba
    out["pred"]  = pred
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False)
    print("Écrit:", args.output, "| lignes:", len(out))

if __name__ == "__main__":
    main()
