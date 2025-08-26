
from pathlib import Path
import pandas as pd
import sys

# --- Chemins relatifs (aucun chemin absolu) ---
# Ce fichier doit être placé dans:  projet7_starter/data/
# Les CSV doivent être dans:       projet7_starter/data/raw/
HERE = Path(__file__).resolve().parent
RAW = HERE / "raw"
OUTPUT = HERE / "all_data_FULL.csv"

# --- Sécurité: repartir de zéro ---
if OUTPUT.exists():
    print(f"[i] Suppression de l'ancien fichier: {OUTPUT}")
    OUTPUT.unlink()

# --- 1) Lister les CSV ---
csv_files = sorted(RAW.rglob("*.csv"))
if not csv_files:
    print(f"[!] Aucun CSV trouvé dans: {RAW}")
    sys.exit(1)

print(f"[i] CSV détectés: {len(csv_files)}")
for p in csv_files:
    print("   -", p.name)

# --- 2) Déterminer l'union des colonnes via un échantillon ---
ENCODINGS = ("utf-8", "latin-1")
union_cols = set()
for path in csv_files:
    ok = False
    for enc in ENCODINGS:
        try:
            tmp = pd.read_csv(path, nrows=1000, encoding=enc)
            union_cols |= set(tmp.columns)
            ok = True
            break
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"[!] Échec lecture échantillon {path.name}: {e}")
            break
    if not ok:
        print(f"[!] Impossible de lire un échantillon pour {path.name} (encodage non géré).")
union_cols = sorted(union_cols)
if not union_cols:
    print("[!] Impossible de déterminer les colonnes (échantillons illisibles).")
    sys.exit(2)

print(f"[i] Colonnes totales (union): {len(union_cols)}")

# --- 3) Concaténation en flux ---
CHUNKSIZE = 200_000
header_written = False
rows_total = 0

for path in csv_files:
    used_enc = None
    for enc in ENCODINGS:
        try:
            for chunk in pd.read_csv(path, chunksize=CHUNKSIZE, encoding=enc):
                # Réindexer chaque chunk pour aligner les colonnes
                chunk = chunk.reindex(columns=union_cols)
                chunk.to_csv(OUTPUT, index=False, mode="a", header=not header_written)
                header_written = True
                rows_total += len(chunk)
            used_enc = enc
            print(f"[OK] {path.name} ✓  (encodage: {enc})")
            break
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"[!] Erreur lecture {path.name}: {e}")
            break
    if used_enc is None:
        print(f"[!] Encodage non géré: {path.name}")

print(f"[✓] Fusion terminée. Lignes écrites: {rows_total}")
print(f"[→] Fichier généré: {OUTPUT}")
