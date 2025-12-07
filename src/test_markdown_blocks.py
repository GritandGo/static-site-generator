import unittest
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from markdown_to_html import markdown_to_html_node


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



class test_markdown_to_html(unittest.TestCase):
    """Unit testing for markdown to HTML function(s)"""

    def test_heading(self):
        md = "# Heading"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading</h1></div>"
        )

    
    def test_quote_block(self):#✅
        md = "> This is a quote."

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote.</blockquote></div>"
        )


    def test_unordered_lists(self):
        md = """
    - Item 1
    - Item 2
    - Item 3

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
        )


    def test_ordered_lists(self):
        md = """
    1. Item 1
    2. Item 2
    3. Item 3

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol></div>"
            
        )


    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


