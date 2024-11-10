import unittest
from lib.utils.enum import SimpleEnum


class TestSimpleEnum(unittest.TestCase):

    def test_smoke(self):
        _ = type('MyEnum', (SimpleEnum,), {'A': 1, 'B': 2})

    def test_simple(self):
        class MyEnum(SimpleEnum):
            A1 = 'a1'
            B1 = 'b1'
        self.assertEqual(MyEnum.A1, 'a1')
        self.assertEqual(MyEnum.B1, 'b1')

    def test_names(self):
        class MyEnum(SimpleEnum):
            intval = 42
            strval = 'string'
            listval = [1, 2, 3]
        self.assertCountEqual(MyEnum.names(), ['intval', 'strval', 'listval'])

    def test_values(self):
        class MyEnum(SimpleEnum):
            intval = 42
            strval = 'string'
            listval = [1, 2, 3]
        self.assertCountEqual(MyEnum.values(), [42, 'string', [1, 2, 3]])
