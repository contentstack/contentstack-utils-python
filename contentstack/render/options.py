# pylint: disable=missing-function-docstring
from contentstack.helper.metadata import Metadata


class OptionsCallback:

    @staticmethod
    def render_options(self, embedded_obj: dict, metadata: Metadata) -> str:
        return 'string'
