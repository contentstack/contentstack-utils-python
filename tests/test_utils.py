import json
import unittest

from contentstack.embedded.style_type import StyleType
from contentstack.helper.metadata import Metadata
from contentstack.render.options import OptionsCallback
from contentstack.utils import Utils


class TestUtility(unittest.TestCase):

    def test_̦if_entry_object_supplied(self):
        key_path = ['global_rich_multiple.group.rich_text_editor',
                    'global_rich_multiple.group'
                    '.rich_text_editor_multiple']
        with open('tests/mocks/multiple_rich_text_content.json') as file:
            json_array = json.load(file)
            entry = json_array['entries'][0]
            callback = OptionsCallback()
            Utils.render(entry, key_path, callback)

    def test_̦if_entry_list_supplied(self):
        key_path = ['rich_text_editor']
        with open('tests/mocks/embedded_items.json') as file:
            json_array = json.load(file)
            entry = json_array['entries']
            callback = OptionsCallback()
            Utils.render(entry, key_path, callback)

    def test_̦if_entry_with_block(self):
        with open('tests/mocks/embedded_items.json') as file:
            json_array = json.load(file)
            entry = json_array['entries'][0]
            callback = OptionsCallback()
            Utils.render(entry, [], callback)

    def test_embedded_objects(self):
        html_string = '<div class=\"redactor-component embedded-entry block-entry\" data-redactor-type=\"embed\" ' \
                      'data-widget-code=\"\" data-sys-entry-uid=\"blt1c9e75e3608f8c6b\" ' \
                      'data-sys-entry-locale=\"en-us\" data-sys-content-type-uid=\"0_solve\" sys-style-type=\"block\" ' \
                      'type=\"entry\"></div>'
        metadata = Metadata('text_example', 'entry', 'blt647367443', 'products', StyleType.BLOCK, 'outer_html',
                            'attributes')
        html, meta = Utils.get_embedded_objects(html_string)
        print(html, meta)

    def test_embedded_rte_string(self):

        html_text = "<p>Global multiple group 1</p><figure class=\"embedded-asset\" data-redactor-type=\"embed\" " \
                    "data-widget-code=\"\" data-sys-asset-filelink=\"https://dev16-images.contentstack.com/v3/assets" \
                    "/blt77263d300aee3e6b/blt7324a68403ee7281/5f83f543d418e407f919e0e4/11.jpg\" " \
                    "data-sys-asset-uid=\"blt7324a68403ee7281\" data-sys-asset-filename=\"11.jpg\" " \
                    "data-sys-asset-contenttype=\"image/jpeg\" type=\"asset\" sys-style-type=\"display\"></figure> "
        metadata = Metadata('text_example', 'entry', 'blt647367443', 'products', StyleType.BLOCK, 'outer_html',
                            'attributes')
        html, meta = Utils.get_embedded_objects(html_text)
        print(html, meta)
