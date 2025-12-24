#!/usr/bin/env python3
"""
Automation Test Script - Automate the Boring Stuff Companion

A sandbox for testing automation scripts safely.
Perfect for experimenting with file operations, regex, and more.

Usage:
    python automation_test.py

Edit the test_automation() function to try your code.
"""

from pathlib import Path

def test_automation():
    """
    Put your automation code here!
    This is your sandbox for experiments.
    """
    # Example: List all files in current directory
    # for file in Path('.').iterdir():
    #     if file.is_file():
    #         print(file.name)
    
    # Try your automation code here:
    pass


if __name__ == "__main__":
    print("=" * 60)
    print("Automate the Boring Stuff - Automation Test Script")
    print("=" * 60)
    print()
    print("Working directory:", Path.cwd())
    print()
    
    try:
        test_automation()
    except Exception as e:
        print(f"\n❌ Error occurred: {type(e).__name__}")
        print(f"   {e}")
        import traceback
        print("\nFull traceback:")
        traceback.print_exc()
    else:
        print("\n✅ Script executed successfully!")
    
    print()
    print("=" * 60)
