# pylint: disable=missing-function-docstring
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

from contentstack.helper.metadata import Metadata


def _title_or_uid(embedded_obj: dict) -> str:
    _title = ""
    if embedded_obj is not None:
        if 'title' in embedded_obj and len(embedded_obj['title']) != 0:
            _title = embedded_obj['title']
        elif 'uid' in embedded_obj:
            _title = embedded_obj['uid']
    return _title


def _asset_title_or_uid(embedded_obj: dict) -> str:
    _title = ""
    if embedded_obj is not None:
        if 'title' in embedded_obj and len(embedded_obj['title']) != 0:
            _title = embedded_obj['title']
        elif 'filename' in embedded_obj:
            _title = embedded_obj['filename']
        elif 'uid' in embedded_obj:
            _title = embedded_obj['uid']
    return _title


class DefaultOptions:

    @staticmethod
    def render_options(embedded_obj: dict, metadata: Metadata) -> str:
        if metadata.style_type.name == 'block':
            return '<div><p>' + _title_or_uid(embedded_obj) \
                   + '</p><div><p>Content type: <span>' + embedded_obj['_content_type_uid'] \
                   + '</span></p></div>'
        elif metadata.style_type.name == 'inline':
            return '<span>' + _title_or_uid(embedded_obj) + '</span>'
        elif metadata.style_type.name == 'link':
            return '<a href=' + embedded_obj['url'] + '>' + _title_or_uid(embedded_obj) + '</a>'
        elif metadata.style_type.name == 'display':
            return '<img src=' + embedded_obj['url'] + ' alt=' \
                   + _asset_title_or_uid(embedded_obj) + '/>'
        return ''
