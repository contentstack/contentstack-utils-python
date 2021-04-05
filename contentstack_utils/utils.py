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

from contentstack_utils.helper.metadata import Metadata
from contentstack_utils.render.options import Options
from contentstack_utils.helper.converter import convert_style


def _is_json(file):
    try:
        json.dumps(file)
        return True
    except ValueError:
        return False


def extract_keys(_embedded_items):
    available_keys: list = _embedded_items.keys()
    return available_keys


def find_embedded_entry(json_array: list, metadata: Metadata):
    for obj in json_array:
        if obj['uid'] == metadata.get_item_uid:
            return obj
    return None


def get_metadata(elements):
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


def get_html_doc(embedded_obj, metadata, callback, html_doc):
    if '_embedded_items' in embedded_obj:
        keys = extract_keys(embedded_obj['_embedded_items'])
        for key in keys:
            items_array = embedded_obj['_embedded_items'][key]
            item = find_embedded_entry(items_array, metadata)
            if item is not None:
                replaceable_str = callback.render_options(item, metadata)
                html_doc = html_doc.replace(metadata.outer_html, replaceable_str)
                break
    return html_doc


class Utils:
    """
    render staticmethod, that accepts entry/entries, key path and render_object
    entry_obj: [list] or [dict] that contains list or dic object
    key_path: list of key_path
    Raises:
        FileNotFoundError: if file not found or invalid resource received
    """

    @staticmethod
    def render(entry_obj, key_path: list, option: Options):
        valid = _is_json(entry_obj)

        if not valid:
            raise FileNotFoundError('Invalid file found')

        if isinstance(entry_obj, list):
            for entry in entry_obj:
                Utils.render(entry, key_path, option)

        if isinstance(entry_obj, dict):
            Utils._get_embedded_keys(entry_obj, key_path, option)

    @staticmethod
    def _get_embedded_keys(entry, key_path, option: Options):

        if '_embedded_items' in entry:
            if key_path is not None:
                for path in key_path:
                    Utils._find_embed_keys(entry, path, option)
            else:
                _embedded_items = entry['_embedded_items']
                available_keys: list = _embedded_items.keys()
                for path in available_keys:
                    Utils._find_embed_keys(entry, path, option)

    @staticmethod
    def _find_embed_keys(entry, path, option: Options):
        keys = path.split('.')
        Utils._get_content(keys, entry, option)

    @staticmethod
    def _get_content(keys_array: list, entry, option: Options):
        if keys_array is not None and len(keys_array) > 0:
            key = keys_array[0]
            if len(keys_array) == 1 and keys_array[0] in entry:
                var_content = entry[key]
                if isinstance(var_content, (list, str)):
                    entry[key] = Utils.render_content(var_content, entry, option)
            else:
                keys_array.remove(key)
                if key in entry and isinstance(entry[key], dict):
                    Utils._get_content(keys_array, entry[key], option)
                elif key in entry and isinstance(entry[key], list):
                    list_json = entry[key]
                    for node in list_json:
                        Utils._get_content(keys_array, node, option)

    @staticmethod
    def render_content(rte_content, embed_obj: dict, callback: Options) -> object:
        if isinstance(rte_content, str):
            return get_embedded_objects(rte_content, embed_obj, callback)
        elif isinstance(rte_content, list):
            temp = []
            for rte in rte_content:
                temp.append(Utils.render_content(rte, embed_obj, callback))
            return temp
        return rte_content


def get_embedded_objects(html_doc, embedded_obj, callback):
    import re
    document = f"<items>{html_doc}</items>"
    tag = etree.fromstring(document)
    html_doc = etree.tostring(tag).decode('utf-8')
    html_doc = re.sub('(?ms)<%s[^>]*>(.*)</%s>' % (tag.tag, tag.tag), '\\1', html_doc)
    elements = tag.xpath("//*[contains(@class, 'embedded-asset') or contains(@class, 'embedded-entry')]")
    metadata = get_metadata(elements)
    return get_html_doc(embedded_obj, metadata, callback, html_doc)
