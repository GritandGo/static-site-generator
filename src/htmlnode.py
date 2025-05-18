class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        return "".join(f" {key}=\"{value}\"" for key, value in self.props.items())
    

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have a value")
        elif self.tag == None:
            return str(self.value)
        else:
            formatted_prop = "".join(f" {key}=\"{value}\"" for key, value in self.props.items()) if self.props else ""
            return f"<{self.tag}{formatted_prop}>{self.value}</{self.tag}>"

            
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("Object must have a tag")
        if not self.children:
            raise ValueError("Missing value")
        else:
            html = f"<{self.tag}{self.props_to_html()}>"
            for child in self.children:
                child_html = child.to_html()
                html += child_html

            html += f"</{self.tag}>"
            return html
            