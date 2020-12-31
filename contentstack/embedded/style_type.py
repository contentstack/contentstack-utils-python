""""
For `Entry`: StyleType.BLOCK, StyleType.INLINE, StyleType.LINKED,
For `Assets`: StyleType.DISPLAY, StyleType.DOWNLOADABLE
 """
import enum


class StyleType(enum.Enum):

    BLOCK = "block"
    INLINE = 'inline'
    LINK = 'link'
    DISPLAY = 'displayable'
    DOWNLOADABLE = 'downloadable'
