import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")


        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    
    def test_props_to_html_with_props(self):
        node = HTMLNode(props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')
        
        
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        
        result = node.props_to_html()
        possible_results = [
            ' href="https://google.com" target="_blank"',
            ' target="_blank" href="https://google.com"'
        ]
        self.assertIn(result, possible_results)


    def test_props_to_html_multiple_attributes(self):
        props = {
            "href": "https://example.com",
            "target": "_blank",
            "data-id": "123"
        }
        node = HTMLNode(props=props)
        
        result = node.props_to_html()
        
        self.assertIn(' href="https://example.com"', result)
        self.assertIn(' target="_blank"', result)
        self.assertIn(' data-id="123"', result)
        
        self.assertTrue(result.startswith(' '))
        
        expected_length = sum(len(f' {k}="{v}"') for k, v in props.items())
        self.assertEqual(len(result), expected_length)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_attributes(self):
        node = LeafNode("a", "Click me!", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()