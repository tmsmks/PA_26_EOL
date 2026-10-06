"""Configuration pytest : ajoute la racine au sys.path.

`import app` crée l'application par défaut : on la fait pointer vers une base
jetable, pour que les tests ne touchent jamais `instance/eol.db`.
"""
import os
import sys
import tempfile

os.environ["DATABASE_URL"] = "sqlite:///" + os.path.join(tempfile.mkdtemp(prefix="eol-tests-"), "app.db")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
