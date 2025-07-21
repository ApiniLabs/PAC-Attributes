import json
from pathlib import Path

# Configuration
json_file_path = Path("example-response.jsonc")         # JSON file path
readme_path = Path("README.md")            # Markdown file to modify
start_marker = "<!-- BEGIN RESPONSE JSON -->"
end_marker = "<!-- END RESPONSE JSON -->"

# Load JSON file
json_content = json_file_path.read_text(encoding="utf-8")
try:
    parsed_json = json.loads(json_content)
    formatted_json = json.dumps(parsed_json, indent=2)
except:
    formatted_json = json_content

# Load README
readme_lines = readme_path.read_text(encoding="utf-8").splitlines()

# Find markers
try:
    start_idx = readme_lines.index(start_marker)
    end_idx = readme_lines.index(end_marker)
except ValueError:
    raise RuntimeError("Markers not found in README.md")

# Replace the section
new_block = [start_marker, "```json"] + formatted_json.splitlines() + ["```", end_marker]
new_readme = readme_lines[:start_idx] + new_block + readme_lines[end_idx+1:]

# Write back to README
readme_path.write_text("\n".join(new_readme) + "\n", encoding="utf-8")
print("README.md updated successfully.")
