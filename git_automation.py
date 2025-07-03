#!/usr/bin/env python3
"""
Git Automation Script
Automates common Git operations: init, add, commit, and push

Usage: python git_automation.py "commit message"
"""

import sys
import subprocess
import os
from datetime import datetime

def run_command(command, description):
    """Execute a shell command and handle errors"""
    try:
        print(f"🔄 {description}...")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(f"📝 Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}: {e}")
        if e.stderr:
            print(f"🔍 Error details: {e.stderr.strip()}")
        return False

def check_git_installed():
    """Check if Git is installed"""
    try:
        subprocess.run(["git", "--version"], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git is not installed or not in PATH")
        return False
def clone():
    """Clone and setup a new repository"""
    # Create README.md
    with open("README.md", "w") as f:
        f.write("# Spring_Boot_Intern_2025_july\n")
    
    # Initialize git repository
    run_command("git init", "Initializing Git repository")
    run_command("git add README.md", "Adding README.md to staging")
    run_command('git commit -m "first commit"', "Making first commit")
    run_command("git branch -M main", "Setting branch to main")
    run_command("git remote add origin https://github.com/Nithyaganesh43/Spring_Boot_Intern_2025_july.git", "Adding remote origin")
    run_command("git push -u origin main", "Pushing to origin main")
def git_automation(commit_message):
    """Main function to automate Git operations"""
    
    print("🚀 Starting Git Automation Process...")
    print(f"📝 Commit Message: {commit_message}")
    print(f"⏰ Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    # Check if Git is installed
    if not check_git_installed():
        return False
    
    # Step 1: Initialize Git repository (if not already initialized)
    if not os.path.exists(".git"):
        if not run_command("git init", "Initializing Git repository"):
            return False
    else:
        print("ℹ️  Git repository already exists")
    
    # Step 2: Add all files to staging
    if not run_command("git add .", "Adding all files to staging"):
        return False
    
    # Step 3: Commit with the provided message
    if not run_command(f'git commit -m "{commit_message}"', "Committing changes"):
        return False
    
    # Step 4: Push to origin main
    if not run_command("git push origin main", "Pushing to origin main"):
        return False
    
    print("-" * 50)
    print("🎉 Git automation completed successfully!")
    print(f"✅ All changes committed and pushed with message: '{commit_message}'")
    return True

def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("❌ Usage: python git_automation.py \"commit message\"")
        print("📝 Example: python git_automation.py \"Initial commit - Hello World Spring Boot app\"")
        sys.exit(1)
    
    commit_message = sys.argv[1]
    
    if not commit_message.strip():
        print("❌ Commit message cannot be empty")
        sys.exit(1)
    
    success = git_automation(commit_message)
    
    if success:
        print("🎯 All operations completed successfully!")
        sys.exit(0)
    else:
        print("💥 Some operations failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 