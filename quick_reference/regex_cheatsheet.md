# Regular Expressions Quick Reference

## Common Patterns

### Basic Patterns
```python
import re

# Literal characters
phone_regex = re.compile(r'415-555-4242')

# Digits
\d    # Any digit (0-9)
\D    # Any non-digit

# Word characters
\w    # Any letter, digit, or underscore
\W    # Any non-word character

# Whitespace
\s    # Any space, tab, or newline
\S    # Any non-whitespace character

# Wildcard
.     # Any character except newline
```

### Repetition
```python
# Quantifiers
?     # 0 or 1 occurrence (optional)
*     # 0 or more occurrences
+     # 1 or more occurrences
{n}   # Exactly n occurrences
{n,}  # n or more occurrences
{n,m} # Between n and m occurrences

# Examples
phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')  # 415-555-1234
email_regex = re.compile(r'\w+@\w+\.\w+')       # user@example.com
```

### Character Classes
```python
# Character sets
[aeiou]      # Any vowel
[a-z]        # Any lowercase letter
[A-Z]        # Any uppercase letter
[a-zA-Z]     # Any letter
[0-9]        # Any digit
[^aeiou]     # Any character except vowels

# Examples
consonant = re.compile(r'[^aeiou]')
alphanumeric = re.compile(r'[a-zA-Z0-9]')
```

### Groups and Alternation
```python
# Parentheses create groups
phone_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phone_regex.search('My number is 415-555-4242.')
mo.group(1)  # '415' (area code)
mo.group(2)  # '555-4242'

# Alternation (or)
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
mo.group()   # 'Batmobile'
mo.group(1)  # 'mobile'
```

### Anchors
```python
^    # Start of string
$    # End of string
\b   # Word boundary

# Examples
starts_with = re.compile(r'^Hello')  # Must start with Hello
ends_with = re.compile(r'world$')    # Must end with world
whole_word = re.compile(r'\bcat\b')  # Match 'cat' not 'catch'
```

## Common Use Cases

### Phone Numbers
```python
# US phone numbers
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?        # Area code (optional)
    (\s|-|\.)?                # Separator
    \d{3}                     # First 3 digits
    (\s|-|\.)                 # Separator
    \d{4}                     # Last 4 digits
)''', re.VERBOSE)

# Examples matched:
# 415-555-1234
# (415) 555-1234
# 415.555.1234
# 555-1234
```

### Email Addresses
```python
# Basic email pattern
email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

# Find all emails in text
text = "Contact us at support@example.com or sales@example.org"
emails = email_regex.findall(text)
# ['support@example.com', 'sales@example.org']
```

### URLs
```python
# URL pattern
url_regex = re.compile(r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[^\s]*)?')

# Examples matched:
# http://example.com
# https://www.example.com/page
# https://example.org/path/to/page.html
```

### Dates
```python
# MM/DD/YYYY format
date_regex = re.compile(r'\d{1,2}/\d{1,2}/\d{4}')

# YYYY-MM-DD format
iso_date = re.compile(r'\d{4}-\d{2}-\d{2}')

# Examples:
# 12/31/2025
# 2025-12-31
```

### Credit Cards
```python
# Basic credit card (groups of 4 digits)
cc_regex = re.compile(r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}')

# Examples matched:
# 1234-5678-9012-3456
# 1234 5678 9012 3456
# 1234567890123456
```

### Social Security Numbers
```python
ssn_regex = re.compile(r'\d{3}-\d{2}-\d{4}')
# 123-45-6789
```

## re Module Methods

### search() - Find First Match
```python
phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phone_regex.search('Call me at 415-555-1234')
if mo:
    print(mo.group())  # '415-555-1234'
```

### findall() - Find All Matches
```python
phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
numbers = phone_regex.findall('Cell: 415-555-1234, Work: 415-555-9999')
# ['415-555-1234', '415-555-9999']

# With groups
phone_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
numbers = phone_regex.findall('Call 415-555-1234')
# [('415', '555-1234')]
```

### sub() - Search and Replace
```python
phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
text = 'My number is 415-555-1234'
censored = phone_regex.sub('XXX-XXX-XXXX', text)
# 'My number is XXX-XXX-XXXX'

# Using groups in replacement
name_regex = re.compile(r'(\w+) (\w+)')
name_regex.sub(r'\2, \1', 'John Smith')
# 'Smith, John'
```

### match() - Match from Start
```python
# Only matches if pattern is at start of string
regex = re.compile(r'Hello')
regex.match('Hello World')  # Match object
regex.match('Say Hello')    # None
```

### split() - Split by Pattern
```python
regex = re.compile(r'\s+')
words = regex.split('Split  by   multiple    spaces')
# ['Split', 'by', 'multiple', 'spaces']
```

## Regex Flags

```python
# Case-insensitive
regex = re.compile(r'hello', re.IGNORECASE)
# Or: re.I

# Multiline (^ and $ match line boundaries)
regex = re.compile(r'^pattern', re.MULTILINE)
# Or: re.M

# Dot matches newline too
regex = re.compile(r'.*', re.DOTALL)
# Or: re.S

# Verbose (allow comments and whitespace)
phone_regex = re.compile(r'''
    \d{3}     # Area code
    -         # Separator
    \d{3}     # First 3 digits
    -         # Separator
    \d{4}     # Last 4 digits
''', re.VERBOSE)
# Or: re.X

# Combine flags
regex = re.compile(r'pattern', re.IGNORECASE | re.VERBOSE)
```

## Greedy vs Non-Greedy

```python
# Greedy (default) - matches as much as possible
greedy = re.compile(r'<.*>')
greedy.search('<tag>text</tag>').group()
# '<tag>text</tag>'

# Non-greedy - matches as little as possible
non_greedy = re.compile(r'<.*?>')
non_greedy.search('<tag>text</tag>').group()
# '<tag>'
```

## Practical Examples

### Extract Data from Text
```python
# Extract all phone numbers from a file
import re

def extract_phones(filename):
    phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
    with open(filename) as f:
        text = f.read()
    return phone_regex.findall(text)
```

### Validate Input
```python
def is_valid_email(email):
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(email_regex.match(email))

def is_valid_phone(phone):
    phone_regex = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return bool(phone_regex.match(phone))
```

### Clean Data
```python
# Remove all phone numbers from text
def remove_phones(text):
    phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
    return phone_regex.sub('[REDACTED]', text)

# Normalize whitespace
def normalize_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()
```

### Extract Structured Data
```python
# Parse log entries
log_regex = re.compile(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+): (.*)')

def parse_log_line(line):
    mo = log_regex.match(line)
    if mo:
        return {
            'date': mo.group(1),
            'time': mo.group(2),
            'level': mo.group(3),
            'message': mo.group(4)
        }
    return None
```

## Common Mistakes to Avoid

```python
# 1. Forgetting to escape special characters
bad = re.compile(r'.')      # Matches any character
good = re.compile(r'\.')    # Matches literal period

# 2. Not using raw strings
bad = re.compile('\d+')     # Might cause issues
good = re.compile(r'\d+')   # Always use raw strings

# 3. Greedy matching when you want non-greedy
bad = re.compile(r'<.*>')
good = re.compile(r'<.*?>')

# 4. Forgetting to check if match exists
mo = regex.search(text)
print(mo.group())          # Bad: might be None
if mo:                     # Good: check first
    print(mo.group())
```

## Testing Your Regex

```python
# Use regex101.com or pythex.org for testing
# Or test in Python:

def test_regex(pattern, test_strings):
    regex = re.compile(pattern)
    for s in test_strings:
        mo = regex.search(s)
        print(f"{s}: {'Match' if mo else 'No match'}")
        if mo:
            print(f"  Matched: {mo.group()}")

# Example
test_regex(
    r'\d{3}-\d{3}-\d{4}',
    ['415-555-1234', '555-1234', 'abc-def-ghij']
)
```
