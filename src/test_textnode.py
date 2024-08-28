import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)
from htmlnode import *
from leafnode import *
from textnode import TextNode
from splitdelimeter import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node2", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", text_type_italic, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
    def test_bold(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = LeafNode("b","This is a text node",None)
        self.assertEqual(
            str(node2), str(node.text_node_to_html_node())
        )
    def test_text(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = LeafNode(None,"This is a text node",None)
        self.assertEqual(
            str(node2), str(node.text_node_to_html_node())
        )
    def test_italic(self):
        node = TextNode("This is a text node", text_type_italic)
        node2 = LeafNode("i","This is a text node",None)
        self.assertEqual(
            str(node2), str(node.text_node_to_html_node())
        )
    def test_italic(self):
        node = TextNode("This is a text node", text_type_code)
        node2 = LeafNode("code","This is a text node",None)
        self.assertEqual(
            str(node2), str(node.text_node_to_html_node())
        )
    def test_link(self):
        node = TextNode("This is a text node", text_type_link,"https://www.boot.dev")
        node2 = LeafNode("a","This is a text node",{"href":"https://www.boot.dev"})
        self.assertEqual(
            str(node2), str(node.text_node_to_html_node())
        )
    def test_image(self):
        node = TextNode("This is a text node", text_type_image,"https://www.boot.dev")
        node2 = LeafNode("img","",{"src":"https://www.boot.dev","alt":"This is a text node"})
        self.assertEqual(
            str(node2), str(node.text_node_to_html_node())
        )


if __name__ == "__main__":
    unittest.main()