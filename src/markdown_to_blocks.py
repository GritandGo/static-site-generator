def markdown_to_blocks(markdown):
    split_block = markdown.split("\n\n")

    final_blocks = []
    for block in split_block:
        stripped_and_split = block.strip()

        


        if stripped_and_split != "":
            final_blocks.append(stripped_and_split)

    return final_blocks