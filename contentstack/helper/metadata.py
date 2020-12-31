from contentstack.embedded.style_type import StyleType


class Metadata:

    def __init__(self, text: str, item_type: str, item_uid: str, content_type_uid: str, style_type: StyleType,
                 outer_html: str, attributes: str):
        self.text = text
        self.item_type = item_type
        self.item_uid = item_uid
        self.content_type_uid = content_type_uid
        self.style_type = style_type
        self.outer_html = outer_html
        self.attributes = attributes

    # getter get_text() method
    @property
    def get_text(self):
        return self.text

    # getter get_item_type() method
    @property
    def get_item_type(self):
        return self.item_type

    # getter get_item_uid() method
    @property
    def get_item_uid(self):
        return self.item_uid

    # getter get_content_type_uid() method
    @property
    def get_content_type_uid(self):
        return self.content_type_uid

    # getter get_style_type() method
    @property
    def get_style_type(self):
        return self.style_type

    # getter get_outer_html() method
    @property
    def get_outer_html(self):
        return self.outer_html

    # getter get_attributes() method
    @property
    def get_attributes(self):
        return self.attributes
