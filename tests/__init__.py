# pytest --html=tests/report/test-report.html 
# above command runs tests and test reports generates in tests/report location.
# nosetests --with-coverage --cover-html
# clean all the .pyc files
# find . -name \*.pyc -delete
# nosetests --with-coverage --cover-html
# pytest --cov=contentstack
# pytest -v --cov=contentstack --cov-report=html
# pytest --html=tests/report/test-report.html
from unittest import TestLoader, TestSuite

from .test_item_types import TestItemType
from .test_metadata import TestMetadata
from .test_style_type import TestStyleType
from .test_utils import TestUtility


def all_tests():
    test_module_itemtype = TestLoader().loadTestsFromTestCase(TestItemType)
    test_module_metadata = TestLoader().loadTestsFromTestCase(TestMetadata)
    test_module_style_type = TestLoader().loadTestsFromTestCase(TestStyleType)
    test_module_utility = TestLoader().loadTestsFromTestCase(TestUtility)
    suite = TestSuite([
        test_module_itemtype,
        test_module_metadata,
        test_module_style_type,
        test_module_utility,
    ])
