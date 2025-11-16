import unittest
from split_delimiter import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestSplitImages(unittest.TestCase):
    # --- 1. Happy Path & Quantity Variation ---
    
    def test_split_images_multiple(self):
        """Test with a text node containing two images."""
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an ", TextType.PLAIN),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.PLAIN),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertListEqual(expected, new_nodes)


    def test_split_images_none(self):
        """Test a text node with no images."""
        node = TextNode("This is just plain text.", TextType.PLAIN)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    # --- 2. Positional Edge Cases ---

    def test_split_images_leading(self):
        """Test when the image is at the very start of the string."""
        node = TextNode("![image](url/img.png)Followed by text.", TextType.PLAIN)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("image", TextType.IMAGE, "url/img.png"),
            TextNode("Followed by text.", TextType.PLAIN),
        ]
        self.assertListEqual(expected, new_nodes)


    def test_split_images_trailing(self):
        """Test when the image is at the very end of the string."""
        node = TextNode("Text ends with an image.![last](url/img.png)", TextType.PLAIN)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("Text ends with an image.", TextType.PLAIN),
            TextNode("last", TextType.IMAGE, "url/img.png"),
        ]
        self.assertListEqual(expected, new_nodes)


    def test_split_images_only(self):
        """Test when the string contains ONLY the image markdown."""
        node = TextNode("![single](only/img.png)", TextType.PLAIN)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("single", TextType.IMAGE, "only/img.png"),
        ]
        self.assertListEqual(expected, new_nodes)
        
    # --- 3. Input Condition Edge Cases ---
    
    def test_split_non_plain_node(self):
        """Test that a non-PLAIN type node is returned unchanged."""
        non_plain_node = TextNode("This is code", TextType.CODE)
        new_nodes = split_nodes_image([non_plain_node])
        self.assertListEqual([non_plain_node], new_nodes)
        

    def test_split_multiple_input_nodes(self):
        """Test when the input list contains multiple nodes (some plain, some not)."""
        node_1 = TextNode("Text with ![image](a.png)", TextType.PLAIN)
        node_2 = TextNode("Plain text", TextType.PLAIN)
        node_3 = TextNode("Bold text", TextType.BOLD)
        
        input_nodes = [node_1, node_2, node_3]
        new_nodes = split_nodes_image(input_nodes)
        expected = [
            TextNode("Text with ", TextType.PLAIN),
            TextNode("image", TextType.IMAGE, "a.png"),
            TextNode("Plain text", TextType.PLAIN),
            TextNode("Bold text", TextType.BOLD), 
        ]
        self.assertListEqual(expected, new_nodes)


class TestSplitLinks(unittest.TestCase):
    
    # --- 1. Happy Path & Quantity Variation ---

    def test_split_links_multiple(self):
        """Test with a text node containing two links."""
        node = TextNode(
            "Text with a [first link](https://boot.dev) and a [second link](https://www.youtube.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("Text with a ", TextType.PLAIN),
            TextNode("first link", TextType.LINK, "https://boot.dev"),
            TextNode(" and a ", TextType.PLAIN),
            TextNode("second link", TextType.LINK, "https://www.youtube.com"),
        ]
        self.assertListEqual(expected, new_nodes)

    def test_split_links_none(self):
        """Test a text node with no links."""
        node = TextNode("This is just plain text.", TextType.PLAIN)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    # --- 2. Positional Edge Cases ---

    def test_split_links_leading(self):
        """Test when the link is at the very start of the string."""
        node = TextNode("[Start Link](start.com)Followed by text.", TextType.PLAIN)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("Start Link", TextType.LINK, "start.com"),
            TextNode("Followed by text.", TextType.PLAIN),
        ]
        self.assertListEqual(expected, new_nodes)

    def test_split_links_trailing(self):
        """Test when the link is at the very end of the string."""
        node = TextNode("Text ends with a [link](end.com)", TextType.PLAIN)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("Text ends with a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "end.com"),
        ]
        self.assertListEqual(expected, new_nodes)

    def test_split_links_only(self):
        """Test when the string contains ONLY the link markdown."""
        node = TextNode("[single link](only.com)", TextType.PLAIN)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("single link", TextType.LINK, "only.com"),
        ]
        self.assertListEqual(expected, new_nodes)
        
    # --- 3. Input Condition Edge Cases ---
    
    def test_split_links_non_plain_node(self):
        """Test that a non-PLAIN type node (e.g., CODE) is returned unchanged."""
        non_plain_node = TextNode("This is code", TextType.CODE) 
        new_nodes = split_nodes_link([non_plain_node])
        self.assertListEqual([non_plain_node], new_nodes)
        
    def test_split_links_multiple_input_nodes(self):
        """Test when the input list contains multiple nodes (some plain, some not)."""
        node_1 = TextNode("Text with [link](a.com)", TextType.PLAIN)
        node_2 = TextNode("Plain text", TextType.PLAIN)
        node_3 = TextNode("Bold text", TextType.BOLD)
        
        input_nodes = [node_1, node_2, node_3]
        new_nodes = split_nodes_link(input_nodes)
        
        expected = [
            TextNode("Text with ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "a.com"),
            TextNode("Plain text", TextType.PLAIN),
            TextNode("Bold text", TextType.BOLD), 
        ]
        self.assertListEqual(expected, new_nodes)


if __name__ == "__main__":
    unittest.main()