import unittest
from split_delimiter import split_nodes_image, split_nodes_link
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType



class TestTextToTextNodes(unittest.TestCase):
    
    def test_full_markdown_conversion(self):
        """Test the conversion of a complex string containing all inline markdown types."""
        
        # This input matches the complex example provided in the assignment
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        
        expected_nodes = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.PLAIN),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        
        result_nodes = text_to_textnodes(text)
        self.assertListEqual(expected_nodes, result_nodes)

    def test_adjacent_delimiters(self):
        """Test markdown elements placed immediately next to each other."""
        text = "Code: `print('hi')`**bold**_italic_![img](a.png)[link](b.com)end"
        
        expected_nodes = [
            TextNode("Code: ", TextType.PLAIN),
            TextNode("print('hi')", TextType.CODE),
            TextNode("bold", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode("img", TextType.IMAGE, "a.png"),
            TextNode("link", TextType.LINK, "b.com"),
            TextNode("end", TextType.PLAIN),
        ]
        
        result_nodes = text_to_textnodes(text)
        self.assertListEqual(expected_nodes, result_nodes)

    def test_no_markdown(self):
        """Test a simple string with no markdown, ensuring it returns one single node."""
        text = "This is a simple sentence with no special formatting at all."
        
        expected_nodes = [
            TextNode(text, TextType.PLAIN)
        ]
        
        result_nodes = text_to_textnodes(text)
        self.assertListEqual(expected_nodes, result_nodes)

if __name__ == "__main__":
    unittest.main()