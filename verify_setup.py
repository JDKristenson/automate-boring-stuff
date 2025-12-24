#!/usr/bin/env python3
"""
Setup Verification Script - Automate the Boring Stuff Companion

Verifies that all automation packages are installed and ready.
"""

import sys

def check_python_version():
    """Check Python version."""
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    if version.major >= 3 and version.minor >= 7:
        print("  ✅ Python version is compatible")
        return True
    else:
        print("  ❌ Python 3.7 or higher required")
        return False

def check_package(package_name, import_name=None):
    """Check if a package is installed."""
    if import_name is None:
        import_name = package_name
    
    try:
        module = __import__(import_name)
        version = getattr(module, '__version__', 'installed')
        print(f"  ✅ {package_name} ({version})")
        return True
    except ImportError:
        print(f"  ❌ {package_name} is not installed")
        return False

def main():
    """Run verification checks."""
    print("=" * 70)
    print("Automate the Boring Stuff - Environment Verification")
    print("=" * 70)
    print()
    
    all_good = True
    
    # Check Python version
    print("1. Checking Python Version...")
    all_good = check_python_version() and all_good
    print()
    
    # Check automation packages
    print("2. Checking Automation Packages...")
    packages = [
        # File and document automation
        ('openpyxl', 'openpyxl'),
        ('python-docx', 'docx'),
        ('PyPDF2', 'PyPDF2'),
        
        # Image processing
        ('Pillow', 'PIL'),
        
        # Web automation
        ('requests', 'requests'),
        ('beautifulsoup4', 'bs4'),
        ('selenium', 'selenium'),
        
        # GUI automation
        ('pyautogui', 'pyautogui'),
        ('pyperclip', 'pyperclip'),
        ('pyinputplus', 'pyinputplus'),
        
        # Text-to-speech and speech recognition
        ('pyttsx3', 'pyttsx3'),
        ('gTTS', 'gtts'),
        ('SpeechRecognition', 'speech_recognition'),
        
        # Scheduling
        ('schedule', 'schedule'),
        
        # Testing
        ('pytest', 'pytest'),
    ]
    
    for package_name, import_name in packages:
        check_package(package_name, import_name)
    
    print()
    
    # Check directory structure
    print("3. Checking Directory Structure...")
    import os
    directories = [
        'my_work',
        'exercises',
        'quick_reference',
        'sample_files',
        'book_resources',
        'venv',
    ]
    
    for directory in directories:
        if os.path.exists(directory):
            print(f"  ✅ {directory}/")
        else:
            print(f"  ❌ {directory}/ not found")
            all_good = False
    
    print()
    print("=" * 70)
    
    if all_good:
        print("✅ ALL CHECKS PASSED - Ready to automate!")
    else:
        print("⚠️  Some issues detected - see above")
    
    print("=" * 70)
    print()
    print("Quick Start:")
    print("  1. Open exercises/CHAPTERS_OVERVIEW.md for chapter guide")
    print("  2. Work in: my_work/chapter_XX/")
    print("  3. Test scripts: python automation_test.py")
    print("  4. Check quick_reference/ for cheat sheets")
    print()

if __name__ == "__main__":
    main()
