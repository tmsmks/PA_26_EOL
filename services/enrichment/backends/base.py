"""Interface commune des backends LLM."""
from __future__ import annotations

from typing import Protocol, runtime_checkable


class LLMBackendError(RuntimeError):
    """Erreur générique d'un backend LLM (réseau, quota, format invalide)."""


@runtime_checkable
class LLMBackend(Protocol):
    """Stratégie d'appel à un LLM pour l'enrichissement.

    Une implémentation reçoit le system message et le user message, retourne
    le contenu textuel du choix principal (souvent un JSON). Les erreurs
    réseau / quota / format DOIVENT lever LLMBackendError.
    """

    name: str

    def complete_json(self, system_msg: str, user_msg: str) -> str:
        """Demande une complétion JSON au LLM. Retourne le contenu brut."""
        ...
