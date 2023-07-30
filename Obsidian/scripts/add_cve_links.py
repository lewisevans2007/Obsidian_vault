# Add CVE links
# Adds CVE details link to the end of all files starting with CVE- in 
# the current directory and all subdirectories only if the link does not
# already exist in the file.
# By: Lewis Evans 
import os
import re
import sys

for root, dirs, files in os.walk("."):
    for file in files:
        if file.startswith("CVE-") and file.endswith(".md"):
            f = open(os.path.join(root, file), "r")
            contents = f.read()
            f.close()
            if "---" in contents:
                print("Ignoring: " + file)
                continue
            else:
                print("Adding link to: " + file)
                cve_id = file.split(".")[0]
                url = "https://www.cvedetails.com/cve/" + cve_id + "/"
                contents = contents + "\n\n---\n#### Links:\n- [CVE Details](" + url + ")\n"
                f = open(os.path.join(root, file), "w")
                f.write(contents)
                f.close()
                