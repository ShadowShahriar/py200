import os

# === hide pygame support prompt ===
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import os.path as path
import sys

script_path = path.abspath(__file__)
__script_dir = path.dirname(script_path)
__script_dir_alt = sys.path[0]
