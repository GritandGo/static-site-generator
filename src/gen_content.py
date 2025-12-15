


def extract_title(markdown):
    split_lines = markdown.split("\n")
    for line in split_lines:
        cleaned_line = line.strip()
        if cleaned_line.startswith("# "):
            return cleaned_line[2:].strip()
    raise Exception("No header found.")

