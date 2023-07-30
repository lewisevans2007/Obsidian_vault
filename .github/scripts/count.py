# Count.py
# Counts the number of pages and links in the vault and updates the README.md file
# By: Lewis Evans

import os
import re

pages = 0
links = 0

for root, dirs, files in os.walk("."):
    for file in files:
        if ".obsidian" in root or ".github" in root or ".git" in root:
            continue
        if file.endswith(".md"):
            if file != "README.md":
                pages += 1
                with open(os.path.join(root, file), "r", encoding="utf8") as f:
                    for line in f:
                        if re.search(r"\[\[.*\]\]", line):
                            links += 1

with open("README.md", "r", encoding="utf8") as f:
    lines = f.readlines()

lines[6] = f"In this vault there are: `{pages}` pages and `{links}` links\n"

with open("README.md", "w", encoding="utf8") as f:
    f.writelines(lines)