"""Backends LLM — Strategy pattern pour l'enrichissement."""
from services.enrichment.backends.base import LLMBackend, LLMBackendError
from services.enrichment.backends.ollama_backend import OllamaBackend
from services.enrichment.backends.openai_backend import OpenAIBackend


def resolve_backend(name: str) -> LLMBackend:
    """Factory : retourne l'instance LLMBackend selon le nom."""
    name = (name or "openai").lower()
    if name == "openai":
        return OpenAIBackend()
    if name == "ollama":
        return OllamaBackend()
    raise LLMBackendError(
        f"ENRICH_BACKEND='{name}' inconnu. Utilisez 'openai' ou 'ollama'."
    )


__all__ = [
    "LLMBackend",
    "LLMBackendError",
    "OllamaBackend",
    "OpenAIBackend",
    "resolve_backend",
]
