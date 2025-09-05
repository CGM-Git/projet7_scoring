
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from pathlib import Path

from serve import load_artifact, predict_records

ART_DIR = Path(__file__).resolve().parent
model, meta = load_artifact(ART_DIR)

app = FastAPI(title="Scoring API", version=meta["version"])

class Payload(BaseModel):
    records: List[dict]

@app.get("/health")
def health():
    return {"ok": True, "model": meta["model_tag"], "version": meta["version"]}

@app.get("/meta")
def get_meta():
    m = meta.copy()
    m["n_features"] = len(m["features"])
    return m

@app.post("/predict")
def predict(payload: Payload):
    try:
        out = predict_records(payload.records, model, meta)
        return {"ok": True, "n": len(out), "predictions": out}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
