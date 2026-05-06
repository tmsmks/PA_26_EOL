"""Backend OpenAI (officiel)."""
from __future__ import annotations

import os

import openai

from services.enrichment.backends.base import LLMBackendError


class OpenAIBackend:
    name = "openai"

    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
    ) -> None:
        self._api_key = api_key or os.getenv("OPENAI_API_KEY")
        self._model = model or os.getenv("ENRICH_OPENAI_MODEL", "gpt-4.1-mini")

    def complete_json(self, system_msg: str, user_msg: str) -> str:
        if not self._api_key:
            raise LLMBackendError(
                "ENRICH_BACKEND=openai mais OPENAI_API_KEY est manquant. "
                "Définissez la variable d'environnement avec votre clé OpenAI."
            )
        client = openai.OpenAI(api_key=self._api_key)
        try:
            completion = client.chat.completions.create(
                model=self._model,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_msg},
                ],
            )
        except openai.RateLimitError as exc:
            raise LLMBackendError(
                "Erreur de quota OpenAI (RateLimitError). "
                "Vérifiez votre plan / crédits ou utilisez ENRICH_BACKEND=ollama."
            ) from exc
        return completion.choices[0].message.content or "{}"
