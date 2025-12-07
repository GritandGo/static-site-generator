from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from conversions import TextNode, text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from htmlnode import ParentNode
from textnode import TextNode, TextType


def markdown_to_html_node(markdown):
    """Converts a full markdown document into a single parent HTMLNode"""

    block_level_nodes = [] #empty list to hold block level nodes
    cleaned_blocks = markdown_to_blocks(markdown) #split markdown into blocks
    for block in cleaned_blocks:
        block_type = block_to_block_type(block)


        if block_type == BlockType.PARAGRAPH:# ✅
            lines = block.split("\n")
            cleaned_lines = [line.strip() for line in lines if line.strip() != ""]
            paragraph_text = " ".join(cleaned_lines)
            child_leaf_nodes = text_to_children(paragraph_text)
            node = ParentNode("p", child_leaf_nodes)

        elif block_type == BlockType.HEADING:# ✅
            level = len(block) - len(block.lstrip("#"))
            heading = block.lstrip("# ")
            tag = f"h{level}"
            child_leaf_nodes = text_to_children(heading)
            node = ParentNode(tag, child_leaf_nodes)

        elif block_type == BlockType.QUOTE:# ✅
            lines = block.split("\n")
            cleaned_lines = []

            for line in lines:
                cleaned_line = line.lstrip("> ").lstrip(">")
                cleaned_lines.append(cleaned_line)

            heading = "\n".join(cleaned_lines)
            tag = "blockquote"
            child_leaf_nodes = text_to_children(heading)
            node = ParentNode(tag, child_leaf_nodes)

        elif block_type == BlockType.UNORDERED_LIST: # ✅
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                cleaned_line = line.lstrip("- ").lstrip("-")
                children = text_to_children(cleaned_line)
                li_node = ParentNode("li", children)
                li_nodes.append(li_node)
            node = ParentNode("ul", li_nodes)

        elif block_type == BlockType.ORDERED_LIST: # ✅
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                index = line.find(".")
                cleaned_line = line[index + 2 :]
                children = text_to_children(cleaned_line)
                li_node = ParentNode("li", children)
                li_nodes.append(li_node)
            node = ParentNode("ol", li_nodes)

        elif block_type == BlockType.CODE: # ✅
            lines = block.split("\n")
            code_lines = [line.lstrip() for line in lines[1:-1]]
            cleaned_line = "\n".join(code_lines) + "\n"
            child = text_node_to_html_node(TextNode(cleaned_line, TextType.PLAIN))
            code_node = ParentNode("code", [child])
            node = ParentNode("pre", [code_node])
            

        
        block_level_nodes.append(node)
        

    return ParentNode("div", children=block_level_nodes)


def text_to_children(text):#text = inline text
    """Takes a string of text and returns a list of HTMLNodes (Leafnodes) that 
    represent the inline markdown"""

    final_list = []
    list_of_text_nodes = text_to_textnodes(text)
    for node in list_of_text_nodes:
        final_list.append(text_node_to_html_node(node))
    return final_list



