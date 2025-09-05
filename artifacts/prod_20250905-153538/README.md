# Artefact modèle (figé)
- modèle : ? (20250905-153538)
- seuil (t*) : 0.091
- coûts : FP=1.0×  |  FN=10.0×
- features (19) : SK_ID_CURR, n_bureau, n_bureau_months, n_prev, n_inst_pay, n_pos_cash, n_ccb, credit_income_perc, annuity_income_perc, goods_price_income_perc, age_years, employed_years, ext1, ext2, ext3, cnt_children, cnt_family_members, n_prev_apps, is_new_to_credit

## Lancer l'API
pip install -r requirements.txt
uvicorn api:app --host 0.0.0.0 --port 8000
