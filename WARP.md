# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a learning environment for "Automate the Boring Stuff with Python" (3rd Edition). It is a learning/reference scaffold organized around 24 chapters, not a complete self-contained or offline environment. See README.md for the dated source review, attribution, licensing uncertainty, and setup limitations. Do not assume local dependencies or practice directories exist.

**Core Purpose:** Educational companion for mastering Python automation - from file operations and web scraping to GUI automation and document processing.

## Environment Setup

### Virtual Environment
Create a local environment with `python3 -m venv venv` if needed, then activate it before running project scripts. No environment is tracked or verified:

```bash
source venv/bin/activate
```

### Verification
Optional diagnostic command after reviewing the README limitations (not proof of correct setup):

```bash
python verify_setup.py
```

This attempts Python/package/directory diagnostics, but package return values are discarded, failure is not reflected in process exit status, and existence checks do not validate contents. Imports may require a GUI session. It is not a reliable CI gate or proof of a working environment.

### Package Management
`requirements.txt` is a pinned list with unmarked macOS-only PyObjC packages, not a verified cross-platform lockfile. Review platform/Python compatibility before optionally installing; the verifier's Python 3.7 claim does not validate these pins:

```bash
pip install -r requirements.txt
```

## Common Commands

### Testing & Development

```bash
# Activate environment (REQUIRED before any Python work)
source venv/bin/activate

# Verify environment setup
python verify_setup.py

# Run automation test sandbox
python automation_test.py

# Optional pytest invocation after installation (not verified installed;
# the tracked sandbox test is empty, not a substantive test suite)
pytest

# Run a single test file
pytest path/to/test_file.py

# Run a specific test function
pytest path/to/test_file.py::test_function_name
```

### Working with Chapter Code

```bash
# Navigate to chapter workspace
cd my_work/chapter_XX

# Run Python interactively
python

# Execute a specific script
python script_name.py
```

## Repository Architecture

### Suggested Local Directory Structure (not a tracked inventory)

At reviewed head `c2e237fa1cb73f8448c2d90fa160d57f083de16f`, `venv/`, `my_work/`, and `sample_files/` were absent from Git. Individual chapter exercise files and templates were not supplied. `book_resources/official_code` is an unresolved gitlink without a tracked `.gitmodules` URL; do not guess its source or license.

```
automate-boring-stuff-companion/
├── venv/                      # Python virtual environment (MUST activate)
├── my_work/                   # User workspace (24 chapter folders + automation_projects/)
├── exercises/                 # Chapter guides (CHAPTERS_OVERVIEW.md)
├── quick_reference/           # Cheat sheets (regex, file automation)
├── sample_files/              # Practice data (pdfs/, excel_files/, images/, etc.)
├── book_resources/            # Unresolved reference gitlink; not bundled examples
├── verify_setup.py            # Environment verification script
└── automation_test.py         # Sandbox for testing automation code
```

### Key Architectural Concepts

#### 1. Workspace Organization
- **my_work/** is the proposed development area for chapter-specific folders (chapter_01 through chapter_24) plus automation_projects/
- Create only the folders needed for personal practice; they are not supplied
- The automation_projects/ folder is for custom automation projects beyond the book

#### 2. Learning Progression
The project follows a clear two-part structure:
- **Part I (Chapters 1-8):** Python fundamentals - language basics, control flow, data structures
- **Part II (Chapters 9-24):** Automation skills - practical tools and libraries for automating real tasks

Key inflection point: Chapter 9 (Regular Expressions) marks the transition from learning Python to applying it for automation.

#### 3. Safety-First Design
- **sample_files/** is a proposed practice-data directory; create disposable synthetic files yourself
- **automation_test.py** is a placeholder with error handling, not an isolation boundary. Review any added code before execution
- Scripts should be tested on sample files before running on real data

#### 4. Reference Materials
- **quick_reference/** contains domain-specific cheat sheets (regex_cheatsheet.md, file_automation_cheatsheet.md)
- **exercises/CHAPTERS_OVERVIEW.md** maps all 24 chapters with focus areas, key skills, and practice guidance
- These are curated references specific to automation tasks, not general Python docs

## Development Patterns

### Testing Automation Scripts

When creating or testing automation code:

1. **Use the sandbox first:**
   ```python
   # Edit automation_test.py
   python automation_test.py
   ```

2. **Test on sample files:**
   ```python
   from pathlib import Path
   test_dir = Path('sample_files/text_files')
   ```

3. **Always verify in appropriate chapter workspace:**
   ```bash
   cd my_work/chapter_XX
   ```

### File Automation Best Practices

The codebase emphasizes safe file operations:

```python
# Always use pathlib.Path for cross-platform compatibility
from pathlib import Path

# Always test on copies first
import shutil
shutil.copy('original.txt', 'test_copy.txt')

# Add error handling for file operations
try:
    file.unlink()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
```

### Common Automation Patterns

**File Organization:**
- Use `Path.iterdir()` for directory contents
- Use `Path.glob('*.ext')` for pattern matching
- Use `Path.rglob('*.ext')` for recursive searches

**Document Processing:**
- openpyxl for Excel (.xlsx)
- python-docx for Word (.docx)
- PyPDF2 for PDFs
- Always use context managers (`with` statements)

**Web Automation:**
- requests for HTTP requests
- beautifulsoup4 for HTML parsing
- selenium for browser automation

**GUI Automation:**
- pyautogui for mouse/keyboard control
- pyperclip for clipboard operations
- Requires macOS accessibility permissions (System Preferences → Security & Privacy → Accessibility)

## Chapter-Specific Guidance

### Chapters 1-8: Fundamentals
Focus on basic Python - no external libraries needed. Work directly in Python REPL or simple scripts.

### Chapter 9: Regular Expressions
Heavy regex usage begins here. Reference `quick_reference/regex_cheatsheet.md` for patterns.

### Chapters 10-12: File Automation
Core file operations. Reference `quick_reference/file_automation_cheatsheet.md`. Always test in sample_files/ first.

### Chapters 13-18: Data & Documents
External data sources (web, Excel, PDFs, databases). Network operations and file I/O with proper error handling.

### Chapters 19-24: Advanced Automation
Scheduling (schedule module), communications (smtplib), image processing (Pillow), OCR, GUI automation (pyautogui), and speech (pyttsx3, gTTS).

## Platform-Specific Notes

### macOS (original dependency-list target; current host not assumed)
- PyAutoGUI requires Accessibility permissions: System Preferences → Security & Privacy → Accessibility → Add Terminal/Editor
- PyObjC frameworks are listed, not verified installed; supported Python/macOS versions remain unvalidated
- Use `open` command to view files from terminal: `open file.txt`

### Browser Automation (Selenium)
If working with Selenium (Chapter 13):
```bash
# Install ChromeDriver
brew install chromedriver
```

## Important Conventions

### When Modifying Files
- Never modify book_resources/official_code - preserve the reference gitlink and any separately resolved upstream material
- All development work belongs in my_work/
- Use sample_files/ for testing file automation scripts

### When Helping with Code
- Check setup rather than assuming a virtual environment, installed packages, or practice directories
- Preserve Al Sweigart/third-edition book attribution, JDKristenson's recorded human credit, and Warp's initial-commit AI co-author credit. This documentation/diagram cleanup was assisted by Reason; no file-level original-authorship claim or new license grant is implied
- Keep the unresolved gitlink unchanged until its actual upstream and rights are established; do not import or redistribute guessed upstream material
- Suggest testing in automation_test.py for quick experiments
- Reference appropriate quick_reference/ cheatsheet when relevant
- Point to specific chapter folder in my_work/ for chapter-specific work

### When Creating New Scripts
- Place chapter-specific practice in my_work/chapter_XX/
- Place general automation projects in my_work/automation_projects/
- Include error handling and user confirmation for destructive operations

## Troubleshooting

### Package Import Errors
```bash
source venv/bin/activate
python verify_setup.py
pip install -r requirements.txt  # If needed
```

### PyAutoGUI Issues
Grant accessibility permissions in System Preferences → Security & Privacy → Accessibility

### File Permission Errors
```python
from pathlib import Path
file = Path('myfile.txt')
print(oct(file.stat().st_mode))
```

### Selenium Browser Issues
```bash
brew install chromedriver  # macOS
```

## Key Learning Resources

- **exercises/CHAPTERS_OVERVIEW.md** - Complete chapter roadmap with skills and project ideas
- **quick_reference/regex_cheatsheet.md** - Comprehensive regex patterns and examples
- **quick_reference/file_automation_cheatsheet.md** - File operations and automation tasks
- **README.md** - Detailed project guide with examples and learning path
