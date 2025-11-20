import unittest
from markdown_to_blocks import markdown_to_blocks



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