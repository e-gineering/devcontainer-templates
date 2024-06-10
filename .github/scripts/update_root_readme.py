#!/usr/bin/env python

# Takes the generated readme files for each template, adjusts the markdown headings, and updates the root readme with the new content.

import os
import re

# Get the list of subdirs in src
template_names = [d for d in os.listdir("src")]

print(f"Found {len(template_names)} templates: {', '.join(template_names)}")

# Read the root readme
with open("README.md", "r") as f:
    root_readme = f.read()

new_content = ""

# Update the root readme with the new content
for template_name in template_names:
    # Read the feature readme
    with open(f"src/{template_name}/README.md", "r") as f:
        template_readme = f.read()

    # Adjust the markdown headings
    template_readme = re.sub(r"^#", "###", template_readme, flags=re.MULTILINE)

    # Remove everything after the --- to the end of the file
    template_readme = re.sub(r"\n---.*", "", template_readme, flags=re.DOTALL)

    new_content += f"\n{template_readme}"

print(f"New readme content to add: {new_content}")

# Replace the old content with the new content
root_readme = re.sub(
    r"<!-- START_TEMPLATES -->.*<!-- END_TEMPLATES -->",
    f"<!-- START_TEMPLATES -->{new_content}<!-- END_TEMPLATES -->",
    root_readme,
    flags=re.DOTALL,
)

# Write the updated root readme
with open("README.md", "w") as f:
    f.write(root_readme)
