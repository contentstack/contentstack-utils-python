"""
    Metadata is the model class for embedded objects

    Returns:
        str: text, item_type, item_uid, type_uid, style_type, outer_html and attributes
"""

import enum


# pylint: disable=too-many-arguments
class StyleType(enum.Enum):
    """
        This StyleType contains four options like below.

        BLOCK
        INLINE
        LINK
        DISPLAY
        DOWNLOADABLE
    """

    BLOCK = "block"
    INLINE = 'inline'
    LINK = 'link'
    DISPLAY = 'displayable'
    DOWNLOADABLE = 'downloadable'


class Metadata:
    """
    model helper class to set and get value
    """

    def __init__(self, text: str, item_type: str, item_uid: str,
                 content_type_uid: str, style_type: StyleType,
                 outer_html: str, attributes: str):
        """Used to set the value to the variables

        Args:
            text (str): [text for embedded objects]
            item_type (str): [item_type for embedded objects]
            item_uid (str): [item_uid for embedded objects]
            content_type_uid (str): [content_type_uid for embedded objects]
            style_type (StyleType): [style_type for embedded objects]
            outer_html (str): [outer_html for embedded objects]
            attributes (str): [attributes for embedded objects]
        """
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
        """retruns text for embedded objects

        Returns:
            str : text for embedded objects
        """
        return self.text

    # getter get_item_type() method
    @property
    def get_item_type(self):
        """retruns item_type for embedded objects

        Returns:
            str :  item_type for embedded objects
        """
        return self.item_type

    # getter get_item_uid() method
    @property
    def get_item_uid(self):
        """retruns item_uid for embedded objects

        Returns:
            str : item_uid for embedded objects
        """
        return self.item_uid

    # getter get_content_type_uid() method
    @property
    def get_content_type_uid(self):
        """retruns content_type_uid for embedded objects

        Returns:
            str :  content_type_uid for embedded objects
        """
        return self.content_type_uid

    # getter get_style_type() method
    @property
    def get_style_type(self):
        """retruns style_type for embedded objects

        Returns:
            StyleType :  style_type for embedded objects
        """
        return self.style_type

    # getter get_outer_html() method
    @property
    def get_outer_html(self):
        """retruns outer_html for embedded objects

        Returns:
            str :  outer_html for embedded objects
        """
        return self.outer_html

    # getter get_attributes() method
    @property
    def get_attributes(self):
        """ retruns attributes for embedded objects

        Returns:
            str :  attributes for embedded objects
        """
        return self.attributes
