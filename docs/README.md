# Editable provenance / workspace map

- [Native editable Excalidraw scene](workspace.excalidraw): open/import this JSON file in an Excalidraw-compatible editor. It contains native text and rectangle elements, not a flattened image.
- [SVG preview](workspace.svg): same geometry and text, rendered without requiring Excalidraw.
- [Theme-aware HTML preview](workspace.html): same map for reading in a browser.

The map describes the reviewed `master` source at `c2e237fa1cb73f8448c2d90fa160d57f083de16f` on 2026-11-12. It is a source/provenance boundary diagram, not an application architecture or a claim of working automation. It contains no credentials, private paths, recipients, or sample personal data.

## Maintain and validate

The stdlib-only [generator](generate_workspace.py) owns the shared layout and labels:

```bash
python3 docs/generate_workspace.py
python3 docs/check_workspace.py
python3 -m json.tool docs/workspace.excalidraw > /dev/null
git diff --check
```

Edit the generator and regenerate all three outputs together. Direct native editor changes are possible, but will be overwritten by regeneration; reconcile them into the generator before regenerating. The SVG is a simple matching preview, not the official Excalidraw renderer. JSON/geometry/text consistency and visual preview can be checked without executing the learning project's scripts. Native editor import, font layout, and save/reopen fidelity remain unverified until an actual editor round trip is performed.

## Attribution and limits

Preserve **Al Sweigart / Automate the Boring Stuff with Python (3rd Edition)** as the learning source, **JDKristenson** as recorded initial author/committer, and **Warp** as the initial commit's explicit AI co-author. This documentation and map were created with **Reason** assistance. These credits do not assign original authorship to every file or establish a license grant.

The `book_resources/official_code` gitlink has no tracked upstream URL. Its contents and rights remain unresolved and it has not been changed. See the root README for setup and licensing boundaries. No runtime fixes, dependency installation, GUI automation, network service calls, sends, or application testing are part of this documentation cleanup.
