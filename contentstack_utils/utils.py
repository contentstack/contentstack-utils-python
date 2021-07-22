# pylint: disable=missing-function-docstring
"""
Utils module helps to get access of public functions like:
    render
    render_content
    get_embedded_objects
    get_embedded_entry
"""

import json
from lxml import etree
from contentstack_utils.helper.converter import convert_style
from contentstack_utils.helper.metadata import Metadata
from contentstack_utils.helper.node_to_html import NodeToHtml
from contentstack_utils.render.options import Options


class Utils:

    @staticmethod
    def render(entry_obj, key_path: list, option: Options):
        valid = Utils.__is_json(entry_obj)
        if not valid:
            raise FileNotFoundError('Invalid file found')

        if isinstance(entry_obj, list):
            for entry in entry_obj:
                Utils.render(entry, key_path, option)

        if isinstance(entry_obj, dict):
            Utils.__get_embedded_keys(entry_obj, key_path, option, render_callback=Utils.render_content)

    @staticmethod
    def __get_embedded_keys(entry, key_path, option: Options, render_callback):
        if '_embedded_items' in entry:
            if key_path is not None:
                for path in key_path:
                    Utils.__find_embed_keys(entry, path, option, render_callback)
            else:
                _embedded_items = entry['_embedded_items']
                available_keys: list = _embedded_items.keys()
                for path in available_keys:
                    Utils.__find_embed_keys(entry, path, option, render_callback)

    @staticmethod
    def __find_embed_keys(entry, path, option: Options, render_callback):
        keys = path.split('.')
        Utils.__get_content(keys, entry, option, render_callback)

    @staticmethod
    def __get_content(keys_array, entry, option: Options, render_callback):
        if keys_array is not None and len(keys_array) > 0:
            key = keys_array[0]
            if len(keys_array) == 1 and keys_array[0] in entry:
                var_content = entry[key]
                if isinstance(var_content, (list, str, dict)):
                    entry[key] = render_callback(var_content, entry, option)
            else:
                keys_array.remove(key)
                if key in entry and isinstance(entry[key], dict):
                    Utils.__get_content(keys_array, entry[key], option, render_callback)
                elif key in entry and isinstance(entry[key], list):
                    list_json = entry[key]
                    for node in list_json:
                        Utils.__get_content(keys_array, node, option, render_callback)

    @staticmethod
    def render_content(rte_content, embed_obj: dict, callback: Options) -> object:
        if isinstance(rte_content, str):
            return Utils.__get_embedded_objects(rte_content, embed_obj, callback)
        elif isinstance(rte_content, list):
            render_callback = []
            for rte in rte_content:
                render_callback.append(Utils.render_content(rte, embed_obj, callback))
            return render_callback
        return rte_content

    @staticmethod
    def __get_embedded_objects(html_doc, embedded_obj, callback):
        import re
        document = f"<items>{html_doc}</items>"
        tag = etree.fromstring(document)
        html_doc = etree.tostring(tag).decode('utf-8')
        html_doc = re.sub('(?ms)<%s[^>]*>(.*)</%s>' % (tag.tag, tag.tag), '\\1', html_doc)
        elements = tag.xpath("//*[contains(@class, 'embedded-asset') or contains(@class, 'embedded-entry')]")
        metadata = Utils.__get_metadata(elements)
        return Utils.__get_html_doc(embedded_obj, metadata, callback, html_doc)

    @staticmethod
    def __get_html_doc(embedded_obj, metadata, callback, html_doc):
        if '_embedded_items' in embedded_obj:
            keys = embedded_obj['_embedded_items'].keys()
            for key in keys:
                items_array = embedded_obj['_embedded_items'][key]
                item = Utils.__find_embedded_entry(items_array, metadata)
                if item is not None:
                    replaceable_str = callback.render_options(item, metadata)
                    html_doc = html_doc.replace(metadata.outer_html, replaceable_str)
                    break
        return html_doc

    @staticmethod
    def __get_metadata(elements):
        for element in elements:
            content_type = None
            typeof = element.attrib['type']
            if typeof == 'asset':
                uid = element.attrib['data-sys-asset-uid']
            else:
                uid = element.attrib['data-sys-entry-uid']
                content_type = element.attrib['data-sys-content-type-uid']
            style = element.attrib['sys-style-type']
            outer_html = etree.tostring(element).decode('utf-8')
            attributes = element.attrib
            style = convert_style(style)
            metadata = Metadata(element.text, typeof, uid, content_type, style, outer_html, attributes)
            return metadata

    ####################################################
    #                   SUPERCHARGED                   #
    ####################################################

    @staticmethod
    def __is_json(file):
        try:
            json.dumps(file)
            return True
        except ValueError:
            return False

    @staticmethod
    def json_to_html(entry_obj, key_path: list, option: Options):
        if not Utils.__is_json(entry_obj):
            raise FileNotFoundError('Could not process invalid content')
        if isinstance(entry_obj, list):
            for entry in entry_obj:
                return Utils.json_to_html(entry, key_path, option)
        if isinstance(entry_obj, dict):
            render_callback = Utils.__enumerate_content
            if key_path is not None:
                for path in key_path:
                    Utils.__find_embed_keys(entry_obj, path, option, render_callback)

    @staticmethod
    def __enumerate_content(content, entry, option):
        if len(content) > 0:
            if isinstance(content, list):
                array_content = []
                for item in content:
                    result = Utils.__enumerate_content(item, entry, option)
                    array_content.append(result)
                return array_content
            if isinstance(content, dict):
                if 'type' and 'children' in content:
                    if content['type'] == 'doc':
                        return Utils.__raw_processing(content['children'], entry, option)
        return ''

    @staticmethod
    def __raw_processing(children, entry, option):
        array_container = []
        for item in children:
            if isinstance(item, dict):
                array_container.append(Utils.__extract_keys(item, entry, option))
        temp = ''.join(array_container)
        return temp

    @staticmethod
    def __extract_keys(item, entry, option: Options):
        if 'type' not in item.keys() and 'text' in item.keys():
            return NodeToHtml.text_node_to_html(item, option)

        elif 'type' in item.keys():
            node_style = item['type']
            if node_style == 'reference':
                metadata = Utils.__return_metadata(item, node_style)
                if '_embedded_items' in entry:
                    keys = entry['_embedded_items'].keys()
                    for key in keys:
                        items_array = entry['_embedded_items'][key]
                        content = Utils.__find_embedded_entry(items_array, metadata)
                        return Utils.__get_string_option(option, metadata, content)
            else:
                def call(children):
                    return Utils.__raw_processing(children, entry, option)

                return option.render_node(node_style, item, callback=call)
        return ''

    @staticmethod
    def __find_embedded_entry(list_json: list, metadata: Metadata):
        for obj in list_json:
            if obj['uid'] == metadata.get_item_uid:
                return obj
        return None

    @staticmethod
    def __get_string_option(option: Options, metadata: Metadata, content: dict):
        string_option = option.render_options(content, metadata)
        if string_option is None:
            string_option = Options().render_options(content, metadata)
        return string_option

    @staticmethod
    def __return_metadata(item, node_style):
        attr = item['attrs']
        text = Utils.__get_child_text(item)
        style = convert_style(attr['display-type'])
        if attr['type'] == 'asset':
            return Metadata(text, node_style,
                            attr['asset-uid'],
                            'sys-asset',
                            style, '', '')
        else:
            return Metadata(text, node_style,
                            attr['entry-uid'],
                            attr['content-type-uid'],
                            style, '', '')

    @staticmethod
    def __get_child_text(item):
        text = ''
        if 'children' in item.keys() and len(item['children']) > 0:
            children = item['children']
            for child in children:
                if text in child.keys():
                    text = child['text']
                    break
        return text
