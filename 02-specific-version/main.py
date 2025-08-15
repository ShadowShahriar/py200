# ===============
# === specific-version.py ===
# === this file shows how to enforce a script's
# === execution to a specific version of Python.
# ===============

import sys
REQUIRED_PYTHON = (3, 11)

if sys.version_info < REQUIRED_PYTHON:
    sys.exit(f"⛔ Python {REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]} or higher is required. You are using Python {sys.version_info.major}.{sys.version_info.minor}")