from markdown_to_html import markdown_to_html_node
import os
from pathlib import Path


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        content = f.read()
    with open(template_path) as f:
        template = f.read()


    node = markdown_to_html_node(content)
    html = node.to_html()
    title = extract_title(content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)


    dir_path = os.path.dirname(dest_path)
    if dir_path != "":
        os.makedirs(dir_path, exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(template)




def extract_title(markdown):
    split_lines = markdown.split("\n")
    for line in split_lines:
        cleaned_line = line.strip()
        if cleaned_line.startswith("# "):
            return cleaned_line[2:].strip()
    raise Exception("No header found.")




def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        from_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(from_path) and from_path.endswith(".md"):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        elif os.path.isdir(from_path):
            generate_pages_recursive(from_path, template_path, dest_path)
            

        


