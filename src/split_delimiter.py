from textnode import TextType, TextNode
from markdown_extraction import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = [] # result list will be old_nodes split up properly


    for each_node in old_nodes:
        if each_node.text_type == TextType.PLAIN:
           parts = each_node.text.split(delimiter)
           if len(parts) % 2 == 0:
               raise Exception("Text is not valid Markdown")
           for index, item in enumerate(parts):
               if item == "":
                   continue
               if index % 2 == 0:
                   new_nodes.append(TextNode(item, TextType.PLAIN)) 
               else: 
                   new_nodes.append(TextNode(item, text_type))
        else:
            new_nodes.append(each_node)

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []


    for each_node in old_nodes:
        if each_node.text_type != TextType.PLAIN:
            new_nodes.append(each_node)
            continue

        remaining_text = each_node.text
        images = extract_markdown_images(remaining_text)

        if not images:
            new_nodes.append(each_node)
            continue

        for image_alt, image_link in images:
            image_markdown = f"![{image_alt}]({image_link})"
            sections = remaining_text.split(image_markdown, 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
            
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            remaining_text = sections[1]
        

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.PLAIN))





def split_nodes_link(old_nodes):
    new_nodes = []


    for each_node in old_nodes:
        if each_node.text_type != TextType.PLAIN:
            new_nodes.append(each_node)
            continue

        remaining_text = each_node.text
        links = extract_markdown_links(remaining_text)

        if not links:
            new_nodes.append(each_node)
            continue

        for link_text, link_url in links:
            link_markdown = f"[{link_text}]({link_url})"
            sections = remaining_text.split(link_markdown, 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
            
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            remaining_text = sections[1]
        

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.PLAIN))





      