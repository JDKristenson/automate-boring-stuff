# Automate the Boring Stuff with Python - Offline Companion

Your complete, self-contained environment for learning Python automation from "Automate the Boring Stuff with Python" by Al Sweigart (3rd Edition).

## 🎯 What This Is

This companion provides everything you need to master Python automation:
- ✅ Complete Python environment with all automation packages
- ✅ Official book resources and code examples
- ✅ Detailed chapter guides and exercises
- ✅ Automation-focused quick reference cheat sheets
- ✅ Test scripts and sandboxes for experimentation
- ✅ Sample files for practicing automation tasks
- ✅ Project templates and examples

## 🚀 Quick Start

### 1. Verify Setup
```bash
source venv/bin/activate
python verify_setup.py
```

### 2. Start Learning
Open `exercises/CHAPTERS_OVERVIEW.md` to see all 24 chapters.

### 3. Your First Automation
```bash
cd my_work/chapter_01
python
>>> print("Hello, automation!")
```

## 📁 Project Structure

```
automate-boring-stuff-companion/
├── README.md                    # You are here!
├── verify_setup.py              # Verify environment
├── automation_test.py           # Test sandbox
├── requirements.txt             # All packages
│
├── book_resources/              # Official book code
│   └── official_code/          # From Al Sweigart's GitHub
│
├── my_work/                     # YOUR workspace
│   ├── chapter_01/             # Python basics
│   ├── chapter_09/             # Regex
│   ├── chapter_11/             # File organization
│   ├── chapter_14/             # Excel automation
│   ├── chapter_23/             # GUI automation
│   └── automation_projects/    # Your automation scripts
│
├── exercises/                   # Chapter guides
│   └── CHAPTERS_OVERVIEW.md    # Complete chapter index
│
├── quick_reference/             # Cheat sheets
│   ├── regex_cheatsheet.md     # Regular expressions
│   └── file_automation_cheatsheet.md  # File operations
│
├── sample_files/                # Practice files
│   ├── pdfs/
│   ├── word_docs/
│   ├── excel_files/
│   ├── images/
│   └── text_files/
│
└── venv/                        # Python environment
```

## 📚 The Book Structure

### Part I: Python Programming Basics (Chapters 1-8)
Build your Python foundation:
- Chapter 1: Python Basics
- Chapter 2: Flow Control (if-else)
- Chapter 3: Loops (while, for)
- Chapter 4: Functions
- Chapter 5: Debugging
- Chapter 6: Lists
- Chapter 7: Dictionaries
- Chapter 8: Strings

### Part II: Automating Tasks (Chapters 9-24)
Learn to automate everything:
- **Chapter 9: Regular Expressions** - Text pattern matching
- **Chapter 10: Files** - Reading and writing files
- **Chapter 11: File Organization** - Bulk file operations
- **Chapter 12: Command Line Programs** - User-friendly scripts
- **Chapter 13: Web Scraping** - Downloading data from websites
- **Chapter 14: Excel** - Spreadsheet automation
- **Chapter 15: Google Sheets** - Cloud spreadsheet automation
- **Chapter 16: Databases** - SQLite data management
- **Chapter 17: PDFs & Word** - Document automation
- **Chapter 18: CSV, JSON, XML** - Data file formats
- **Chapter 19: Time & Scheduling** - Time-based automation
- **Chapter 20: Email & Notifications** - Communication automation
- **Chapter 21: Images** - Image manipulation
- **Chapter 22: OCR** - Text recognition from images
- **Chapter 23: GUI Automation** - Control keyboard and mouse
- **Chapter 24: Speech** - Text-to-speech and recognition

## 🛠 Installed Automation Packages

### File & Document Automation
- **openpyxl** - Excel files (.xlsx)
- **python-docx** - Word documents (.docx)
- **PyPDF2** - PDF manipulation

### Image Processing
- **Pillow (PIL)** - Image editing and manipulation

### Web Automation
- **requests** - HTTP requests
- **beautifulsoup4** - HTML parsing
- **selenium** - Browser automation

### Desktop GUI Automation
- **pyautogui** - Control mouse and keyboard
- **pyperclip** - Clipboard operations
- **pyinputplus** - Validated input

### Audio & Speech
- **pyttsx3** - Text-to-speech (offline)
- **gTTS** - Google Text-to-Speech
- **SpeechRecognition** - Speech-to-text

### Utilities
- **schedule** - Task scheduling
- **python-dateutil** - Date/time manipulation
- **pytz** - Timezone handling

## 💡 Common Automation Projects

### File Organization
```python
# Organize downloads by file type
from pathlib import Path
import shutil

downloads = Path.home() / 'Downloads'
for file in downloads.iterdir():
    if file.is_file():
        ext_folder = downloads / file.suffix[1:]
        ext_folder.mkdir(exist_ok=True)
        shutil.move(str(file), str(ext_folder / file.name))
```

### Bulk File Renaming
```python
# Add date prefix to all files
from pathlib import Path
import datetime

date = datetime.datetime.now().strftime('%Y%m%d')
for file in Path('.').glob('*.txt'):
    file.rename(f"{date}_{file.name}")
```

### Web Scraping
```python
# Download images from a webpage
import requests
from bs4 import BeautifulSoup

response = requests.get('https://example.com')
soup = BeautifulSoup(response.text, 'html.parser')

for img in soup.find_all('img'):
    img_url = img.get('src')
    # Download and save...
```

### Excel Automation
```python
# Update Excel spreadsheet
from openpyxl import load_workbook

wb = load_workbook('data.xlsx')
sheet = wb.active

for row in range(2, sheet.max_row + 1):
    sheet[f'C{row}'] = sheet[f'A{row}'].value * sheet[f'B{row}'].value

wb.save('data_updated.xlsx')
```

### Email Automation
```python
# Send notification emails
import smtplib
from email.mime.text import MIMEText

msg = MIMEText('Task completed!')
msg['Subject'] = 'Automation Alert'
msg['From'] = 'you@example.com'
msg['To'] = 'recipient@example.com'

# Send via SMTP...
```

## 🎓 Your Learning Path

### Week 1: Python Fundamentals (Ch 1-4)
- Master Python basics
- Understand flow control
- Write functions
- **Goal:** Comfort with Python syntax

### Week 2: Data Structures (Ch 5-8)
- Debug your code
- Work with lists and dictionaries
- Manipulate strings
- **Goal:** Handle complex data

### Week 3: Text Processing (Ch 9)
- Master regular expressions
- Extract data from text
- Validate input
- **Goal:** Regex proficiency

### Week 4: File Automation (Ch 10-12)
- Read and write files
- Organize file systems
- Create command-line tools
- **Goal:** Automate file tasks

### Week 5: Web & Data (Ch 13-16)
- Scrape websites
- Automate spreadsheets
- Work with databases
- **Goal:** Data automation skills

### Week 6: Documents (Ch 17-18)
- Process PDFs and Word docs
- Handle CSV, JSON, XML
- **Goal:** Document automation

### Week 7: Advanced Automation (Ch 19-24)
- Schedule tasks
- Send notifications
- Process images
- Control GUI
- **Goal:** Full automation toolkit

## 🔍 Quick Reference Guides

### Regex Cheat Sheet
`quick_reference/regex_cheatsheet.md`
- Common patterns (phone, email, URL)
- Search, replace, validate
- Practical examples

### File Automation Cheat Sheet
`quick_reference/file_automation_cheatsheet.md`
- Path operations
- Reading/writing files
- Directory operations
- Common automation tasks

## 🧪 Testing Your Scripts

### Use the Test Sandbox
```bash
# Edit automation_test.py and run:
python automation_test.py
```

### Run Automation Scripts Safely
```python
# Always test on sample files first!
from pathlib import Path

# Work in sample_files directory
test_dir = Path('sample_files/text_files')
```

### Debug with Print Statements
```python
# Add debug output
for file in Path('.').glob('*.txt'):
    print(f"Processing: {file}")  # See what's happening
    # Your automation code...
```

## 🐛 Troubleshooting

### Package Import Errors
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Verify packages
python verify_setup.py

# Reinstall if needed
pip install -r requirements.txt
```

### PyAutoGUI Issues (macOS)
```
# Grant accessibility permissions:
System Preferences → Security & Privacy → Accessibility
# Add Terminal or your editor
```

### File Permission Errors
```python
# Check file permissions
from pathlib import Path
file = Path('myfile.txt')
print(oct(file.stat().st_mode))
```

### Selenium Browser Issues
```bash
# Install ChromeDriver or GeckoDriver
# macOS: brew install chromedriver
# Or download from official sites
```

## 📝 Best Practices

### 1. Always Test First
```python
# Test on copies, not originals
import shutil
shutil.copy('original.txt', 'test_copy.txt')
# Test on test_copy.txt
```

### 2. Add Confirmation for Destructive Operations
```python
response = input("Delete all files? (yes/no): ")
if response.lower() == 'yes':
    # Delete files
```

### 3. Use Error Handling
```python
try:
    # Risky operation
    file.unlink()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
```

### 4. Log Your Automation
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Processing started")
```

### 5. Make Backups
```python
# Backup before modifying
import shutil
import datetime

timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
shutil.copy('data.xlsx', f'backup_{timestamp}_data.xlsx')
```

## 🎯 Project Ideas

### Beginner
- Organize your downloads folder
- Rename vacation photos with dates
- Create a to-do list manager
- Build a simple password keeper

### Intermediate
- Automated file backup system
- Web scraper for news headlines
- Excel report generator
- Bulk image resizer

### Advanced
- Email notification system
- Automated data entry from PDFs
- GUI automation for repetitive tasks
- Scheduled web scraping dashboard

## 📖 Additional Resources

### In This Package
- Official Al Sweigart book code in `book_resources/`
- Sample files for practice in `sample_files/`
- Cheat sheets in `quick_reference/`

### Online (When Available)
- Book website: https://automatetheboringstuff.com
- Video course: https://www.udemy.com/course/automate/
- Author's website: https://inventwithpython.com
- Reddit: r/learnpython

## 🤝 Tips for Success

1. **Type code yourself** - Don't copy-paste
2. **Experiment freely** - Break things and fix them
3. **Start small** - Automate one task at a time
4. **Use real problems** - Automate your actual boring tasks
5. **Share your wins** - Show off your automation scripts!

## 🌟 What You'll Be Able to Do

After completing this book, you can:
- ✅ Organize thousands of files in seconds
- ✅ Scrape data from websites automatically
- ✅ Generate and update Excel reports
- ✅ Send automated email notifications
- ✅ Process PDFs and Word documents in bulk
- ✅ Control your mouse and keyboard with code
- ✅ Schedule tasks to run automatically
- ✅ Build command-line tools
- ✅ Save hours every week on repetitive tasks

## 🚀 Ready to Automate?

```bash
# Activate your environment
source venv/bin/activate

# Verify everything works
python verify_setup.py

# Start with Chapter 1
open exercises/CHAPTERS_OVERVIEW.md

# Begin automating!
cd my_work/chapter_01
```

Remember: **Every boring task you automate is time saved for the things you actually enjoy!**

Happy automating! 🤖🐍
