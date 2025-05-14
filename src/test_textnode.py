import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_different_text(self):
        node = TextNode("First text", TextType.BOLD)
        node2 = TextNode("Second text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_none_inequality(self):
        node = TextNode("Same text", TextType.LINK)
        node2 = TextNode("Same text", TextType.LINK, "https://example.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()