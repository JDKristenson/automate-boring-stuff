# File Automation Quick Reference

## Path Objects (pathlib)

```python
from pathlib import Path

# Current directory
cwd = Path.cwd()

# Home directory
home = Path.home()

# Create path
p = Path('folder/subfolder/file.txt')

# Join paths
p = Path('folder') / 'subfolder' / 'file.txt'

# Check if exists
p.exists()
p.is_file()
p.is_dir()

# Get parts
p.name          # 'file.txt'
p.stem          # 'file'
p.suffix        # '.txt'
p.parent        # Path('folder/subfolder')
p.anchor        # '/' or 'C:\\'
```

## Reading Files

```python
# Read entire file
with open('file.txt') as f:
    content = f.read()

# Read lines into list
with open('file.txt') as f:
    lines = f.readlines()

# Read line by line
with open('file.txt') as f:
    for line in f:
        print(line.rstrip())

# Using Path
from pathlib import Path
content = Path('file.txt').read_text()
```

## Writing Files

```python
# Write (overwrite)
with open('file.txt', 'w') as f:
    f.write('Hello World\n')

# Append
with open('file.txt', 'a') as f:
    f.write('New line\n')

# Write lines
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('file.txt', 'w') as f:
    f.writelines(lines)

# Using Path
from pathlib import Path
Path('file.txt').write_text('Hello World')
```

## File Operations (shutil)

```python
import shutil
from pathlib import Path

# Copy file
shutil.copy('source.txt', 'dest.txt')
shutil.copy('source.txt', 'dest_folder/')

# Copy entire directory
shutil.copytree('source_folder', 'dest_folder')

# Move/rename
shutil.move('source.txt', 'dest.txt')
shutil.move('source.txt', 'folder/')

# Delete file
Path('file.txt').unlink()

# Delete empty directory
Path('folder').rmdir()

# Delete directory and contents
shutil.rmtree('folder')
```

## Directory Operations

```python
from pathlib import Path
import os

# Create directory
Path('new_folder').mkdir()

# Create directory with parents
Path('parent/child/grandchild').mkdir(parents=True, exist_ok=True)

# List directory contents
for item in Path('.').iterdir():
    print(item)

# List only files
for file in Path('.').iterdir():
    if file.is_file():
        print(file)

# Glob patterns
for file in Path('.').glob('*.txt'):
    print(file)

# Recursive glob
for file in Path('.').rglob('*.py'):
    print(file)  # Finds all .py files in subfolders too
```

## Walking Directory Trees

```python
import os
from pathlib import Path

# Using os.walk
for folder, subfolders, files in os.walk('.'):
    print(f'Folder: {folder}')
    print(f'Subfolders: {subfolders}')
    print(f'Files: {files}')
    print()

# Using Path.rglob
for file in Path('.').rglob('*'):
    if file.is_file():
        print(file)
```

## Zip Files

```python
import zipfile
from pathlib import Path

# Create zip file
with zipfile.ZipFile('archive.zip', 'w') as zip_file:
    zip_file.write('file1.txt')
    zip_file.write('file2.txt')

# Extract zip file
with zipfile.ZipFile('archive.zip') as zip_file:
    zip_file.extractall('extracted_folder')

# Extract single file
with zipfile.ZipFile('archive.zip') as zip_file:
    zip_file.extract('file1.txt', 'dest_folder')

# List contents
with zipfile.ZipFile('archive.zip') as zip_file:
    for info in zip_file.namelist():
        print(info)

# Compress entire folder
def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in Path(folder_path).rglob('*'):
            if file.is_file():
                zipf.write(file, file.relative_to(folder_path))
```

## Common Automation Tasks

### Organize Files by Extension

```python
from pathlib import Path
import shutil

def organize_by_extension(source_folder):
    source = Path(source_folder)
    for file in source.iterdir():
        if file.is_file():
            # Get extension (without dot)
            ext = file.suffix[1:] if file.suffix else 'no_extension'
            
            # Create folder for extension
            dest_folder = source / ext
            dest_folder.mkdir(exist_ok=True)
            
            # Move file
            shutil.move(str(file), str(dest_folder / file.name))
```

### Rename Files in Bulk

```python
from pathlib import Path

def rename_with_prefix(folder, prefix):
    for file in Path(folder).iterdir():
        if file.is_file():
            new_name = f"{prefix}_{file.name}"
            file.rename(file.parent / new_name)

def add_date_to_filenames(folder):
    import datetime
    date_str = datetime.datetime.now().strftime('%Y%m%d')
    
    for file in Path(folder).iterdir():
        if file.is_file():
            new_name = f"{file.stem}_{date_str}{file.suffix}"
            file.rename(file.parent / new_name)
```

### Find and Copy Specific Files

```python
from pathlib import Path
import shutil

def find_and_copy_files(source, dest, pattern='*.txt'):
    dest_path = Path(dest)
    dest_path.mkdir(parents=True, exist_ok=True)
    
    for file in Path(source).rglob(pattern):
        if file.is_file():
            shutil.copy(str(file), str(dest_path / file.name))
```

### Delete Old Files

```python
from pathlib import Path
import time

def delete_old_files(folder, days=30):
    cutoff = time.time() - (days * 86400)
    
    for file in Path(folder).iterdir():
        if file.is_file() and file.stat().st_mtime < cutoff:
            print(f"Deleting {file}")
            file.unlink()
```

### Backup Files

```python
from pathlib import Path
import shutil
import datetime

def backup_folder(source, backup_root):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f"backup_{timestamp}"
    backup_path = Path(backup_root) / backup_name
    
    shutil.copytree(source, backup_path)
    print(f"Backup created: {backup_path}")
```

### Find Duplicate Files

```python
from pathlib import Path
import hashlib

def find_duplicates(folder):
    hashes = {}
    duplicates = []
    
    for file in Path(folder).rglob('*'):
        if file.is_file():
            # Calculate file hash
            file_hash = hashlib.md5(file.read_bytes()).hexdigest()
            
            if file_hash in hashes:
                duplicates.append((file, hashes[file_hash]))
            else:
                hashes[file_hash] = file
    
    return duplicates
```

### Search File Contents

```python
from pathlib import Path
import re

def search_in_files(folder, pattern, file_pattern='*.txt'):
    regex = re.compile(pattern)
    results = []
    
    for file in Path(folder).rglob(file_pattern):
        if file.is_file():
            try:
                content = file.read_text()
                matches = regex.findall(content)
                if matches:
                    results.append((file, matches))
            except Exception as e:
                print(f"Error reading {file}: {e}")
    
    return results
```

### Get Folder Size

```python
from pathlib import Path

def get_folder_size(folder):
    total = 0
    for file in Path(folder).rglob('*'):
        if file.is_file():
            total += file.stat().st_size
    return total

def format_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
```

### Create File Index

```python
from pathlib import Path
import csv

def create_file_index(folder, output='index.csv'):
    with open(output, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Path', 'Name', 'Extension', 'Size', 'Modified'])
        
        for file in Path(folder).rglob('*'):
            if file.is_file():
                stat = file.stat()
                writer.writerow([
                    str(file),
                    file.name,
                    file.suffix,
                    stat.st_size,
                    stat.st_mtime
                ])
```

## Safe File Operations

```python
from pathlib import Path
import shutil

def safe_delete(file_path):
    """Delete file with confirmation."""
    file = Path(file_path)
    if file.exists():
        response = input(f"Delete {file}? (yes/no): ")
        if response.lower() == 'yes':
            file.unlink()
            print(f"Deleted {file}")
    else:
        print(f"{file} does not exist")

def safe_move(source, dest):
    """Move file with backup if destination exists."""
    source = Path(source)
    dest = Path(dest)
    
    if dest.exists():
        backup = dest.with_suffix(dest.suffix + '.backup')
        shutil.move(str(dest), str(backup))
        print(f"Backed up existing file to {backup}")
    
    shutil.move(str(source), str(dest))
    print(f"Moved {source} to {dest}")
```

## Error Handling

```python
from pathlib import Path

def safe_file_operation(file_path):
    try:
        file = Path(file_path)
        if not file.exists():
            raise FileNotFoundError(f"{file} not found")
        
        content = file.read_text()
        # Process content...
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print(f"Permission denied: {file}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

## File Permissions

```python
from pathlib import Path
import os
import stat

# Check if file is readable/writable
file = Path('file.txt')
file.stat().st_mode & stat.S_IRUSR  # Readable by user
file.stat().st_mode & stat.S_IWUSR  # Writable by user

# Make file readonly
os.chmod('file.txt', stat.S_IRUSR)

# Make file executable
os.chmod('script.py', stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
```

## Temporary Files

```python
import tempfile

# Temporary file
with tempfile.TemporaryFile(mode='w+') as temp:
    temp.write('Hello')
    temp.seek(0)
    print(temp.read())
# File is automatically deleted

# Named temporary file
with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp:
    temp.write('Hello')
    temp_name = temp.name
# Can access file after closing using temp_name

# Temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Working in {temp_dir}")
    # Do work...
# Directory is automatically deleted
```
