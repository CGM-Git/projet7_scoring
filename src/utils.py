"""
Fonctions utilitaires générales.
Commentaires neutres et professionnels.
"""
import os
import random
import numpy as np

def set_seed(seed: int = 42) -> None:
    """Fixe l'aléatoire pour rendre les expériences reproductibles."""
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
