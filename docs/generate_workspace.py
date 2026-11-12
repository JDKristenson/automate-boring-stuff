#!/usr/bin/env python3
"""Generate the editable scene and matching previews using only the stdlib.

Run from any directory: python3 docs/generate_workspace.py
No project imports, network, dependency installation, or automation execution.
"""
import html
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHA = "c2e237fa1cb73f8448c2d90fa160d57f083de16f"
# The same geometry and text drives the native scene and SVG preview.
CARDS = [
    (24, 130, 350, 175, "Learning source", [
        "Al Sweigart · 3rd Edition", "Book / course references", "Not proof of course completion", "Preserve edition-specific attribution"]),
    (426, 130, 350, 175, "Tracked companion scaffold", [
        "Chapter overview + 2 cheat sheets", "requirements.txt: macOS-heavy pins", "Verifier: diagnostic, not a CI gate", "Sandbox function: pass placeholder"]),
    (828, 130, 350, 175, "Personal practice · planned", [
        "my_work/ and sample_files/ absent", "Create disposable local practice data", "No completed exercises evidenced", "Label adaptations and assistance"]),
    (24, 355, 350, 190, "Upstream reference · unresolved", [
        "official_code is a Git gitlink", "No tracked .gitmodules URL", "Source / contents / rights unresolved", "Do not guess a source or license"]),
    (426, 355, 350, 190, "Setup boundary · not run", [
        "No app build step defined", "No bundled venv or offline guarantee", "PyObjC pins are not cross-platform", "GUI imports may require a desktop"]),
    (828, 355, 350, 190, "Contribution / rights boundary", [
        "Initial commit: JDKristenson + Warp", "Docs / diagram: Reason-assisted", "No repository license grant found", "No file-level authorship assumption"]),
]
ELEMENTS = []

def base(kind, x, y, w, h):
    n = len(ELEMENTS) + 1
    return dict(id=f"workspace-{n}", type=kind, x=x, y=y, width=w, height=h,
                angle=0, strokeColor="#1e1e1e", backgroundColor="transparent",
                fillStyle="solid", strokeWidth=1, strokeStyle="solid", roughness=0,
                opacity=100, groupIds=[], frameId=None, roundness=None, seed=n,
                version=1, versionNonce=n, isDeleted=False, boundElements=None,
                updated=0, link=None, locked=False)

def text(x, y, value, size, width):
    e = base("text", x, y, width, len(value.splitlines()) * size * 1.25)
    e.update(text=value, originalText=value, fontSize=size, fontFamily=2,
             textAlign="left", verticalAlign="top", containerId=None,
             autoResize=False, lineHeight=1.25)
    ELEMENTS.append(e)

text(24, 20, "Automate the Boring Stuff · provenance & workspace", 28, 1150)
text(24, 65, "Learning/reference scaffold — not completed personal automation", 20, 1150)
for x, y, w, h, title, lines in CARDS:
    e = base("rectangle", x, y, w, h)
    e["backgroundColor"] = "#f5f5f5"
    ELEMENTS.append(e)
    text(x + 16, y + 16, title, 19, w - 32)
    text(x + 16, y + 55, "\n".join(lines), 16, w - 32)
text(24, 585, "Source review: 2026-11-12 · master @ " + SHA, 16, 1150)
text(24, 615, "Map describes the reviewed source, not installation, runtime success, or permission to reuse upstream material.", 16, 1150)
scene = dict(type="excalidraw", version=2, source="https://excalidraw.com",
             elements=ELEMENTS, appState=dict(viewBackgroundColor="#ffffff", gridSize=None), files={})
(HERE / "workspace.excalidraw").write_text(json.dumps(scene, indent=2) + "\n")
parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1202 665" role="img" aria-labelledby="title desc">',
         '<title id="title">Learning companion provenance and workspace</title>',
         '<desc id="desc">Six panels separate book references, tracked scaffolding, planned practice, unresolved upstream, setup limits, and contribution rights.</desc>',
         '<rect width="1202" height="665" fill="white"/>']
for e in ELEMENTS:
    if e["type"] == "rectangle":
        parts.append(f'<rect x="{e["x"]}" y="{e["y"]}" width="{e["width"]}" height="{e["height"]}" fill="#f5f5f5" stroke="#1e1e1e"/>')
    else:
        for i, line in enumerate(e["text"].splitlines()):
            y = e["y"] + e["fontSize"] + i * e["fontSize"] * 1.25
            parts.append(f'<text x="{e["x"]}" y="{y}" font-family="Arial, sans-serif" font-size="{e["fontSize"]}" fill="#1e1e1e">{html.escape(line)}</text>')
parts.append('</svg>')
svg = "\n".join(parts) + "\n"
(HERE / "workspace.svg").write_text(svg)
# Inline SVG follows the host theme; repository SVG remains a portable light preview.
themed = svg.replace('fill="white"', 'fill="var(--background, white)"').replace('fill="#f5f5f5"', 'fill="var(--muted, #f5f5f5)"').replace('#1e1e1e', 'currentColor')
page = '<!doctype html><html lang="en"><meta charset="utf-8"><title>Learning companion map</title><style>body{margin:0;color:var(--foreground);font-family:var(--font-sans,Arial,sans-serif)}svg{display:block;width:100%;height:auto}p{margin:16px 0;color:var(--muted-foreground)}</style><main>' + themed + '<p>Editable source: docs/workspace.excalidraw. Generated from the same scene geometry and text as this preview; native Excalidraw import/round-trip not verified.</p></main></html>\n'
(HERE / "workspace.html").write_text(page)
print("Generated scene, SVG, and theme-aware page from shared geometry/text.")
