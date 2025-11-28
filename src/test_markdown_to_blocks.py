import unittest
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType


class test_block_to_block_type(unittest.TestCase):
    def test_heading_block(self):
        block = "# Heading"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING
        )


    def test_code_block(self):
        block = "```code block```"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE
        )
    

    def test_quote_block(self):
        block = "> quote block"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE
        ) 


    def test_unordered_list_block(self):
        block = "- "
        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST
        )


    def test_ordered_list_block(self):
        block = "1. first\n2. second"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST
        )


    def test_paragraph_block(self):
        block = "This is a regular paragraph"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )
        
    
    def test_badly_ordered_list(self):
        block = "1. first\n3. second"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )


    
    
    




class test_markdown_to_blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    #Additional test to include blocks with leading whitespace or excessive new lines.
    def test_markdown_to_blocks_with_whitespace(self):
        md = """
      # Heading one




This is a paragraph



- List Item One
- List Item Two



"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading one",
                "This is a paragraph",
                "- List Item One\n- List Item Two",
                
            ]
        )