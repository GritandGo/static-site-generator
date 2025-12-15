import unittest
from gen_content import extract_title




class TestExtractTitle(unittest.TestCase):
    def test_extract_title_basic(self):
        md = "# This is header text."

        header_text = extract_title(md)
        self.assertEqual(
            header_text,
            "This is header text."
        )


    def test_extract_title_error_raises_without_h1(self):
        md = "This is header text."

        with self.assertRaises(Exception):
            extract_title(md)