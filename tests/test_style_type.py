import unittest

from contentstack.embedded.style_type import StyleType


class TestStyleType(unittest.TestCase):

    def test_style_type_block(self):
        style = StyleType.BLOCK
        self.assertEqual('block', style.value)

    def test_style_type_inline(self):
        style = StyleType.INLINE
        self.assertEqual('inline', style.value)

    def test_style_type_link(self):
        style = StyleType.LINK
        self.assertEqual('link', style.value)

    def test_style_type_display(self):
        style = StyleType.DISPLAY
        self.assertEqual('displayable', style.value)

    def test_style_type_downloadable(self):
        style = StyleType.DOWNLOADABLE
        self.assertEqual('downloadable', style.value)