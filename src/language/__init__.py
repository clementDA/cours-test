# src/lang/__init__.py


from .lang_es import MESSAGES as ES
from .lang_en import MESSAGES as EN
from .lang_fr import MESSAGES as FR
from .lang_default import MESSAGES as DEFAUT

LANGUAGES = {
    "es": ES,
    "en": EN,
    "fr": FR,
    "": DEFAUT
    
}
