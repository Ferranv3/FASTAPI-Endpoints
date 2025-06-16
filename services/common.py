"""Shared utilities for service layer."""

def validate_language(language: str) -> None:
    """Ensure that the language value is either 'es' or 'en'.

    Raises:
        ValueError: If the language is not supported.
    """
    if language not in {"es", "en"}:
        raise ValueError("Idioma no válido")
