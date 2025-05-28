import unittest
from markdown_extraction import extract_markdown_images, extract_markdown_links


class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_markdown_multiple_different_images(self):
        matches = extract_markdown_images(
            "This is text with an ![Ximage](https://i.imgur.com/zjjcJKX.png) and "
            "This is text with an ![Yimage](https://i.imgur.com/zjjcJKY.png) and "
            "This is text with an ![Zimage](https://i.imgur.com/zjjcJKZ.png) and "
        )
        self.assertListEqual([("Ximage", "https://i.imgur.com/zjjcJKX.png"), 
                              ("Yimage", "https://i.imgur.com/zjjcJKY.png"),
                              ("Zimage", "https://i.imgur.com/zjjcJKZ.png")
                              ], matches)




    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with an [title](https://www.example.com)"
        )
        self.assertListEqual([("title", "https://www.example.com")], matches)


    def test_extract_markdown_multiple_different_links(self):
        matches = extract_markdown_links(
            "This is text with a [Xlink](https://example.com/x) and "
            "This is text with a [Ylink](https://example.com/y) and "
            "This is text with a [Zlink](https://example.com/z) and "
        )
        self.assertListEqual([("Xlink", "https://example.com/x"), 
                              ("Ylink", "https://example.com/y"),
                              ("Zlink", "https://example.com/z")
                              ], matches)
        

    def test_extract_markdown_links_handles_images_gracefully(self):
        matches = extract_markdown_links("![alt text](image.jpg)")

        self.assertListEqual([], matches)