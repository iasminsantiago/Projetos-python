# mypackage/utils.py
def to_uppercase(text: str) -> str:
    """Converte uma string para maiúsculas."""
    return text.upper()

def to_lowercase(text: str) -> str:
    """Converte uma string para minúsculas."""
    return text.lower()

# mypackage/__init__.py
from .utils import to_uppercase, to_lowercase

__all__ = ["to_uppercase", "to_lowercase"]
