from unittest.case import TestCase

from exceptiom import Exceptioms


class TestExceptioms(TestCase):
    def test_check_exceptions(self):
        try:
            5 / 0
        except Exception as e:
            raise Exceptioms(e)
