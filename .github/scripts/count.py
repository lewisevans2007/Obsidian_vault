import os
import re

pages = 0
links = 0

# for files in the current directory and subdirectories
for root, dirs, files in os.walk("."):
    # for each file in the files
    for file in files:
        if ".obsidian" in root or ".github" in root or ".git" in root:
            continue
        # if the file is a markdown file
        if file.endswith(".md"):
            # if the file is not the README.md file
            if file != "README.md":
                # add one to the page count
                pages += 1
                # open the file
                with open(os.path.join(root, file), "r", encoding="utf8") as f:
                    # for each line in the file
                    for line in f:
                        # if the line contains a link
                        if re.search(r"\[\[.*\]\]", line):
                            # add one to the link count
                            links += 1

# open the README.md file
with open("README.md", "r", encoding="utf8") as f:
    # read the file
    lines = f.readlines()

# replace the line with the new line
lines[6] = f"In this vault there are: {pages} pages and {links} links\n"

# open the README.md file
with open("README.md", "w", encoding="utf8") as f:
    # write the new lines
    f.writelines(lines)