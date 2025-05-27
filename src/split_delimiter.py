from textnode import TextType, TextNode


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
