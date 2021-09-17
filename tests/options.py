from contentstack_utils.render.options import Options


class DemoOption(Options):

    def render_options(self, _obj, metadata):
        if metadata.style_type == 'block':
            return '<p>' + _obj['title'] + '</p><span>' + _obj['multi'] + '</span>'
        if metadata.style_type == 'inline':
            return '<p>' + _obj['title'] + '</p><span>' + _obj['line'] + '</span>'
        if metadata.style_type == 'link':
            return '<p>' + _obj['title'] + '</p><span>' + _obj['key'] + '</span>'
        if metadata.style_type == 'display':
            return '<p>' + _obj['title'] + '</p><span>' + _obj['multi'] + '</span>'

    def render_mark(self, mark_type, render_text) -> str:
        if mark_type == 'bold':
            return '<b>' + render_text + '</b>'
        else:
            return ''

    def render_node(self, node_type, node_obj: dict, callback):
        if node_type == 'paragraph':
            children = callback(node_obj['children'])
            return "<p class='class-id'>" + children + '</p>'
        else:
            return ''
