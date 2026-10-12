#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Processus de synthèse vocale Piper, pour la lecture audio du parcours joueur.

Piper (https://github.com/OHF-voice/piper1-gpl) est sous licence GPL-3.0 : ce
fichier l'utilise, il est donc lui aussi sous GPL-3.0 ou ultérieure. Il tourne
dans un processus séparé de l'application (services/tts_service.py), qui lui
parle par des lignes JSON sur l'entrée et la sortie standard. Les modèles
restent chargés en mémoire d'une phrase à l'autre.

Requête : {"model": "<chemin .onnx>", "speaker": 1, "text": "…", "out": "<chemin .mp3>",
           "length_scale": 1.05, "sentence_silence": 0.32}
Réponse : {"ok": true, "seconds": 12.3} ou {"ok": false, "error": "…"}
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np
import soundfile as sf
from piper import PiperVoice, SynthesisConfig

_voices: dict[str, PiperVoice] = {}


def _voice(model: str) -> PiperVoice:
    if model not in _voices:
        _voices[model] = PiperVoice.load(model)
    return _voices[model]


def synthesize(req: dict) -> float:
    voice = _voice(req["model"])
    config = SynthesisConfig(
        speaker_id=req.get("speaker"),
        length_scale=req.get("length_scale"),
        noise_scale=req.get("noise_scale"),
        noise_w_scale=req.get("noise_w_scale"),
    )
    rate = voice.config.sample_rate
    # Un court silence entre deux phrases : la lecture respire.
    silence = np.zeros(int(rate * float(req.get("sentence_silence", 0.3))), dtype=np.float32)
    parts: list[np.ndarray] = []
    for chunk in voice.synthesize(req["text"], syn_config=config):
        if parts:
            parts.append(silence)
        parts.append(chunk.audio_float_array.astype(np.float32))
    audio = np.concatenate(parts) if parts else np.zeros(rate // 10, dtype=np.float32)
    tmp = req["out"] + ".part"
    sf.write(tmp, audio, rate, format="MP3")
    os.replace(tmp, req["out"])  # jamais de fichier à moitié écrit dans le cache
    return len(audio) / rate


def main() -> int:
    # La sortie standard ne sert qu'aux réponses : tout autre message va sur
    # la sortie d'erreur.
    out = sys.stdout
    sys.stdout = sys.stderr
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            seconds = synthesize(json.loads(line))
            reply = {"ok": True, "seconds": round(seconds, 2)}
        except Exception as e:  # noqa: BLE001 — l'application décide quoi faire
            reply = {"ok": False, "error": f"{type(e).__name__}: {e}"[:300]}
        out.write(json.dumps(reply) + "\n")
        out.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
