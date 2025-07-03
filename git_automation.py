#!/usr/bin/env python3
"""
Simple Git Automation Script
Usage: python git_automation.py "commit message"
"""

import sys
import subprocess

def run_command(command, description):
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

def main():
    if len(sys.argv) != 2:
        print("❌ Usage: python git_automation.py \"commit message\"")
        sys.exit(1)
    commit_message = sys.argv[1]
    if not commit_message.strip():
        print("❌ Commit message cannot be empty")
        sys.exit(1)

    # Add all files
    if not run_command("git add .", "Adding all files to staging"):
        sys.exit(1)
    # Commit
    if not run_command(f'git commit -m "{commit_message}"', "Committing changes"):
        sys.exit(1)
    # Get current branch
    try:
        branch_result = subprocess.run("git branch --show-current", shell=True, check=True, capture_output=True, text=True)
        current_branch = branch_result.stdout.strip()
    except subprocess.CalledProcessError:
        current_branch = "main"
    # Push
    if not run_command(f"git push origin {current_branch}", f"Pushing to origin {current_branch}"):
        sys.exit(1)
    print(f"🎉 All changes committed and pushed with message: '{commit_message}'")

if __name__ == "__main__":
    main() 