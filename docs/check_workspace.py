#!/usr/bin/env python3
"""Static documentation checks; does not import or run learning-project code."""
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
outputs = [HERE / name for name in ("workspace.excalidraw", "workspace.svg", "workspace.html")]
before = [p.read_bytes() for p in outputs]
subprocess.run([sys.executable, str(HERE / "generate_workspace.py")], check=True)
assert before == [p.read_bytes() for p in outputs], "Generated outputs were stale; review regenerated files"
scene = json.loads(outputs[0].read_text())
assert scene["type"] == "excalidraw" and scene["version"] == 2
assert not scene["files"], "No embedded assets expected"
elements = scene["elements"]
assert len(elements) == len({e["id"] for e in elements})
assert all(e["type"] in ("text", "rectangle") for e in elements)
assert all(0 <= e["x"] and e["x"] + e["width"] <= 1202 and
           0 <= e["y"] and e["y"] + e["height"] <= 665 for e in elements)
xml = ET.parse(outputs[1]).getroot()
assert [line for e in elements if e["type"] == "text" for line in e["text"].splitlines()] == [
    e.text for e in xml.findall("{http://www.w3.org/2000/svg}text")]
for path in (ROOT / "README.md", ROOT / "exercises/CHAPTERS_OVERVIEW.md", HERE / "README.md"):
    for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
        if not link.startswith(("https://", "http://", "#")):
            assert (path.parent / link.split("#")[0]).exists(), (path, link)
readme = (ROOT / "README.md").read_text()
assert all(credit in readme for credit in ("Al Sweigart", "3rd Edition", "JDKristenson", "Warp", "Reason"))
print("PASS: deterministic generation; native scene shape/IDs/bounds; SVG XML/text parity; local links; attribution labels.")
print("Not checked: native editor round trip, dependency install, learning-project runtime or automation behavior.")
