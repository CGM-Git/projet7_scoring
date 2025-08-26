# One-Pager — Modèle baseline (Projet 7)
Date : 2025-08-26 22:30

## Objectif
Prédire la probabilité qu'un client soit en défaut (**TARGET=1**) à partir de plusieurs tables.

## Données (train)
- Lignes : **307 511**
- Classe positive : **~8%**

## Features (15)
- **Comptages** : n_bureau, n_bureau_months, n_prev, n_inst_pay, n_pos_cash, n_ccb
- **Ratios/Âges** : credit_income_perc, annuity_income_perc, credit_term, goods_credit_ratio, age_years, employed_years
- **Scores externes** : EXT_SOURCE_1/2/3
Top variables (RF) : EXT_SOURCE_2, EXT_SOURCE_3, EXT_SOURCE_1, credit_term, employed_years.

## Modèle retenu
RandomForest (n_estimators=400, max_depth=12, class_weight=balanced, seed=42)

## Validation croisée (5 plis)
- **ROC-AUC** : 0.741
- **PR-AUC**  : 0.220
- **F1** (OOF, seuil 0.593) : 0.286

## Seuil de décision
- Choix “métier” (FN = 5x FP) → **seuil 0.600**
- Variante “F1 max” ≈ 0.593 (très proche)

## Livrables
- Modèle : `models/rf_model.joblib`
- Imputer : `models/imputer.joblib`
- Meta : `models/model_meta.json`
- Figure importance : `reports/figures/feature_importance_rf.png`
- Prédictions test : `data/processed/predictions_test_rf.csv`

## Notes
- Calibration testée → pas de gain → on garde **baseline v1**.
- Pistes d'amélioration : nouvelles features (interactions), gradient boosting, ajuster coûts FP/FN réels.
