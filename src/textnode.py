text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"
text_type_list = [text_type_text,text_type_bold,text_type_italic,text_type_code,text_type_link,text_type_image]
from leafnode import *
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    def text_node_to_html_node(text_node):
        if text_node.text_type in text_type_list:
            match text_node.text_type:
                case "bold":
                    return LeafNode("b",text_node.text)
                case "text":
                    return LeafNode(None,text_node.text)
                case "italic":
                    return LeafNode("i",text_node.text)
                case "code":
                    return LeafNode("code",text_node.text)
                case "link":
                    return LeafNode("a",text_node.text,{"href":text_node.url})
                case "image":
                    return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})
        else:
            raise Exception("not valid text type")