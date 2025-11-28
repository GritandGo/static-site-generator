from enum import Enum


class BlockType(Enum):
    """Represents the different types of markdown blocks supported."""

    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block_text):
    """
    Classify a single markdown block into its BlockType.


    Assumes leading/trailing whitespace is already stripped and
    lines are separated by '\n'.
    """
    
    lines = block_text.split("\n")
    if block_text.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
        
    
    if block_text.startswith("```") and block_text.endswith("```"):
        return BlockType.CODE
    

    if lines[0].startswith(">"):
        valid_quote = True
        for line in lines:
            if not line.startswith(">"):
                valid_quote = False
                break
        if valid_quote:
            return BlockType.QUOTE
    

    if lines[0].startswith("- "):
        valid_unordered_list = True
        for line in lines:
            if not line.startswith("- "):
                valid_unordered_list = False
                break
        if valid_unordered_list:
            return BlockType.UNORDERED_LIST
    

    if not block_text.startswith("1. "):
        return BlockType.PARAGRAPH
    

    valid = True
    for i, line in enumerate(lines, start=1):
        prefix = f"{i}. "
        if not line.startswith(prefix):
            valid = False
            break
    if valid:
        return BlockType.ORDERED_LIST
    

    return BlockType.PARAGRAPH  

    

