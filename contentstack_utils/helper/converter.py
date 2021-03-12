from contentstack_utils.embedded.styletype import StyleType


def convert_style(style) -> StyleType:
    if style == 'block':
        return StyleType.BLOCK
    elif style == 'inline':
        return StyleType.INLINE
    elif style == 'link':
        return StyleType.LINK
    elif style == 'display':
        return StyleType.DISPLAY
    elif style == 'download':
        return StyleType.DOWNLOAD

