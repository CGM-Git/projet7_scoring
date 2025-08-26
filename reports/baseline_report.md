# Rapport Baseline — Projet 7
Date: 2025-08-26 21:52

## Données
- Lignes (train): 307,511
- Cible (classe 1) : 8.07%

## Modèle
- RandomForest (n_estimators=400, max_depth=12, class_weight=balanced)
- Features utilisées (15): n_bureau, n_bureau_months, n_prev, n_inst_pay, n_pos_cash, n_ccb, credit_income_perc, annuity_income_perc, credit_term, goods_credit_ratio, age_years, employed_years, EXT_SOURCE_1, EXT_SOURCE_2, EXT_SOURCE_3

## Validation (5-plis)
- ROC-AUC: **0.741**
- PR-AUC : **0.220**
- F1 (OOF, seuil 0.593): **0.286**

## Seuil retenu pour la décision
- Seuil coût (FP=1, FN=5): **0.600**

## Artefacts
- Modèle   : `models/rf_model.joblib`
- Imputer  : `models/imputer.joblib`
- Métadonnées : `models/model_meta.json`
- Figure importance : `reports/figures/feature_importance_rf.png`
- Prédictions test : `data/processed/predictions_test_rf.csv`


## Lock test 10%
```
seed=2025
seuil=0.600
F1=0.281
PR_AUC=0.233
ROC_AUC=0.745
TP=895 FP=2983 FN=1588 TN=25286
```
