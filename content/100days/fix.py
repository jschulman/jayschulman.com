import os
import re
import yaml

def fix_yaml_front_matter(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()

                # Extract YAML front matter
                match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
                if match:
                    yaml_front_matter = match.group(1)

                    # Split the YAML front matter into lines
                    lines = yaml_front_matter.split("\n")

                    # Remove any leading whitespace from each line
                    lines = [line.lstrip() for line in lines]

                    # Find the minimum indentation level
                    min_indent = min(len(line) - len(line.lstrip()) for line in lines if line.strip())

                    # Adjust the indentation of each line
                    adjusted_lines = [line[min_indent:] if line.strip() else line for line in lines]

                    # Join the lines back together
                    yaml_front_matter = "\n".join(adjusted_lines)

                    # Load the YAML front matter using yaml.safe_load()
                    data = yaml.safe_load(yaml_front_matter)

                    # Check if 'tags' field exists and is not already a list
                    if "tags" in data and not isinstance(data["tags"], list):
                        # Convert 'tags' field to a list
                        tags = [tag.strip() for tag in data["tags"].split(",")]
                        data["tags"] = tags

                    # Update YAML front matter in the content
                    updated_yaml_front_matter = yaml.dump(data, default_flow_style=False)
                    updated_content = re.sub(r"^---\n.*?\n---", f"---\n{updated_yaml_front_matter}---", content, flags=re.DOTALL)

                    # Write the updated content back to the file
                    with open(file_path, "w") as f:
                        f.write(updated_content)

                    print(f"Updated YAML front matter in {file_path}")

# Specify the directory where your Markdown files are located
directory = "./blockchain"

fix_yaml_front_matter(directory)
