# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a learning environment for "Automate the Boring Stuff with Python" (3rd Edition). It's designed as a self-contained workspace where learners practice Python automation through 24 chapters, progressing from basics to advanced automation tasks.

**Core Purpose:** Educational companion for mastering Python automation - from file operations and web scraping to GUI automation and document processing.

## Environment Setup

### Virtual Environment
Always activate the virtual environment before running any Python scripts:

```bash
source venv/bin/activate
```

### Verification
To verify the environment is correctly set up:

```bash
python verify_setup.py
```

This checks Python version, installed packages, and directory structure.

### Package Management
All required packages are in `requirements.txt`. If packages need reinstalling:

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

# Run tests (pytest is installed)
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

### Directory Structure

```
automate-boring-stuff-companion/
├── venv/                      # Python virtual environment (MUST activate)
├── my_work/                   # User workspace (24 chapter folders + automation_projects/)
├── exercises/                 # Chapter guides (CHAPTERS_OVERVIEW.md)
├── quick_reference/           # Cheat sheets (regex, file automation)
├── sample_files/              # Practice data (pdfs/, excel_files/, images/, etc.)
├── book_resources/            # Official Al Sweigart code examples
├── verify_setup.py            # Environment verification script
└── automation_test.py         # Sandbox for testing automation code
```

### Key Architectural Concepts

#### 1. Workspace Organization
- **my_work/** is the primary development area with 24 chapter-specific folders (chapter_01 through chapter_24) plus an automation_projects/ folder
- Each chapter folder is initially empty, intended for learner's practice scripts
- The automation_projects/ folder is for custom automation projects beyond the book

#### 2. Learning Progression
The project follows a clear two-part structure:
- **Part I (Chapters 1-8):** Python fundamentals - language basics, control flow, data structures
- **Part II (Chapters 9-24):** Automation skills - practical tools and libraries for automating real tasks

Key inflection point: Chapter 9 (Regular Expressions) marks the transition from learning Python to applying it for automation.

#### 3. Safety-First Design
- **sample_files/** directory provides safe practice data organized by type (pdfs/, excel_files/, images/, text_files/, word_docs/)
- **automation_test.py** serves as an isolated sandbox with error handling
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

### macOS (Current Platform)
- PyAutoGUI requires Accessibility permissions: System Preferences → Security & Privacy → Accessibility → Add Terminal/Editor
- pyobjc frameworks are installed for macOS-specific automation features
- Use `open` command to view files from terminal: `open file.txt`

### Browser Automation (Selenium)
If working with Selenium (Chapter 13):
```bash
# Install ChromeDriver
brew install chromedriver
```

## Important Conventions

### When Modifying Files
- Never modify files in book_resources/official_code/ - these are reference materials
- All development work belongs in my_work/
- Use sample_files/ for testing file automation scripts

### When Helping with Code
- Assume the virtual environment is active (or remind to activate it)
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
