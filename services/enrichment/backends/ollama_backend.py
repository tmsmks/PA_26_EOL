"""Backend Ollama (serveur local, API compat OpenAI)."""
from __future__ import annotations

import os

import requests

from services.enrichment.backends.base import LLMBackendError


class OllamaBackend:
    name = "ollama"

    def __init__(
        self,
        url: str | None = None,
        model: str | None = None,
        timeout_s: float | None = None,
    ) -> None:
        self._url = url or os.getenv(
            "ENRICH_OLLAMA_URL", "http://localhost:11434/v1/chat/completions"
        )
        self._model = model or os.getenv("ENRICH_OLLAMA_MODEL", "llama3.1:8b")
        try:
            env_timeout = float(os.getenv("ENRICH_OLLAMA_TIMEOUT", "300"))
        except ValueError:
            env_timeout = 300.0
        self._timeout_s = timeout_s if timeout_s is not None else env_timeout

    def complete_json(self, system_msg: str, user_msg: str) -> str:
        payload = {
            "model": self._model,
            "messages": [
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg},
            ],
            "response_format": {"type": "json_object"},
        }
        try:
            resp = requests.post(self._url, json=payload, timeout=self._timeout_s)
        except requests.Timeout as exc:
            raise LLMBackendError(
                f"Ollama a dépassé le timeout de {int(self._timeout_s)}s sur {self._url}. "
                "Le premier appel peut être long (chargement du modèle). "
                "Essayez de précharger le modèle avec `ollama run <modèle> ''` "
                "ou augmentez ENRICH_OLLAMA_TIMEOUT."
            ) from exc
        except requests.RequestException as exc:
            raise LLMBackendError(
                f"Impossible de joindre Ollama sur {self._url}. "
                "Assurez-vous que 'ollama serve' est démarré."
            ) from exc
        if resp.status_code != 200:
            raise LLMBackendError(
                f"Erreur Ollama {resp.status_code}: {resp.text[:400]}"
            )
        data = resp.json()
        return (
            data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "{}")
        )
