import json
import os
import unittest

from contentstack_utils.render.options import Options
from contentstack_utils.utils import Utils


def read_mock_path(path):
    path_to_json = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'mocks', path)
    return path_to_json


class TestUtility(unittest.TestCase):

    def test_if_entry_object_render_content_asset(self):
        key_path = ['global_rich_multiple.group.rich_text_editor',
                    'global_rich_multiple.group'
                    '.rich_text_editor_multiple']
        path = read_mock_path('multiple_rich_text_content.json')
        with open(path) as file:
            json_array = json.load(file)
            entry_list = json_array['entries'][0]
            callback = Options()
            rte_content = "<p>Global multiple group 1</p><figure class=\"embedded-asset\" " \
                          "data-redactor-type=\"embed\" data-widget-code=\"\" " \
                          "data-sys-asset-filelink=\"https://dev16-images.contentstack.com/v3/assets" \
                          "/blt77263d300aee3e6b/blt7324a68403ee7281/5f83f543d418e407f919e0e4/11.jpg\" " \
                          "data-sys-asset-uid=\"blt7324a68403ee7281\" data-sys-asset-filename=\"11.jpg\" " \
                          "data-sys-asset-contenttype=\"image/jpeg\" type=\"asset\" " \
                          "sys-style-type=\"display\"></figure>"
            reini = Utils.render_content(rte_content, entry_list, callback)
            print(reini)

    def test_if_entry_object_render_content_entry(self):
        path = read_mock_path('multiple_rich_text_content.json')
        with open(path) as file:
            json_array = json.load(file)
            entry_list = json_array['entries'][0]
            option = Options()
            rte_content = "<p><a data-sys-entry-uid=\"blt1c9e75e3608f8c6b\" data-sys-entry-locale=\"en-us\" " \
                          "data-sys-content-type-uid=\"0_solve\" sys-style-type=\"link\" data-sys-can-edit=\"true\" " \
                          "class=\"embedded-entry\" type=\"entry\" href=\"/untitled\" title=\"Entry 001 123\">Global " \
                          "multiple modular 1</a></p>"
            reini = Utils.render_content(rte_content, entry_list, option)
            print(reini)

    # def test_if_entry_object_supplied_if_entry_obj_list(self):
    #     key_path = ['global_rich_multiple.group.rich_text_editor',
    #                 'global_rich_multiple.group'
    #                 '.rich_text_editor_multiple']
    #     path = read_mock_path('multiple_rich_text_content.json')
    #     with open(path) as file:
    #         json_array = json.load(file)
    #         entry_list = json_array['entries']
    #         callback = Options()
    #         metadata = Metadata(
    #             "11.jpg", 'entry', 'blt5662565323', 'content_type_uid',
    #             StyleType.BLOCK,
    #             'outer_html_of_embedded_obj', 'embedded_attributes'
    #         )
    #         callback.render_options(embedded_obj=json_array, metadata=metadata)
    #         html = Utils.render(entry_list, key_path, callback)
    #         print(html)

    # def test_if_entry_object_supplied_if_entry_obj(self):
    #     key_path = ['global_rich_multiple.group.rich_text_editor',
    #                 'global_rich_multiple.group'
    #                 '.rich_text_editor_multiple']
    #     path = read_mock_path('multiple_rich_text_content.json')
    #     with open(path) as file:
    #         json_array = json.load(file)
    #         entry_obj = json_array['entries'][0]
    #         callback = Options()
    #         metadata = Metadata()
    #         callback.render_options(embedded_obj=json_array, metadata=metadata)
    #         Utils.render(entry_obj, key_path, callback)

    #
    # def test_̦if_entry_list_not_supplied(self):
    #     key_path = ['rich_text_editor']
    #     with open('tests/mocks/embedded_items.json') as file:
    #         json_array = json.load(file)
    #         entry = json_array['entries']
    #         callback = OptionsCallback()
    #         Utils.render(entry, key_path, callback)
    #
    # def test_̦if_entry_with_block(self):
    #     with open('tests/mocks/embedded_items.json') as file:
    #         json_array = json.load(file)
    #         entry = json_array['entries'][0]
    #         callback = OptionsCallback()
    #         Utils.render(entry, [], callback)

    # def test_embedded_objects(self): html_string = '<div class=\"redactor-component embedded-entry block-entry\"
    # data-redactor-type=\"embed\" ' \ 'data-widget-code=\"\" data-sys-entry-uid=\"blt1c9e75e3608f8c6b\" ' \
    # 'data-sys-entry-locale=\"en-us\" data-sys-content-type-uid=\"0_solve\" sys-style-type=\"block\" ' \
    # 'type=\"entry\"></div>' Metadata('text_example', 'entry', 'blt647367443', 'products', StyleType.BLOCK,
    # 'outer_html', 'attributes') html, meta = get_embedded_objects(html_string) print(html, meta)

    # def test_embedded_rte_string(self): html_text = "<p>Global multiple group 1</p><figure class=\"embedded-asset\"
    # data-redactor-type=\"embed\" " \ "data-widget-code=\"\"
    # data-sys-asset-filelink=\"https://dev16-images.contentstack.com/v3/assets" \
    # "/blt77263d300aee3e6b/blt7324a68403ee7281/5f83f543d418e407f919e0e4/11.jpg\" " \
    # "data-sys-asset-uid=\"blt7324a68403ee7281\" data-sys-asset-filename=\"11.jpg\" " \
    # "data-sys-asset-contenttype=\"image/jpeg\" type=\"asset\" sys-style-type=\"display\"></figure> " metadata =
    # Metadata('text_example', 'entry', 'blt647367443', 'products', StyleType.BLOCK, 'outer_html', 'attributes')
    # html, meta = Utils.get_embedded_objects(html_text) print(html, meta)
