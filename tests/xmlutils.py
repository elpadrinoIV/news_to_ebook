import re

def flatten_list(tree, elements):
    for elem in elements:
        flatten(tree, elem)

def flatten(tree, elem):
    elem_tail = elem.tail
    if not elem_tail:
        elem_tail = ""

    prev_elem = elem.getprevious()
    if prev_elem is not None:
        # put tail on previous sibling's tail
        prev_tail = prev_elem.tail
        if not prev_tail:
            prev_tail = ""

        final_content = prev_tail + elem.text_content() + elem_tail
        if len(final_content) > 0:
            prev_elem.tail = final_content
    else:
        # put tail to text of parent
        parent_text = elem.getparent().text
        if not parent_text:
            parent_text = ""

        final_content = parent_text + elem.text_content() + elem_tail
        if len(final_content) > 0:
            elem.getparent().text = final_content

    elem.getparent().remove(elem)

only_whitespace_regex = re.compile(r"^\s*$")
def remove_empty(tree, **params):
    for elem in tree.getchildren():
        remove_empty(elem, **params)

    if tree.getparent() is None:
        return

    if "ignore_whitespace" in params and params["ignore_whitespace"]:
        if only_whitespace_regex.match(tree.text_content()):
            remove_element(tree)
    else:
        if len(tree.text_content()) == 0:
            remove_element(tree)

def keep_only_wanted(tree, wanted):
    for elem in tree.getchildren():
        if elem.tag not in wanted:
            remove_element(elem)
        else:
            keep_only_wanted(elem, wanted)

    

def remove_tag(tree, tag):
    for elem in tree.xpath(".//" + tag):
        remove_element(elem)

def remove_element(elem):
    elem_tail = elem.tail
    if elem_tail:
        prev_elem = elem.getprevious()
        if prev_elem is not None:
            prev_tail = prev_elem.tail
            if not prev_tail:
                prev_tail = ""
            prev_elem.tail = prev_tail + elem_tail
        else:
            parent_text = elem.getparent().text
            if not parent_text:
                parent_text = ""
            elem.getparent().text = parent_text + elem_tail
    
    elem.getparent().remove(elem)

    
