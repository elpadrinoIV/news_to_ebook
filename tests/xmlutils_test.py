import unittest

from xmlutils import *
from lxml import etree,html

class XMLUtilsTest(unittest.TestCase):
    def test_flatten(self):
        p = '<a><b>AAA</b></a>'
        p_exp = '<a>AAA</a>'

        tree = html.fromstring(p)
        flatten(tree, tree.xpath("./b")[0])
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a><b>AAA</b></a>'
        p_exp = '<a>AAA</a>'

        tree = html.fromstring(p)
        flatten_list(tree, tree.xpath("./b"))
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a><b>AAA</b>BBB</a>'
        p_exp = '<a>AAABBB</a>'

        tree = html.fromstring(p)
        flatten_list(tree, tree.xpath("./b"))
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b>BBB</b></a>'
        p_exp = '<a>AAABBB</a>'

        tree = html.fromstring(p)
        flatten_list(tree, tree.xpath("./b"))
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b>BBB</b>CCC</a>'
        p_exp = '<a>AAABBBCCC</a>'

        tree = html.fromstring(p)
        flatten_list(tree, tree.xpath("./b"))
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b>BBB<c>CCC</c>DDD<c>EEE</c>FFF</b>GGG</a>'
        p_exp = '<a>AAABBBCCCDDDEEEFFFGGG</a>'

        tree = html.fromstring(p)
        flatten_list(tree, tree.xpath("./b"))
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b>BBB</b><b>CCC</b><b>DDD</b>EEE</a>'
        p_exp = '<a>AAABBBCCCDDDEEE</a>'

        tree = html.fromstring(p)
        flatten_list(tree, tree.xpath("./b"))
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b>BBB</b><b>CCC</b>DDD<b>EEE</b>FFF</a>'
        p_exp = '<a>AAABBBCCCDDDEEEFFF</a>'

        tree = html.fromstring(p)
        flatten_list(tree, tree.xpath("./b"))
        self.assertEqual(etree.tostring(tree), p_exp)

    def test_remove(self):
        p = '<a><b>AAA</b></a>'
        p_exp = ''

        tree = html.fromstring(p)
        remove_tag(tree, "b")
        self.assertEqual(tree.text_content(), p_exp)

        p = '<a><b>AAA</b>BBB</a>'
        p_exp = '<a>BBB</a>'

        tree = html.fromstring(p)
        remove_tag(tree, "b")
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b>BBB</b></a>'
        p_exp = '<a>AAA</a>'

        tree = html.fromstring(p)
        remove_tag(tree, "b")
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b>BBB</b>CCC</a>'
        p_exp = '<a>AAACCC</a>'

        tree = html.fromstring(p)
        remove_tag(tree, "b")
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b>BBB<c>CCC</c>DDD<c>EEE</c>FFF</b>GGG</a>'
        p_exp = '<a>AAAGGG</a>'

        tree = html.fromstring(p)
        remove_tag(tree, "b")
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b>BBB<c>CCC</c>DDD<c>EEE</c>FFF</b>GGG</a>'
        p_exp = '<a>AAA<b>BBBDDDFFF</b>GGG</a>'

        tree = html.fromstring(p)
        remove_tag(tree, "c")
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b>BBB</b><b>CCC</b><b>DDD</b>EEE</a>'
        p_exp = '<a>AAAEEE</a>'

        tree = html.fromstring(p)
        remove_tag(tree, "b")
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b>BBB</b><b>CCC</b>DDD<b>EEE</b>FFF</a>'
        p_exp = '<a>AAADDDFFF</a>'

        tree = html.fromstring(p)
        remove_tag(tree, "b")
        self.assertEqual(etree.tostring(tree), p_exp)


        p = '<a><b><b><b></b></b></b><b><b><b>AAA</b>BBB</b></b>CCC<b>DDD<b>EEE</b></b>FFF</a>'
        p_exp = '<a>CCCFFF</a>'

        tree = html.fromstring(p)
        remove_tag(tree, "b")
        self.assertEqual(etree.tostring(tree), p_exp)

    def test_remove_empty(self):
        p = '<a><b></b></a>'
        p_exp = ['<a></a>', '<a/>']

        tree = html.fromstring(p)
        remove_empty(tree)
        self.assertIn(etree.tostring(tree), p_exp)

        p = '<a><b>AAA</b></a>'
        p_exp = '<a><b>AAA</b></a>'

        tree = html.fromstring(p)
        remove_empty(tree)
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b></b></a>'
        p_exp = '<a>AAA</a>'

        tree = html.fromstring(p)
        remove_empty(tree)
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a><b></b>AAA</a>'
        p_exp = '<a>AAA</a>'

        tree = html.fromstring(p)
        remove_empty(tree)
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b></b>BBB</a>'
        p_exp = '<a>AAABBB</a>'

        tree = html.fromstring(p)
        remove_empty(tree)
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b></b>BBB<b>CCC</b>DDD<b></b>EEE</a>'
        p_exp = '<a>AAABBB<b>CCC</b>DDDEEE</a>'

        tree = html.fromstring(p)
        remove_empty(tree)
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b><c><d/></c></b>BBB</a>'
        p_exp = '<a>AAABBB</a>'

        tree = html.fromstring(p)
        remove_empty(tree)
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b><c><d/>BBB</c></b>CCC</a>'
        p_exp = '<a>AAA<b><c>BBB</c></b>CCC</a>'

        tree = html.fromstring(p)
        remove_empty(tree)
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a><b></b>AAA<b><c></c></b>BBB<b>CCC</b><b></b><b><c></c></b>DDD</b></a>'
        p_exp = '<a>AAABBB<b>CCC</b>DDD</a>'

        tree = html.fromstring(p)
        remove_empty(tree)
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a><b> </b></a>'
        p_exp = ''

        tree = html.fromstring(p)
        remove_empty(tree, ignore_whitespace=True)
        self.assertEqual(tree.text_content(), p_exp)

        p = '<a><b> </b></a>'
        p_exp = '<a><b> </b></a>'

        tree = html.fromstring(p)
        remove_empty(tree, ignore_whitespace=False)
        self.assertEqual(etree.tostring(tree), p_exp)

        p = '<a>AAA<b>  <c>  <d/>  </c>  </b>BBB</a>'
        p_exp = '<a>AAABBB</a>'

        tree = html.fromstring(p)
        remove_empty(tree, ignore_whitespace=True)
        self.assertEqual(etree.tostring(tree), p_exp)

if __name__ == '__main__':
    unittest.main()
