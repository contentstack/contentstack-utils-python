# pip install -r requirements.txt
# pytest --html=tests/report/test-report.html
# coverage report -m
# coverage html -d coveragereport
"""
The __init__.py files are required to make Python treat the directories as containing
packages; this is done to prevent directories with a common name, such as string,
from unintentionally hiding valid modules that occur later on the module search path
Used: Safety checks your installed dependencies for known security vulnerabilities
file __init__.py contains package information like

__author__, __status__, __version__, __endpoint__ and __email__

`Your code has been rated at 10.00/10`
"""

from contentstack_utils.embedded.item_type import ItemType
from contentstack_utils.embedded.styletype import StyleType
from contentstack_utils.helper.metadata import Metadata
from contentstack_utils.render.options import Options
from contentstack_utils.utils import Utils

__title__ = 'contentstack_utils'
__author__ = 'contentstack'
__status__ = 'debug'
__version__ = '0.0.1'
__endpoint__ = 'cdn.contentstack.io'
__contact__ = 'support@contentstack.com'
