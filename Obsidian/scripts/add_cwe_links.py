# Add CWE links
# Adds CWE details link to the end of all files starting with CWE- in 
# the current directory and all subdirectories only if the link does not
# already exist in the file.
# By: Lewis Evans 
import os
import re
import sys

for root, dirs, files in os.walk("."):
    for file in files:
        if file.startswith("CWE-") and file.endswith(".md"):
            f = open(os.path.join(root, file), "r")
            contents = f.read()
            f.close()
            if "---" in contents:
                print("Ignoring: " + file)
                continue
            else:
                print("Adding link to: " + file)
                CWE_id = file.split(".")[0]
                CWE_id = CWE_id.split("-")[1]
                #https://cwe.mitre.org/data/definitions/200.html
                url = "https://cwe.mitre.org/data/definitions/" + CWE_id + ".html"
                contents = contents + "\n\n---\n#### Links:\n- [Mitre CWE](" + url + ")\n"
                f = open(os.path.join(root, file), "w")
                f.write(contents)
                f.close()
                