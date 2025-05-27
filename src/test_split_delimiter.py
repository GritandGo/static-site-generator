import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class Test_split_nodes_delimiter(unittest.TestCase):
    def test_test_splits_single_bold_delimiter(self):
        node = TextNode("text **bold** more text", TextType.PLAIN)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        correct_node_list = [TextNode("text ", TextType.PLAIN), 
                             TextNode("bold", TextType.BOLD), 
                             TextNode(" more text", TextType.PLAIN)
                            ]
        self.assertEqual(result, correct_node_list)

    
    def test_test_splits_multiple_bold_delimiter(self):
        node = TextNode("**bold** **bold** more text", TextType.PLAIN)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        correct_node_list = [TextNode("bold", TextType.BOLD), 
                             TextNode(" ", TextType.PLAIN), 
                             TextNode("bold", TextType.BOLD),
                             TextNode(" more text", TextType.PLAIN)
                            ]
        self.assertEqual(result, correct_node_list)


    def test_test_splits_no_delimiter(self):
        node = TextNode("text more text", TextType.PLAIN)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        correct_node_list = [TextNode("text more text", TextType.PLAIN)]
        self.assertEqual(result, correct_node_list)


    def test_unmatched_delimiter_raises_exception(self):
        node = TextNode("text with **unmatched delimiter", TextType.PLAIN)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)




