# pylint: disable=missing-function-docstring
"""[summary]

    Raises:
        FileNotFoundError: [description]
        NameError: [description]

    Returns:
        [type]: [description]
"""

import json

from lxml import etree

from contentstack.helper.metadata import Metadata
from contentstack.render.options import OptionsCallback


def _is_json(file):
    try:
        json.dumps(file)
        return True
    except ValueError:
        return False


class Utils:
    """
    render staticmethod, that accepts entry/entries, key path and render_object
    entry_obj: [list] or [dict] that contains list or dic object
    key_path: list of key_path
    Raises:
        FileNotFoundError: [description]
        NameError: [description]
    """

    @staticmethod
    def render(entry_obj, key_path: list, option_callback: OptionsCallback):
        valid = _is_json(entry_obj)
        if not valid:
            raise FileNotFoundError('Invalid file found')
        elif isinstance(entry_obj, list):
            for entry in entry_obj:
                Utils.render(entry, key_path, option_callback)
        elif isinstance(entry_obj, dict):
            Utils._get_embedded_keys(entry_obj, key_path, option_callback)
        raise NameError('Invalid file found')

    @staticmethod
    def _get_embedded_keys(entry, key_path, option_callback: OptionsCallback):
        """[summary]

        Args:
            entry ([type]): [description]
            key_path ([type]): [description]
            option_callback ([type]): [description]
        """
        if '_embedded_items' in entry:
            if key_path is not None:
                for path in key_path:
                    Utils._find_content(entry, path, option_callback)
            else:
                _embedded_items = entry['_embedded_items']
                available_keys: list = _embedded_items.keys()
                for path in available_keys:
                    Utils._find_content(entry, path, option_callback)

    @staticmethod
    def _find_content(entry, path, option_callback: OptionsCallback):
        """
        [summary]
        Args:
            entry ([type]): [description]
            path ([type]): [description]
            option_callback (function): [description]
        """
        keys = path.split('.')
        Utils._get_content(keys, entry, option_callback)

    @staticmethod
    def _get_content(keys_array: list, entry, option_callback: OptionsCallback):
        """[summary]
        Args:
            keys_array (list): [description]
            entry ([type]): [description]
            option_callback (function): [description]

        Returns:
            [type]: [description]
        """
        if keys_array is not None and len(keys_array) > 0:
            key = keys_array[0]
            if len(keys_array) == 1 and keys_array[0] in entry:
                var_content = entry[key]
                if isinstance(var_content, (list, str)):
                    entry[key] = Utils.render_content(var_content, entry, option_callback)
                    # call function
            else:
                keys_array.remove(key)
                if key in entry and isinstance(entry[key], dict):
                    Utils._get_content(keys_array, entry[key], option_callback)
                elif key in entry and isinstance(entry[key], list):
                    list_json = entry[key]
                    for node in list_json:
                        Utils._get_content(keys_array, node, option_callback)

    @staticmethod
    def render_content(rte_array, embed_obj: dict,
                       option_callback: OptionsCallback) -> object:
        if isinstance(rte_array, str):
            # convert to html
            html, metadata = Utils.get_embedded_objects(rte_array)
            return None
        elif isinstance(rte_array, list):
            for rte in rte_array:
                return None
        return None

    @staticmethod
    def get_embedded_objects(html_doc):
        tag = etree.fromstring(html_doc)
        typeof = tag.attrib['type']
        uid = tag.attrib['data-sys-entry-uid']
        content_type = tag.attrib['data-sys-content-type-uid']
        style = tag.attrib['sys-style-type']
        # outer_html = tag.attrib['outer_html']
        # Elements embeddedEntries = html.body().getElementsByClass("embedded-entry");
        # Elements embeddedAssets = html.body().getElementsByClass("embedded-asset");
        metadata = Metadata('text', typeof, uid, content_type, style, 'outer_html', 'attributes')
        return tag, metadata

    @staticmethod
    def find_embedded_entry(json_array: list, metadata: Metadata):
        for obj in json_array:
            if obj['uid'] == metadata.get_item_uid and \
                    obj['_content_type_uid'] == metadata.content_type_uid:
                return obj
        return None
