"""Moteur du parcours joueur : tests JavaScript lancés avec Node."""
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


@pytest.mark.skipif(shutil.which("node") is None, reason="Node.js n'est pas installé")
def test_engine_js():
    run = subprocess.run(
        ["node", "--test", str(ROOT / "tests" / "js" / "engine.test.mjs")],
        capture_output=True, text=True, cwd=ROOT, timeout=60,
    )
    assert run.returncode == 0, run.stdout + run.stderr
