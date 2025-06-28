# src/lang/__init__.py

from .lang_fr import MESSAGES as FR
from .lang_default import MESSAGES as DEFAUT

LANGUAGES = {
    "fr": FR,
    "": DEFAUT
    
}
