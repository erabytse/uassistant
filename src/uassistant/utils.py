# src/uassistant/utils.py
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    # Ajustement pour la structure src/ en dev
    if not hasattr(sys, '_MEIPASS'):
        # En dev, on est dans src/uassistant, donc on remonte de 2 niveaux pour atteindre la racine projet
        # Ou on utilise un chemin relatif depuis le fichier utils
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", relative_path)
    
    return os.path.join(base_path, relative_path)