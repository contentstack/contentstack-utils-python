import unittest

from contentstack.embedded.style_type import StyleType
from contentstack.helper.metadata import Metadata


class TestMetadata(unittest.TestCase):

    def setUp(self):
        self.metadata = Metadata('product', 'entry', 'blt87483473746', 'products',
                                 StyleType.BLOCK, 'text_for_outer_html', 'attributes_is_string_for, now')

    # matching if not None
    def test_metadata_mojo(self):
        self.assertIsNotNone(self.metadata)

    def test_metadata_object_text(self):
        self.assertIsNotNone(self.metadata.get_text)

    def test_metadata_object_attributes(self):
        self.assertIsNotNone(self.metadata.get_attributes)

    def test_metadata_object_outer_html(self):
        self.assertIsNotNone(self.metadata.outer_html)

    def test_metadata_item_type(self):
        self.assertIsNotNone(self.metadata.get_item_type)

    def test_metadata_item_uid(self):
        self.assertIsNotNone(self.metadata.get_item_uid)

    def test_metadata_content_type_uid(self):
        self.assertIsNotNone(self.metadata.get_content_type_uid)

    def test_metadata_style_type(self):
        self.assertIsNotNone(self.metadata.get_style_type)

    # matching values
    def test_metadata_object_text_value(self):
        self.assertEqual('product', self.metadata.get_text)

    def test_metadata_object_outer_html_value(self):
        self.assertEqual('text_for_outer_html', self.metadata.outer_html.lower())

    def test_metadata_item_type_value(self):
        self.assertEqual('entry', self.metadata.get_item_type)

    def test_metadata_item_uid_value(self):
        self.assertEqual('blt87483473746', self.metadata.get_item_uid)

    def test_metadata_content_type_uid_value(self):
        self.assertEqual('products', self.metadata.get_content_type_uid)

    def test_metadata_style_type_value(self):
        self.assertEqual('block', self.metadata.get_style_type.value)

